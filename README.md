# ABWEICHUNG

Erster echter Romanlauf mit `Satte882/Buch-Framework` v0.2.

## Aktueller Stand

**G0 APPROVED → G1 APPROVED → G2 APPROVED → G3 APPROVED → 40/40 PROSA → 3× WHOLE-MANUSCRIPT REVIEW → CONTROLLED G2 BACKTRACK → CLEAN SCENE-SHAPE REREVIEW → G2 RE-APPROVED → REVIEW ADJUDICATED → READY_FOR_HUMAN_G4**

- 18 Bausteine
- 54 Ereignisse
- 40 Szenen
- 253 Beats
- 40/40 Szenen mit `PROSA.md`
- G1-Storywahrheit unverändert
- erster Gesamtmanuskript-Review: 6 Findings, 3 Major
- reiner Prosa-Rework
- zweiter Gesamtmanuskript-Review: 5 Findings, 2 wiederholte Major
- daraus kontrollierter G2-Backtrack
- Scene-/Beat-Träger strukturell geändert in S008, S014, S018, S020, S024, S032
- reiner Rework-Zielstand: `78222a7e99c80378c35379ad42684ee332a412a6`
- Fresh-Context-Szenen-/Beat-Re-Review: `CLEAN_FRESH_CONTEXT`, 0 Findings
- Human `G2-APPROVE` am 2026-08-31: aktueller Rework-Stand erneut G2 / Prose Ready
- dritter Gesamtmanuskript-Review gegen denselben Target: 2 Findings, davon 1 raw Major / 1 Minor
- Raw Major nach Evidenzprüfung **nicht als Major bestätigt**, sondern als non-blocking residual risk dispositioniert
- Minor zur wiederholten Beweislast-/Schlussrhetorik akzeptiert, non-blocking
- offene bestätigte Blocker: 0
- offene bestätigte Major-Findings: 0
- Human Gate G4 / Manuskript: **READY_FOR_HUMAN_G4**
- Lessons Learned dokumentiert in `LESSONS_LEARNED.md`
- Framework-Transfer vorgemerkt als `Satte882/Buch-Framework` Issue #17; noch keine Framework-Dateien geändert

## Arbeitsprinzip

Die Story wurde konsequent vom Groben ins Feine aufgebaut:

`Buchidee / Gesamtarchitektur → Baustein → Ereignisse → Szene → Beats → Prosa`

Der Pilot hat zwei zusätzliche Qualitätsprinzipien gezeigt:

1. **Semantische Vollständigkeit allein reicht nicht.** Die Verteilung dramaturgischer Szenenformen muss bereits vor Vollprosa über das ganze Buch geprüft werden.
2. **Fresh-Context-Reviews brauchen Adjudikation.** Ein Review liefert Findings; erst die Prüfung von Evidenz, Severity und kleinster sinnvoller Rework-Ebene entscheidet, ob ein Finding das nächste Human Gate blockiert.

## Scene-Shape-Backtrack

Die Storyursachen und Ereignisse blieben gleich. Verändert wurde ausschließlich, **wie** ausgewählte Szenen ihre freigegebene Storyfunktion tragen:

| Szene | neuer dominanter Träger |
|---|---|
| S008 | erste Governance-Regel wird live im klinischen Workflow erlebt |
| S014 | klinischer Low-Confidence-Fall löst den Analyseauftrag aus |
| S018 | Eva führt allein die persönliche Gegenprobe auf ihre eigenen Fälle aus |
| S020 | personenbezogene Governance erscheint als persönliche Einstufung / Statusverlust |
| S024 | Eva entwickelt die Wert-/Kontext-Gegenarchitektur zuerst allein |
| S032 | Solo-Break-glass wird in einem funktionalen Stresstest praktisch verifiziert |

Der unabhängige Re-Review der vollständigen Szenen-/Beat-Verteilung meldete danach keine Findings. Der Stand wurde anschließend erneut durch Human `G2-APPROVE` freigegeben.

## Dritter Manuskript-Review und Adjudikation

Der dritte unabhängige Whole-Manuscript-Review meldete noch:

- `scene_repetition` als Major,
- wiederholte Beweislast-/Schlussrhetorik als Minor.

