# Fresh-Context-Task – Szenenebene ABWEICHUNG

## Auftrag

Prüfe die **vollständige Szenenebene** des Romans `Satte882/ABWEICHUNG` in einem frischen Kontext gegen die bereits freigegebene G1-Storyarchitektur.

Dies ist ein **Blind Review**. Du sollst keine neue Story erfinden und keine Prosa schreiben.

## Fester Review-Target

Prüfe exakt den Stand dieses Commits:

`dea9fe2e2119cbd85950fca89c398f7459d28775`

Verwende für alle geprüften Dateien diesen Commit-Stand. Prüfe nicht einfach die jeweils aktuelle `main`-Version, falls sie später abweicht.

## Erlaubte Quellen

Am Ziel-Commit darfst du lesen:

1. `BOOK_IDEA.md`
2. `STORY_PACKAGE.md`
3. `CHARACTERS.md`
4. `RESEARCH_REGISTER.md`
5. `R06_MEDIZINISCHE_ANKERFAELLE.md`
6. `gates/G0.md`
7. `gates/G1.md`
8. alle `BAUSTEINE/**/BAUSTEIN.md`
9. alle `BAUSTEINE/**/EREIGNISSE/EREIGNISSE.md`
10. alle 40 `BAUSTEINE/**/SZENEN/**/SZENE.md`

## Verbotene Quellen

Nicht verwenden:

- `SCENE_LAYER_SELF_REVIEW.md`
- `G1_FRESH_CONTEXT_RESULT.md`
- `SEMANTIC_G1_SELF_REVIEW.md`
- frühere Review-Findings oder Korrekturlisten
- Issue-/PR-Kommentare
- Git-Diffs, die spätere Korrekturen zeigen
- frühere Chats, Memory oder sonstiges Wissen darüber, welche Fehler schon bekannt waren

Wenn du eine verbotene Quelle gesehen oder genutzt hast, setze `review_status: CONTAMINATED` und brich den Review als unabhängigen Nachweis ab.

## Prüffragen

Prüfe die Szenenebene auf echte Abweichungen oder Lücken gegenüber G1, insbesondere:

1. **Event-Abdeckung:** Sind E001–E054 vollständig und ohne widersprüchliche Umdeutung in Szenen überführt?
2. **Kausalität:** Entsteht die Folge jeder zentralen Entscheidung aus den gesetzten Ursachen, oder muss eine spätere Beat-Ebene neue Kausalität erfinden?
3. **Informationsarchitektur:** Werden Informationen zu früh, zu spät oder doppelt so eingeführt, dass spätere Szenen ihre Funktion verlieren?
4. **Figurenbögen:** Handeln Eva, Miriam, Felix, Nele, Jan und Laura entlang der freigegebenen Rollen und Beziehungsentwicklungen?
5. **Verantwortungszuordnung:** Wird eine Entscheidung versehentlich einer anderen Figur zugeschrieben oder geteilt, obwohl G1 klare Verantwortung setzt?
6. **Governance:** Bleiben alle Stufen, Ausnahmegrenzen und der Break-glass in der freigegebenen Reihenfolge und Bedeutung?
7. **Midpoint:** Bleibt der Reversal Evas eigene Bilanz, ohne KORA durch einen neuen Fehler/Twist zu entwerten?
8. **Felix:** Ist Umgehung → ausgeschaltete Zweitfreigabe → Schadensfall sauber kausal, ohne sicheren kontrafaktischen Ausgang zu behaupten?
9. **Finale:** Ist Neles Ablehnung vollständig aus der vor B17 gesetzten Wert-/Kontextregel und der medizinischen Informationslage ableitbar? Bleibt Evas Break-glass real?
10. **Medizinische Anker:** Bleiben die Szenen innerhalb der in R-06 freigegebenen Mechaniken, ohne neue medizinische Storyannahmen zu erfinden?
11. **Szenengranularität:** Gibt es Szenen, die funktional redundant sind, oder einzelne Szenen, die zwei unvereinbare dramatische Aufgaben zusammenpressen und deshalb vor Beats getrennt werden müssten?
12. **Beat Readiness:** Gibt es noch storyrelevante Entscheidungen, die auf Szenenebene offen sind und sonst erst beim Beatschreiben erfunden werden müssten?

Nicht als Finding melden:

- reine Stilpräferenz
- Wunsch nach „mehr Drama“
- alternative Plotideen
- Dialogformulierungen
- Prosa-Rhythmus
- Geschmacksfragen bei Szenentiteln

## Output

Beginne exakt mit:

```text
review_status: CLEAN_FRESH_CONTEXT | CONTAMINATED
review_target: dea9fe2e2119cbd85950fca89c398f7459d28775
finding_count: <n>
```

Für jedes echte Finding:

```text
finding_id: SL-FR-001
location: <Szene(n) / Baustein / Event>
finding_type: event_coverage | causality | information | character | governance | chronology | medical_boundary | scene_granularity | beat_readiness
problem: <konkretes Problem>
canonical_evidence: <welche erlaubte G1-Quelle zeigt den Widerspruch/die Lücke>
impact: <was würde bei Beats/Prosa falsch oder spontan erfunden>
recommended_rework_level: scene | event | story_architecture | research
```

Regeln:

- Keine Gesamt-Qualitätsnote.
- Keine Confidence-Scores.
- Keine Prosa-Rewrites.
- Keine neuen Plotideen als „Lösung“.
- Wenn kein belastbares Finding existiert, `finding_count: 0` ausgeben und nichts erfinden.