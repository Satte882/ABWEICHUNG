# STORY_PACKAGE

working_title: ABWEICHUNG
version: v0.1
concept_ref: `BOOK_IDEA.md` blob `812c1a4d5fb7100be420e2f885e52f1026d45c3a`
premise_summary: Dr. Eva Riedel, ärztliche Leiterin einer großen Notaufnahme und Mitbefürworterin des klinischen KI-Systems KORA, verteidigt menschliche Letztentscheidung, obwohl KORA im definierten Entscheidungsraum nachweislich bessere Ergebnisse erzielt. Ein von Eva verantworteter Override rettet den Patienten vor ihr, verdrängt aber einen für sie unsichtbaren Patienten im Klinikverbund von der letzten intensivmedizinischen Kapazität. Aus nachvollziehbaren Sicherheitsmaßnahmen wächst schrittweise ein System, in dem der Mensch formal entscheiden darf, faktisch aber jede Abweichung rechtfertigen muss.
core_conflict_summary: bessere klinische Ergebnisqualität und Schutz vor vermeidbarem Schaden kollidieren mit ärztlicher Therapiefreiheit, individueller Verantwortung und der Frage, ob eine Entscheidung noch menschlich ist, wenn sie nur innerhalb maschinell definierter Abweichungsgrenzen legitim bleibt.
central_question: Wie lange darf ein Mensch eine schlechtere Entscheidung treffen, wenn eine Maschine nachweislich die bessere kennt?
mechanism_summary: Jeder relevante menschliche Override erzeugt nicht automatisch Schaden, wird aber messbar. Reale adverse Ereignisse, systemweite Ressourcenfolgen und belastbare Outcome-Daten führen nacheinander zu Dokumentationspflicht, Zweitfreigabe, personenbezogener Abweichungsanalyse und engeren Notfallregeln. Der Override-Button verschwindet nie; die Beweislast verschiebt sich.
promise_to_reader: Psychologisch enger Near-Future-Thriller ohne böse KI und ohne einfachen Technikfehler. Spannung entsteht aus konkreten Entscheidungen, unsichtbaren Folgekosten, institutionell legitimen Gegenpositionen, Schuld und der schrittweisen Umkehr dessen, wer seine Entscheidung begründen muss.
protagonist_arc_summary: Eva startet als evidenzorientierte Ärztin, die KORA gegen Technikfeindlichkeit verteidigt und zugleich menschliche Letztentscheidung für unverzichtbar hält. Nach einem lokal erfolgreichen, systemisch folgenreichen Override akzeptiert sie erste Governance-Schritte. Sie kämpft erst dann, als aus Qualitätssicherung individuelle Autoritätsbegrenzung wird. Der Midpoint zwingt sie anzuerkennen, dass gerade ihre eigenen hochkonfidenten Abweichungen schlechter abschneiden und dass ihre Erinnerung lokale Erfolge stärker gewichtet als unsichtbare Kosten. Im Finale bleibt ihr ein echter Notfall-Override, aber sie findet weder einen medizinischen Gegenbeleg noch einen nach der eigenen Wert-/Kontextregel zulässigen patientenspezifischen Ausnahmegrund; übrig bleibt ihre Nähe zum Patienten vor ihr. Sie nutzt den Override nicht. Formal behält sie die Entscheidungsmacht; innerlich hat sich die Beweislast umgekehrt.
plot_architecture_summary: Achtzehn Makro-Bausteine führen von einem lokal erfolgreichen Override über die Entdeckung seiner unsichtbaren systemweiten Kosten, erste Governance-Schritte, einen zweiten Schaden, Widerstand und Datenprüfung bis zum Midpoint, an dem Evas eigene Abweichungsbilanz gegen sie spricht. Ein Versuch, wertbezogene Ausnahmen institutionell zu schützen, wird durch uneinheitliche Nutzung geschwächt und anschließend auf patientenspezifische, prüfbare Wert-/Kontextgründe begrenzt; ein enger Kollege umgeht KORA durch Input-/Zeitpunktmanipulation und verhindert in einem konkreten Schadensfall die eigentlich erforderliche Zweitfreigabe. Unter realem Kapazitätsdruck erreicht die Governance ihren Endzustand: Break-glass bleibt möglich, aber jede hochkonfidente Abweichung ist sichtbar und persönlich zurechenbar. Die finale Entscheidung spiegelt den Anfang, diesmal mit vollständiger Sicht auf beide Patienten.
reversal_summary: Der zentrale Reversal ist keine Enthüllung eines KI-Fehlers. Eva erhält die bislang nur aggregiert betrachtete Abweichungsanalyse und erkennt, dass ihre eigene klinische Intuition in genau den Fällen, in denen sie KORA mit hoher Sicherheit widersprochen hat, schlechtere Outcome- und Ressourcenfolgen erzeugt. Der erste Override, den sie als Beweis menschlicher Überlegenheit erinnert, war nur lokal erfolgreich; seine systemische Gegenrechnung blieb für sie unsichtbar. Damit kippt ihr Konflikt von „System gegen ärztliche Erfahrung“ zu „Wer trägt die Kosten des Rechts, trotz besserer Evidenz anders zu entscheiden?“
information_architecture_summary: Drei Informationsstränge werden getrennt geführt. O = Outcome/Performance: Wie belastbar ist KORAs tatsächlicher Vorteil und wo endet seine Aussagekraft? G = Governance/Macht: Welche formalen Regeln gelten für Overrides und wie verschiebt sich dadurch faktische Autorität? X = Externalität/Sichtbarkeit: Welche Folgen einer lokalen Entscheidung entstehen außerhalb des Sichtfelds des handelnden Arztes? Leser und Eva erhalten keine geheime KI-Perspektive. Spannung entsteht aus verzögert sichtbaren Folgen, nicht aus verborgenem Maschinenbewusstsein.
character_functions_summary: Eva trägt POV und finale Entscheidung; Prof. Miriam Ahlers verkörpert legitime Patientensicherheits- und Governance-Logik; Dr. Felix Brandt verteidigt klinische Autonomie radikaler und überschreitet später die Grenze zur Manipulation; Dr. Nele Yilmaz ist Evas jüngere Kollegin und durchläuft den Gegenbogen von gelebter Override-Kultur zu evidenzbasierter Zurückhaltung; Dr. Jan Völker verantwortet Validierung und technische Grenzen von KORA und darf weder als kalter Technokrat noch als geheimer Strippenzieher funktionieren; Laura Berg macht die unsichtbare systemische Gegenrechnung des ersten Overrides menschlich sichtbar.
story_decisions_open: no

