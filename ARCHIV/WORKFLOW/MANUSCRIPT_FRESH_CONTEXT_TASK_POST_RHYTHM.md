# Review-Auftrag – Gesamtmanuskript ABWEICHUNG nach Final-Prosa-/Rhythmuspass

control_file_ref: `main`
review_target: `c0bc7fc5b23d29da60ed6784fd31ebdcd4f899fb`
review_scope: full manuscript S001–S040
review_mode: evidence-bound semantic whole-manuscript review
result_file: `MANUSCRIPT_FRESH_CONTEXT_RESULT_POST_RHYTHM.md`
prerequisite: review exactly the fixed post-rhythm manuscript target and derive every finding from target evidence

## Wichtige Trennung: Auftrag vs. Prüfgegenstand

Diese Datei ist die Steuerdatei und muss vom aktuellen Branch `main` gelesen werden.

Der Wert `review_target` bezeichnet ausschließlich den festen Manuskript-Snapshot, aus dem die unten zugelassenen fachlichen Produktionsquellen gelesen werden.

Vor Beginn müssen beide Bedingungen erfüllt sein:

1. Steuerdatei gelesen von `main`.
2. `review_target` ist exakt `c0bc7fc5b23d29da60ed6784fd31ebdcd4f899fb`.

Wenn Bedingung 2 nicht erfüllt ist, Auftrag nicht ausführen und `review_status: REVIEW_INVALID_TARGET` ausgeben.

## Review-Modus: Evidence Bound

Dieser Review verlangt **keinen kontextfreien Chat**.

Vorwissen über das Manuskript, frühere Diskussionen, frühere Findings oder den Prosa-/Rhythmuspass ist zulässig und macht den Review nicht ungültig.

Verbindlich ist stattdessen:

- Jedes Finding muss aus dem fixierten Zielstand **neu hergeleitet** werden.
- Jedes Finding muss durch konkrete Evidenz aus den unten zugelassenen Quellen belegbar sein.
- Frühere Reviews, Diffs, Chat-Erinnerungen, Lessons Learned oder bekannte Korrekturlisten dürfen nicht als Beweis verwendet werden.
- Ein bereits bekanntes Problem zählt nur, wenn es im Zielstand weiterhin konkret nachweisbar ist.
- Ein früher bekanntes Problem, das im Zielstand nicht mehr nachweisbar ist, ist kein Finding.

Ein versehentlich eingesehener früherer Review führt **nicht** zu `CONTAMINATED`. Der Review wird fortgesetzt und die betreffende Frage ausschließlich am Zielstand neu geprüft.

`CONTAMINATED` ist für diesen produktiven Gate-Review kein zulässiger Status.

## Verbindlicher Zielstand

Prüfe ausschließlich die fachlichen Produktionsquellen des Repository-Stands am Commit:

`c0bc7fc5b23d29da60ed6784fd31ebdcd4f899fb`

Nicht den aktuellen Branch-Head für diese Produktionsquellen, falls dieser inzwischen weitergelaufen ist.

Die einzige Datei, die ausdrücklich von `main` gelesen wird, ist diese Steuerdatei.

## Zulässige Finding-Evidenz

Lies für die Prüfung die folgenden fachlichen Produktionsquellen des Ziel-Commits:

1. `BOOK_IDEA.md`
2. `STORY_PACKAGE.md`
3. `CHARACTERS.md`
4. `R06_MEDIZINISCHE_ANKERFAELLE.md`
5. alle `BAUSTEINE/**/SZENE.md`
6. alle `BAUSTEINE/**/BEATS.md`
7. alle `BAUSTEINE/**/PROSA.md` von S001 bis S040

`RESEARCH_REGISTER.md` darf konsultiert werden, wenn eine konkrete faktische Plausibilitätsfrage anders nicht beurteilbar ist.

## Nicht als Finding-Evidenz verwenden

Die folgenden Quellen dürfen nicht als Beweis für ein Finding dienen:

