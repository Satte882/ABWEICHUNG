#!/usr/bin/env python3
"""Build deterministic production artifacts from the G4-approved manuscript commit.

The canonical manuscript remains the distributed PROSA.md set at the supplied source ref.
This script derives a consolidated Markdown manuscript and a standalone HTML reading/print artifact.
It never rewrites source prose.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import subprocess
from pathlib import Path

PROSA_RE = re.compile(r"^BAUSTEINE/[^/]+/SZENEN/[^/]+/PROSA\.md$")
SCENE_ID_RE = re.compile(r"^scene_id:\s*S(\d+)\s*$", re.MULTILINE)
WORD_RE = re.compile(r"[A-Za-zÄÖÜäöüß0-9]+(?:['’\-][A-Za-zÄÖÜäöüß0-9]+)*")


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    return result.stdout


def content_at(ref: str, path: str) -> str:
    return git("show", f"{ref}:{path}").replace("\r\n", "\n")


def prose_body(content: str, path: str) -> tuple[int, str]:
    match = SCENE_ID_RE.search(content)
    if not match:
        raise ValueError(f"scene_id missing in {path}")
    scene_no = int(match.group(1))

    lines = content.splitlines()
    try:
        divider = lines.index("---")
    except ValueError as exc:
        raise ValueError(f"prose divider '---' missing in {path}") from exc

    body = "\n".join(lines[divider + 1 :]).strip()
    if not body:
        raise ValueError(f"empty prose body in {path}")
    return scene_no, body


def inline_html(text: str) -> str:
    escaped = html.escape(text, quote=False)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", escaped)
    return escaped


def body_to_html(body: str) -> str:
    paragraphs = re.split(r"\n\s*\n", body.strip())
    rendered: list[str] = []
    for paragraph in paragraphs:
        text = "\n".join(line.strip() for line in paragraph.splitlines()).strip()
        if not text:
            continue
        rendered.append(f"<p>{inline_html(text).replace(chr(10), '<br>')}</p>")
    return "\n".join(rendered)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-ref", required=True)
    parser.add_argument("--out-dir", required=True)
    args = parser.parse_args()

    source_commit = git("rev-parse", f"{args.source_ref}^{{commit}}").strip()
    source_tree = git("rev-parse", f"{args.source_ref}^{{tree}}").strip()

    all_paths = git("ls-tree", "-r", "--name-only", source_commit).splitlines()
    prosa_paths = sorted(path for path in all_paths if PROSA_RE.match(path))
    if len(prosa_paths) != 40:
        raise SystemExit(f"expected 40 PROSA.md files, found {len(prosa_paths)}")

    scenes: list[tuple[int, str, str]] = []
    for path in prosa_paths:
        scene_no, body = prose_body(content_at(source_commit, path), path)
        scenes.append((scene_no, path, body))

    scenes.sort(key=lambda item: item[0])
    scene_numbers = [number for number, _, _ in scenes]
    if scene_numbers != list(range(1, 41)):
        raise SystemExit(f"scene IDs must be S001-S040 exactly, got {scene_numbers}")

    full_text = "\n\n".join(body for _, _, body in scenes)
    forbidden = re.findall(r"\bsondern\b", full_text, flags=re.IGNORECASE)
    if forbidden:
        raise SystemExit(f"hard prose guard failed: found {len(forbidden)} occurrence(s) of 'sondern'")

    word_count = len(WORD_RE.findall(full_text))
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    md_path = out_dir / "ABWEICHUNG_v01.md"
    html_path = out_dir / "ABWEICHUNG_v01.html"
    info_path = out_dir / "BUILD_INFO.json"

    md_parts = ["# ABWEICHUNG", ""]
    for index, (_, _, body) in enumerate(scenes, start=1):
        md_parts.extend([f"## Kapitel {index}", "", body, ""])
    md_path.write_text("\n".join(md_parts).rstrip() + "\n", encoding="utf-8", newline="\n")

    chapters = []
    for index, (_, _, body) in enumerate(scenes, start=1):
        chapters.append(
            f'<section class="chapter"><h2>Kapitel {index}</h2>\n{body_to_html(body)}\n</section>'
        )

    html_doc = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>ABWEICHUNG</title>
<style>
@page {{ size: A5; margin: 18mm 16mm 20mm 18mm; }}
html {{ font-family: Georgia, 'Times New Roman', serif; color: #111; background: #fff; }}
body {{ max-width: 42rem; margin: 0 auto; padding: 2rem 1.25rem 5rem; font-size: 11.5pt; line-height: 1.5; }}
.title-page {{ min-height: 78vh; display: flex; align-items: center; justify-content: center; text-align: center; break-after: page; page-break-after: always; }}
h1 {{ font-size: 2.2rem; letter-spacing: .12em; font-weight: 600; }}
.chapter {{ break-before: page; page-break-before: always; }}
.chapter:first-of-type {{ break-before: auto; page-break-before: auto; }}
h2 {{ font-size: 1rem; text-align: center; font-weight: 400; margin: 0 0 3.5rem; letter-spacing: .08em; }}
p {{ margin: 0 0 .85em; text-align: justify; hyphens: auto; orphans: 2; widows: 2; }}
strong {{ font-weight: 600; }}
@media screen {{ .chapter {{ margin-top: 4rem; }} }}
</style>
</head>
<body>
<div class="title-page"><h1>ABWEICHUNG</h1></div>
{''.join(chapters)}
<!-- source_commit={source_commit}; source_tree={source_tree}; scenes=40; words={word_count} -->
</body>
</html>
"""
    html_path.write_text(html_doc, encoding="utf-8", newline="\n")

    info = {
        "title": "ABWEICHUNG",
        "source_commit": source_commit,
        "source_tree": source_tree,
        "scene_count": len(scenes),
        "scene_ids": [f"S{number:03d}" for number, _, _ in scenes],
        "word_count": word_count,
        "hard_guard_sondern_count": 0,
        "source_paths": [path for _, path, _ in scenes],
        "artifacts": {
            md_path.name: {"sha256": sha256(md_path), "bytes": md_path.stat().st_size},
            html_path.name: {"sha256": sha256(html_path), "bytes": html_path.stat().st_size},
        },
    }
    info_path.write_text(
        json.dumps(info, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    print(json.dumps(info, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