## Setting und System

Die Handlung spielt in einem großen fiktiven deutschen Klinikverbund **Falkenried** in naher Zukunft. Mehrere Akutstandorte teilen Intensivkapazitäten, Spezialteams und Verlegungsoptionen. Engpässe entstehen nicht permanent, aber häufig genug, dass Priorisierung und zeitkritische Koordination zum Alltag gehören.

**KORA** ist ein zertifiziertes klinisches Entscheidungsunterstützungssystem. Es ist kein autonomer Behandler und keine allwissende generative KI. KORA bündelt aktuelle Patientendaten, Verlauf, Risikoprognosen und verbundweite Ressourcenlage und gibt Empfehlungen für zeitkritische Priorisierung, Eskalation, Verlegung und knappe kritische Kapazitäten.

KORA liefert mindestens:

- Empfehlung,
- prognostizierten klinischen Nutzen bzw. Schaden bei Verzögerung,
- Unsicherheits-/Konfidenzbereich,
- relevante Einflussfaktoren,
- sichtbare Ressourcenkonflikte,
- dokumentierbare Override-Möglichkeit.

Der **medizinische Zweck und die Zielgrößen sind von Menschen festgelegt**. KORA soll vermeidbaren schweren Schaden reduzieren und den erwarteten akuten Behandlungsnutzen knapper Ressourcen verbessern. Nichtmedizinische Kriterien menschlichen „Werts“ sind keine zulässigen Eingaben.