- `LESSONS_LEARNED.md`
- `FULL_MANUSCRIPT_SELF_REVIEW.md`
- `G3_REVIEW_REQUEST.md`
- `G4_REVIEW_REQUEST.md`
- `G5_REVIEW_REQUEST.md`
- sonstige `*_REVIEW_*`-Dateien
- `*_FRESH_CONTEXT_RESULT*`-Dateien oder frühere Review-Ergebnisse
- `FINAL_PROSE_RHYTHM_AUDIT.md`
- `FINAL_PROSE_RHYTHM_AUDIT_POST.md`
- `FINAL_PROSE_RHYTHM_COMPARISON.md`
- `FINAL_PROSE_RHYTHM_APPLIED.md`
- `gates/`
- `MANUSCRIPT_EXPANSION_ANALYSIS.md`
- Audit-Artefakte
- Issues, Commit-Nachrichten oder PR-Diskussionen mit früheren Findings/Korrekturen

Falls solche Informationen bereits bekannt sind, ignorieren und die konkrete Frage am fixierten Zielstand neu prüfen.

## Kernauftrag

Bewerte das gesamte Manuskript als Roman, nicht als Sammlung einzelner Szenen und nicht als Erfüllung einer Zielwortzahl.

Lies S001–S040 vollständig. Lokale Auffälligkeiten sind nur dann Findings, wenn sie selbst relevant sind oder sich zu einem manuskriptweiten Muster verdichten.

### A. Architekturtreue

- Widerspricht Prosa einer freigegebenen Szene oder einem Beat?
- Wird Information zu früh oder zu spät offengelegt?
- Werden neue Plotentscheidungen, Kausalitäten oder Gegenfakten in der Prosa erfunden?
- Bleiben Midpoint, Felix-Kette, Wert-/Kontextregel und Finale kausal sauber?

### B. Figuren und POV

- Bleibt Eva als POV konsistent?
- Bleiben Eva, Miriam, Felix, Nele, Jan und Laura unterscheidbar in Haltung, Sprache und Funktion?
- Gibt es unverdiente Einstellungswechsel oder Gedankenwissen außerhalb des POV?

### C. Medizinische / faktische Plausibilität

- Prüfe die medizinischen Anker gegen `R06_MEDIZINISCHE_ANKERFAELLE.md`.
- Markiere erfundene Gewissheiten, falsche zeitliche Diagnostik oder unzulässige Kausalbehauptungen.
- KORA darf nicht heimlich von probabilistischem System zu unfehlbarer Instanz werden.

### D. Whole-Manuscript Pattern Review

Beurteile Muster über alle 40 Szenen hinweg. Tracke sie während der Lektüre sinngemäß, statt jede Szene isoliert zu bewerten.

Achte besonders auf:

- übermäßige Frage–Kurzantwort–Gegenfrage-Ketten (`dialogue_pingpong`),
- wiederkehrenden Szenentyp `Daten/Regel werden gezeigt → Eva stellt Prüfungsfragen → Klärung`,
- gleiche Gesprächschoreografie zwischen Eva/Miriam, Eva/Jan und Eva/Felix,
- wiederkehrende Übergangsfloskeln wie `Eva sah ...`, `Eva nickte`, `Eva schwieg`,
- wiederkehrende Kontrastformeln wie `Nicht X. Nicht Y. Aber Z.`,
- Negationsketten und rhetorische Dreier-/Parallelstrukturen,
- Erklärungsechos: Prosa erklärt nach einem Dialog noch einmal, was der Dialog bereits gezeigt hat,
- wiederkehrende Schlussmechaniken oder Absatzrhythmen,
- künstliche Stakkato-Häufung bzw. übermäßige Kurzabsatzmechanik,
- interne Produktions-/Architekturlabels im Romantext.

Entscheidend ist die Verteilung und Ermüdungswirkung im Gesamtroman, nicht die bloße Existenz eines Stilmittels.

### E. Pacing und Szenenvariation

