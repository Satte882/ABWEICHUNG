# CHARACTERS

version: v0.1
characters_status: ready

| character | role | starting_position | core_need | pressure | arc | must_not_become |
|---|---|---|---|---|---|---|
| Dr. Eva Riedel | POV; ärztliche Leiterin ZNA | evidenzorientiert, pro KORA, aber überzeugt von menschlicher Letztentscheidung | Verantwortung tragen, ohne ärztliche Urteilskraft preiszugeben | eigene schädliche Externalitäten und schlechte high-confidence Override-Bilanz | von „Verantwortung verlangt Freiheit“ zu „Freiheit ohne Rechenschaft ist keine neutrale Größe“ | Anti-KI-Heldin oder moralisch unfehlbare Ärztin |
| Prof. Miriam Ahlers | medizinische Vorständin; legitime Gegenkraft | unterstützt KORA wegen besserer Outcomes | vermeidbaren Schaden reduzieren und Governance auditierbar machen | jede menschliche Ausnahme erzeugt neue Varianz und Haftungs-/Sicherheitsrisiken | von liberaler Pilot-Governance zu immer stärker formalisierten Abweichungsregeln | kalte Kostenmanagerin oder autoritäre Strohfrau |
| Dr. Felix Brandt | leitender Intensivmediziner; Evas langjähriger Verbündeter | hohe klinische Selbstwirksamkeit, skeptisch gegenüber formalisierten Overrides | fachliche Autonomie bewahren | Zweitfreigaben und personenbezogene Review-Schwellen | von legitimer Kritik über Umgehung zu Grenzüberschreitung; sein Verhalten liefert Argumente für strengere Governance | geheimer Bösewicht oder Technikfeind ohne Sachargumente |
| Dr. Nele Yilmaz | jüngere Fachärztin; Evas Protegé | lernt von Eva, Empfehlungen kritisch zu prüfen | gute Ärztin sein, ohne Verantwortung an KORA abzugeben | eigener schädlicher Override | entwickelt strengere Evidenzdisziplin; wird im Finale zur zweiten Freigabe und widerspricht Eva | willenlose Systemgläubige |
| Dr. Jan Völker | Arzt/Data Scientist; klinische Validierung KORA | transparent, methodisch nüchtern | Systemgrenzen und Leistungsdaten korrekt darstellen | wird von beiden Lagern als Beleglieferant instrumentalisiert | aus technischer Nebenrolle zum unbequemen Spiegel für Evas eigene Daten | kalter Technokrat, Herstelleragent oder Geheimnisträger |
| Laura Berg | Tochter des im Cold-Open-Ressourcenkonflikt verstorbenen entfernten Patienten | kennt Eva zunächst nur als Teil des Systems, das die Kapazität anders verteilte | verstehen, wer entschieden hat und was tatsächlich gewusst werden konnte | keine kontrafaktische Gewissheit möglich | macht die unsichtbare Gegenrechnung menschlich sichtbar, ohne Racheplot | Anklägerin als Plotwerkzeug oder sentimentale Erlösungsfigur |

## Beziehungsarchitektur

### Eva ↔ Miriam

- B02: Verbündete bei KORA-Einführung.
- B03–B06: Dissens über Bedeutung einzelner Schäden und zulässige Override-Hürden.
- B09: härtester Konflikt, weil Evas eigene Daten Miriams Argument stärken.
- B12: gemeinsame Arbeit an einer Wert-/Kontextabweichung zeigt, dass beide echte Balance suchen.
- B15–B18: institutionelle Balance bleibt unbefriedigend; persönlicher Respekt bleibt.

### Eva ↔ Felix

- Vor B06: langjähriges klinisches Vertrauen.
- B06: Felix wird Evas stärkster Verbündeter im Therapiefreiheitsargument.
- B08: auffällige Dokumentationsmuster erzeugen Misstrauen.
- B14: Eva meldet seine bewusste Umgehung nach realem Schaden; Beziehung bricht.

### Eva ↔ Nele

- B01–B04: Eva modelliert kritisches, selbstbewusstes ärztliches Entscheiden.
- B05: Neles Override-Schaden macht diese Kultur persönlich.
- B06–B10: Nele entwickelt stärkere Evidenzdisziplin und weniger Statusdenken.
- B17: Nele verweigert Eva die Zweitfreigabe aus genau der Logik, die Eva selbst früher gefordert hat: konkrete Gründe statt Autorität.

### Eva ↔ Laura

- B03: Laura existiert zunächst als Name/Angehörige in der Aufarbeitung.
- B11: direkte Begegnung; Eva kann den lokalen Erfolg ihres Overrides nicht mehr als vollständige Bilanz erzählen.
- Danach keine künstliche Freundschaft und kein Racheplot.

## Figurenwissen – G1-Grenzen

- Niemand kennt individuelle kontrafaktische Patientenverläufe sicher.
- Jan kann statistische Leistungs-/Kalibrierungsdaten erklären, nicht die Zukunft eines einzelnen Patienten beweisen.
- Miriam kennt keine geheime Wahrheit über KORA.
- Felix hat keinen Beleg dafür, dass Menschen insgesamt besser sind; sein Konflikt ist Autonomie, nicht Leistungsüberlegenheit.
- Nele darf im Finale wissen, was die G2-Planung explizit für beide Patienten freigibt; keine spontane Zusatzinformation löst den Konflikt.
