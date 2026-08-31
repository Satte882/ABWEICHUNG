# BUILD MANIFEST – ABWEICHUNG

status: BUILD_PASS
date: 2026-08-31
format: consolidated Markdown + standalone HTML reading/print artifact
artifact_name: `abweichung-production-v01`
human_gate: G5 pending

## Freigegebene Quelle

- G4-approved manuscript commit: `78222a7e99c80378c35379ad42684ee332a412a6`
- source tree: `cc5639e85d27c0ed7403871af0989994bd0e4dd4`
- `gates/G4.md`: G4 APPROVED
- 40/40 `PROSA.md`
- scene IDs: S001–S040 vollständig
- hard guard `sondern`: 0

## Builder

- `scripts/build_production.py`
- Workflow: `.github/workflows/production-build.yml`
- Build arbeitet absichtlich gegen den festen G4-Commit und nicht gegen den jeweils aktuellen `main`.

Erzeugte Dateien:

1. `ABWEICHUNG_v01.md` – konsolidierte Lesefassung
2. `ABWEICHUNG_v01.html` – standalone Lese-/Druckartefakt
3. `BUILD_INFO.json` – Produktionsidentität und Hashes

## Kanonischer Produktionsnachweis

GitHub Actions:

- Workflow: `Production Build`
- Run #1 / ID: `33366125536`
- Build-Commit: `2be09a54645c6d1b77b7932c1b3cc93f8caaf1a2`
- Ergebnis: **PASS**
- Artifact-ID: `9748335150`
- Artifact-Name: `abweichung-production-v01`
- Artifact-Größe: 83.842 Bytes
- Artifact-ZIP SHA-256: `b6d6fde371e14d9f2f03b5e4a5839ff1e85e72f03345ab508c31373bb3e0d765`
- Artifact-Ablaufdatum: 2026-11-29T06:55:05Z

### Output-Hashes

- `ABWEICHUNG_v01.md`
  - Bytes: 120.412
  - SHA-256: `9c00cb0632b0729f43bf0d74f565573d52a794de4d6227eac06a3cf966ff478d`

- `ABWEICHUNG_v01.html`
  - Bytes: 137.108
  - SHA-256: `debc8a08023ca793c4ab4b35c2e5c428d3eb94f4d9ce97dcbd6bdfe3e12b4be4`

## Produktions-QA

PASS:

- G4-Source-Commit exakt bestätigt,
- 40 `PROSA.md` gefunden,
- S001–S040 exakt und lückenlos,
- `sondern = 0`,
- konsolidiertes Markdown erzeugt,
- standalone HTML erzeugt,
- Hashes erzeugt,
- GitHub-Actions-Artefakt erfolgreich hochgeladen.

## Produktumfang

Der deterministische Build zählt im vollständigen G4-Manuskript:

**16.527 Wörter**

bei 40 Szenen.

Diese Zahl war vor G4 nicht als feste Produktionskennzahl etabliert. Deshalb wird sie nicht rückwirkend zu einem automatischen G4-Fehler erklärt.

Sie ist jedoch für G5 eine **verpflichtende Produkt-Scope-Entscheidung**: Ein `G5-APPROVE` akzeptiert diesen Umfang bewusst als finalen Produktionsumfang. Wenn ein deutlich längerer Roman beabsichtigt ist, muss `G5-REWORK` gewählt und der Manuskriptstand wieder geöffnet werden.

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

Diese weiteren Formate dürfen nach einem G5-Rework bzw. als bewusst definierte Produktionsvariante ergänzt werden; sie sind nicht stillschweigend Teil dieses Builds.
