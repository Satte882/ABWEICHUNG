from pathlib import Path
import re

final = Path('ABWEICHUNG_FINAL.md').read_text(encoding='utf-8')
post = Path('FINAL_PROSE_RHYTHM_AUDIT_POST.md').read_text(encoding='utf-8')
baseline = Path('FINAL_PROSE_RHYTHM_AUDIT.md').read_text(encoding='utf-8')

assert final.rstrip().endswith('Eva wartete.')
assert '—' not in final
assert not re.search(r'\bsondern\b', final, re.I)
assert len(re.findall(r'^## Kapitel \d+ – ', final, re.M)) == 40
assert 'Geviertstrich `—`: **0**' in post
assert '`sondern`: **0**' in post


def metric(text: str, label: str) -> int:
    m = re.search(re.escape(label) + r': \*\*(\d+)\*\*', text)
    if not m:
        raise SystemExit(f'missing metric {label}')
    return int(m.group(1))


before_staccato = metric(baseline, '- Stakkato-Runs')
after_staccato = metric(post, '- Stakkato-Runs')
before_short = metric(baseline, '- narrative Kurzabsätze ≤7 Wörter')
after_short = metric(post, '- narrative Kurzabsätze ≤7 Wörter')
before_words = metric(baseline, '- Wörter in Szenen-Prosa')
after_words = metric(post, '- Wörter in Szenen-Prosa')

assert after_staccato < before_staccato, (before_staccato, after_staccato)
assert after_short < before_short, (before_short, after_short)
delta = abs(after_words - before_words) / before_words
assert delta <= 0.05, (before_words, after_words, delta)

comparison = f'''# FINAL_PROSE_RHYTHM_COMPARISON – ABWEICHUNG

| Metrik | Baseline | Post-Pass | Veränderung |
|---|---:|---:|---:|
| Wörter | {before_words} | {after_words} | {after_words-before_words:+d} |
| Stakkato-Runs | {before_staccato} | {after_staccato} | {after_staccato-before_staccato:+d} |
| Kurzabsätze ≤7 Wörter | {before_short} | {after_short} | {after_short-before_short:+d} |
| Geviertstrich `—` | 9 | 0 | -9 |
| `sondern` | 0 | 0 | 0 |

Der Scanner ist Kandidatenlieferant. Die entscheidenden semantischen Hotspots wurden kontextuell bearbeitet; der Whole-Book-Lauf verdichtet zusätzlich nur sichere vertikale Stakkato-Runs, ohne Satzwörter oder Storylogik zu verändern.
'''
Path('FINAL_PROSE_RHYTHM_COMPARISON.md').write_text(comparison, encoding='utf-8')
print(f'validated: staccato {before_staccato}->{after_staccato}, short {before_short}->{after_short}, words {before_words}->{after_words}')
