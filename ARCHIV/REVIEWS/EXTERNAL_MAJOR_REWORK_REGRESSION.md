# External-Major-Rework – Regression

status: PASS_PENDING_EXTERNAL_REREVIEW
candidate_commit: `7b476fe63e933592d36e9ab9a385a01187de60d5`
review_basis: `EXTERNAL_REVIEW_RESULT.md` + `EXTERNAL_REVIEW_ADJUDICATION.md`
confirmed_majors: `XR-001, XR-002`

## Ergebnis

Der kontrollierte G2-Backtrack wurde auf die bestätigten externen Majors begrenzt. G1-Storyarchitektur, Ereignisfolge, Midpoint, Felix-Kausalität, Wert-/Kontextgrenzen und Finale wurden nicht neu geöffnet.

### XR-001 – Scene-Repetition / institutionelle Trägerdichte

Disposition nach Rework: **resolved for rereview**.

Die analytische Arbeit liegt nicht mehr in einer Folge gleichartiger Meeting-/Review-Szenen:

- S012: Zweitfreigabe wird im laufenden Stationsworkflow und an einer Trainingskopie geprüft.
- S015: Evidenz wird zuerst über konkrete Fallkarten erarbeitet, erst danach aggregiert.
- S016: Felix' Gegenposition entsteht im Intensivalltag an einem realen Patienten statt in einer abstrakten Governance-Runde.
- S025: Wert-/Kontextlogik wird an einem realen Patienten mit dokumentiertem Therapieziel entwickelt.
- S026: Kategorienmissbrauch wird zuerst in einer konkreten Entscheidung erlebt und erst danach als Muster geprüft.
- S031: End-Governance wird als Vor-Ort-Implementierungswalkthrough gezeigt; Felix' Funktionsverlust ist sichtbar im Dienstplan verankert.

S003 und S019 bleiben bewusst als institutionelle bzw. datengetriebene Anker, weil sie jeweils einmal eine eigenständige dramaturgische Funktion erfüllen.

### XR-002 – Dialog-Pingpong / Review-Protokoll-Rhythmus

Disposition nach Rework: **resolved for rereview**.

Messwerte aus den Whole-Manuscript-Audits:

- vor External-Major-Rework: **58** Dialog-Pingpong-Runs,
- nach erstem Scene-Shape-Rework: **44**,
- finaler gezielter Dialog-Rework: **27**.

Das entspricht gegenüber dem Ausgangswert einer Reduktion um **31 Runs / 53,4 %**.

Gezielt entschärft wurden die verbliebenen Hochdichte-Stellen in S005, S006, S010, S011, S022 und S039. Funktionale kurze Dialoge in Akutsituationen oder emotional bewusst gesetzte Einzelantworten wurden nicht pauschal entfernt.

## Whole-Manuscript-Regression

Quelle: `FINAL_PROSE_RHYTHM_AUDIT_EXTERNAL_REWORK.md`, Status `POST_EXTERNAL_MAJOR_REWORK_FINAL`.

- Szenen: **40**
- Wörter in Szenen-Prosa: **37.615**
- Geviertstrich `—`: **0**
- `sondern`: **0**
- Dialog-Pingpong-Runs: **27**
- Stakkato-Runs: **11**
- kurze Negations-Runs: **2**
- narrative Kurzabsätze ≤7 Wörter: **1.143**

Der CI-Guard akzeptiert den Stand nur bei höchstens 34 Dialog-Pingpong-Runs; der tatsächliche Wert liegt mit 27 deutlich darunter.

## Semantische Regression

Keine Änderung an:

- 40-Szenen-Reihenfolge,
- zentraler Ressourcenkausalität,
- KORA als nicht-böse Entscheidungsunterstützung,
- Neles Schadensfall,
- Midpoint-Reversal,
- personenbezogener Ressourcen-/Eskalationsklasse,
- Felix' Umgehungsmechanismus,
- Wert-/Kontextausnahme,
- realem Solo-Break-glass,
- Schlussmechanik und letztem Satz `Eva wartete.`.

## Gate-Empfehlung

`g2_rework_readiness: READY_FOR_REAPPROVAL`

`g4_candidate_readiness: READY_FOR_EXTERNAL_REREVIEW_AFTER_G2`

Der erste externe Review hat seinen Zweck erfüllt und zwei echte Majors aufgedeckt. Da diese relevantes Rework ausgelöst haben, verlangt `Buch-Framework/EXTERNAL_LLM_REVIEW_PROTOCOL.md` noch einen zweiten externen Vollreview auf dem neuen fixierten Kandidaten, bevor G4 geschlossen wird.
