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

## Framework-Transfer

Dieses Lesson Learned stammt aus dem ersten realen Romanpiloten und soll in `Satte882/Buch-Framework` übernommen werden, **nachdem ABWEICHUNG den Rework bis G4 erfolgreich durchlaufen hat**.

Bis dahin bleibt ABWEICHUNG der Validierungsträger; das Framework wird nicht vorschnell anhand eines noch nicht abgeschlossenen Reworks umgebaut.