from __future__ import annotations

from pathlib import Path
import re

from build_final_manuscript import FRONT, TITLES

SCENE_GLOB = "BAUSTEINE/*/SZENEN/*/PROSA.md"
WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß0-9]+(?:['’\-][A-Za-zÄÖÜäöüß0-9]+)*")


def words(text: str) -> int:
    return len(WORD_RE.findall(text))


def is_dialogue(p: str) -> bool:
    t = p.strip()
    return (t.startswith("„") and t.endswith("“")) or (t.startswith("»") and t.endswith("«"))


def is_special(p: str) -> bool:
    t = p.strip()
    return (
        t.startswith("**")
        or t.startswith("*")
        or t.startswith("#")
        or t.startswith(">")
        or t.startswith("`")
        or t.endswith(":")
    )


def compact_staccato(paras: list[str]) -> tuple[list[str], int]:
    """Collapse only obvious vertical staccato runs.

    Wording and sentence boundaries stay untouched; the operation changes paragraph
    rhythm, not story content. Dialogue, display/system text, emphasis and the final
    paragraph are protected.
    """
    out: list[str] = []
    merged_runs = 0
    i = 0
    last = len(paras) - 1

    while i < len(paras):
        p = paras[i]
        eligible = (
            i != last
            and not is_dialogue(p)
            and not is_special(p)
            and words(p) <= 7
        )
        if not eligible:
            out.append(p)
            i += 1
            continue

        j = i
        run: list[str] = []
        while j < len(paras):
            q = paras[j]
            q_eligible = (
                j != last
                and not is_dialogue(q)
                and not is_special(q)
                and words(q) <= 7
            )
            if not q_eligible:
                break
            run.append(q)
            j += 1

        if len(run) >= 3:
            out.append(" ".join(run))
            merged_runs += 1
            i = j
        else:
            out.extend(run)
            i = j

    return out, merged_runs


def scene_id(text: str, path: Path) -> str:
    m = re.search(r"^scene_id:\s*(S\d+)\s*$", text, re.M)
    if not m:
        raise SystemExit(f"missing scene_id in {path}")
    return m.group(1)


def main() -> None:
    scene_rows = []
    touched: list[str] = []
    merged_total = 0
    em_total = 0

    for path in sorted(Path(".").glob(SCENE_GLOB)):
        original = path.read_text(encoding="utf-8")
        sid = scene_id(original, path)
        if "\n---\n" not in original:
            raise SystemExit(f"missing separator in {path}")
        meta, body = original.split("\n---\n", 1)
        body = body.strip()

        em_count = body.count("—")
        em_total += em_count
        body = body.replace("—", "–")

        paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
        paras, merged = compact_staccato(paras)
        merged_total += merged
        body = "\n\n".join(paras).strip()

        candidate = meta.replace("prose_status: expansion_rework", "prose_status: final_rhythm_rework")
        candidate = candidate.rstrip() + "\n\n---\n\n" + body + "\n"

        if candidate != original:
            path.write_text(candidate, encoding="utf-8")
            touched.append(sid)

        scene_rows.append((int(sid[1:]), sid, path, body))

    scene_rows.sort()
    if [n for n, *_ in scene_rows] != list(range(1, 41)):
        raise SystemExit(f"scene sequence invalid: {[sid for _, sid, *_ in scene_rows]}")

    # Deterministic whole-book aggregation from the canonical scene prose sources.
    chapters = []
    for n, sid, path, _ in scene_rows:
        text = path.read_text(encoding="utf-8")
        body = text.split("\n---\n", 1)[1].strip()
        chapters.append(f"## Kapitel {n} – {TITLES[n-1]}\n\n{body}")

    final = FRONT + "\n\n".join(chapters).rstrip() + "\n"
    Path("ABWEICHUNG_FINAL.md").write_text(final, encoding="utf-8")

    # Hard regression guards.
    if "—" in final:
        raise SystemExit("forbidden em dash remains")
    if re.search(r"\bsondern\b", final, re.I):
        raise SystemExit("forbidden 'sondern' remains")
    headings = re.findall(r"^## Kapitel (\d+) – .+$", final, re.M)
    if headings != [str(i) for i in range(1, 41)]:
        raise SystemExit(f"chapter sequence invalid: {headings}")
    if not final.rstrip().endswith("Eva wartete."):
        raise SystemExit("protected ending changed")

    total_words = 0
    for _, _, path, _ in scene_rows:
        body = path.read_text(encoding="utf-8").split("\n---\n", 1)[1]
        total_words += words(body)

    report = [
        "# FINAL_PROSE_RHYTHM_APPLIED – ABWEICHUNG",
        "",
        "Status: **WHOLE-BOOK PASS APPLIED / vor Human-G4-Reapprove**",
        "",
        "Der horizontale Prosa-/Rhythmuspass wurde auf die 40 kanonischen `PROSA.md`-Szenen angewendet.",
        "",
        "## Deterministische Eingriffe",
        "",
        f"- Geviertstriche `—` ersetzt: **{em_total}**",
        f"- vertikale Stakkato-Runs konservativ zu normalen Prosapara­grafen verdichtet: **{merged_total}**",
        f"- berührte Szenen: **{len(touched)} / 40**",
        f"- Szenen-Prosa-Wortzahl nach Pass: **{total_words}**",
        "- `sondern`: **0**",
        "- Geviertstrich `—`: **0**",
        "- geschütztes Ende: **`Eva wartete.`**",
        "",
        "## Semantische Eingriffe",
        "",
        "Vor diesem Whole-Book-Lauf wurden die stärksten bestätigten Rhythmus-/KI-Prosa-Hotspots bereits kontextuell überarbeitet, darunter Opening, frühe Governance-Passage, zentrale Ressourcen-Gegenrechnung und Finale/Nachhall. Der automatische Teil dieses Skripts verändert keine Satzwörter außer dem typografischen Hard Guard; er normalisiert nur nachweislich überhäufte vertikale Kurzabsatz-Runs.",
        "",
        "## Gate-Folge",
        "",
        "Der Text ist ein neuer Manuskriptstand und benötigt einen erneuten G4-Fresh-Context-Check sowie Human-G4-REAPPROVE. Der bisherige G5-Produktionsstand ist bis zum Neubuild stale.",
        "",
    ]
    Path("FINAL_PROSE_RHYTHM_APPLIED.md").write_text("\n".join(report), encoding="utf-8")
    print(f"applied: touched={len(touched)} merged_runs={merged_total} em_dash={em_total} words={total_words}")


if __name__ == "__main__":
    main()
