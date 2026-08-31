# KDP-Cover – ABWEICHUNG

status: current-333-page-cover-candidate

## Verbindliches Design

Das Printcover ist bewusst minimalistisch. Es enthält **keinen Autorennamen, kein Genrelabel, keinen Rückseitentext und keine ISBN-/Barcode-Platzhaltergrafik**.

### Vorderseite

- Titel: `ABWEICHUNG`
- darunter eine horizontale Linie über die **komplette Breite der Vorderseite**
- in der Linie ein einzelner Ausschlag
- darunter ausschließlich der Untertitel: `Wenn die Maschine recht hat`
- sonst nichts

### Buchrücken

- kein Titel
- kein Text
- exakt dasselbe Linien-/Ausschlagmotiv wie auf der Vorderseite, um 90 Grad gedreht
- die vertikale Linie läuft über die **komplette Höhe des Buchrückens**

### Rückseite

- ausschließlich eine durchgehende horizontale Flatline über die komplette Rückseitenbreite
- sonst vollständig leer
- **kein Rahmen, kein ISBN-Feld, kein Barcode-Dummy, kein Platzhaltertext**
- Amazon KDP setzt den Barcode selbst

## Aktuelle Produktionsgeometrie

Innenraum laut freigegebenem Produktionsstand:

- Trim Size: **5,06 × 7,81 Zoll**
- CI-PDF-Render: **333 Seiten**
- Schwarzweiß-Inhalt
- weißes Papier
- Cover-Beschnitt: **0,125 Zoll an allen Außenkanten**

KDP-Faktor für Schwarzweiß auf weißem Papier:

- Rückenbreite: `333 × 0,002252" = 0,749916"`
- Gesamtbreite: `0,125 + 5,06 + 0,749916 + 5,06 + 0,125 = 11,119916"`
- Gesamthöhe: `0,125 + 7,81 + 0,125 = 8,060"`
- metrisch: ca. **282,446 × 204,724 mm**

`ABWEICHUNG_COVER.pdf` wird aktuell exakt in dieser Größe erzeugt.

## Technische Regeln

- eine PDF-Seite
- Full-Wrap: Rückseite | Rücken | Vorderseite
- keine Crop Marks oder Hilfslinien
- Fonts vollständig eingebettet
- weißer Full-Bleed-Hintergrund
- schwarze Vektortypografie und Vektorlinien
- keine Transparenz notwendig
- keine Anmerkungen/Formfelder
- Barcode-Bereich gestalterisch unberührt

Build:

```bash
python scripts/build_kdp_cover.py --pages 333 --paper white --output ABWEICHUNG_COVER.pdf
```

## Live-KDP-Gate

Die 333 Seiten stammen aus dem validierten Repository-/LibreOffice-Render. Für den finalen Upload ist trotzdem die im **KDP-Previewer** tatsächlich gemeldete Seitenzahl maßgeblich.

Wenn KDP eine andere Seitenzahl meldet:

1. keine Gestaltung verändern,
2. nur die tatsächliche Seitenzahl in den Cover-Build übernehmen,
3. Rückenbreite und Gesamtbreite neu berechnen lassen,
4. `ABWEICHUNG_COVER.pdf` neu erzeugen und preflighten,
5. erst danach hochladen.