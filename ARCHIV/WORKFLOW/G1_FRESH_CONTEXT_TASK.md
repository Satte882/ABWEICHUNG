# Fresh-Context-Task – G1 ABWEICHUNG

review_target: G1 Story-Architektur ABWEICHUNG
required_status: CLEAN_FRESH_CONTEXT
review_type: independent_semantic_review

## Auftrag

Prüfe die G1-Storyarchitektur von `Satte882/ABWEICHUNG` als unabhängiger semantischer Reviewer.

**Keine neuen Plotideen, Twists, Figuren oder Alternativarchitekturen entwickeln. Keine Texte umschreiben. Keine Qualitätsnote vergeben.**

Gesucht sind ausschließlich konkrete Widersprüche, Kausalitätslücken oder belastbare Risiken gegen die bereits freigegebene Konzept- und G1-Architektur.

## Erlaubte Inputs

Aus `Satte882/ABWEICHUNG` ausschließlich:

- `BOOK_IDEA.md`
- `gates/G0.md`
- `STORY_PACKAGE.md`
- `STORY_BLOCKS.md`
- `EVENTS.md`
- `CHARACTERS.md`
- `RESEARCH_REGISTER.md`

Aus `Satte882/Buch-Framework`:

- `SEMANTIC_REVIEW_PROTOCOL.md`

## Verbotene Inputs

Nicht lesen oder verwenden:

- `SEMANTIC_G1_SELF_REVIEW.md`
- `G1_REVIEW_REQUEST.md`, falls bereits vorhanden
- Issue-/PR-Kommentare
- Chat-/Erzeugungshistorie
- spätere Beats, Szenenkarten oder Prosa, falls zwischenzeitlich vorhanden
- andere Review-/Completion-Dateien

Wenn ein verbotener Input gelesen wurde:

`review_status: CONTAMINATED`

und den Review nicht fortsetzen.

## Prüffragen

1. **G0-Treue:** Widerspricht G1 einer irreversiblen G0-Entscheidung?
2. **Kausalität:** Löst jeder Governance-Schritt nachvollziehbar aus vorherigen Ereignissen aus oder springt die Geschichte institutionell zu weit?
3. **Outcome-Logik:** Bleibt KORA tatsächlich besser, ohne dass einzelne Outcomes unzulässig als kontrafaktischer Beweis behandelt werden?
4. **Information/Reveal:** Werden O = Outcome, G = Governance und X = Externalität in plausibler Reihenfolge sichtbar oder weiß eine Figur etwas zu früh?
5. **Figuren:** Tragen Eva, Miriam, Felix, Nele, Jan und Laura ihre gesetzten Funktionen ohne unmotivierte Rollenwechsel?
6. **Midpoint:** Folgt Evas eigene negative Abweichungsbilanz kausal aus den gesetzten Daten, ohne Statistik als individuelle Gewissheit auszugeben?
7. **Finale:** Ist B16–B18 aus den vorherigen Governance- und Figurenentwicklungen verdient, insbesondere Neles Weigerung und Evas Nicht-Nutzung von Break-glass?
8. **Research Boundary:** Behauptet G1 medizinische, regulatorische oder rechtliche Details, die `RESEARCH_REGISTER.md` noch nicht trägt?
9. **G1-Vollständigkeit:** Gibt es eine relevante Storyentscheidung, die auf G1 noch offen ist und später Beats/Prosa zwingen würde, Plotwahrheit spontan zu erfinden?

## Finding-Schema

Für jeden Befund exakt:

```text
finding_id: G1-SR-XXX
location: <Artefakt / Block / Event>
finding_type: <causality | information | character | chronology | research_boundary | story_architecture>
problem: <konkreter Widerspruch oder belastbares Risiko>
canonical_evidence: <Pfad / Block / Event / G0-Entscheidung>
impact: <was dadurch falsch oder unklar wird>
recommended_rework_level: <story_architecture | event | research | none>
```

Wenn keine Befunde:

```text
review_status: CLEAN_FRESH_CONTEXT
finding_count: 0
```

Wenn Befunde:

```text
review_status: CLEAN_FRESH_CONTEXT
finding_count: <n>
<Findings>
```

Keine Rewrite-Vorschläge im Review.
