#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "expansion_audit"
WORD_RE = re.compile(r"\b[\wÄÖÜäöüß’'-]+\b", re.UNICODE)
SONDERN_RE = re.compile(r"\bsondern\b", re.IGNORECASE)


def prose_body(text: str) -> str:
    parts = text.split("\n---\n", 1)
    return parts[1].strip() if len(parts) == 2 else text


def meta(text: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", text)
    return m.group(1).strip() if m else ""


def main() -> int:
    paths = sorted(ROOT.glob("BAUSTEINE/**/PROSA.md"))
    rows = []
    total_words = 0
    total_sondern = 0
    total_paras = 0
    short_paras = 0
    very_short_paras = 0

    for path in paths:
        text = path.read_text(encoding="utf-8")
        body = prose_body(text)
        words = WORD_RE.findall(body)
        paragraphs = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
        para_counts = [len(WORD_RE.findall(p)) for p in paragraphs]
        sondern_count = len(SONDERN_RE.findall(body))
        scene_id = meta(text, "scene_id")
        status = meta(text, "prose_status")
        rel = path.relative_to(ROOT).as_posix()

        total_words += len(words)
        total_sondern += sondern_count
        total_paras += len(para_counts)
        short_paras += sum(n <= 7 for n in para_counts)
        very_short_paras += sum(n <= 3 for n in para_counts)

        rows.append({
            "scene_id": scene_id,
            "status": status,
            "words": len(words),
            "sondern": sondern_count,
            "paragraphs": len(para_counts),
            "short_para_share": round(sum(n <= 7 for n in para_counts) / len(para_counts), 4) if para_counts else 0,
            "path": rel,
        })

    scene_ids = [r["scene_id"] for r in rows]
    expected_ids = [f"S{i:03d}" for i in range(1, 41)]
    scene_id_ok = scene_ids == expected_ids
    scene_count_ok = len(rows) == 40
    expanded_count = sum(r["status"] == "expansion_rework" for r in rows)

    summary = {
        "scene_count": len(rows),
        "scene_count_ok": scene_count_ok,
        "scene_ids_ok": scene_id_ok,
        "expanded_count": expanded_count,
        "total_words": total_words,
        "mean_words_per_scene": round(total_words / len(rows), 2) if rows else 0,
        "sondern_count": total_sondern,
        "paragraph_count": total_paras,
        "short_para_share_le_7": round(short_paras / total_paras, 4) if total_paras else 0,
        "very_short_para_share_le_3": round(very_short_paras / total_paras, 4) if total_paras else 0,
        "guard_pass": scene_count_ok and scene_id_ok and total_sondern == 0,
    }

    OUT.mkdir(exist_ok=True)
    (OUT / "AUDIT.json").write_text(json.dumps({"summary": summary, "scenes": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Expansion Audit – ABWEICHUNG",
        "",
        f"- scenes: {summary['scene_count']} / 40",
        f"- scene IDs S001–S040: {'PASS' if summary['scene_ids_ok'] else 'FAIL'}",
        f"- `expansion_rework`: {summary['expanded_count']} / 40",
        f"- total words: {summary['total_words']}",
        f"- mean words/scene: {summary['mean_words_per_scene']}",
        f"- `sondern`: {summary['sondern_count']}",
        f"- paragraphs <= 7 words: {summary['short_para_share_le_7']:.1%}",
        f"- paragraphs <= 3 words: {summary['very_short_para_share_le_3']:.1%}",
        f"- hard guard: {'PASS' if summary['guard_pass'] else 'FAIL'}",
        "",
        "| Scene | Status | Words | sondern | <=7-word paragraphs |",
        "|---|---|---:|---:|---:|",
    ]
    for r in rows:
        lines.append(f"| {r['scene_id']} | {r['status']} | {r['words']} | {r['sondern']} | {r['short_para_share']:.1%} |")
    (OUT / "AUDIT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if summary["guard_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
