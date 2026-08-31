# Prosa – S032

scene_id: S032
prose_status: expansion_rework
source_scene: `SZENE.md`
source_beats: `BEATS.md`

---

Der Patient auf dem Bildschirm existierte nicht.

Das machte die Entscheidung leichter.

Nur nicht harmlos.

Jan hatte den Testfall so gebaut, dass die neue Governance an ihrer engsten Stelle geprüft wurde.

High confidence.

Hohe Schadensrelevanz.

Zweitfreigabe erforderlich.

Und im Szenario war keine zweite Person rechtzeitig verfügbar.

Eva stand vor dem Testsystem. Miriam lehnte am Tisch hinter ihr, Jan saß am zweiten Bildschirm und kontrollierte die Simulation.

„Keine Sonderbehandlung für mich“, sagte Eva.

Jan sah kurz auf.

„Das ist der Sinn des Tests.“

„Ich meine technisch. Kein vorbereiteter Shortcut.“

„Gibt es nicht.“

Miriam sagte: „Wenn du einen findest, haben wir ein anderes Problem.“

Eva legte die Hand auf die Maus.

„Los.“

Jan startete den Fall.

Die simulierten Patientendaten erschienen. KORA berechnete die Empfehlung und markierte sie wenige Sekunden später als high confidence.

Eva öffnete den regulären Override-Weg.

**Zweitfreigabe erforderlich.**

Darunter begann die Erreichbarkeitsprüfung.

Erster Name.

Nicht verfügbar.

Zweiter Name.

Keine Antwort innerhalb des simulierten Zeitfensters.

Dritter möglicher Zweitentscheider war bereits in einem anderen Notfall gebunden.

Der Status wechselte.

**Kein verfügbarer Zweitentscheider im erforderlichen Zeitfenster.**

Eva wartete, bis die Meldung stabil stehen blieb.

„Wenn ich jetzt nichts mache?“

Jan deutete auf die Uhr im Testfenster.

„Dann bleibt der reguläre Weg blockiert, bis jemand erreichbar ist.“

„Und die Behandlung?“

„Im Szenario verschlechtert sich der Patient weiter.“

Eva nickte.

Genau dafür hatte sie den Test verlangt.

Eine Schutzregel war wertlos, wenn sie nur funktionierte, solange genug Menschen frei waren. In einem echten Engpass konnte gerade die fehlende zweite Person Teil derselben Krise sein.

Sie scrollte weiter.

Unterhalb des regulären Wegs erschien die Option.

**SOLO-BREAK-GLASS – unmittelbare Abweichung mit automatischem Review**

Eva öffnete die Erklärung.

Der Text war kurz.

Die Abweichung wurde sofort wirksam.

Keine vorherige Bestätigung durch eine zweite Person.

Automatische Kennzeichnung als persönlicher Reviewfall.

Vollständige Protokollierung der verfügbaren Daten und des dokumentierten Grunds.

Eva las bis zur letzten Zeile.

„Keine versteckte Wartezeit?“

„Nein“, sagte Jan.

„Kein Hintergrundprozess, der erst noch jemanden sucht?“

„Nein.“

„Kein Timeout vor Wirksamkeit?“

„Nein.“

Miriam sagte: „Das wolltest du doch.“

Eva sah auf die Schaltfläche.

„Ich will wissen, ob es wirklich so ist.“

Sie klickte.

Ein neues Fenster öffnete sich.

**Abweichung sofort wirksam machen?**

Darunter das Begründungsfeld.

Eva trug den für den Testfall vorgesehenen klinischen Grund ein.

Dann bestätigte sie.

Der Behandlungspfad wechselte sofort.

Kein Ladesymbol.

Kein weiterer Name.

Kein zweiter Dialog.

Die Abweichung war wirksam.

Fast gleichzeitig erschien rechts ein neuer Eintrag.

**Persönlicher Reviewfall erstellt.**

