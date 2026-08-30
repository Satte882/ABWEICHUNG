# Fresh-Context-Auftrag – Beat-Ebene ABWEICHUNG

review_status_required: CLEAN_FRESH_CONTEXT
review_target: Beat-Ebene S001–S040

## Kontextregel

Dieser Review muss in einem **neuen, sauberen Chat ohne Kenntnis des Generierungsdialogs** durchgeführt werden.

Wenn du bereits vorherige Review-Ergebnisse, Korrekturlisten, Generierungsentscheidungen oder die Diskussion kennst, antworte nur:

`review_status: CONTAMINATED`

und stoppe.

## Erlaubte Quellen

Lies ausschließlich im Repo `Satte882/ABWEICHUNG`:

- `BOOK_IDEA.md`
- `STORY_PACKAGE.md`
- `CHARACTERS.md`
- `RESEARCH_REGISTER.md`
- `R06_MEDIZINISCHE_ANKERFAELLE.md`
- `gates/G0.md`
- `gates/G1.md`
- `BAUSTEINE/**/BAUSTEIN.md`
- `BAUSTEINE/**/EREIGNISSE/EREIGNISSE.md`
- `BAUSTEINE/**/SZENEN/**/SZENE.md`
- `BAUSTEINE/**/SZENEN/**/BEATS.md`

## Verbotene Quellen

Nicht lesen oder verwenden:

- `SEMANTIC_BEAT_SELF_REVIEW.md`
- `SCENE_FRESH_CONTEXT_RESULT.md`
- `G1_FRESH_CONTEXT_RESULT.md`
- `G1_FRESH_CONTEXT_TASK.md`
- `G1_REVIEW_REQUEST.md`
- Issue-/PR-Kommentare
- frühere Chat-/Generierungsverläufe
- spätere Prosa oder andere Review-/Completion-Dateien

## Auftrag

Prüfe die gesamte Beat-Ebene **semantisch und horizontal über den kompletten Roman**.

Prüfe insbesondere:

1. **Ableitungstreue:** Ist jeder Beat aus seiner `SZENE.md` ableitbar oder führt er neue Storywahrheit ein?
2. **Vollständigkeit:** Ist jede der 40 Szenen ausreichend granularisiert, sodass spätere Prosa keine relevante Storyentscheidung neu erfinden muss?
3. **Kausalität:** Bleiben Ursachen, Entscheidungen und Folgen innerhalb und zwischen Szenen konsistent?
4. **Informationsreihenfolge:** Wird Information in Beats früher offengelegt, als die Szenen-/G1-Architektur erlaubt?
5. **Figurenverantwortung:** Bleiben Agency, Wissen und Verantwortlichkeit insbesondere bei Eva, Nele, Felix, Miriam und Jan konsistent?
6. **Medizinische Grenze:** Erfinden Beats neue Diagnosen, Zeitfenster, sichere Gegenfaktiken oder medizinische Kausalitäten außerhalb der gesetzten R-06-Anker?
7. **Midpoint:** Bleibt S019 ein Reversal von Evas Selbstbild und kein versteckter KORA-Fehler?
8. **Wert-/Kontextregel:** Determiniert S027 die spätere Prüfung in S035/S036 vollständig genug?
9. **Felix:** Bleibt S028–S030 kausal geschlossen, ohne zu behaupten, Zweitfreigabe hätte den Schaden sicher verhindert?
10. **Finale:** Ist S033–S040 vollständig aus der vorher gesetzten Architektur verdient, insbesondere Neles Ablehnung und Evas freiwilliger Nichtgebrauch des realen Break-glass?
11. **Prose Readiness:** Gibt es noch eine relevante Storyentscheidung, die auf Beat-Ebene offen bleibt und deshalb beim Prosaschreiben improvisiert werden müsste?

## Nicht tun

- keine Umschreibungen
- keine neuen Plotideen
- keine alternativen Szenen
- keine Prosa
- keine Qualitätsscores
- keine Geschmacksbewertung

## Ausgabeformat

Erste Zeile:

`review_status: CLEAN_FRESH_CONTEXT`

Dann:

`review_target: <aktueller Commit oder eindeutige Beat-Basis>`

`finding_count: N`

Für jedes Finding exakt:

```text
finding_id: BEAT-SR-XXX
location: <Szene / Beat / Artefakt>
finding_type: <causality | information | character | chronology | research_boundary | story_architecture | prose_readiness>
problem: <konkretes Problem>
canonical_evidence: <konkreter vorgelagerter Beleg>
impact: <was dadurch später bricht oder improvisiert werden müsste>
recommended_rework_level: <beat | scene | event | story_architecture | research | none>
```

Wenn keine Findings vorliegen, nach `finding_count: 0` stoppen.
