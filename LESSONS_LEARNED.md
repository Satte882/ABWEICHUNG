# Lessons Learned – ABWEICHUNG

## LL-001 – Semantische Vollständigkeit verhindert keine Szenenmonotonie

status: confirmed_from_real_pilot
source: Fresh-Context-Gesamtmanuskript-Reviews vor G4
scope: Scene Layer / Beat Layer / G2 / G3 / Whole-Manuscript Review

### Beobachtung

ABWEICHUNG war vor der Prosa semantisch ungewöhnlich sauber:

- G1-Storywahrheit konsistent,
- 18 Bausteine / 54 Ereignisse vollständig,
- 40 Szenen deckten die Ereignisse ab,
- 253 Beats granularisierten die Szenen,
- Fresh-Context-Szenen- und Beat-Reviews fanden keine offenen Architekturblocker.

Trotzdem meldeten zwei unabhängige Gesamtmanuskript-Durchgänge wiederholt dieselben Major-Probleme:

1. zu viele strukturell ähnliche Governance-/Review-Szenen,
2. zu häufig dieselbe Dialogmechanik Frage → Kurzantwort → Gegenfrage,
3. dadurch Pacing-/Ermüdungsrisiko im Mittelteil.

### Root Cause

Die Pipeline prüfte vor G2 vor allem:

- Ereignisabdeckung,
- Kausalität,
- Informationsreihenfolge,
- Figurenverantwortung,
- Research-/Storykonsistenz,
- Beat-Vollständigkeit.

Nicht systematisch geprüft wurde die **Verteilung der dramaturgischen Szenenformen über das ganze Buch**.

Dadurch konnten viele Szenen einzeln korrekt und sogar gut sein, während ihre Summe monoton wirkte.

Der Fehler lag deshalb nicht primär in einzelnen Formulierungen. Er lag eine Ebene höher: in der wiederholten Wahl desselben **dramaturgischen Trägers** für unterschiedliche Storyfunktionen.

Beispiel des problematischen Musters:

`Regel / Daten werden gezeigt → Eva prüft → Gegenposition antwortet → Regel wird präzisiert / akzeptiert`

Dieses Muster war lokal plausibel und wurde von szenenweisen Reviews nicht als Major erkannt. Erst die Lektüre des gesamten Manuskripts machte die Häufung sichtbar.

## Korrektur in ABWEICHUNG

Der erste reine Prosa-Hardening-Pass reichte nicht. Deshalb wurde bewusst zu G2 zurückgesprungen und bei ausgewählten Szenen die dramaturgische Trägerform geändert, ohne G1-Storywahrheit zu verändern.

### Strukturell geänderte Szenen

| Szene | vorher dominanter Träger | nach Backtrack |
|---|---|---|
| S008 | Regelbesprechung | erste Governance-Regel wird live im klinischen Workflow erlebt |
| S014 | Analysebesprechung | klinischer Low-Confidence-Fall löst den Analyseauftrag aus |
| S018 | Eva/Miriam/Jan-Besprechung | Eva prüft allein ihre eigenen Fälle und gibt die Gegenprobe frei |
| S020 | Verhandlung personalisierter Governance | Eva erhält ihre persönliche Einstufung und erlebt den Statusverlust direkt |
| S024 | Whiteboard-Verhandlung | Eva entwickelt die Gegenarchitektur zuerst allein; Miriam testet nur die Schwachstelle |
| S032 | zweite SOP-/Break-glass-Verhandlung | funktionaler Stresstest beweist praktisch, dass der Break-glass real ist |

Storyursachen, Governance-Stufen, Figurenverantwortung und Finale bleiben unverändert.

## Präventive Regel für zukünftige Romanläufe

### 1. Scene-Shape Review vor G2

Jede Szene bekommt zusätzlich zur Storyfunktion einen **Primary Dramatic Carrier**. Beispielklassen:

- `clinical_action`
- `personal_confrontation`
- `solo_analysis`
- `data_review`
- `governance_design`
- `audit_investigation`
- `relationship_scene`
- `implementation_test`
- `aftermath`
- `resource_conflict`

Die Benennung ist sekundär. Entscheidend ist, dass die **Form** der Szene sichtbar wird.

### 2. Whole-Book Distribution Guard

