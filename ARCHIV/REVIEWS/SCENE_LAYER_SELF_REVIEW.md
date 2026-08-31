# Scene Layer Self Review – ABWEICHUNG

review_target: `dea9fe2e2119cbd85950fca89c398f7459d28775`
review_type: same-context semantic review
status: PASS_WITH_ONE_CORRECTION
independent: no

## Scope

Geprüft wurde die vollständige horizontale Szenenebene gegen die G1-freigegebene Storywahrheit:

- 18 Bausteine
- 54 Ereignisse
- 40 Szenen S001–S040
- `CHARACTERS.md`
- `RESEARCH_REGISTER.md`
- `R06_MEDIZINISCHE_ANKERFAELLE.md`

Keine Beats und keine Prosa wurden erzeugt.

## Ergebnis

### Abdeckung

- Alle 54 G1-Ereignisse E001–E054 sind einer Szene zugeordnet.
- Kein G1-Baustein bleibt ohne Szene.
- Die Szenenebene führt keinen neuen Plotstrang, keine neue Hauptfigur und keinen neuen Twist ein.

### Kritische Architekturpunkte

- Midpoint bleibt der G1-Reversal: Evas eigene high-confidence Override-Bilanz schneidet schlechter ab; KORA wird nicht nachträglich entwertet.
- B13 setzt die Grenze der Wert-/Kontextabweichung vor dem Finale.
- Felix' Umgehung bleibt kausal mit der ausgeschalteten Zweitfreigabe verbunden, ohne einen sicheren kontrafaktischen Patientenausgang zu behaupten.
- Im Finale prüft Nele exakt die vorab gesetzten zwei Wege: medizinischer Gegenbeleg oder zulässiger patientenspezifischer Wert-/Kontextgrund.
- Der Solo-Break-glass bleibt real; Eva nutzt ihn bewusst nicht.
- S040 endet mit der verinnerlichten Beweislast: „Was sieht KORA nicht?“

### Medizinische Plausibilität

Die medizinisch konkreten Szenen verwenden nur die in R-06 festgelegten Ankermechaniken: schwerer Asthmaanfall, Sepsis/septischer Schock und akute hypoxämische respiratorische Insuffizienz. Keine Szene führt neue Dosierungen, Geräteparameter oder Spezialverfahren ein, die zusätzliche blockierende Recherche auslösen.

## Korrigierter Befund

### SL-SR-001 – S010 / Neles Fall

**Problem:** Die erste Fassung machte Eva zur konkreten Mitfreigebenden von Neles Override. Das hätte die G1-Wahrheit verschoben: E014 legt fest, dass Nele selbst überschreibt und Verantwortung übernimmt; E015 gibt Eva nur Mitverantwortung für die von ihr geprägte Teamkultur.

**Korrektur:** Eva wird nicht mehr als Mitfreigebende gesetzt. Nele trifft den Override selbst; Eva erkennt später ihre eigene geprägte Entscheidungslogik darin wieder.

**Rework-Level:** Szene, kein G1-Backtrack.

## Bewertung

Die Szenenebene ist nach Same-Context-Review **bereit für einen unabhängigen Fresh-Context-Review**. Wegen der bekannten Grenzen eines Same-Context-Reviews wird noch nicht mit der Beat-Ebene begonnen.