Darunter stand Evas Name.

Zeitpunkt.

Fallklasse.

KORA-Konfidenz.

Dokumentierter Grund.

Die ursprüngliche Empfehlung.

Der Zustand der Erreichbarkeitsprüfung.

Eva öffnete den Reviewfall.

„Kann irgendjemand meine Abweichung rückwirkend so behandeln, als wäre sie bis zur Prüfung nur vorläufig?“

Jan schüttelte den Kopf.

„Nein. Der medizinische Schritt ist vollzogen. Das Review bewertet deine Entscheidung danach.“

„Kann ein Reviewer den Datensatz verändern?“

„Nicht die damalige Entscheidungsgrundlage.“

„Kann ich den Reviewfall selbst schließen?“

„Nein.“

Miriam trat neben sie.

„Du bekommst deinen Knopf. Du bekommst nur nicht die Unsichtbarkeit dazu.“

Eva sah auf ihren Namen im Reviewfenster.

„Damit kann ich leben.“

Sie klickte durch die gespeicherten Informationen.

Kein anonymer Notfallmodus.

Kein technisches Schlupfloch, in dem später niemand mehr wusste, dass die Entscheidung allein getroffen worden war.

Auch keine nachträgliche Genehmigung, die so tat, als hätte der zweite Blick vorher stattgefunden.

Das gefiel Eva besser, als sie erwartet hatte.

Die Verantwortung wurde nicht verteilt, nachdem die Handlung bereits abgeschlossen war.

Sie blieb bei der Person, die den Break-glass-Weg genutzt hatte.

„Noch einmal“, sagte Eva.

Jan hob die Augenbrauen.

„Der Test ist durch.“

„Noch einmal.“

„Warum?“

„Weil ein Weg, der beim ersten vorbereiteten Fall funktioniert, noch kein belastbarer Weg ist.“

Jan sah zu Miriam.

Miriam hob die Schultern.

„Du kennst sie.“

Jan setzte die Simulation zurück.

Beim zweiten Durchlauf änderte er die Reihenfolge der verfügbaren Zweitentscheider. Eine Person war zunächst sichtbar, fiel dann während der Prüfung aus dem Zeitfenster.

Eva ging wieder den regulären Weg.

Zweitfreigabe erforderlich.

Erreichbarkeitsprüfung.

Keine rechtzeitige Freigabe.

Solo-Break-glass.

Diesmal wartete Eva absichtlich einige Sekunden vor dem Klick.

„Was passiert mit der damaligen Datenlage?“

Jan zeigte auf den Zeitstempel.

„Der Snapshot für die Entscheidung wird beim Auslösen festgeschrieben.“

„Also kann mir später niemand mit Daten kommen, die erst danach verfügbar waren?“

„Im Review können spätere Daten betrachtet werden. Aber sie werden getrennt von der damaligen Informationslage angezeigt.“

Eva nickte.

„Gut.“

Sie bestätigte erneut.

Sofortige Abweichung.

Sofortiger Reviewfall.

Gleicher Mechanismus.

Jan nahm die Hände von der Tastatur.

„Dritter?“

Eva schloss die Ansicht.

„Nein.“

Sie trat vom Bildschirm zurück.

Der Testpatient verschwand. Zurück blieb die leere Startoberfläche.

Niemand hatte ihr die Letztentscheidung technisch genommen.

Wenn die reguläre Schutzstufe in einer akuten Lage nicht erreichbar war, konnte sie allein handeln.

Aber der Weg trug die spätere Frage bereits in sich.

Nicht als moralischen Kommentar.

Als unvermeidbaren Datensatz.

Warum war dein Grund stark genug, allein abzuweichen?

Eva sah noch einmal auf die Stelle, an der die Break-glass-Schaltfläche eben gestanden hatte.

Der Knopf war da.

Er war schnell.

Er war echt.

Das reichte ihr.

Fast.