Innerhalb dieses definierten Raums gilt als kanonische Story-Wahrheit: KORA ist prospektiv validiert und klinisch relevant besser als die vorherige rein menschliche Praxis. Es bleibt probabilistisch, kennt keine individuelle Zukunft sicher und ersetzt keine Werteentscheidung.

## Hauptfigur: Dr. Eva Riedel

Eva, 44, ist ärztliche Leiterin der Zentralen Notaufnahme am größten Falkenried-Standort. Sie hat die Einführung von KORA mitgetragen, weil sie erlebt hat, wie Überlastung, Erfahrungsunterschiede und lokale Informationsgrenzen zu vermeidbaren Fehlern führen. Sie ist weder Technikgegnerin noch gläubige Automatisiererin.

Ihr professioneller Glaubenssatz zu Beginn:

> Ein gutes System zwingt Menschen, genauer hinzusehen. Es darf ihnen die Entscheidung nicht abnehmen.

Ihr blinder Fleck: Sie setzt „ich trage die Verantwortung“ mit „ich muss auch die letzte freie Entscheidung haben“ gleich. Erst später wird sichtbar, dass Verantwortung auch bedeutet, die Folgen eigener Abweichungen über den einzelnen Patienten vor ihr hinaus anzuerkennen.

## Institutionelle Gegenkraft: Prof. Miriam Ahlers

Miriam, 52, ist medizinische Vorständin des Verbunds und frühere Intensivmedizinerin. Sie hat KORA nicht aus Kostengründen eingeführt, sondern weil die Pilotdaten klinisch besser waren. Sie ist Evas stärkste Gegenfigur, gerade weil ihre Argumente legitim sind.

Sie glaubt:

> Human Oversight kann nicht bedeuten, dass menschliche Fehler dauerhaft weniger überprüft werden als maschinelle Empfehlungen.

Miriam will keinen Autopiloten. Sie will nachvollziehbare, auditierbare Abweichungen. Jeder Governance-Schritt, den sie unterstützt, muss aus einem realen Problem hervorgehen.

## Drei Informationsstränge

### O – Outcome / Performance

Zu klären und über den Roman zu verschärfen:

- Wie gut ist KORA gegenüber der bisherigen Versorgung?
- In welchen Entscheidungstypen ist der Vorteil belastbar?
- Wie sicher ist eine einzelne Empfehlung?
- Was sagen aggregierte Daten über individuelle ärztliche Abweichungen?

Regel: Kein späterer Twist darf KORAs Vorteil durch einen simplen Bug, manipulierte Trainingsdaten oder versteckte Bosheit entwerten.

### G – Governance / Macht

Die formale Eskalation lautet:

1. freie Empfehlung + freier Override,
2. Pflichtbegründung bei Override,
3. Zweitfreigabe bei definierten hochriskanten/high-confidence Abweichungen,
4. individuelle Abweichungsprofile und engere Aufsicht bei systematisch schlechten Ergebnissen,
5. manipulationssichere Datengrundlage und formalisierte Ausnahmearten,
6. Break-glass bleibt technisch möglich, erzeugt aber unmittelbare persönliche Rechenschaft.

Kein einzelner Schritt ist als autoritärer Coup geschrieben.

### X – Externalität / Sichtbarkeit

KORA sieht verbundweite Knappheit, Eva zunächst primär den Patienten vor sich.

Der erste große Konflikt zeigt:

- Eva sieht den Nutzen ihres Overrides direkt,
- die Kosten derselben Entscheidung entstehen an einem anderen Standort,
- erst die nachträgliche Rekonstruktion verbindet beide.

Dieser Strang ist entscheidend, damit „bessere Ergebnisqualität“ nicht abstrakt bleibt.

