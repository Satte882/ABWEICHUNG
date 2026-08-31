# Manuskript-Ausbauanalyse – G5 REWORK

status: ANALYSIS_COMPLETE
trigger: human `G5-REWORK`
date: 2026-08-31
source_manuscript: `78222a7e99c80378c35379ad42684ee332a412a6`
source_production_run: `33366125536`

## Entscheidung

Der G5-Rework wird **PROSA-first** durchgeführt.

Es gibt aktuell keinen belastbaren Grund für einen pauschalen erneuten G2-Backtrack. Die Szenen-/Beat-Architektur wurde vor G4 bereits gezielt reworked und anschließend unabhängig mit `finding_count: 0` gegen denselben Manuskriptstand geprüft.

Die neue G5-Evidenz betrifft primär den Produktumfang und die Ausspielung:

- 40 Szenen
- 16.527 Wörter
- Ø 413 Wörter pro Szene
- viele Szenen realisieren 6–7 Beats in nur ca. 300–500 Wörtern

Die konsolidierte Produktionsfassung zeigt zusätzlich eine starke Kurzabsatz-Kompression. Bei einer einfachen Absatzanalyse des Build-Artefakts liegen rund 65 % der Absätze bei höchstens sieben Wörtern; der Median liegt ungefähr bei sechs Wörtern. Das ist kein automatischer Stil-FAIL, erklärt aber zusammen mit dem Szenenumfang, warum der Text häufig eher wie eine sehr stark verdichtete Szenenausführung als wie ein voll ausgespielter Roman wirkt.

## Rework-Grenze

Der Ausbau darf **keine Wortzahloptimierung** sein.

Jede Ergänzung muss mindestens eine bestehende dramatische Funktion verstärken:

1. körperliche / räumliche Präsenz,
2. konkrete Handlung statt Zusammenfassung,
3. Reaktion und Nachwirkung,
4. Beziehungs- oder Statusdruck,
5. operativer Widerstand / Zeit / Material / Umgebung,
6. Subtext im Dialog,
7. konkrete Konsequenz einer Entscheidung.

Nicht zulässig als bloßer Längenfüller:

- Wiederholung bereits verstandener Governance-Logik,
- erneute Erklärung von KORA-Funktionen ohne neuen Szeneneffekt,
- paraphrasierende Gedanken nach klarer Handlung,
- rhetorische Kontrastketten,
- künstliche Synonymvariation,
- neue Plotfakten nur für mehr Text.

Harter Stilguard bleibt: `sondern = 0`.

## Eskalationsregel

Für jede Szene gilt:

- bestehende Beats tragen die gewünschte Ausspielung → `PROSA`,
- fehlender notwendiger Handlungsschritt innerhalb derselben Szene → `BEAT_CANDIDATE`,
- fehlender eigener dramaturgischer Träger / Zeit- oder Ortswechsel → `SZENE_CANDIDATE`,
- neue Ursache, neue Entscheidung oder neue Storywahrheit → upstream.

Eine Szene wird **nicht** auf eine Zielwortzahl gedehnt. Wenn sinnvolle Prosa-Ausspielung ausgeschöpft ist, bleibt sie kürzer und wird bei Bedarf als Kandidat für einen lokalen Beat-/Scene-Rework markiert.

## Arbeitskorridore – keine Acceptance-Grenzen

Die folgenden Korridore dienen nur als Ausführungsheuristik, damit Ankerszenen erkennbar mehr Gewicht bekommen als Übergangs-/Analyseszenen:

- `A – Anchor`: häufig ca. 1.200–1.800 Wörter
- `B – Standard`: häufig ca. 800–1.200 Wörter
- `C – Lean/Transition`: häufig ca. 500–800 Wörter
- `CODA`: häufig ca. 350–600 Wörter

Abweichungen sind ausdrücklich zulässig. Der Text entscheidet, nicht der Zähler.

## Szenenmatrix

