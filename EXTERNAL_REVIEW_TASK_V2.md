# EXTERNAL REVIEW TASK V2 – ABWEICHUNG

review_mode: INDEPENDENT_FULL_MANUSCRIPT_REREVIEW
provider_policy: MODEL_AND_PROVIDER_AGNOSTIC
candidate_commit: `7b476fe63e933592d36e9ab9a385a01187de60d5`
primary_artifact: `ABWEICHUNG_FINAL.md`

## Auftrag

Prüfe den vollständigen Roman **ABWEICHUNG** als unabhängiger externer Reviewer.

Repository: `Satte882/ABWEICHUNG`

Bewertet wird ausschließlich der feste Manuskriptstand:

`7b476fe63e933592d36e9ab9a385a01187de60d5`

Primäres Artefakt:

`ABWEICHUNG_FINAL.md`

Lies das Manuskript vollständig von Kapitel 1 bis 40 in narrativer Reihenfolge. Stichproben reichen nicht für Aussagen über Pacing, Wiederholungen, Figurenbogen oder Leserwirkung.

## Anti-Anchoring

Dieser Durchlauf soll unabhängig sein. Lies vor deinem Review keine internen Review-, Audit-, Finding-, Adjudikations- oder Rework-Dateien des Repositories.

Insbesondere nicht verwenden:

- `EXTERNAL_REVIEW_RESULT.md`
- `EXTERNAL_REVIEW_ADJUDICATION.md`
- `EXTERNAL_MAJOR_REWORK.md`
- `EXTERNAL_MAJOR_REWORK_REGRESSION.md`
- `MANUSCRIPT_FRESH_CONTEXT_RESULT_POST_RHYTHM.md`
- `MANUSCRIPT_REVIEW_POST_REWORK.md`
- `FULL_MANUSCRIPT_SELF_REVIEW.md`
- `FINAL_PROSE_RHYTHM_AUDIT*.md`

Wenn du versehentlich auf eine solche Datei stößt, verwende deren Inhalt nicht als Evidenz. Leite jedes Finding neu aus dem fixierten Manuskript ab.

Für Konsistenz- oder Plausibilitätsprüfungen darfst du bei Bedarf zusätzlich folgende kanonische Dateien verwenden:

- `BOOK_IDEA.md`
- `STORY_PACKAGE.md`
- `CHARACTERS.md`
- `R06_MEDIZINISCHE_ANKERFAELLE.md`

## Prüffelder

Prüfe mindestens:

1. **Story, Kausalität und Kontinuität**
   - Widersprüche zwischen früheren und späteren Ereignissen
   - unzureichend vorbereitete Folgen oder Eskalationen
   - wechselnde Regeln oder institutionelle Mechanismen
   - falsche Wissensstände oder unverdiente Gewissheit

2. **Figuren, Motivation und Beziehungen**
   - Eva Riedels Entwicklung und Entscheidungen
   - Miriam, Felix, Nele, Jan und Laura als eigenständige Figuren statt bloße Argumentträger
   - persönliche Konsequenzen von Konflikten
   - unterscheidbare Sprachregister

3. **Spannung, Pacing und Leserwirkung**
   - Spannungsabfälle über mehrere Kapitel
   - redundante oder vorhersehbare Abschnitte
   - Häufung ähnlicher Meeting-, Review-, Daten-, Governance- oder Analyse-Szenen
   - Kapitel, die dramaturgisch dieselbe Arbeit wie Nachbarkapitel leisten
   - Stellen, an denen Erklärung Handlung verdrängt

4. **Prosa, Dialog und sichtbare Produktionsmuster**
   - gleichförmige Frage–Kurzantwort–Gegenfrage-Dialoge
   - zu ähnliche Szeneneröffnungen oder Schlussmechaniken
   - Erklär-Echos
   - überhäufige Mikro-Choreografie
   - künstlich symmetrische Argumentation
   - Satzbau- oder Rhythmusmuster mit maschineller Wirkung

   Ein einzelnes Stilmittel ist kein Finding. Relevant sind Häufung und konkrete Leserwirkung.

5. **Plausibilität und Fachlichkeit**
   - klinische Abläufe
   - Entscheidungsunterstützung durch KORA
   - Governance- und Override-Prozesse
   - institutionelle Reaktionen
   - Daten- und Auditlogik

   Falls du Web-/Research-Funktionen besitzt, nutze sie nur für konkrete überprüfbare Sachfragen. Trenne reale Fachkritik von literarischer Bewertung. Die Near-Future-Prämisse ist nicht automatisch falsch, nur weil eine Praxis heute noch nicht Standard ist.

6. **Reversal, Finale und Payoff**
   - Midpoint als echte Neu-Rahmung
   - Vorbereitung der Governance-Eskalation
   - organische Entwicklung von Felix' Umgehung
   - Spiegelung des Anfangs im Finale
   - Verdientheit von Evas Schlussentscheidung
   - Wirkung von `Was sieht KORA nicht?`

7. **Blind Spots**
   - relevante Probleme außerhalb der Kategorien

## Severity

- `blocker`: fundamentaler Defekt, der zentrale Story-, Figuren- oder Finalelogik beschädigt
- `major`: relevantes Problem mit spürbarer Wirkung auf Logik, Glaubwürdigkeit, Spannung, Figurenbogen oder manuskriptweite Leserwirkung
- `minor`: reales, aber begrenztes Problem ohne fundamentale Wirkung

## Finding-Format

Für jedes Finding exakt:

```text
finding_id: XR2-XXX
location: <Kapitel/Szene/Stelle oder Bereich>
finding_type: <causality | character | information | chronology | pacing | repetition | dialogue | exposition | plausibility | research | finale | other>
severity: <blocker | major | minor>
problem: <konkret beobachtetes Problem>
text_evidence: <kurzer eindeutiger Text-/Stellenbezug>
impact: <konkrete Wirkung auf Logik, Figur oder Leser>
external_source: <nur bei Sach-Finding mit externer Recherche; sonst none>
recommended_rework_level: <prose | scene | beat | event | story_architecture | research | none>
```

Am Ende:

```text
external_review_status: COMPLETE
finding_count: <n>
blocker_count: <n>
major_count: <n>
minor_count: <n>
external_gate_recommendation: <READY | REWORK_REQUIRED>
```

## Nicht gewünscht

- keine Punktzahl oder Sternebewertung
- kein pauschales Gefallen/Nichtgefallen
- keine alternative Story nur aus Geschmack
- keine neuen Twists ohne konkreten Befund
- kein vollständiger Rewrite
- keine kosmetischen Alternativformulierungen ohne Problem
- keine Kenntnis oder Bestätigung früherer Findings simulieren

Deine Empfehlung ist advisory. Du setzt keinen Gate-Status und schreibst das Manuskript nicht selbst um.

Ziel ist eine echte unabhängige zweite Sicht auf den aktuellen, reworkten Stand: Suche nach belastbaren verbliebenen Problemen, nicht nach Bestätigung früherer Arbeit.
