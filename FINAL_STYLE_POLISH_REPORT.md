# FINAL STYLE POLISH – ABWEICHUNG

status: PASS
scope: prose_only
trigger: external random-sample style review

## Ziel

Letzter chirurgischer Prosa-Pass gegen vier bestätigte Minor-Muster:

1. Erklär-Echos nach bereits verständlicher Handlung,
2. wiederkehrende Prägnanz-/Kontrastschlüsse,
3. sichtbar symmetrische Reihungen,
4. formelhafte Mikro-/Display-Choreografie, soweit sie keine eigene Funktion trägt.

Keine Story-, Beat-, Figuren- oder Kausalitätsänderung.

## Umfang

- gezielt bearbeitete Szenen: 13
- Änderungen ausschließlich in `PROSA.md`
- Stilprofil `de_anti_ki_prosa_v1` bleibt erhalten

## Regression

| Metrik | Vorher | Nachher |
|---|---:|---:|
| Wörter | 38013 | 37919 |
| Dialog-Pingpong-Runs | 26 | 26 |
| Stakkato-Runs | 7 | 3 |
| kurze Negations-Runs | 3 | 2 |
| Kurzabsätze ≤7 Wörter | 1129 | 1083 |
| Binary-/Negations-Kandidaten | 18 | 11 |
| Explanation-Echo-Kandidaten | 45 | 23 |
| Geviertstrich `—` | 0 | 0 |
| `sondern` | 0 | 0 |

Der Audit ist Kandidaten-Heuristik, kein Qualitätsautomat. Entscheidend war die semantische Auswahl der tatsächlich redundanten Stellen.