| ID | Szene | Ist-Wörter | Gewicht | Rework | Primärer Ausbauhebel |
|---|---|---:|---|---|---|
| S001 | Die letzte Kapazität | 654 | A | PROSA | klinische Echtzeit, Körper, Raum, Zeitdruck, fernes Gegenrisiko |
| S002 | Der sichtbare Erfolg | 448 | B | PROSA | unmittelbare Nachwirkung, institutionelle Reaktion, Evas Restspannung |
| S003 | Morgenreview | 406 | C | PROSA | bewusst knapp halten; Arbeitsablauf und Subtext statt Zusatzexposition |
| S004 | Die besseren Zahlen | 389 | B | PROSA | Evidenz als konkrete Arbeit, Reibung zwischen Zahlen und Verantwortung |
| S005 | Die Bettenkette | 407 | B | PROSA | operative Kette und sichtbare Folgen statt bloßer Datenfolge |
| S006 | Der zweite Ausgang | 417 | A | PROSA | Konsequenz des entfernten Falls, Evas Wahrnehmungsverschiebung |
| S007 | Laura Berg | 355 | A | PROSA | Person statt Fallakte, Beziehungsspannung und Erinnerung |
| S008 | Grund angeben | 338 | B | PROSA | Live-Anwendung der Regel im klinischen Workflow ausspielen |
| S009 | Freitext | 427 | B | PROSA | Reibung durch Dokumentation, praktische Nebenwirkungen |
| S010 | Neles Fall | 328 | A | PROSA | klinischer Verlauf, Neles Eigenentscheidung, Evas indirekte Verantwortung |
| S011 | Zu spät | 427 | A | PROSA | Schadensnachwirkung, Mentoring-/Kulturbruch, körperliche Präsenz |
| S012 | Zweite Unterschrift | 398 | B | PROSA | Zweitfreigabe als konkrete Arbeitsstörung und Verantwortungsverschiebung |
| S013 | Schutz oder Gehorsam | 413 | B | PROSA | Felix/Nele-Beziehungsdruck, Stationsrealität, Entscheidungskosten |
| S014 | Getrennte Daten | 329 | B | PROSA | konkreter Low-Confidence-Auslöser, Evas Analyseauftrag in Handlung |
| S015 | Wo KORA irrt | 345 | B | PROSA | Fallmaterial und Unsicherheit sichtbar machen, nicht nur Ergebnis melden |
| S016 | Zu wenige Konflikte | 291 | B | PROSA | Felix als Person, Misstrauen, nonverbale Spannung, Arbeitsplatzkontext |
| S017 | Der Zeitpunkt | 401 | B | PROSA | Auditlogik über konkrete Rekonstruktion und Reibung ausspielen |
| S018 | Meine Fälle | 372 | B | PROSA | Solo-Analyse körperlich/räumlich verankern; Erkenntnis entstehen lassen |
| S019 | Die Bilanz | 761 | A | PROSA | Midpoint-Gewicht, emotionale und methodische Umwertung vertiefen |
| S020 | Schwelle für Eva | 319 | A | PROSA | Statusverlust erlebbar machen; Wirkung im Arbeitsalltag vor Erklärung |
| S021 | Kein Gegenbeleg | 430 | B | PROSA | Prüfung als Handlung, Friktion der neuen persönlichen Grenze |
| S022 | Die Chronologie | 584 | A | PROSA | Konfrontation, Zeitfolge, Lauras Druck, Evas Verteidigung |
| S023 | Würden Sie es wieder tun? | 643 | A | PROSA | persönliche Konfrontation, Pausen, Subtext, unvollständige Antworten |
| S024 | Zwei Arten von Abweichung | 344 | B | PROSA | Gegenarchitektur aus konkreten Fällen/Notizen entstehen lassen |
| S025 | Der Werteraum | 408 | B | PROSA | Grenzfälle als konkrete Prüfobjekte statt abstrakte Kategorien |
| S026 | Zu viele Ausnahmen | 400 | B | PROSA | Missbrauchs-/Umdeklarationsdruck konkretisieren |
| S027 | Nähe zählt nicht | 446 | B | PROSA | Regeltext, Widerstand und Konsequenz als echte Verhandlung ausspielen |
| S028 | Unter der Schwelle | 425 | A | PROSA | akuter Schadensfall, klinische Präsenz, Verzögerung und Folgen |
| S029 | Zeitstempel | 435 | A | PROSA | Audit als Rekonstruktion; Verdacht und Beweisschritte körperlich/operativ |
| S030 | Felix | 521 | A | PROSA | Konfrontation, Beziehungsvorgeschichte, Rechtfertigung, Bruch |
| S031 | Drei Risiken | 390 | B | PROSA | Endgovernance über konkrete Failure-Modes und Interessen |
| S032 | Break glass | 358 | B | PROSA | Stresstest als Vorgang, nicht als bloßes Konzeptgespräch |
| S033 | Kapazitätsspitze | 326 | A | PROSA | Finalspiegel zum Cold Open: Patient, Team, Zeit, Körper, entfernte Lage |
| S034 | Beide Patienten | 344 | A | PROSA | Duty-to-care-Konflikt maximal ausspielen; Gegenprüfung ohne Expositionsdopplung |
| S035 | Zweite Freigabe | 361 | A | PROSA | Nele/Eva-Konflikt, Rollenwechsel und Entscheidungsdruck |
| S036 | Der Knopf | 492 | A | PROSA | Solo-Break-glass, Zeit, Körper, Versuchung und freiwilliger Verzicht |
| S037 | Der lokale Ausgang | 381 | A | PROSA | Tod/Nachwirkung ohne melodramatische Erklärung; Team und Eva |
| S038 | Der andere Ausgang | 349 | A | PROSA | entfernter Überlebender als reale Gegenwirklichkeit, kein KORA-Triumph |
| S039 | Human Oversight | 513 | A | PROSA | institutionelle Erfolgserzählung vs. Evas Erfahrung; Nachhall |
| S040 | Was sieht KORA nicht? | 152 | CODA | PROSA | neuen Fall konkret genug verkörpern, Frage offen lassen |

