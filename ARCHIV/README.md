# ARCHIV – ABWEICHUNG

Dieser Ordner enthält abgeschlossene Entwicklungs-, Review-, Gate-, Workflow-, Skript- und Produktionsartefakte. Sie bleiben vollständig im Repository erhalten, sind aber **keine aktive Source of Truth** mehr.

## Struktur

- `ARCHIV/REVIEWS/` – externe Reviews, Adjudikationen, Rework-/Regression-Berichte, Rhythmus-/Stil-Audits, Self-Reviews und finale Stil-QA-Nachweise
- `ARCHIV/GATES/` – abgeschlossene Gate-Review-Requests; die verbindlichen Gate-Records bleiben unter `gates/`
- `ARCHIV/WORKFLOW/` – Fresh-Context-Tasks/-Results und historische Ausbau-/Arbeitsanalysen
- `ARCHIV/WORKFLOWS/` – nicht mehr aktive GitHub-Actions-Workflows
- `ARCHIV/SCRIPTS/` – nicht mehr aktive Rework-, Audit- und historische Produktionsskripte
- `ARCHIV/PRODUCTION/` – historische Produktionsmanifeste und frühere Produktionsnachweise
- `ARCHIV/PROJECT/` – projektbezogene Lessons Learned

## Aktive Quellen

Maßgeblich bleiben insbesondere:

- `ABWEICHUNG_FINAL.md`
- `ABWEICHUNG_FINAL.docx`
- `ABWEICHUNG_COVER.pdf`
- `BOOK_IDEA.md`
- `STORY_PACKAGE.md`
- `CHARACTERS.md`
- `RESEARCH_REGISTER.md`
- `R06_MEDIZINISCHE_ANKERFAELLE.md`
- `BAUSTEINE/`
- `gates/`
- `BUCHBESCHREIBUNG_KDP.md`
- `KDP_METADATA.md`
- `KDP_SUBMISSION.md`
- `COVER_SPEC.md`
- aktive Build-Skripte und Workflows laut Root-`README.md`

## Bereinigungsregel

**Nichts wird zur Bereinigung inhaltlich gelöscht.** Ein abgeschlossenes oder nicht mehr aktives Artefakt wird in den passenden `ARCHIV/`-Unterordner verschoben. Referenzen aus aktiven Gate-/Build-Dateien werden auf den Archivpfad aktualisiert.