- Wirkt der Roman über längere Strecken wie eine Folge ähnlicher Meetings/Reviews?
- Gibt es ausreichende Variation von Handlung, Konfliktträger, körperlicher Präsenz und Informationsvermittlung?
- Gibt es Strecken, die wie Architektur-Abarbeitung statt erzählte Geschichte wirken?
- Sind Übergänge und Eskalation bis Midpoint, Felix und Finale ausreichend dynamisch?

### F. Exposition und Lesbarkeit

- Werden Governance, Daten und KORA-Funktionsweise verständlich, ohne dass Figuren zu Erklärmaschinen werden?
- Wiederholen sich Argumente unnötig?
- Gibt es Passagen, die eher wie ein Fach-/Policy-Text als Romanprosa wirken?

### G. Emotionale Tragfähigkeit

- Tragen Laura, Nele, Felix und die beiden Ressourcenkonflikte genug menschliches Gewicht?
- Ist das Finale emotional verdient oder nur logisch korrekt?
- Funktioniert S040 als offener Nachhall nach dem gesamten Roman?

### H. Stilqualität / Anti-KI-Leserpass

- Prüfe KI-typische Über-Symmetrie, zu saubere Antithesen, künstliche Stakkato-Häufung, austauschbare Übergänge und zu häufige rhetorische Perfektion.
- Kurze Sätze, Pingpong und Kontraste sind nicht automatisch Fehler. Entscheidend ist Häufung, Vorhersagbarkeit und Ermüdung.
- Der Geviertstrich `—` darf in der Romanprosa nicht vorkommen.
- Das Wort `sondern` darf in der Romanprosa nicht vorkommen.
- Ein guter Pass darf die Storylogik nicht für bloße stilistische Variation verändern.

## Rework-Ebene

Ordne jeden Finding der kleinsten nötigen Rework-Ebene zu:

- `prose` – innerhalb bestehender Szene/Beats lösbar
- `scene` – Szenenfunktion oder Informationsarchitektur muss geändert werden
- `beat` – Beat-Reihenfolge/-Logik muss geändert werden
- `upstream` – Ereignis/G1-Storywahrheit müsste geändert werden

Bevorzuge `prose`, wenn der Befund ohne Storyänderung behebbar ist.

## Ausgabe

Beginne exakt mit:

`review_status: EVIDENCE_BOUND_REVIEW`
`review_target: c0bc7fc5b23d29da60ed6784fd31ebdcd4f899fb`
`finding_count: <n>`

Danach pro Finding:

```text
finding_id: MANUSCRIPT-POST-RHYTHM-001
location: <Szene(n) / Bereich>
finding_type: <architecture|information|character|medical|continuity|pacing|scene_repetition|dialogue_pattern|style_pattern|exposition|framework_leak|other>
severity: <blocker|major|minor>
problem: <konkret und prüfbar>
evidence: <konkrete Stellen/Muster aus dem Zielstand>
impact: <warum es im Gesamtroman relevant ist>
recommended_rework_level: <prose|scene|beat|upstream>
```

Priorisiere Findings. Fasse dasselbe manuskriptweite Muster in einem Finding zusammen, statt jede betroffene Szene separat zu melden.

Maximal 12 Findings. Keine kosmetische Vollständigkeitsliste.

Wenn nach vollständiger Lektüre kein relevanter Befund vorliegt, `finding_count: 0` ausgeben.

## Abschlussurteil

Nach den Findings genau eine Zeile:

`g4_readiness: READY | REWORK_REQUIRED`

`READY` bedeutet: keine Blocker/Major-Findings, die vor Human G4 behoben werden müssen.

`REWORK_REQUIRED` bedeutet: mindestens ein relevanter Befund sollte vor G4 dispositioniert werden.

## Persistenz

Schreibe das vollständige Ergebnis nach:

`MANUSCRIPT_FRESH_CONTEXT_RESULT_POST_RHYTHM.md`

Verändere während dieses Review-Schritts keine Prosa, keine Gates und keine Produktionsdateien.