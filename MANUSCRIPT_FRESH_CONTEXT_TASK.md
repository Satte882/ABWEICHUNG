# Fresh-Context-Auftrag – Gesamtmanuskript ABWEICHUNG

review_target: `78222a7e99c80378c35379ad42684ee332a412a6`
review_scope: full manuscript S001–S040
review_mode: independent semantic whole-manuscript review
prerequisite: execute only after the reworked scene/beat layer has been independently reviewed and human G2 re-approved

## Clean-Room-Voraussetzung

Dieser Auftrag darf **nur in einer wirklich kontextfreien Session** ausgeführt werden, vorzugsweise in einem nicht personalisierten Temporary Chat.

Wenn du bereits Kenntnis hast von:

- der Entstehung dieses Manuskripts,
- früheren Reviews oder Findings,
- früheren Korrekturen/Reworks,
- Diskussionen über konkrete Schwächen einzelner Szenen,
- Bewertungen anderer Reviewer,

antworte **ausschließlich**:

`review_status: CONTAMINATED`

und beende den Auftrag.

Nutze keine Erinnerungen, frühere Chats oder außerhalb dieses Auftrags bekannte Bewertungen des Manuskripts.

## Verbindlicher Zielstand

Prüfe ausschließlich den Repository-Stand des Commits:

`78222a7e99c80378c35379ad42684ee332a412a6`

Nicht den aktuellen Branch-Head, falls dieser inzwischen weitergelaufen ist.

## Erlaubte Quellen

Lies für die Prüfung ausschließlich die fachlichen Produktionsquellen des Ziel-Commits:

1. `BOOK_IDEA.md`
2. `STORY_PACKAGE.md`
3. `CHARACTERS.md`
4. `R06_MEDIZINISCHE_ANKERFAELLE.md`
5. alle `BAUSTEINE/**/SZENE.md`
6. alle `BAUSTEINE/**/BEATS.md`
7. alle `BAUSTEINE/**/PROSA.md` von S001 bis S040

`RESEARCH_REGISTER.md` darf nur konsultiert werden, wenn eine konkrete faktische Plausibilitätsfrage anders nicht beurteilbar ist.

## Verbotene Quellen

Nicht öffnen oder verwenden:

- `LESSONS_LEARNED.md`
- `FULL_MANUSCRIPT_SELF_REVIEW.md`
- `G3_REVIEW_REQUEST.md`
- sonstige `*_REVIEW_*`-Dateien
- `*_FRESH_CONTEXT_*`-Dateien oder frühere Review-Ergebnisse
- `gates/`
- Issues, Commit-Nachrichten oder PR-Diskussionen, die frühere Findings/Korrekturen verraten

Wenn du versehentlich eine solche Quelle inhaltlich gelesen hast, gilt der Review als kontaminiert. Gib dann nur `review_status: CONTAMINATED` aus.

## Kernauftrag

Bewerte das **gesamte Manuskript als Roman**, nicht als Sammlung einzelner Szenen.

Lies S001–S040 vollständig. Lokale Auffälligkeiten sind nur dann Findings, wenn sie selbst relevant sind oder sich zu einem manuskriptweiten Muster verdichten.

Prüfe insbesondere:

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

### D. Whole-Manuscript Pattern Review – besonders wichtig

Beurteile Muster **über alle 40 Szenen hinweg**. Zähle/tracke sie während der Lektüre sinngemäß, statt jede Szene isoliert zu bewerten.

Achte besonders auf:

- übermäßige Frage–Kurzantwort–Gegenfrage-Ketten (`dialogue_pingpong`),
- wiederkehrenden Szenentyp `Daten/Regel werden gezeigt → Eva stellt Prüfungsfragen → Klärung`,
- gleiche Gesprächschoreografie zwischen Eva/Miriam, Eva/Jan und Eva/Felix,
- wiederkehrende Übergangsfloskeln wie `Eva sah ...`, `Eva nickte`, `Eva schwieg`,
- wiederkehrende Kontrastformeln wie `Nicht X. Nicht Y. Aber Z.`,
- Negationsketten und rhetorische Dreier-/Parallelstrukturen,
- Erklärungsechos: Prosa erklärt nach einem Dialog noch einmal, was der Dialog bereits gezeigt hat,
- wiederkehrende Schlussmechaniken oder Absatzrhythmen,
- interne Produktions-/Architekturlabels im Romantext.

Entscheidend ist die **Verteilung und Ermüdungswirkung im Gesamtroman**, nicht die bloße Existenz eines Stilmittels.

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

### H. Stilqualität

- Prüfe KI-typische Über-Symmetrie, zu saubere Antithesen, künstliche Stakkato-Häufung, austauschbare Übergänge und zu häufige rhetorische Perfektion.
- Kurze Sätze, Pingpong und Kontraste sind **nicht automatisch Fehler**. Entscheidend ist Häufung, Vorhersagbarkeit und Ermüdung.
- Das Wort `sondern` darf in der Romanprosa nicht vorkommen.

## Rework-Ebene

Ordne jeden Finding der kleinsten nötigen Rework-Ebene zu:

- `prose` – innerhalb bestehender Szene/Beats lösbar
- `scene` – Szenenfunktion oder Informationsarchitektur muss geändert werden
- `beat` – Beat-Reihenfolge/-Logik muss geändert werden
- `upstream` – Ereignis/G1-Storywahrheit müsste geändert werden

Bevorzuge `prose`, wenn der Befund ohne Storyänderung behebbar ist. Fordere keinen Upstream-Rework nur zur Stilvariation.

## Ausgabe

Wenn die Session sauber ist, beginne exakt mit:

`review_status: CLEAN_FRESH_CONTEXT`
`review_target: 78222a7e99c80378c35379ad42684ee332a412a6`
`finding_count: <n>`

Danach pro Finding:

```text
finding_id: MANUSCRIPT-FR-001
location: <Szene(n) / Bereich>
finding_type: <architecture|information|character|medical|continuity|pacing|scene_repetition|dialogue_pattern|style_pattern|exposition|framework_leak|other>
severity: <blocker|major|minor>
problem: <konkret und prüfbar>
evidence: <konkrete Stellen/Muster aus dem Manuskript>
impact: <warum es im Gesamtroman relevant ist>
recommended_rework_level: <prose|scene|beat|upstream>
```

Priorisiere Findings. Fasse dasselbe manuskriptweite Muster **in einem Finding** zusammen, statt jede betroffene Szene separat zu melden.

Maximal 12 Findings. Keine kosmetische Vollständigkeitsliste.

Wenn du nach vollständiger Lektüre keinen relevanten Befund findest, gib `finding_count: 0` aus.

## Abschlussurteil

Nach den Findings genau eine Zeile:

`g4_readiness: READY | REWORK_REQUIRED`

`READY` bedeutet: keine Blocker/Major-Findings, die vor Human G4 behoben werden müssen.

`REWORK_REQUIRED` bedeutet: mindestens ein relevanter Befund sollte vor G4 dispositioniert werden.