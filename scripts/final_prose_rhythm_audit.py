from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import re

OUT = Path("FINAL_PROSE_RHYTHM_AUDIT.md")
SCENE_GLOB = "BAUSTEINE/*/SZENEN/*/PROSA.md"

WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß0-9]+(?:['’\-][A-Za-zÄÖÜäöüß0-9]+)*")
FILTER_RE = re.compile(r"\b(merkte|bemerkte|wusste|dachte|spürte|fühlte|erkannte)\b", re.I)
MICRO_RE = re.compile(r"\b(sah|blickte|nickte|schwieg|atmete|hob|legte|setzte|stand|ging)\b", re.I)
SOFTENER_RE = re.compile(r"\b(vielleicht|möglicherweise|vermutlich|offenbar|schien|wirkte|könnte|soweit|zumindest)\b", re.I)
NEG_START_RE = re.compile(r"^(Nicht|Kein|Keine|Keinen|Keinem|Keiner|Nichts)\b", re.I)
CONTRAST_RE = re.compile(r"\b(?:Es|Das|Sie|Er) war nicht\b|^Nicht\b", re.I)


def words(text: str) -> int:
    return len(WORD_RE.findall(text))


def scene_id(text: str, path: Path) -> str:
    m = re.search(r"^scene_id:\s*(S\d+)\s*$", text, re.M)
    if not m:
        raise SystemExit(f"missing scene_id in {path}")
    return m.group(1)


def body_only(text: str) -> str:
    marker = "\n---\n"
    if marker not in text:
        raise SystemExit("missing prose metadata separator")
    return text.split(marker, 1)[1].strip()


def paragraphs(body: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]


def dialogue_only(p: str) -> bool:
    t = p.strip()
    return (t.startswith("„") and t.endswith("“")) or (t.startswith("»") and t.endswith("«"))


def compact(text: str, limit: int = 190) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def find_runs(paras: list[str], predicate, minimum: int) -> list[tuple[int, int]]:
    runs: list[tuple[int, int]] = []
    start = None
    for i, p in enumerate(paras):
        if predicate(p):
            if start is None:
                start = i
        elif start is not None:
            if i - start >= minimum:
                runs.append((start, i))
            start = None
    if start is not None and len(paras) - start >= minimum:
        runs.append((start, len(paras)))
    return runs


scenes = []
for path in sorted(Path(".").glob(SCENE_GLOB)):
    text = path.read_text(encoding="utf-8")
    sid = scene_id(text, path)
    body = body_only(text)
    scenes.append((int(sid[1:]), sid, path, body, paragraphs(body)))

scenes.sort()
if [n for n, *_ in scenes] != list(range(1, 41)):
    raise SystemExit(f"expected S001-S040, got {[sid for _, sid, *_ in scenes]}")

rows = []
totals = Counter()
all_micro = Counter()
all_filters = Counter()
all_softeners = Counter()
all_formula = Counter()
all_candidates: list[tuple[int, str, str, str]] = []

for n, sid, path, body, paras in scenes:
    wc = words(body)
    em = body.count("—")
    sondern = len(re.findall(r"\bsondern\b", body, flags=re.I))
    filters = Counter(m.group(1).lower() for m in FILTER_RE.finditer(body))
    micro = Counter(m.group(1).lower() for m in MICRO_RE.finditer(body))
    soft = Counter(m.group(1).lower() for m in SOFTENER_RE.finditer(body))
    neg_starts = sum(1 for p in paras if NEG_START_RE.search(p))
    short_single = sum(1 for p in paras if not dialogue_only(p) and words(p) <= 7)

    dialogue_runs = find_runs(
        paras,
        lambda p: dialogue_only(p) and words(p) <= 10,
        4,
    )
    staccato_runs = find_runs(
        paras,
        lambda p: (not dialogue_only(p)) and words(p) <= 7 and not p.startswith("**"),
        3,
    )
    neg_runs = find_runs(
        paras,
        lambda p: (not dialogue_only(p)) and NEG_START_RE.search(p) is not None and words(p) <= 12,
        2,
    )

    binary_candidates = 0
    echo_candidates = 0
    for i, p in enumerate(paras):
        # Heuristic only: short contrast paragraphs and repeated explanatory wrappers.
        if not dialogue_only(p) and CONTRAST_RE.search(p) and words(p) <= 16:
            binary_candidates += 1
            all_candidates.append((3, sid, "binary/negation", compact(p)))
        if re.search(r"\b(das|dies) (?:war|bedeutete|machte|hieß)\b", p, re.I) and words(p) <= 22:
            echo_candidates += 1
            all_candidates.append((2, sid, "possible explanation echo", compact(p)))

    # Formula families explicitly relevant for Eva-led prose.
    formula_patterns = {
        "Eva sah": len(re.findall(r"\bEva sah\b", body)),
        "Eva wusste": len(re.findall(r"\bEva wusste\b", body)),
        "Eva nickte": len(re.findall(r"\bEva nickte\b", body)),
        "Eva spürte": len(re.findall(r"\bEva spürte\b", body)),
        "Eva merkte": len(re.findall(r"\bEva merkte\b", body)),
        "Sie sah": len(re.findall(r"\bSie sah\b", body)),
        "Sie nickte": len(re.findall(r"\bSie nickte\b", body)),
        "Sie wusste": len(re.findall(r"\bSie wusste\b", body)),
        "Sie spürte": len(re.findall(r"\bSie spürte\b", body)),
    }

    for k, v in formula_patterns.items():
        all_formula[k] += v
    all_micro.update(micro)
    all_filters.update(filters)
    all_softeners.update(soft)

    for start, end in dialogue_runs:
        snippet = " / ".join(compact(p, 75) for p in paras[start:end][:7])
        all_candidates.append((7 + (end-start), sid, "dialogue pingpong", snippet))
    for start, end in staccato_runs:
        snippet = " / ".join(compact(p, 75) for p in paras[start:end][:7])
        all_candidates.append((6 + (end-start), sid, "staccato", snippet))
    for start, end in neg_runs:
        snippet = " / ".join(compact(p, 75) for p in paras[start:end][:7])
        all_candidates.append((8 + (end-start), sid, "negation run", snippet))

    if em:
        for p in paras:
            if "—" in p:
                all_candidates.append((20, sid, "FORBIDDEN em dash", compact(p)))

    rows.append({
        "sid": sid,
        "path": str(path),
        "words": wc,
        "em": em,
        "sondern": sondern,
        "dialogue": len(dialogue_runs),
        "staccato": len(staccato_runs),
        "neg_runs": len(neg_runs),
        "neg_starts": neg_starts,
        "filters": sum(filters.values()),
        "soft": sum(soft.values()),
        "short_single": short_single,
        "binary": binary_candidates,
        "echo": echo_candidates,
    })

    totals.update({
        "words": wc,
        "em": em,
        "sondern": sondern,
        "dialogue": len(dialogue_runs),
        "staccato": len(staccato_runs),
        "neg_runs": len(neg_runs),
        "neg_starts": neg_starts,
        "filters": sum(filters.values()),
        "soft": sum(soft.values()),
        "short_single": short_single,
        "binary": binary_candidates,
        "echo": echo_candidates,
    })

all_candidates.sort(key=lambda x: (-x[0], int(x[1][1:])))

lines = []
lines.append("# FINAL_PROSE_RHYTHM_AUDIT – ABWEICHUNG")
lines.append("")
lines.append("Status: **BASELINE / vor Rework**")
lines.append("")
lines.append("Automatischer Kandidaten-Audit nach `Buch-Framework/FINAL_PROSE_RHYTHM_PASS.md`. Die semantischen Treffer sind Review-Kandidaten, keine automatischen Änderungsbefehle.")
lines.append("")
lines.append("## Gesamtwerte")
lines.append("")
lines.append(f"- Szenen: **{len(scenes)}**")
lines.append(f"- Wörter in Szenen-Prosa: **{totals['words']}**")
lines.append(f"- Geviertstrich `—`: **{totals['em']}** (Hard Guard: 0)")
lines.append(f"- `sondern`: **{totals['sondern']}** (Hard Guard: 0)")
lines.append(f"- Dialog-Pingpong-Runs: **{totals['dialogue']}**")
lines.append(f"- Stakkato-Runs: **{totals['staccato']}**")
lines.append(f"- kurze Negations-Runs: **{totals['neg_runs']}**")
lines.append(f"- narrative Kurzabsätze ≤7 Wörter: **{totals['short_single']}**")
lines.append(f"- Filterwort-Treffer: **{totals['filters']}**")
lines.append(f"- Weichmacher-Treffer: **{totals['soft']}**")
lines.append(f"- heuristische Binary-/Negations-Kandidaten: **{totals['binary']}**")
lines.append(f"- heuristische Explanation-Echo-Kandidaten: **{totals['echo']}**")
lines.append("")

lines.append("## Szene für Szene")
lines.append("")
lines.append("| Szene | Wörter | — | Dialog | Stakkato | Neg.-Runs | Kurzabs. | Filter | Binary | Echo |")
lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
for r in rows:
    lines.append(
        f"| {r['sid']} | {r['words']} | {r['em']} | {r['dialogue']} | {r['staccato']} | {r['neg_runs']} | {r['short_single']} | {r['filters']} | {r['binary']} | {r['echo']} |"
    )
lines.append("")

lines.append("## Wiederkehrende Filter-/Mikro-Choreografie")
lines.append("")
lines.append("### Filterverben")
lines.append("")
for k, v in all_filters.most_common():
    lines.append(f"- `{k}`: {v}")
lines.append("")
lines.append("### Mikro-Choreografie")
lines.append("")
for k, v in all_micro.most_common():
    lines.append(f"- `{k}`: {v}")
lines.append("")
lines.append("### Eva-/Sie-Formeln")
lines.append("")
for k, v in all_formula.most_common():
    if v:
        lines.append(f"- `{k}`: {v}")
lines.append("")

lines.append("## Stärkste Kandidaten")
lines.append("")
for idx, (score, sid, family, snippet) in enumerate(all_candidates[:220], 1):
    lines.append(f"{idx}. **{sid} · {family} · score {score}** — {snippet}")
lines.append("")

# Preserve exact mechanical invariants for the audit itself.
if totals["sondern"] != 0:
    lines.append("## HARD-GUARD-FINDING")
    lines.append("")
    lines.append(f"`sondern` ist {totals['sondern']}× vorhanden und muss vor G4-Freeze adjudiziert/bereinigt werden.")
    lines.append("")
if totals["em"] != 0:
    lines.append("## HARD-GUARD-FINDING")
    lines.append("")
    lines.append(f"Geviertstrich `—` ist {totals['em']}× vorhanden. Für `de_anti_ki_prosa_v1` gilt 0.")
    lines.append("")

OUT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
print(f"wrote {OUT}: scenes={len(scenes)} words={totals['words']} em_dash={totals['em']} candidates={len(all_candidates)}")
