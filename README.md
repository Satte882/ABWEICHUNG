# ABWEICHUNG

Erster echter Romanlauf mit `Satte882/Buch-Framework` v0.2.

## Aktueller Stand

**G0 APPROVED → G1 APPROVED → ursprüngliches G2 APPROVED → G3 APPROVED → 40/40 PROSA → 2× WHOLE-MANUSCRIPT REVIEW → REPEATED MAJORS → CONTROLLED G2 BACKTRACK → AWAITING FRESH-CONTEXT SCENE-SHAPE REREVIEW**

- 18 Bausteine
- 54 Ereignisse
- 40 Szenen
- 253 Beats
- 40/40 Szenen mit `PROSA.md`
- G1-Storywahrheit unverändert
- erster Gesamtmanuskript-Review: 6 Findings, 3 Major
- reiner Prosa-Rework
- zweiter Gesamtmanuskript-Review gegen `1d717f...`: 5 Findings, 2 Major
- wiederholte Majors: Scene-Repetition + Dialogue-Pingpong
- daraus bewusst kontrollierter G2-Backtrack ausgelöst
- Scene-/Beat-Träger strukturell geändert in S008, S014, S018, S020, S024, S032
- zugehörige Prosa synchron angepasst
- reiner Rework-Zielstand: `78222a7e99c80378c35379ad42684ee332a412a6`
- Lesson Learned dokumentiert in `LESSONS_LEARNED.md`
- Framework-Transfer vorgemerkt als `Satte882/Buch-Framework` Issue #17; noch keine Framework-Dateien geändert
- Human Gate G2: historisch APPROVED, **aktueller Rework-Stand requires reapproval**
- Human Gate G3 / Prosa-Stil: historische Stilreferenz bleibt APPROVED
- Human Gate G4 / Manuskript: **blockiert bis G2-Reapproval + neuer Gesamtmanuskript-Review**

## Arbeitsprinzip

Die Story wurde konsequent vom Groben ins Feine aufgebaut:

`Buchidee / Gesamtarchitektur → Baustein → Ereignisse → Szene → Beats → Prosa`

Der Pilot hat zusätzlich gezeigt: **Semantische Vollständigkeit allein reicht nicht.** Eine Szenenfolge kann in Kausalität, Information und Figurenverantwortung korrekt sein und trotzdem auf Whole-Book-Ebene monoton werden, wenn zu viele Storyfunktionen über denselben dramaturgischen Träger erzählt werden.

Deshalb wurde nach wiederholten manuskriptweiten Majors nicht weiter nur Prosa poliert, sondern kontrolliert auf Szene/Beat zurückgesprungen.

## Scene-Shape-Backtrack

Die Storyursachen und Ereignisse bleiben gleich. Verändert wurde ausschließlich, **wie** ausgewählte Szenen ihre bereits freigegebene Storyfunktion tragen:

| Szene | neuer dominanter Träger |
|---|---|
| S008 | erste Governance-Regel wird live im klinischen Workflow erlebt |
| S014 | klinischer Low-Confidence-Fall löst den Analyseauftrag aus |
| S018 | Eva führt allein die persönliche Gegenprobe auf ihre eigenen Fälle aus |
| S020 | personenbezogene Governance erscheint als persönliche Einstufung / Statusverlust |
| S024 | Eva entwickelt die Wert-/Kontext-Gegenarchitektur zuerst allein |
| S032 | Solo-Break-glass wird in einem funktionalen Stresstest praktisch verifiziert |

Damit bleibt jeweils nur dort ein klassischer Review-/Governance-Termin stehen, wo er dramaturgisch selbst die notwendige Handlung ist.

## Lesson Learned

`LESSONS_LEARNED.md` hält die Ursache und Prävention fest.

Kernregeln für zukünftige Läufe:

- Whole-Book Scene-Shape Review bereits vor G2,
- dramaturgischen Primary Carrier pro Szene sichtbar machen,
- nicht nur Einzel-Szenen, sondern Verteilung über Sequenzen prüfen,
- G3 zusätzlich mit einem zusammenhängenden Mittelteil-Run testen,
- globale Dialog-/Scene-Repetition-Muster statt nur lokale Scanner-Findings bewerten,
- wiederholt derselbe Manuskript-Major nach Prosa-Rework → kontrollierter G2-Backtrack statt weiterer Satzpolitur.

Der Transfer ins Framework ist als Issue #17 erfasst, wird aber erst nach erfolgreichem G4 dieses Piloten implementiert.

## Stilreferenz G3

- `S001 – Die letzte Kapazität`: akuter medizinischer Druck
- `S019 – Die Bilanz`: analytischer Midpoint
- `S023 – Würden Sie es wieder tun?`: persönliche Konfrontation

Diese Szenen bleiben die interne Stilkalibrierung. Der aktuelle Backtrack verändert deren freigegebene Kernfunktion nicht.

## Aktuelle Phase

**G2-Re-Review des geänderten Szenen-/Beat-Stands.**

Nächster Auftrag:

`SCENE_FRESH_CONTEXT_TASK.md`

Fester Zielstand:

`78222a7e99c80378c35379ad42684ee332a412a6`

Der Review prüft ohne Prosa:

- G1-/Event-Treue,
- Beat-Readiness,
- Whole-Book Scene-Shape-Verteilung,
- insbesondere, ob der wiederkehrende Meeting-/Review-Träger noch strukturell als Major angelegt ist.

Danach zwingende Reihenfolge:

1. Fresh-Context-Szenen-/Beat-Re-Review,
2. Findings dispositionieren,
3. bei `READY_FOR_REAPPROVAL` erneuter Human-Token `G2-APPROVE`,
4. danach `MANUSCRIPT_FRESH_CONTEXT_TASK.md` gegen denselben Rework-Target ausführen,
5. nur ohne offene Blocker/Major-Findings → `READY_FOR_HUMAN_G4`,
6. Human Gate **G4 – Manuskript**,
7. danach Produktion / G5.

## Reihengedanke

Die Bücher sind keine klassische Fortsetzungsreihe mit denselben Figuren. Gemeinsam ist die dramaturgische Denkmaschine:

> Ein gesellschaftlich nachvollziehbares Problem trifft auf eine zunächst vernünftige Lösung. Die Lösung funktioniert. Gerade ihr Erfolg verschiebt schrittweise eine Grenze, bis etwas normal oder legitim erscheint, das zu Beginn kaum akzeptabel gewesen wäre.

## Thematischer Kern

**Thema:** KI + Entscheidungsmacht  
**Konflikt:** Ergebnisqualität vs. legitime menschliche Entscheidungsmacht

> **Wie lange darf ein Mensch eine schlechtere Entscheidung treffen, wenn eine Maschine nachweislich die bessere kennt?**

Kernumkehr:

> **Nicht mehr die Maschine muss beweisen, dass sie recht hat. Der Mensch muss beweisen, warum er von ihr abweichen darf.**