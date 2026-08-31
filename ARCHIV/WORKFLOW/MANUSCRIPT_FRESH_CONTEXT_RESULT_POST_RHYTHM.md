review_status: EVIDENCE_BOUND_REVIEW
review_target: c0bc7fc5b23d29da60ed6784fd31ebdcd4f899fb
finding_count: 3

finding_id: MANUSCRIPT-POST-RHYTHM-001
location: S020–S021 / Kapitel 20 „Die neue Schwelle“ → Kapitel 21 „Kein Gegenbeleg“
finding_type: continuity
severity: major
problem: Die personenbezogene Zweitfreigabeschwelle wird in S020/Prosa ausdrücklich aufgrund von Evas ungünstiger Bilanz bei high-confidence Ressourcenabweichungen auf Ressourcenentscheidungen begrenzt; Eva verlangt zusätzlich, dass die Einstufung nicht automatisch auf andere Entscheidungsklassen übertragen wird. In S021 greift die persönliche Schwelle unmittelbar danach bei einer Eskalationsentscheidung und wird in der Oberfläche sogar als „high-confidence Ressourcen-/Eskalationsklasse“ bezeichnet. Damit überschreitet die Governance genau die Klassengrenze, die S020 unmittelbar zuvor ausdrücklich festschreibt.
evidence: `BAUSTEINE/10_PERSONENBEZOGENE_GOVERNANCE/SZENEN/10_10_01_SCHWELLE_FUER_EVA/SZENE.md` bindet die Kriterien an eine definierte Entscheidungsklasse und verlangt ausdrücklich keine automatische Übertragung; `BEATS.md` S020-B04 wiederholt diese Grenze. In `ABWEICHUNG_FINAL.md` Kapitel 20 lautet die aktive Regel „Individuelle Zweitfreigabeschwelle aktiv – high-confidence Ressourcenentscheidungen“ und die Begründung nennt „high-confidence Ressourcenabweichungen“. Kapitel 21 ist dagegen ein Eskalationsfall („KORA empfahl ... die nächste Eskalationsstufe“) und zeigt „Individuelle Zweitfreigabe erforderlich – high-confidence Ressourcen-/Eskalationsklasse“.
impact: Die erste konkrete Wirkung der personenbezogenen Governance ist ein zentraler Schritt von Evas Rollenwechsel. Wenn die Institution die gerade zugesicherte Klassengrenze im unmittelbar nächsten Fall still überschreitet, wirkt die Eskalation entweder inkonsistent oder ungewollt autoritärer als die kanonische Architektur. Das schwächt die Legitimität der Governance-Kette und Evas spätere Akzeptanz der Regel.
recommended_rework_level: scene

finding_id: MANUSCRIPT-POST-RHYTHM-002
location: S022 / Kapitel 22 „Die Chronologie“, Begrüßung Laura Berg ↔ Eva
finding_type: continuity
severity: minor
problem: Laura spricht Eva mit „Frau Dr. König“ an, obwohl die Protagonistin kanonisch Dr. Eva Riedel heißt.
evidence: `CHARACTERS.md` und `STORY_PACKAGE.md` führen die Hauptfigur durchgehend als Dr. Eva Riedel. In `BAUSTEINE/11_LAURA_KONFRONTATION/SZENEN/11_11_01_DIE_CHRONOLOGIE/PROSA.md` steht bei der Begrüßung wörtlich „Frau Dr. König.“
impact: Sichtbarer Namens-/Kontinuitätsfehler in einer emotional wichtigen Begegnung; leicht behebbar, aber im Lesertext unmittelbar auffällig.
recommended_rework_level: prose

finding_id: MANUSCRIPT-POST-RHYTHM-003
location: Whole manuscript, besonders S014–S021 und S024–S032
finding_type: scene_repetition
severity: minor
problem: Trotz deutlich verbessertem Satzrhythmus bleibt im mittleren Romanabschnitt eine erkennbare Häufung desselben institutionellen Szenenträgers: Bildschirm/Datensatz oder Regel wird geöffnet → Eva prüft in Frage-Antwort-Folge → Differenzierung wird expliziert → ein Governance-Satz wird festgehalten. Die einzelnen Szenen erfüllen unterschiedliche Funktionen, aber die wiederkehrende Choreografie bleibt über längere Strecken vorhersehbar.
evidence: S014/S015 arbeiten über getrennte Daten und Konfidenzgruppen; S016/S017 über Felix' Konfliktmuster und Entscheidungszeitpunkt; S018/S019 über Evas Fallregister und Bilanz; S020/S021 über persönliche Schwelle und Gegenbeleg. S024–S027 wiederholen Whiteboard/Testfälle/Regelformulierung für den Wert-/Kontextweg; S029–S032 arbeiten erneut über Zeitachsen, Audit, SOP und Systemtest. Dazwischen verändern sich Inhalt und Stakes, die Vermittlungsmechanik bleibt jedoch mehrfach ähnlich.
impact: Kein Architekturbruch und deutlich weniger ermüdend als vor dem Rhythmuspass, aber der Mittelteil kann weiterhin stellenweise wie institutionelle Argumententwicklung statt unmittelbare Thrillerhandlung wirken. Das ist ein Rest-Risiko, kein G4-Blocker.
recommended_rework_level: scene

g4_readiness: REWORK_REQUIRED