Vor G2 muss die gesamte Szenenfolge als Verteilung geprüft werden, nicht Szene für Szene isoliert.

Arbeitsregeln für den nächsten Pilot:

- nicht mehr als **2 aufeinanderfolgende Szenen** mit demselben Primary Dramatic Carrier,
- in einem gleitenden Fenster von **8 Szenen höchstens 4** Szenen, deren Hauptform `meeting / review / governance / data discussion` ist,
- nach einer neuen Governance-Stufe soll vor der nächsten Governance-Verhandlung möglichst eine **Anwendung, Folge, Konflikt- oder Beziehungsszene** liegen,
- wenn mehrere aufeinanderfolgende Szenen dieselbe Erkenntnismechanik benutzen, muss mindestens eine davon auf Scene-Ebene anders getragen werden.

Diese Schwellen sind Review-Heuristiken, keine mathematischen Romanregeln. Ein Überschreiten verlangt Begründung und bewusste Prüfung, nicht automatische Ablehnung.

### 3. G2 bekommt eine zusätzliche Gate-Frage

Zusätzlich zu `Ist alles prose-ready?` muss geprüft werden:

> Ist die Szenenfolge als Leseerlebnis ausreichend variiert, oder wiederholt die Architektur über längere Strecken denselben dramaturgischen Träger?

G2 darf künftig nicht nur semantische Vollständigkeit bestätigen.

### 4. G3-Sample darf nicht nur isolierte Einzelszenen prüfen

ABWEICHUNG zeigte: Drei repräsentative Einzelszenen können stilistisch tragen und trotzdem ein manuskriptweites Rhythmusproblem übersehen.

Für zukünftige Läufe:

- weiterhin 2–3 repräsentative Einzel-Szenen,
- **zusätzlich ein zusammenhängender Mittelteil-Run von mindestens 6 aufeinanderfolgenden Szenen**.

Dieser zusammenhängende Run prüft:

- Dialogrhythmus über Szenengrenzen,
- Wiederholung von Meeting-/Review-Choreografien,
- Übergangsfloskeln,
- Expositionsdichte,
- Wechsel zwischen Handlung, Analyse und Beziehung.

### 5. Scanner/Review muss global statt nur lokal denken

Ein lokaler Befund wie `dialogue_pingpong = INFO` kann manuskriptweit ein Major werden.

Deshalb künftig zusätzlich auf Gesamtmanuskript-Ebene verfolgen:

- Anteil sehr kurzer Dialogzeilen pro Szene und über Sequenzen,
- Häufung gleicher Szenenformen,
- wiederkehrende Blick-/Übergangsformeln,
- gleiche Eröffnungs-/Schlussmechaniken,
- Verteilung von klinischer/körperlicher Präsenz gegen reine Analyse-/Policy-Szenen.

## Stop-Regel

Wenn ein Fresh-Context-Gesamtmanuskript-Review nach einem reinen Prosa-Rework **dieselben Scene-Repetition-/Pacing-Majors erneut meldet**, darf nicht erneut nur Satzprosa poliert werden.

Dann gilt:

`repeated manuscript-level major → inspect scene architecture → controlled G2 backtrack`

Das verhindert Endlosschleifen aus Prosa-Rework auf einer unveränderten monotonen Szenenarchitektur.

---

## LL-002 – Fresh-Context-Reviews brauchen Adjudikation, sonst entsteht Reviewer-Overfitting

status: confirmed_from_real_pilot
source: dritter Whole-Manuscript-Review nach kontrolliertem G2-Backtrack
scope: Review Protocol / Gate Decisions / G4

### Beobachtung

Nach dem strukturellen Backtrack wurde die vollständige Szenen-/Beat-Ebene unabhängig geprüft. Dieser Review kontrollierte ausdrücklich die Whole-Book-Scene-Shape-Verteilung und meldete:

- `CLEAN_FRESH_CONTEXT`
- `finding_count: 0`
- `READY_FOR_REAPPROVAL`

Der Stand wurde anschließend erneut durch Human `G2-APPROVE` freigegeben.

Ein danach durchgeführter Whole-Manuscript-Review desselben Targets meldete erneut `scene_repetition` als Major. In seiner Evidenz wurden jedoch mehrere Szenen als gleichartige Meeting-/SOP-Träger behandelt, obwohl der geprüfte Target sie gerade strukturell unterschiedlich ausführt:

