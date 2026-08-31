# G5 Review Request – Produktion

status: READY_FOR_HUMAN_G5
human_gate: G5
prior_gate: `gates/G4.md`
source_manuscript: `78222a7e99c80378c35379ad42684ee332a412a6`
build_manifest: `production/BUILD_MANIFEST.md`
production_run: `33366125536`
product_scope_decision_required: yes

## Produktionsstand

Der G4-freigegebene Manuskriptstand wurde reproduzierbar in einen konkreten Produktionsstand überführt.

Erzeugte Artefakte:

- `ABWEICHUNG_v01.md` – konsolidierte Manuskriptfassung
- `ABWEICHUNG_v01.html` – standalone Lese-/Druckfassung
- `BUILD_INFO.json` – Hash-/Quellnachweis

GitHub Actions Run #1 / ID `33366125536`: **PASS**.

Artifact:

- ID `9748335150`
- Name `abweichung-production-v01`
- ZIP SHA-256 `b6d6fde371e14d9f2f03b5e4a5839ff1e85e72f03345ab508c31373bb3e0d765`

Produktions-QA:

- G4-Commit exakt: PASS
- 40/40 Prosaszenen: PASS
- S001–S040 lückenlos: PASS
- `sondern = 0`: PASS
- Build/Upload: PASS

## Produkt-Scope – vor G5 bewusst zu entscheiden

Der Build misst erstmals den vollständigen Manuskriptumfang belastbar:

**16.527 Wörter** bei 40 Szenen.

Vor G4 existierte kein explizit freigegebener Ziel-Wortumfang. Deshalb ist dies kein nachträglich erfundener mechanischer G4-Blocker.

Für die Produktionsfreigabe ist die Konsequenz aber wesentlich:

### `G5-APPROVE`

Akzeptiert den aktuellen G4-Manuskriptstand **mit 16.527 Wörtern** bewusst als finalen Buch-/Produktionsumfang und gibt den oben identifizierten Markdown-/HTML-Produktionsstand frei.

### `G5-REWORK`

Bedeutet: Der aktuelle Build ist technisch korrekt, aber der Produktumfang soll **nicht** als final gelten. Das Manuskript muss bewusst wieder geöffnet und substanziell erweitert bzw. anders als Produkt positioniert werden. Danach sind die betroffenen Gates erneut zu durchlaufen.

### `G5-STOP`

Stoppt die Produktion ohne Freigabe.

## Nicht Bestandteil dieses G5-Stands

- kein erfundener Autorenname,
- kein Impressum,
- keine ISBN,
- kein Cover,
- kein KDP-spezifisches Interior,
- kein DOCX/PDF als freizugebendes Hauptartefakt.

Der aktuelle G5-Entscheid betrifft ausschließlich den **reproduzierbaren konsolidierten Markdown-/HTML-Produktionsstand** aus dem G4-Manuskript und die bewusste Akzeptanz seines Umfangs.

## Gate

Erforderlicher Human-Token:

`G5-APPROVE`  
oder  
`G5-REWORK`  
oder  
`G5-STOP`