## Zentrale Beziehungsbögen

### Eva ↔ Miriam

- Start: professionelle Verbündete bei der Einführung von KORA.
- Druck: Eva hält Governance zunächst für notwendige Qualitätssicherung, später für schleichende Entmachtung.
- Konflikt: Miriam zwingt Eva, zwischen abstrakter Therapiefreiheit und messbaren Folgen zu unterscheiden.
- Ende: keine Versöhnung und kein Sieg; beide akzeptieren, dass wirksame menschliche Aufsicht zugleich Freiheit und Rechenschaft braucht, ohne eine stabile Grenze dafür gefunden zu haben.

### Eva ↔ Felix Brandt

Felix, 47, ist leitender Intensivmediziner und Evas langjähriger klinischer Verbündeter.

- Start: gegenseitiges Vertrauen in Erfahrungsmedizin.
- Druck: Felix sieht jede zusätzliche Override-Hürde als Beginn fremder fachlicher Weisung.
- Grenzüberschreitung: Er verändert Eingabe-/Zeitpunktlogik so, dass KORA eine von ihm gewünschte Entscheidung nicht mehr als hochkonfidente Abweichung erkennt.
- Folge: In einem konkreten Fall verhindert diese Umgehung die sonst erforderliche Zweitfreigabe; nach dem anschließenden schweren Schaden rekonstruiert das Audit die Kette und weitere gleichartige Muster. Eva meldet den Vorgang trotz Loyalität.
- Funktion: Der Roman zeigt, dass eine schlecht gesetzte Governance nicht nur Gehorsam, sondern auch Umgehungsverhalten erzeugen kann – und dass dieses Umgehen wiederum strengere Governance plausibel macht.

### Eva ↔ Nele Yilmaz

Nele, 31, ist jüngere Fachärztin in Evas Notaufnahme.

- Start: Sie lernt von Eva, Empfehlungen kritisch zu prüfen und bei Bedarf zu überstimmen.
- früher Bruch: Ein eigener Override endet mit schwerem vermeidbarem Schaden.
- Entwicklung: Nele wird nicht „maschinenhörig“, sondern strenger darin, zwischen konkretem Gegenbeleg und bloßem Bauchgefühl zu unterscheiden.
- Finale: Sie ist die erforderliche zweite ärztliche Freigabe und prüft zwei Wege: einen konkreten medizinischen Gegenbeleg oder einen nach der Wert-/Kontextregel zulässigen patientenspezifischen Ausnahmegrund. Eva kann keinen von beiden benennen; Nähe und behandelnde Beziehung allein sind innerhalb der gesetzten Ressourcenkategorie kein solcher Ausnahmegrund.

## Cold Open / Anfangsentscheidung

Der Roman beginnt **nicht** mit einer versagenden KI.

In einer überfüllten Nacht konkurrieren zwei kritisch kranke Patienten an unterschiedlichen Standorten um die letzte unmittelbar verfügbare Intensivkapazität. KORA priorisiert den für Eva unsichtbaren Patienten am anderen Standort mit höherem erwarteten akutem Behandlungsnutzen.

Eva steht am Bett ihres eigenen, rasch schlechter werdenden Patienten. Sie erkennt ein klinisches Signal, das sie für entscheidend hält, und überschreibt KORAs Empfehlung. Der lokale Patient bekommt die Kapazität und stabilisiert sich.

Für Eva und das Team wirkt der Override zunächst wie der Beweis, warum menschliche Letztentscheidung unverzichtbar ist.

Erst später wird rekonstruiert, dass der andere Patient dadurch länger auf eine adäquate Versorgung warten musste und starb. Der Roman behauptet nicht, KORA könne den individuellen Gegenverlauf beweisen. Die **Ressourcenkausalität und Verzögerung sind real**, die kontrafaktische Überlebensfrage bleibt probabilistisch.

## Midpoint-Reversal

