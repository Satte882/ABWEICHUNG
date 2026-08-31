# G5 Review Request – Produktion

status: REWORK
human_gate: G5
current_decision: REWORK
current_decided_by: human
current_date: 2026-08-31
prior_gate: `gates/G4.md`
source_manuscript: `78222a7e99c80378c35379ad42684ee332a412a6`
build_manifest: `production/BUILD_MANIFEST.md`
production_run: `33366125536`

## Human-Entscheidung

Human `G5-REWORK` vom 2026-08-31 lehnt den aktuellen Produktionsumfang als finalen Buchstand ab.

Der technische Build selbst bleibt korrekt und reproduzierbar:

- 40/40 Prosaszenen: PASS
- S001–S040 lückenlos: PASS
- `sondern = 0`: PASS
- Markdown-/HTML-Build: PASS
- GitHub Actions Run `33366125536`: PASS

Der Rework wird durch den **Produktumfang** ausgelöst:

**16.527 Wörter bei 40 Szenen** sind für den beabsichtigten vollständigen Roman nicht als finaler Umfang akzeptiert.

## Konsequenz

Der Produktionsstand `ABWEICHUNG_v01` bleibt als technischer Nachweis erhalten, ist aber **nicht G5-freigegeben**.

Das Manuskript wird kontrolliert wieder geöffnet. Ziel ist keine mechanische Wortzahlerhöhung, sondern substanzieller Ausbau von:

- Erlebnisdichte,
- Szenengewicht,
- körperlicher/klinischer Präsenz,
- Figuren- und Beziehungsdruck,
- Konsequenz und Nachwirkung,
- sinnvoll ausgespielten Entscheidungsprozessen.

Story- oder Szenenarchitektur wird nur dort geöffnet, wo die Ausbauanalyse zeigt, dass reine Prosa-Erweiterung nicht ausreicht.

## Nächster Schritt

1. Wortverteilung und Erlebnisdichte S001–S040 messen.
2. Ausbaupotenzial je Szene gegen `SZENE.md` und `BEATS.md` prüfen.
3. Rework-Ebene pro Abschnitt festlegen: `PROSA`, `BEAT`, `SZENE` oder bei echter Notwendigkeit upstream.
4. Ausbau durchführen.
5. betroffene Gates erneut prüfen; ein geändertes Gesamtmanuskript benötigt erneut G4.
6. erst danach neuer Produktionsbuild und erneuter Human Gate G5.

Aktuell:

**G5 REWORK → MANUSKRIPT-AUSBAUANALYSE**
