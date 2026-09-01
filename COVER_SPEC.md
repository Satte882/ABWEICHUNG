# KDP-Cover – ABWEICHUNG

status: APPROVED-233-page-cover
approved_by: human
date: 2026-09-01

## Verbindliches Design

Das Printcover ist minimalistisch, vollständig schwarz auf weiß und wird als **flaches Full-Wrap-Cover** produziert. Kein Buch-Mockup, keine 3D-Darstellung, keine Schatten-/Falzsimulation.

Es enthält **keinen Autorennamen, kein Genrelabel, keinen Rückseitentext und keine ISBN-/Barcode-Platzhaltergrafik**.

### Vorderseite

Von oben nach unten:

1. Titel: `ABWEICHUNG`
2. direkt darunter kursiv: `Zwischen Mensch und System`
3. horizontale Linie über die komplette Breite der Vorderseite mit genau einem integrierten Ausschlag
4. darunter zweizeilig:
   - `Du darfst widersprechen.`
   - `Die Beweislast liegt bei dir.`

Titelregeln:

- innerhalb der beschnittenen Vorderseite zentriert
- links und rechts mindestens **0,675 Zoll Sicherheitsabstand** innerhalb der Trim-Fläche
- maximale Titelbreite: **3,710 Zoll**
- Tracking: **1,5 pt**; Schriftgröße wird im Build automatisch reduziert, bis die Sicherheitszone eingehalten wird

### Buchrücken

- **kein Text**
- **kein Titel**
- ausschließlich eine schwarze vertikale Linie von ganz oben bis ganz unten
- in diese Linie ist genau derselbe Ausschlag wie auf der Vorderseite integriert, lediglich um **90 Grad gedreht**
- Linie und Ausschlag bilden **einen einzigen durchgängigen Pfad**; der Ausschlag darf nicht als separates Symbol neben oder auf der Linie erscheinen

### Rückseite

- ausschließlich **eine gerade horizontale schwarze Linie** über die komplette Rückseitenbreite
- **kein Ausschlag** auf der Rückseite
- sonst vollständig leer
- kein Rahmen, kein ISBN-Feld, kein Barcode-Dummy, kein Platzhaltertext
- Amazon KDP setzt den Barcode selbst

## Aktuelle Produktionsgeometrie

Finale Innen-PDF laut aktuellem Export:

- Trim Size: **5,06 × 7,81 Zoll**
- Seitenzahl: **233 Seiten**
- Seitenzahlquelle: final exportierte Innen-PDF, vom Nutzer am 2026-09-01 bestätigt
- Schwarzweiß-Inhalt
- weißes Papier
- Cover-Beschnitt: **0,125 Zoll an allen Außenkanten**

KDP-Faktor für Schwarzweiß auf weißem Papier:

- Rückenbreite: `233 × 0,002252" = 0,524716"`
- Gesamtbreite: `0,125 + 5,06 + 0,524716 + 5,06 + 0,125 = 10,894716"`
- Gesamthöhe: `0,125 + 7,81 + 0,125 = 8,060"`
- metrisch: ca. **276,726 × 204,724 mm**

`ABWEICHUNG_COVER.pdf` wird exakt in dieser Größe erzeugt.

## Technische Regeln

- eine PDF-Seite
- Full-Wrap: Rückseite | Rücken | Vorderseite
- flache Produktionsgrafik, kein Mockup
- ausschließlich Schwarz und Weiß
- keine Crop Marks oder Hilfslinien
- Fonts vollständig eingebettet
- weißer Full-Bleed-Hintergrund
- schwarze Vektortypografie und Vektorlinien
- keine Transparenz notwendig
- keine Anmerkungen/Formfelder
- Barcode-Bereich gestalterisch unberührt
- Titelbreite wird gegen die definierte Sicherheitszone geprüft
- PNG-Preview wird ausschließlich aus demselben Produktions-PDF gerendert

Build:

```bash
python scripts/build_kdp_cover.py --pages 233 --paper white --output ABWEICHUNG_COVER.pdf
```

## Live-KDP-Gate

Die Produktionsgeometrie basiert jetzt auf der final exportierten Innen-PDF mit **233 Seiten**. Für den finalen Upload ist trotzdem die im **KDP-Previewer** tatsächlich gemeldete Seitenzahl maßgeblich.

Wenn KDP eine andere Seitenzahl meldet:

1. Gestaltung unverändert lassen,
2. tatsächliche Seitenzahl in den Cover-Build übernehmen,
3. Rückenbreite und Gesamtbreite neu berechnen lassen,
4. `ABWEICHUNG_COVER.pdf` neu erzeugen und preflighten,
5. PNG-Preview aus genau diesem PDF rendern und visuell prüfen,
6. erst danach hochladen.
