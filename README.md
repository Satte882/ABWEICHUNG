# ABWEICHUNG

**Zwischen Mensch und System**

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

Das Cover ist für den aktuellen **333-Seiten-Stand, Schwarzweiß auf weißem Papier** erzeugt. Die Live-Seitenzahl im KDP-Previewer bleibt für die endgültige Rückenbreite maßgeblich. Ändert KDP die Seitenzahl, wird dasselbe Design mit `scripts/build_kdp_cover.py` neu erzeugt. Der Rücken enthält keinen Text; sein vertikales Linien-/Ausschlagmotiv ist exakt das um 90° gedrehte Vorderseitenmotiv und wird als ein durchgängiger Pfad erzeugt. Die Rückseite enthält ausschließlich eine gerade horizontale Flatline.

## Marketing / A+ Content

Amazon-KDP-A+-Content wird in diesem Repo zunächst als **reale Teststrecke für ABWEICHUNG** entwickelt.

- `MARKETING/A_PLUS_REFERENCE.md` – Amazon-Regeln, Modullogik, Bild-/Textanforderungen, Erstellungsprozess und Compliance-Check
- `MARKETING/README.md` – Arbeitsmodell für Konzept, Produktion, QA, Submission und späteren Lessons-Learned-Transfer

Nach Abschluss der A+-Teststrecke werden ausschließlich die **generalisierbaren** Erkenntnisse in `Satte882/Buch-Framework` übernommen. Buchspezifische Texte, Motive und Geschmacksentscheidungen bleiben in diesem Repo.

## Aktive Story-/Research-Quellen

- `BOOK_IDEA.md` – Grundidee und irreversible Konzeptentscheidungen
- `STORY_PACKAGE.md` – vollständige Story-, Konflikt- und Informationsarchitektur
- `CHARACTERS.md` – Figurenlogik
- `TITLE_DECISION.md` – Titelentscheidung
- `RESEARCH_REGISTER.md` – Research- und Plausibilitätsregister
- `R06_MEDIZINISCHE_ANKERFAELLE.md` – medizinische Ankerfälle
- `BAUSTEINE/` – Bausteine, Ereignisse, Beats, Szenenkarten und kanonische Szenen-Prosa

## Archivregel

Der Root enthält nur aktive Buch-, KDP-, Gate- und Build-Quellen. Abgeschlossene Task-, Review-, Rework-, Audit-, alte Produktions- und nicht mehr aktive Build-Artefakte liegen unter `ARCHIV/`.

**Es wird für die Repo-Bereinigung nichts inhaltlich verworfen.** Dateien werden aus dem aktiven Bereich in das Archiv verschoben; historische Binär- und Textinhalte bleiben dort erhalten.

Die finalen Stil-QA-Nachweise liegen unter `ARCHIV/REVIEWS/`; `gates/G4.md` und `gates/G5.md` referenzieren die Archivpfade direkt.

## Aktive Technik

- `scripts/build_final_manuscript.py` – konsolidiert das finale Manuskript
- `scripts/build_final_docx.py` – erzeugt die KDP-/Word-Ausgabe
- `scripts/build_kdp_cover.py` – erzeugt das Full-Wrap-Cover und erzwingt die Titel-Sicherheitszone
- `.github/workflows/finalize-direct.yml` – finaler Manuskript-/DOCX-Build
- `.github/workflows/build-kdp-cover.yml` – Cover-Build, PDF-Preflight und PNG-Preview

Historische Skripte, Workflows und Produktionsnachweise liegen unter `ARCHIV/SCRIPTS/`, `ARCHIV/WORKFLOWS/` und `ARCHIV/PRODUCTION/`.

## Arbeitsregel ab G5

Story und Prosa sind eingefroren. KDP-/Produktionsarbeit darf **keine neue Story-, Figuren- oder Stilentscheidung** in das freigegebene Manuskript einführen.
