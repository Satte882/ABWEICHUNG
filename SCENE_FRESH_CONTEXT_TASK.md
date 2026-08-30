# Fresh-Context-Task – Szenen-/Beat-Re-Review ABWEICHUNG

review_target: `78222a7e99c80378c35379ad42684ee332a412a6`
review_scope: full scene + beat layer, whole-book distribution
review_mode: independent semantic and scene-shape review

## Clean-Room-Voraussetzung

Dieser Auftrag darf nur in einer wirklich kontextfreien Session ausgeführt werden.

Wenn du bereits Kenntnis hast von:

- früheren Manuskript-Reviews,
- konkreten Findings oder Rework-Diskussionen,
- früheren Korrekturen einzelner Szenen,
- Bewertungen anderer Reviewer,

antworte ausschließlich:

`review_status: CONTAMINATED`

und beende den Auftrag.

## Verbindlicher Zielstand

Prüfe ausschließlich den Repository-Stand des Commits:

`78222a7e99c80378c35379ad42684ee332a412a6`

Nicht den aktuellen Branch-Head, falls dieser inzwischen weitergelaufen ist.

## Erlaubte Quellen

Am Ziel-Commit darfst du lesen:

1. `BOOK_IDEA.md`
2. `STORY_PACKAGE.md`
3. `CHARACTERS.md`
4. `RESEARCH_REGISTER.md`
5. `R06_MEDIZINISCHE_ANKERFAELLE.md`
6. alle `BAUSTEINE/**/BAUSTEIN.md`
7. alle `BAUSTEINE/**/EREIGNISSE/EREIGNISSE.md`
8. alle `BAUSTEINE/**/SZENEN/**/SZENE.md`
9. alle `BAUSTEINE/**/SZENEN/**/BEATS.md`

## Verbotene Quellen

Nicht öffnen oder verwenden:

- alle `PROSA.md`
- `LESSONS_LEARNED.md`
- `FULL_MANUSCRIPT_SELF_REVIEW.md`
- `MANUSCRIPT_FRESH_CONTEXT_RESULT.md`
- frühere `*_REVIEW_*`-Ergebnisse
- frühere Fresh-Context-Ergebnisse
- `gates/`
- Issues, PRs, Commit-Nachrichten oder Diffs
- frühere Chats oder Memory

Wenn du versehentlich eine verbotene Quelle inhaltlich gelesen hast, gilt der Review als kontaminiert.

## Kernauftrag

Prüfe die **gesamte Szenen- und Beat-Ebene als Romanarchitektur**, nicht nur einzelne Dateien.

### A. G1-/Event-Treue

- Sind E001–E054 vollständig abgedeckt?
- Bleiben Ursache, Entscheidung und Folge der Ereignisse unverändert?
- Werden keine neuen plotrelevanten Kausalitäten oder Gegenfakten eingeführt?
- Bleiben Figurenverantwortung und Informationsreihenfolge korrekt?

### B. Kritische Storyketten

Prüfe besonders:

- Nele trägt ihren Override selbst; Eva übernimmt später Kultur-/Mentoring-Verantwortung, nicht direkte Mitentscheidung.
- Midpoint bleibt Evas eigene Bilanz und widerlegt nicht KORA durch einen neuen Systemfehler.
- Felix: Prozessumgehung wird vor Absicht bewiesen; Absicht wird erst in der Konfrontation bestätigt; kein sicherer alternativer Patientenausgang.
- Wert-/Kontextweg wird vor dem Finale klar gesetzt und begrenzt.
- Nähe/Behandlerbindung allein reichen im Falkenried-Ressourcenkonflikt nicht.
- Solo-Break-glass bleibt technisch real.
- Finale bleibt aus den vorher gesetzten Regeln ableitbar.

### C. Beat Readiness

- Granularisieren die Beats weiterhin ausschließlich die jeweilige Szene?
- Gibt es neue storyrelevante Entscheidungen, die erst in Prosa erfunden werden müssten?
- Gibt es Beats, die Szenenfunktion oder G1-Information verschieben?

