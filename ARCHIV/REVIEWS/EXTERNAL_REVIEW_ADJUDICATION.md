# EXTERNAL_REVIEW_ADJUDICATION – ABWEICHUNG

review_target: `5a92116a20100267ccaa9a70086824be2e5c2942`
external_result: `EXTERNAL_REVIEW_RESULT.md`
adjudication_status: COMPLETE

## Ergebnis

- bestätigte Blocker: **0**
- bestätigte Major: **2**
- bestätigte Minor: **4**
- auf Minor heruntergestuft: **1**
- rejected / accepted trade-off ohne Reworkpflicht: **2**

human_gate_effect: `REWORK_REQUIRED`
controlled_g2_backtrack_required: `yes`
g3_style_direction_remains_valid: `yes`
g4_status: `REWORK_REQUIRED`

## XR-001 – institutionelle Scene-Repetition / Pacing

disposition: confirmed
confirmed_severity: major
correction_triggered: yes
recommended_rework_level: scene | beat

### Begründung

Der Befund ist nicht nur eine externe Geschmacksäußerung. Das Projekt hatte denselben Problemkomplex bereits früher als manuskriptweiten Major erkannt und deshalb einen kontrollierten G2-Scene-Shape-Backtrack durchgeführt. `gates/G2.md` dokumentiert ausdrücklich wiederholte Major-Probleme bei `Scene-Repetition / Meeting-Governance-Choreografie`, `Dialogue-Pingpong` und daraus entstehendem Pacing-/Ermüdungsrisiko.

Der damalige Rework änderte gezielt S008, S014, S018, S020, S024 und S032. Der externe Reviewer findet das Muster jetzt unabhängig erneut, diesmal vor allem in einer anderen großen Gruppe von Kapiteln (3, 5–6, 9, 11–12, 15–16, 19, 22–23, 25–26, 29, 31). Damit ist die Restdichte größer als intern zuletzt als Minor akzeptiert.

Die frühere interne Einstufung als bloßes Rest-Minor war zu tolerant. Dass ein unabhängiger Reviewer denselben Whole-Book-Effekt ohne Kenntnis der internen Finding-Liste erneut als Major identifiziert, ist ausreichende Evidenz für einen erneuten gezielten Scene-/Beat-Backtrack.

### Rework-Prinzip

Nicht alle genannten Kapitel neu schreiben und keine neuen Plotereignisse erfinden. Stattdessen die Szenenfolge in den betroffenen Clustern neu projizieren und dort, wo mehrere Nachbarkapitel denselben institutionellen Träger besitzen:

- Information in laufende klinische Handlung verlagern,
- reine Review-/Daten-/Regel-Szenen verkürzen oder mit einer konkreten Konsequenz koppeln,
- analytische Erkenntnis nicht in mehreren direkt benachbarten Szenen erneut explizieren,
- mindestens einzelne Träger in Beziehung, unmittelbare Handlung, Entscheidung unter Zeitdruck oder Nachwirkung verschieben.

## XR-002 – Dialog-Pingpong / Review-Protokoll-Stimme

disposition: confirmed
confirmed_severity: major
correction_triggered: yes
recommended_rework_level: scene | prose

### Begründung

Der aktuelle Post-Rhythmus-Audit weist trotz bereits erfolgtem Rhythmus-Rework noch **58 Dialog-Pingpong-Runs** aus. Besonders hohe lokale Werte bleiben u. a. in S030 (5 Runs) sowie zahlreichen Szenen mit 2–3 Runs. Der externe Reviewer beschreibt unabhängig genau die daraus entstehende Leserwirkung: kurze Frage → knappe Antwort → Präzisierung/Gegenfrage über viele institutionelle Dialoge.

S030 zeigt exemplarisch, dass das Muster zwar inhaltlich funktioniert, aber über längere Strecken tatsächlich als eng getaktete Argumentkette gebaut ist. Das Problem ist damit nicht die Existenz kurzer Repliken, sondern ihre manuskriptweite Verteilung.

### Rework-Prinzip

