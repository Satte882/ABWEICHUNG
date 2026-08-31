# ABWEICHUNG

**Wenn die Maschine recht hat**

Psychologischer Near-Future-Thriller über Ergebnisqualität, Verantwortung und die schleichende Verschiebung menschlicher Entscheidungsmacht.

> **Du darfst widersprechen.**  
> **Die Beweislast liegt bei dir.**

## Release-Status

Der Roman ist inhaltlich und produktionstechnisch abgeschlossen.

- G2: **APPROVED**
- G4: **APPROVED**
- G5: **APPROVED**
- 40 Kapitel
- 37.919 Wörter Szenen-Prosa
- finale Manuskriptfreigabe: `1014deda39ae5c5503558fabd88bf8b519b56548`
- finaler Produktions-Snapshot: `268b580e3345d842eba5e3e0a30b5aed79db05bf`
- DOCX-QA: PASS
- CI-PDF-Render: 333 Seiten
- Format: 5,06 × 7,81 Zoll / 12,85 × 19,84 cm
- letzter Satz: `Eva wartete.`

Verbindliche Gate-Records liegen unter `gates/`.

## Finale Buchdateien

| Zweck | Datei |
|---|---|
| finales Manuskript | `ABWEICHUNG_FINAL.md` |
| KDP-/Word-Innenraum | `ABWEICHUNG_FINAL.docx` |
| KDP Full-Wrap-Cover | `ABWEICHUNG_COVER.pdf` |

## Amazon KDP

| Zweck | Datei |
|---|---|
| Buchbeschreibung | `BUCHBESCHREIBUNG_KDP.md` |
| Metadaten, Keywords, Kategorien, Preis-/ISBN-Strategie | `KDP_METADATA.md` |
| operative Upload-/Submission-Checkliste | `KDP_SUBMISSION.md` |
| verbindliche Cover-Spezifikation | `COVER_SPEC.md` |

Das Cover ist für den aktuellen **333-Seiten-Stand, Schwarzweiß auf weißem Papier** erzeugt. Die Live-Seitenzahl im KDP-Previewer bleibt für die endgültige Rückenbreite maßgeblich. Ändert KDP die Seitenzahl, wird dasselbe Design mit `scripts/build_kdp_cover.py` neu erzeugt.

## Aktive Story-/Research-Quellen

- `BOOK_IDEA.md` – Grundidee und irreversible Konzeptentscheidungen
- `STORY_PACKAGE.md` – vollständige Story-, Konflikt- und Informationsarchitektur
- `CHARACTERS.md` – Figurenlogik
- `TITLE_DECISION.md` – Titelentscheidung
- `RESEARCH_REGISTER.md` – Research- und Plausibilitätsregister
- `R06_MEDIZINISCHE_ANKERFAELLE.md` – medizinische Ankerfälle
- `BAUSTEINE/` – Bausteine, Ereignisse, Beats, Szenenkarten und kanonische Szenen-Prosa

## Finale Qualitätsnachweise

Diese vier Dateien bleiben bewusst im Root, weil die finalen Gate-Records darauf verweisen:

- `FINAL_STYLE_POLISH_REPORT.md`
- `FINAL_STYLE_POLISH_AUDIT_POST.md`
- `EXTERNAL_STYLE_RETEST_RESULT.md`
- `EXTERNAL_STYLE_RETEST_ADJUDICATION.md`

Abgeschlossene Task-, Review-, Rework-, Gate-Request- und Zwischen-Audit-Artefakte liegen unter `ARCHIV/` und sind keine aktive Source of Truth.

## Technik

- `scripts/build_final_manuscript.py` – konsolidiert das finale Manuskript
- `scripts/build_final_docx.py` – erzeugt die KDP-/Word-Ausgabe
- `scripts/build_kdp_cover.py` – erzeugt das Full-Wrap-Cover
- `.github/workflows/finalize-direct.yml` – finaler Manuskript-/DOCX-Build
- `.github/workflows/build-kdp-cover.yml` – Cover-Build und PDF-Preflight

## Arbeitsregel ab G5

Story und Prosa sind eingefroren. KDP-/Produktionsarbeit darf **keine neue Story-, Figuren- oder Stilentscheidung** in das freigegebene Manuskript einführen.