### D. Whole-Book Scene-Shape Review – entscheidend

Beurteile zusätzlich die **dramaturgische Trägerform** jeder Szene und ihre Verteilung über S001–S040.

Mögliche Träger sind z. B.:

- klinische Handlung,
- Ressourcenkonflikt,
- persönliche Konfrontation,
- Solo-Analyse/Reflexion,
- Datenreview,
- Governance-/Regeldesign,
- Audit/Investigation,
- praktische Anwendung einer Regel,
- Implementationstest,
- Nachhall/Beziehung.

Die genaue Taxonomie ist nicht wichtig. Entscheidend ist, ob die Szenenfolge als Leseerlebnis variiert.

Prüfe insbesondere:

1. Gibt es mehr als zwei direkt aufeinanderfolgende Szenen mit praktisch derselben dramaturgischen Form?
2. Gibt es in längeren Mittelteil-Strecken eine Übermacht von Meeting/Review/Governance/Data-Discussion gegenüber Handlung, Anwendung, persönlicher Reibung oder Konsequenz?
3. Wird eine neue Regelstufe zu häufig direkt durch die nächste Regel-/Review-Szene fortgesetzt, ohne dass ihre Wirkung dazwischen erlebt wird?
4. Wiederholt sich dieselbe Erkenntnismechanik `Regel/Daten → Eva prüft → Gegenposition antwortet → Klärung` über längere Strecken?
5. Sind Szenen funktional redundant, obwohl ihre Storyinformation verschieden ist?
6. Ist die Scene-Shape-Verteilung vor Midpoint, zwischen Midpoint und Felix sowie vor dem Finale ausreichend dynamisch?

### E. Heuristiken als Warnsignale

Nutze folgende Werte nur als Review-Heuristik, nicht als starre Romanregeln:

- mehr als 2 direkt aufeinanderfolgende Szenen mit gleichem Primary Carrier → prüfen,
- mehr als 4 Meeting/Review/Governance/Data-Szenen in einem Fenster von 8 Szenen → prüfen,
- wiederholte Überschreitung ohne starke dramaturgische Begründung → Finding-Kandidat.

Ein Finding braucht immer eine konkrete Ermüdungs-/Redundanzwirkung; reine Zählwerte reichen nicht.

## Nicht als Finding melden

- Prosa-Rhythmus oder einzelne Formulierungen,
- Dialogstil auf Satzebene,
- Wunsch nach mehr Action ohne strukturelle Begründung,
- alternative Plotideen,
- Geschmacksfragen bei Titeln.

## Output

Wenn die Session sauber ist, beginne exakt mit:

```text
review_status: CLEAN_FRESH_CONTEXT
review_target: 78222a7e99c80378c35379ad42684ee332a412a6
finding_count: <n>
```

Pro Finding:

```text
finding_id: G2R-FR-001
location: <Szene(n) / Bereich / Event>
finding_type: event_coverage | causality | information | character | governance | chronology | medical_boundary | scene_granularity | beat_readiness | scene_shape | scene_repetition | pacing
severity: blocker | major | minor
problem: <konkret und prüfbar>
canonical_evidence: <welche erlaubte Quelle den Befund stützt>
impact: <warum dies G2/prose-ready oder das Leseerlebnis strukturell betrifft>
recommended_rework_level: scene | beat | event | story_architecture | research
```

Priorisiere echte Befunde und fasse manuskriptweite Muster zusammen. Maximal 10 Findings.

## Abschluss

Nach den Findings genau eine Zeile:

`g2_readiness: READY_FOR_REAPPROVAL | REWORK_REQUIRED`

`READY_FOR_REAPPROVAL` bedeutet: keine offenen Blocker/Major-Findings auf Szenen-/Beat-Ebene und keine strukturelle Scene-Shape-Monotonie, die vor Prosa erneut behoben werden müsste.