- kurze Repliken dort behalten, wo Konflikt oder Druck sie motiviert;
- in analytischen Gesprächen mehrere atomisierte Q/A-Schritte in charakteristischere vollständige Redezüge, Reaktion oder Handlung überführen;
- Figuren nicht abwechselnd Beweisbausteine sprechen lassen;
- Konflikt öfter über Auslassen, Missverstehen, Abbruch, Handlung und unterschiedliche Prioritäten tragen statt über perfekte Präzisierungsketten.

## XR-003 – Nebenfiguren als funktionale Positionen

disposition: confirmed
confirmed_severity: minor
correction_triggered: yes
recommended_rework_level: scene | prose

### Begründung

Der Kernbeobachtung ist teilweise richtig: Vor allem Jan und Miriam werden häufig über Daten-/Governance-Funktionen eingesetzt, wodurch ihre Stimmen in institutionellen Szenen funktional wirken können. Die externe Severity `major` ist jedoch zu hoch.

Die kanonische Figurenarchitektur enthält bereits eigenständige Rollen, Druckpunkte und Beziehungen. Felix besitzt im Konflikt S030 eine persönliche gemeinsame Vorgeschichte mit Eva, explizite Verletzung und einen realen Beziehungsbruch. Miriam bleibt im Finale nicht bloß Regelhüterin, sondern widerspricht einer simplen institutionellen Erfolgserzählung und anerkennt ausdrücklich, dass Governance Freiheit beeinflusst. Nele besitzt einen eigenen Lernbogen und wird im Finale zur unabhängigen Prüferin Evas.

Das Defizit liegt daher nicht in fehlenden Figurenarchitekturen oder zwingend notwendigen privaten Nebenplots, sondern in der Art, wie einige institutionelle Szenen diese Figuren zu oft primär als argumentative Funktionen benutzen.

### Rework-Prinzip

Im Rework von XR-001/XR-002 Beziehungen und individuelle Sprach-/Handlungslogik stärker in bestehende Szenen tragen. Keine zusätzlichen privaten Subplots nur zur „Abrundung“ erfinden.

## XR-004 – Finale löse die Leitfrage nur erneut aus

disposition: accepted_tradeoff
confirmed_severity: none
correction_triggered: no
recommended_rework_level: none

### Begründung

Die externe Beobachtung, dass das Ende offen bleibt, ist korrekt; die Wertung als Major widerspricht jedoch der ausdrücklich gesetzten Funktion von S040. Die Szenenkarte verlangt: `Den Roman mit verschobener Denklogik statt mit einer politischen Schlussrede beenden` und als Konsequenz ein `Offenes Ende auf der zentralen Frage des Romans; keine Behauptung, die neue Ordnung sei endgültig richtig.`

Zugleich ist Evas Veränderung nicht nur verbal. In S040 reagiert sie auf die junge Ärztin anders als früher: Sie prüft zuerst, ob ein neuer Befund, Patientenwille, Therapieziel oder eine andere nicht abgebildete Information existiert, und stellt erst dann die Frage `Was sieht KORA nicht?`. Damit ist die verschobene Beweislast als Handlung sichtbar.

Ein stärker abschließendes moralisches oder politisches Ergebnis würde gerade die gewünschte Ambivalenz beschädigen. Kein G4-Rework aus diesem Finding.

## XR-005 – kontrollierte Prosa / Mikro-Choreografie / Erklär-Echos

disposition: confirmed
confirmed_severity: minor
correction_triggered: yes
recommended_rework_level: prose

### Begründung

Der Post-Rhythmus-Audit zeigt weiterhin 127 Filterwort-Treffer, 96 Weichmacher und 49 heuristische Explanation-Echo-Kandidaten. Die Werte allein sind kein Finding, aber der externe Reviewer beschreibt dazu eine konkrete Leserwirkung: hohe kontrollierte Gleichförmigkeit und maschinell wirkende Klarheit.

Das passt zur bereits gesetzten Anti-KI-Prosa-Anforderung. Der Befund wird deshalb als Minor bestätigt, aber nicht mit einem neuen globalen kosmetischen Pass bearbeitet. Er wird lokal in den durch XR-001/XR-002 ohnehin geöffneten Szenen mitbehoben.