- S008 als Live-Anwendung im klinischen Workflow,
- S014 als klinischer Low-Confidence-Auslöser mit anschließendem Analyseauftrag,
- S032 als funktionaler Break-glass-Stresstest,
- S013 als Anwendung der Zweitfreigabe im laufenden Stationsbetrieb.

Der Review war damit nicht wertlos; er markierte weiterhin ein mögliches **Restrisiko institutioneller Dichte**. Die gemeldete Severity `major` wurde durch die angeführte Evidenz aber nicht ausreichend getragen.

### Root Cause

Die bisherige Prozesslogik behandelte ein Fresh-Context-Urteil implizit zu stark wie einen automatischen Gate-Entscheid.

Das ist problematisch, weil auch ein unabhängiger Reviewer:

- Szenen unterschiedlich klassifizieren kann,
- thematische Ähnlichkeit mit dramaturgischer Gleichförmigkeit verwechseln kann,
- dieselbe Eigenschaft je nach Lesart unterschiedlich gewichten kann,
- nach mehreren Rework-Runden immer neue Varianten desselben Geschmacksrisikos finden kann.

Ohne Adjudikation entsteht eine Endlosschleife:

`review → rework → neuer review → ähnliche Kritik → weiterer rework`

Irgendwann wird der Text nicht mehr auf Leserwirkung, Storyfunktion und definierte Qualitätsregeln optimiert, sondern auf die wechselnde Präferenz einzelner Reviewer.

### Präventive Regel

Fresh-Context-Reviews liefern **Findings**, keine automatische Gate-Entscheidung.

Für jedes Blocker-/Major-Finding gilt künftig vor Rework:

1. **Evidence Check** – Trägt die konkret genannte Stelle den behaupteten Befund am tatsächlich geprüften Commit?
2. **Cross-Layer Check** – Widerspricht das Finding einem bereits bestandenen gezielten Review derselben Eigenschaft?
3. **Novelty Check** – Ist dies ein neuer konkreter Defekt oder nur eine strengere Variante eines bereits dispositionierten Restrisikos?
4. **Smallest-Rework Check** – Gibt es eine konkrete Änderung, die das Problem behebt, ohne einen anderen freigegebenen Qualitätsaspekt zu beschädigen?
5. **Overfitting Check** – Würde der vorgeschlagene Rework primär eine Reviewer-Präferenz befriedigen oder einen nachvollziehbaren Leser-/Architekturdefekt beheben?

Erst danach wird ein Finding als `confirmed blocker/major`, `minor`, `residual risk` oder `not sustained` dispositioniert.

### Gate-Regel

Ein Raw-Review darf weiterhin `REWORK_REQUIRED` ausgeben. Die Gate-Datei muss dieses Rohurteil unverändert dokumentieren.

Die finale Readiness entsteht jedoch **nach nachvollziehbarer Disposition**:

`raw review → finding adjudication → confirmed open blockers/majors → gate readiness`

Nur **bestätigte** offene Blocker/Majors blockieren das Human Gate.

### Stop-Regel gegen Review-Endlosschleifen

Wenn nach:

1. bestätigtem Major,
2. passendem Rework auf der kleinsten sinnvollen Ebene,
3. unabhängig sauberem Re-Review dieser Ebene,
4. erneutem Whole-Manuscript-Review

wieder dieselbe abstrakte Kritik erscheint, ohne dass die neue Evidenz den behaupteten Major sauber trägt, gilt:

`repeated abstract finding + weak target evidence → adjudicate, do not auto-rework`

Damit bleibt menschliche Gate-Verantwortung real und der Review-Prozess wird nicht selbst zu einer unendlichen Optimierungsschleife.

## Framework-Transfer

LL-001 und LL-002 stammen aus dem ersten realen Romanpiloten und sollen in `Satte882/Buch-Framework` übernommen werden, **nachdem ABWEICHUNG G4 erfolgreich durchlaufen hat**.

Bis dahin bleibt ABWEICHUNG der Validierungsträger; das Framework wird nicht vorschnell anhand eines noch nicht abgeschlossenen Piloten umgebaut.