Eva verlangt belastbare Daten, weil sie die zunehmende Override-Governance für zu pauschal hält.

Jan Völker stellt ihr deshalb eine nach Entscheidungstyp, Konfidenz und Fallmix getrennte Auswertung zur Verfügung. Sie zeigt:

- KORA ist nicht in jedem Einzelfall richtig,
- Abweichungen bei niedriger Konfidenz können sinnvoll sein,
- aber Evas eigene Overrides in hochkonfidenten Ressourcen-/Eskalationsfällen schneiden signifikant schlechter ab als die Empfehlung,
- der lokal erfolgreiche Cold-Open-Fall gehört zu dieser Gruppe,
- Evas Erinnerung bewertet sichtbare Rettungen stärker als verbundweit entstandene Verzögerungskosten.

Der Reversal verändert nicht die Vergangenheit. Er verändert Evas Interpretation ihrer eigenen Rolle.

## Versuch einer legitimen Gegenarchitektur

Eva argumentiert nach dem Midpoint, dass nicht jede Abweichung eine Prognosekorrektur ist. Manche Konflikte betreffen Werte, Patientenwillen, Therapieziel oder eine klinische Unsicherheit, die im Modell nicht entscheidbar ist.

Miriam lässt deshalb mit klinischer Ethik eine **Wert-/Kontextabweichung** als eigene Begründungskategorie pilotieren.

Der Versuch scheitert nicht, weil Werte irrelevant wären. Er scheitert teilweise, weil:

- die Kategorie uneinheitlich genutzt wird,
- einige Ärztinnen und Ärzte sie als allgemeines Schlupfloch für nicht belegte Intuition verwenden,
- die Institution dadurch erneut zwischen echter Wertentscheidung und bloßem Widerspruch unterscheiden muss.

Die Konsequenz ist keine Abschaffung der Kategorie, sondern zusätzliche Struktur und Review – erneut ein vernünftiger Schritt, der Freiheit in Verfahren übersetzt.

### Verbindliche Grenze der Wert-/Kontextabweichung

Für Falkenried gilt nach dem Review des Piloten:

- Zulässig sind **patientenspezifische** Gründe, die nicht einfach behaupten, KORAs Prognose sei falsch, z. B. dokumentierter Patientenwille, Therapieziel, relevante Behandlungsbelastung oder ein anderer für die Entscheidung wesentlicher Kontextfaktor, den KORA im konkreten Fall nicht abbildet.
- Der Grund muss benennbar und für die zweite ärztliche bzw. ethische Prüfung nachvollziehbar sein.
- **Nicht ausreichend** sind allein räumliche Nähe, bestehende behandelnde Beziehung, emotionaler Handlungsdruck oder die allgemeine Pflicht gegenüber dem gerade sichtbaren Patienten. Diese Gründe würden im verbundweiten Ressourcenkonflikt genau den in B03/B09/B11 erkannten Sichtfeld-Bias erneut privilegieren.
- Diese Grenze ist eine kanonische Governance-Entscheidung des fiktiven Verbunds, keine Behauptung einer allgemeinen realen Rechts- oder Ethikregel.

Damit bleibt ein echter menschlicher Werteraum erhalten, ohne dass jede Intuition nachträglich als „Kontext“ etikettiert werden kann.

## Später Konflikt: Felix' Umgehung

Felix will sich der wachsenden Zweitfreigabe nicht unterwerfen. Er manipuliert nicht KORA selbst, sondern verändert in einem konkreten Ressourcen-/Eskalationsfall den Zeitpunkt bzw. die Klassifikation entscheidungsrelevanter Eingaben so, dass KORAs Konflikt unter die für Zweitfreigabe relevante high-confidence Schwelle fällt.