## XR-006 – wiederholte Kausalitätsqualifikation dämpft emotionale Wirkung

disposition: confirmed
confirmed_severity: minor
correction_triggered: yes
recommended_rework_level: beat | prose

### Begründung

Die epistemische Grenze selbst ist kanonisch und darf nicht entfernt werden: `CHARACTERS.md` legt fest, dass niemand individuelle kontrafaktische Patientenverläufe sicher kennt. Die externe Kritik richtet sich jedoch plausibel gegen die wiederholte explizite Ausformulierung derselben Unsicherheit an mehreren emotionalen Höhepunkten.

Rework deshalb nur auf Vermittlungsebene: Wo die Grenze bereits verstanden ist, darf sie später durch Verhalten, Schweigen oder kürzere Formulierung getragen werden, statt erneut vollständig erklärt zu werden. Keine falsche Kausalgewissheit erzeugen.

## XR-007 – Laura werde nach Kapitel 7 kaum noch genutzt

disposition: rejected
confirmed_severity: none
correction_triggered: no
recommended_rework_level: none

### Begründung

Das Finding beschreibt den geprüften Text nicht korrekt. Laura wird in Kapitel 7 als Name/Angehörigenanfrage eingeführt, kehrt aber in Kapitel 22 **und Kapitel 23** in zwei vollständigen direkten Konfrontationsszenen zurück. In S022 rekonstruiert sie mit Eva den Ressourcenkonflikt; S023 stellt mit `Würden Sie es wieder tun?` eine der zentralen persönlichen Fragen des Romans und führt direkt zur späteren Nähe-/Kontextlogik.

Dass danach keine Freundschaft oder wiederkehrende Nebenhandlung entsteht, ist zudem explizit kanonisch (`CHARACTERS.md`: danach keine künstliche Freundschaft und kein Racheplot).

## XR-008 – Felix' Regelbruch habe zu wenig Nachwirkung

disposition: confirmed
confirmed_severity: minor
correction_triggered: yes
recommended_rework_level: scene | beat

### Begründung

S030 enthält bereits eine deutliche persönliche Konsequenz: gemeinsame klinische Vorgeschichte, offener Vertrauensbruch, Meldung durch Eva, Funktionsverlust und die Feststellung, dass zwischen beiden nichts mit einem sachlichen Gespräch zu reparieren bleibt. Damit ist der externe Befund nicht in voller Stärke richtig.

Er trifft jedoch einen Restpunkt: Direkt danach abstrahiert S031 Felix sehr schnell zum dritten `Failure-Mode` neben Eva und Nele. Die Stations-/Beziehungsnachwirkung wird fast ausschließlich in einem kurzen Schlussabsatz von S030 behauptet und kaum noch erlebt.

Ein kleiner downstream Beat mit beobachtbarer Abwesenheit/Veränderung reicht; keine neue Felix-Nebenhandlung und kein zusätzliches Großkapitel.

## Gate-Konsequenz

Zwei bestätigte Majors bleiben offen:

1. XR-001 – Scene-Repetition/Pacing
2. XR-002 – Dialogue-Pingpong

Beide betreffen denselben bereits früher reworkten Problemkomplex. Deshalb gilt die Framework-Stop-Regel:

`repeated manuscript-level major -> inspect scene architecture -> controlled G2 backtrack`

Der nächste Schritt ist **kein weiterer Whole-Book-Satzpass**. Es folgt ein gezielter zweiter Scene-/Beat-Shape-Rework der vom externen Review identifizierten Cluster, wobei G1/Events und die zentrale Storywahrheit unverändert bleiben sollen.

Nach diesem Rework:

1. betroffene Prosa neu ableiten/reworken,
2. Whole-Manuscript-Regression,
3. finaler Prosa-/Rhythmuscheck nur auf die geänderten/angrenzenden Bereiche plus deterministische Whole-Book-Guards,
4. externer Vollreview erneut, weil bestätigte Majors relevantes Rework ausgelöst haben,
5. externe Findings adjudizieren,
6. erst dann G4 Human Gate.
