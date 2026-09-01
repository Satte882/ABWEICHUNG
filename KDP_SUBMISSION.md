# KDP Submission – ABWEICHUNG

status: ready-for-live-kdp
market: Amazon.de
language: Deutsch

Diese Datei ist die operative Feld-für-Feld-Checkliste. Positionierung und Begründungen stehen in `KDP_METADATA.md`.

## 1. Buchdetails

| KDP-Feld | Eingabe |
|---|---|
| Sprache | Deutsch |
| Buchtitel | `ABWEICHUNG` |
| Untertitel | `Zwischen Mensch und System` |
| Reihe | leer |
| Auflagennummer | leer |
| Primärautor | **OPEN USER VALUE** |
| Mitwirkende | keine |
| Beschreibung | HTML aus `BUCHBESCHREIBUNG_KDP.md` |
| Veröffentlichungsrechte | urheberrechtlich geschütztes Werk / eigene Rechte |
| Primärer Marketplace | Amazon.de |

## 2. KI-Angabe

Konservativ angeben:

- KI-generierte Inhalte: **Ja**
- Text: **Ja**
- Cover/Bild: **Ja**, sofern das aktuelle Formular die KI-erarbeitete, programmgesteuert erzeugte Covergestaltung als KI-generiertes Bild/Cover einordnet

## 3. Keywords

1. `künstliche intelligenz medizin`
2. `medizinischer psychothriller`
3. `ki krankenhaus thriller`
4. `algorithmus entscheidungsfreiheit`
5. `ärztliche verantwortung`
6. `near future thriller deutsch`
7. `mensch maschine ethik`

## 4. Kategorien

Drei engste Live-Kategorien auswählen:

1. Psychothriller
2. Technothriller / technologische Thriller
3. Medical Thriller / medizinische Thriller

## 5. Paperback – Innenraum

Upload:

- Datei: `ABWEICHUNG_FINAL.docx` bzw. die daraus final exportierte Innen-PDF
- Trim Size: **5,06 × 7,81 Zoll / 12,85 × 19,84 cm**
- schwarze Tinte
- weißes Papier
- **kein Beschnitt** im Innenraum
- Leserichtung links nach rechts

Aktueller finaler Export:

- 40 Kapitel
- 37.919 Wörter Szenen-Prosa
- **233 Seiten**
- letzter Satz `Eva wartete.`

### Previewer-QA

Mindestens prüfen:

- 40 Kapitel vollständig vorhanden
- Inhaltsverzeichnis vollständig
- Titel- und Frontmatter-Seiten korrekt
- keine abgeschnittenen Zeilen
- keine Rand-/Bundstegwarnung
- Seitenzahlen sauber
- keine sichtbaren Fehltrennungen
- keine unerwarteten Leerseiten
- letzter Satz korrekt
- finale Seitenzahl notieren

## 6. Paperback – ISBN

Default: **kostenlose KDP-ISBN**.

Stop und eigene ISBN verwenden, wenn die identische Printausgabe bewusst außerhalb KDP unter eigener Verlags-/Imprint-Identität distribuiert werden soll.

## 7. Paperback – Cover

Aktueller Kandidat:

- Datei: `ABWEICHUNG_COVER.pdf`
- Basis: **233 Seiten**
- Schwarzweiß / weißes Papier
- Format: 5,06 × 7,81 Zoll
- PDF: **10,894716 × 8,060 Zoll**
- Rücken: **0,524716 Zoll**

Coverinhalt:

### Vorderseite

- `ABWEICHUNG`
- kursiv darunter `Zwischen Mensch und System`
- horizontale Linie über die komplette Vorderseitenbreite mit einem integrierten Ausschlag
- darunter `Du darfst widersprechen.`
- darunter `Die Beweislast liegt bei dir.`

### Buchrücken

- kein Text
- dieselbe Linie mit Ausschlag wie vorn, um 90° gedreht
- Linie und Ausschlag sind ein einziger durchgängiger vertikaler Pfad
- Linie läuft von oben bis unten über den vollständigen Rücken

### Rückseite

- ausschließlich eine komplette gerade horizontale Flatline
- kein Ausschlag
- sonst leer
- **kein Barcode-Rahmen, kein ISBN-Feld, kein Dummy, kein Rückseitentext**
- Amazon KDP setzt den Barcode selbst

### Live-Gate

Wenn der KDP-Previewer nicht exakt **233 Seiten** meldet:

1. tatsächliche Seitenzahl übernehmen
2. `python scripts/build_kdp_cover.py --pages <KDP_SEITENZAHL> --paper white --output ABWEICHUNG_COVER.pdf`
3. PDF-Geometrie erneut prüfen
4. erst dann Cover hochladen

## 8. Preis

Startvorschlag Amazon.de: **14,99 €**.

Repo-interne Schätzung bei 233 Seiten:

- Druckkosten ca. **3,55 €**
- Tantieme bei 60 % ca. **5,45 €**

Live-Druckkosten vor Veröffentlichung prüfen und Preis bewusst bestätigen.

## 9. Release-Gates

Repository-seitig:

- [x] finales Manuskript vorhanden
- [x] finale DOCX vorhanden
- [x] Buchbeschreibung vorhanden
- [x] Keywords definiert
- [x] Kategorien-Zielrichtung definiert
- [x] KI-Offenlegung festgelegt
- [x] ISBN-Default festgelegt
- [x] Preisvorschlag festgelegt
- [x] Cover-Spezifikation vorhanden
- [x] **233-Seiten-Cover-PDF vorhanden**

Live/Human:

- [ ] Veröffentlichungsname des Autors eintragen
- [ ] KDP-Paperback anlegen
- [ ] Innenraum hochladen
- [ ] Previewer-Seitenzahl bestätigen
- [ ] bei abweichender Seitenzahl Cover neu bauen
- [ ] ISBN-Entscheidung final bestätigen
- [ ] Cover hochladen
- [ ] finalen Previewer ohne Fehler abschließen
- [ ] Preis final bestätigen
- [ ] Veröffentlichung auslösen