Dadurch wird die sonst erforderliche Mitzeichnung nicht ausgelöst; Felix entscheidet allein. Der Patient erleidet anschließend einen schweren Schaden. Das Audit rekonstruiert aus Zeitstempeln und den bereits vorhandenen klinischen Daten, dass der Fall bei regelgerechter Eingabe als high-confidence Konflikt behandelt worden wäre und eine Zweitfreigabe erforderlich gewesen wäre. Es zeigt zusätzlich weitere gleichartige Muster. Der Roman behauptet dabei nicht, dass die Zweitfreigabe den individuellen Ausgang mit Sicherheit verhindert hätte; kausal belegt ist die Umgehung der Schutzstufe.

Eva muss zwischen Kollegialität und Patientensicherheit entscheiden und meldet Felix. Damit verliert sie ihren stärksten Verbündeten gegen die Governance und liefert der Institution zugleich den überzeugendsten Grund für manipulationssichere Inputs und strengere Override-Protokolle.

## Finale

Unter einer realen verbundweiten Kapazitätsspitze entsteht erneut ein Konflikt um eine letzte kritische Ressource.

Diesmal ist die Situation gegenüber dem Cold Open verändert:

- Eva sieht nicht nur ihren lokalen Patienten, sondern auch die wesentlichen Daten des konkurrierenden Falls,
- KORA hat hohe Konfidenz,
- keine entscheidende medizinische Information fehlt,
- es gibt keinen Technikfehler,
- der medizinische erwartete Nutzen spricht klar für den anderen Patienten,
- für keinen der beiden Fälle liegt ein patientenspezifischer Wert-/Kontextgrund vor, der die gesetzte Allokationslogik verändert,
- Evas lokaler Patient erzeugt dennoch einen starken unmittelbaren ärztlichen Handlungsimpuls.

Nach der geltenden Governance braucht die Abweichung eine zweite ärztliche Freigabe. Nele lehnt ab: Eva kann weder einen medizinischen Gegenbeleg noch einen zulässigen patientenspezifischen Wert-/Kontextgrund benennen. Ihr verbleibender Grund ist, dass der eine Patient vor ihr liegt und der andere nicht – genau die lokale Sichtverzerrung, die der Roman zuvor sichtbar gemacht hat.

Ein **Break-glass-Override bleibt technisch und formal möglich**. Eva könnte ihn allein auslösen und müsste ihn anschließend persönlich verantworten.

Sie tut es nicht.

Der lokale Patient stirbt später; der andere erhält die Ressource und überlebt. Das ist kein Beweis, dass KORA immer recht hat. Es nimmt Eva nur die einfache Möglichkeit, ihren Verzicht nachträglich als offensichtlichen Fehler des Systems umzudeuten.

## Schlusswirkung

Die finale institutionelle Kommunikation betont, die ärztliche Letztentscheidung sei vollständig erhalten geblieben: Der Break-glass-Override existiert weiterhin.

In der letzten Sequenz bittet eine jüngere Ärztin Eva um Zustimmung zu einer Abweichung in einem neuen Fall.

Eva fragt nicht zuerst: „Warum willst du der KI nicht folgen?“

Sie fragt:

> „Was sieht KORA nicht?“

Damit hat sich die Beweislast vollständig gedreht. Der Knopf ist noch da.

## Nicht erlaubt für spätere Ebenen

- KORA entwickelt Bewusstsein oder eigene Interessen.
- Hersteller oder Vorstand manipulieren heimlich das System, um Kosten zu sparen, und lösen dadurch den Hauptkonflikt auf.
- Ein einzelner spektakulärer Fehlfall beweist, dass menschliche Intuition KORA eigentlich überlegen ist.
- Patientendaten oder Diversitätsprobleme dürfen konkrete Grenzen zeigen, aber nicht als bequemer Twist die gesetzte Gesamtüberlegenheit beseitigen.
- Miriam darf nicht zur autoritären Strohfrau werden.
- Felix darf nicht zum heimlichen Superschurken werden; seine Grenzüberschreitung entsteht aus einer nachvollziehbaren, aber falschen Autonomie-Logik.
- Nele darf im Finale nicht als willenlose Systemgläubige geschrieben werden.