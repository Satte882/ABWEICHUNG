# G1 Semantic Self-Review – ABWEICHUNG

status: complete
review_context: same_chat_same_model_context
independent_review: no

## Zweck

Vor dem unabhängigen Fresh-Context-Review wurden nur offensichtliche Architekturdrifts gegen G0 und interne Kausalität geprüft. Dieser Self-Review zählt nicht als unabhängige semantische QA.

## Prüfungen

### SR-G1-01 – KI darf nicht nachträglich zum eigentlichen Problem umgeschrieben werden

disposition: PASS

`STORY_PACKAGE.md`, `STORY_BLOCKS.md` und `EVENTS.md` halten durchgehend fest, dass KORA im definierten Entscheidungsraum besser ist, probabilistisch bleibt und weder Bewusstsein noch geheime Agenda erhält.

### SR-G1-02 – Cold-Open-Schaden darf keine unmögliche kontrafaktische Gewissheit behaupten

disposition: PASS

Die Story setzt reale Ressourcenbindung und reale Verzögerung als Kausalität. Ob der entfernte Patient bei früherer Behandlung sicher überlebt hätte, bleibt ausdrücklich probabilistisch.

### SR-G1-03 – Evas Rolle darf keine unrealistische verbundweite Befehlsgewalt voraussetzen

disposition: PASS_WITH_G2_PRECISION

Eva entscheidet als lokal verantwortliche ärztliche Leitung über die von ihrem Standort beanspruchte/weiterzugebende akute Kapazität. KORA macht die verbundweite Gegenrechnung sichtbar. G2 darf daraus keine zentrale „Eva verteilt alle Betten des Verbunds“-Rolle machen.

### SR-G1-04 – Wert-/Kontextabweichung darf KORA nicht heimlich als moralisch defekt entwerten

disposition: PASS

Die Architektur trennt Prognoseleistung von Patientenwillen/Therapieziel/Wertentscheidung. Das ist keine Enthüllung eines Algorithmusfehlers.

### SR-G1-05 – medizinische Einzelfälle sind noch nicht ausreichend konkret recherchiert

disposition: DEFERRED_BY_REGISTER

`R-06` bleibt offen, `blocking_now: no` für G1. Vor medizinisch konkreten Beats/Szenenkarten muss diese Recherche blockierend geschlossen werden.

## Ergebnis

- G0-Drift: 0
- neue Storyentscheidung aus Self-Review: 0
- zwingendes G1-Rework aus Same-Context-Review: 0
- unabhängige Review-Fähigkeit: hier nicht behauptet

Nächster Schritt: Fresh-Context-Review nach `G1_FRESH_CONTEXT_TASK.md`, danach Human-Disposition und erst dann G1-Human-Gate.