## Befund an kritischen Beispielen

### S033/S034 – Finale Kapazitätsspitze

Die Szenenkarten und Beats enthalten bereits die notwendigen dramatischen Schritte:

- mehrere Standorte unter Last,
- nur eine freie Intensivressource,
- lokaler respiratorischer Patient,
- entfernter septischer Patient,
- KORA-Vergleich,
- Evas erneute medizinische Gegenprüfung,
- kein tragfähiger Gegenbeleg,
- unmittelbarer Pflichtimpuls,
- Abweichungsantrag.

Dass S033/S034 zusammen aktuell nur rund 670 Wörter tragen, ist daher zunächst ein **Ausspielungsproblem**, kein Beleg für fehlende Storyarchitektur.

### S040 – Coda

S040 besitzt sechs klare Beats und eine tragfähige Schlussfunktion. Die Szene muss offen enden, aber Offenheit verlangt keine extreme Kürze. Ein neuer klinischer Fall, die jüngere Ärztin, Evas Prüfung und die veränderte Denklogik können konkreter erlebt werden, ohne die Antwort auf die Schlussfrage vorwegzunehmen.

## Manuskriptweite Diagnose

Der Rework soll nicht nur die kürzesten Szenen aufblasen. Die Kompression ist **manuskriptweit** vorhanden.

Das bedeutet:

1. alle 40 Szenen werden prose-seitig geprüft,
2. Ankerszenen erhalten deutlich mehr Zeit und Erlebnisgewicht,
3. analytische Szenen werden nur dort erweitert, wo konkrete Handlung/Material/Subtext trägt,
4. bewusst knappe Übergangsszenen dürfen knapp bleiben,
5. nach jedem Batch wird geprüft, ob der neue Text wieder in Erklärung, Meeting-Monotonie oder rhetorische Symmetrie kippt.

## Gate-Konsequenz

Aktuell erforderlich:

- G1: bleibt gültig
- G2: bleibt gültig; keine pauschale Neuöffnung
- G3: Stilrichtung bleibt gültig
- G4: `REAPPROVAL_REQUIRED`
- G5: `REWORK`

Nach vollständigem Prosa-Ausbau folgen:

1. mechanischer Prosa-Audit,
2. Same-Context-Manuskriptprüfung,
3. unabhängiger Fresh-Context-Gesamtmanuskriptreview,
4. Adjudikation konkreter Befunde,
5. Human `G4-REAPPROVE`,
6. neuer reproduzierbarer Produktionsbuild,
7. erneuter Human Gate G5.

## Aktiver nächster Schritt

**PROSA-Ausbau S001–S040 in kontrollierten Batches, mit Schwerpunkt auf dramatischer Ausspielung statt zusätzlicher Erklärung.**
