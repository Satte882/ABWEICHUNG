# BUILD MANIFEST – ABWEICHUNG

status: BUILD_PASS
date: 2026-08-31
format: consolidated Markdown + standalone HTML reading/print artifact
artifact_name: `abweichung-production-g5-rebuild`
human_gate: G5 pending

## Freigegebene Quelle

- G4-approved manuscript commit: `14563bc5ea63d2b77c10e63f1d23a751e136c617`
- source tree: `fbbe9704813f27251b1d5e9e77d89b1ba419ee02`
- `gates/G4.md`: G4 REAPPROVED
- 40/40 `PROSA.md`
- scene IDs: S001–S040 vollständig
- hard guard `sondern`: 0
- Wortzahl: 39.331

## Builder

- `scripts/build_production.py`
- Workflow: `.github/workflows/production-build.yml`
- Build arbeitet deterministisch gegen den festen G4-approved Commit und nicht gegen den aktuellen `main`.

Erzeugte Dateien:

1. `ABWEICHUNG_v01.md` – konsolidierte Lesefassung
2. `ABWEICHUNG_v01.html` – standalone Lese-/Druckartefakt
3. `BUILD_INFO.json` – Produktionsidentität und Hashes

## Kanonischer Produktionsnachweis

GitHub Actions:

- Workflow: `Production Build`
- Run #3 / ID: `33377576980`
- Workflow-Commit: `68eb5d738e08be2fecb45eed614eba7412dcc55d`
- Ergebnis: **PASS**
- Artifact-ID: `9752446466`
- Artifact-Name: `abweichung-production-g5-rebuild`
- Artifact-Größe: 188.686 Bytes
- Artifact-ZIP SHA-256: `c9379c14893e09b1051d59f24d64304d1dfd37d6d27d7ceedd9541e07ab6b180`
- Artifact-Ablaufdatum: 2026-11-29T09:25:16Z

### Output-Hashes

- `ABWEICHUNG_v01.md`
  - Bytes: 284.933
  - SHA-256: `ab4fe873ee91482da1d10a8bf16f148a569a283c66e6dcbb8a5a2c2df11d4a31`

- `ABWEICHUNG_v01.html`
  - Bytes: 319.019
  - SHA-256: `1ccd519396d71d03a83de7190a83b5de34a20ec946e8dd6df2d17743980c7954`

## Produktions-QA

PASS:

- G4-Source-Commit exakt bestätigt,
- 40 `PROSA.md` gefunden,
- S001–S040 exakt und lückenlos,
- Build-Wortzahl exakt 39.331,
- `sondern = 0`,
- konsolidiertes Markdown erzeugt,
- standalone HTML erzeugt,
- Hashes erzeugt und geprüft,
- GitHub-Actions-Artefakt erfolgreich hochgeladen.

## Produktumfang

Der deterministische Build zählt im vollständigen G4-freigegebenen Manuskript:

**39.331 Wörter**

bei 40 Szenen.

Der frühere G5-Rework-Auslöser von 16.527 Wörtern ist damit behoben. Die neue Wortzahl ist Ergebnis des freigegebenen inhaltlichen Ausbaus und kein künstliches Produktions-Padding.

## Vorheriger Build

Der erste Build aus `78222a7e99c80378c35379ad42684ee332a412a6` mit 16.527 Wörtern bleibt historischer technischer Nachweis, wurde durch Human `G5-REWORK` jedoch nicht als finaler Produktstand freigegeben.

## Scope des aktuellen Artefakts

Das aktuelle Produktionsformat ist bewusst minimal und reproduzierbar:

- Lesen / Review / Drucken: ja
- konsolidierte Manuskriptdatei: ja
- standalone HTML: ja
- DOCX: noch nicht Teil dieses Produktionsstands
- PDF: noch nicht Teil dieses Produktionsstands
- KDP-spezifisches Interior: nein
- Cover: nein
- ISBN/Impressum/Autor-Metadaten: nicht erfunden

Diese weiteren Formate sind Folgeprodukte nach G5 und kein stillschweigender Bestandteil der Manuskriptfreigabe.