Das Raw-Urteil `REWORK_REQUIRED` bleibt in `MANUSCRIPT_FRESH_CONTEXT_RESULT.md` dokumentiert.

Die anschließende Adjudikation kam jedoch zu folgendem Ergebnis:

- Das `scene_repetition`-Finding nennt mehrere Szenen als gleichartige Meeting-/SOP-Träger, die am geprüften Target gerade unterschiedlich gebaut sind (u. a. Live-Anwendung, klinischer Auslöser, Implementierungstest). Zusammen mit dem unmittelbar vorher bestandenen Scene-Shape-Re-Review reicht die Evidenz nicht für einen erneuten Architektur-Major. Disposition: `NOT_SUSTAINED_AS_MAJOR / non-blocking residual risk`.
- Das Stil-Finding zur wiederholt expliziten Beweislast-Formulierung ist plausibel, aber minor und nicht G4-blockierend. Disposition: `ACCEPTED_MINOR / non-blocking`.

Damit bestehen nach Disposition keine bestätigten offenen Blocker/Majors mehr.

## Lessons Learned

`LESSONS_LEARNED.md` enthält inzwischen zwei bestätigte Pilot-Erkenntnisse:

### LL-001 – Scene-Shape-Verteilung

- Whole-Book Scene-Shape Review vor G2,
- Primary Dramatic Carrier pro Szene sichtbar machen,
- G3 zusätzlich mit einem zusammenhängenden Mittelteil-Run testen,
- globale Dialog-/Scene-Repetition-Muster statt nur lokale Scanner-Findings bewerten,
- wiederholt derselbe Manuskript-Major nach Prosa-Rework → kontrollierter G2-Backtrack.

### LL-002 – Review-Adjudikation

- Raw-Review nicht automatisch mit Gate-Entscheidung gleichsetzen,
- Major-Findings gegen den tatsächlichen Target prüfen,
- widersprüchliche Reviews explizit adjudizieren,
- Reviewer-Overfitting vermeiden,
- nur bestätigte Blocker/Majors blockieren das Human Gate.

Der Transfer ins Framework ist als Issue #17 erfasst und wird erst nach erfolgreichem G4 dieses Piloten umgesetzt.

## Stilreferenz G3

- `S001 – Die letzte Kapazität`: akuter medizinischer Druck
- `S019 – Die Bilanz`: analytischer Midpoint
- `S023 – Würden Sie es wieder tun?`: persönliche Konfrontation

Diese Szenen bleiben die interne Stilkalibrierung.

## Aktuelle Phase

**Human Gate G4 – Manuskript.**

Fester Manuskriptstand:

`78222a7e99c80378c35379ad42684ee332a412a6`

Review- und Dispositionsbasis:

`MANUSCRIPT_FRESH_CONTEXT_RESULT.md`

Gate-Anforderung:

`G4_REVIEW_REQUEST.md`

Gültiger Approval-Token:

`G4-APPROVE`

Nach `G4-APPROVE`:

1. vollständigen Manuskriptstand als kanonisch markieren,
2. `full-prose-generation` nach `main` übernehmen,
3. Arbeitsbranch anschließend bereinigen,
4. Lesson Learned in `Buch-Framework` Issue #17 umsetzen,
5. danach Produktion / G5.

## Reihengedanke

Die Bücher sind keine klassische Fortsetzungsreihe mit denselben Figuren. Gemeinsam ist die dramaturgische Denkmaschine:

> Ein gesellschaftlich nachvollziehbares Problem trifft auf eine zunächst vernünftige Lösung. Die Lösung funktioniert. Gerade ihr Erfolg verschiebt schrittweise eine Grenze, bis etwas normal oder legitim erscheint, das zu Beginn kaum akzeptabel gewesen wäre.

## Thematischer Kern

**Thema:** KI + Entscheidungsmacht  
**Konflikt:** Ergebnisqualität vs. legitime menschliche Entscheidungsmacht

> **Wie lange darf ein Mensch eine schlechtere Entscheidung treffen, wenn eine Maschine nachweislich die bessere kennt?**

Kernumkehr:

> **Nicht mehr die Maschine muss beweisen, dass sie recht hat. Der Mensch muss beweisen, warum er von ihr abweichen darf.**
