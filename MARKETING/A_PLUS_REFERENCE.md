# Amazon KDP A+ – Referenzbasis

status: REFERENCE
scope: ABWEICHUNG test implementation
source_type: Amazon-KDP-Hilfeseiten / vom Nutzer bereitgestellte Dokumentation
last_reviewed: 2026-09-01

## Zweck

Diese Datei ist die **Regel- und Bedienbasis** für die Entwicklung von A+-Inhalten für `ABWEICHUNG`.

Sie enthält bewusst **noch keine konkrete A+-Kampagne und keine finalen Modultexte**. Die konkrete Gestaltung wird in einem separaten Arbeitsartefakt entwickelt. Nach Umsetzung, Review und KDP-Erfahrung werden die übertragbaren Erkenntnisse als Lessons Learned extrahiert und anschließend in `Satte882/Buch-Framework` übernommen.

## Offizielle Quellen

- A+-Inhalte: https://kdp.amazon.com/de_DE/help/topic/GHL7P99B7AA543CN
- Beispiele für A+-Inhalte: https://kdp.amazon.com/de_DE/help/topic/GCKLH8V7ULLD5EXY
- A+-Inhalte erstellen / verwalten: https://kdp.amazon.com/de_DE/help/topic/G8EP5W6H9CY7T8GS
- A+-Inhaltsrichtlinien: https://kdp.amazon.com/de_DE/help/topic/G4WB7VPPEAREHAAD

## Grundlogik

- Amazon stellt **17 A+-Module** zur Auswahl bereit.
- Pro Detailseitenlayout können **bis zu fünf Module** verwendet werden.
- A+ dient dazu, zusätzliche visuelle und textliche Produktinformationen auf der Buchdetailseite bereitzustellen.
- Die Inhalte werden über den **A+-Inhalte-Manager** erstellt, einer oder mehreren ASINs aus dem eigenen KDP-Konto zugewiesen, geprüft und anschließend zur Genehmigung eingereicht.
- Mehrere Formate desselben Buchs können einem Projekt zugeordnet werden, sofern die ASINs im eigenen KDP-Konto liegen.
- A+-Inhalte werden marketplacebezogen veröffentlicht. Für andere Stores müssen sie separat erstellt bzw. als Entwurf dupliziert und erneut veröffentlicht werden.

## Erstellungsprozess in KDP

1. KDP-Marketingseite öffnen.
2. Bereich **A+-Inhalte** aufrufen.
3. Shop / Marketplace auswählen.
4. **A+-Inhalte verwalten** öffnen.
5. **Erstellen von A+-Inhalten starten**.
6. Inhaltsname und Sprache festlegen.
7. Bis zu fünf Module hinzufügen und anordnen.
8. Bilder in der jeweils geforderten Modulgröße hochladen.
9. Texte in die vorgesehenen Textfelder eintragen.
10. **Weiter: ASINs anwenden**.
11. Nur ASINs aus dem eigenen KDP-Konto auswählen.
12. Desktop- und Mobilvorschau prüfen.
13. **Zur Genehmigung übermitteln**.

Amazon nennt für regelkonforme Inhalte eine Veröffentlichung innerhalb von bis zu acht Werktagen; in Zeiten hoher Auslastung kann die Prüfung länger dauern.

## Beispielhafte Module aus der Amazon-Dokumentation

Die Amazon-Beispielseite ordnet Module u. a. folgenden Anwendungsfällen zu. Dies ist **keine vollständige Liste aller 17 Module**.

### Serien

**Vergleichstabellenmodul**

- bis zu fünf ASINs vergleichbar
- mehrere Vergleichstabellen pro Detailseite möglich
- nur für andere Bücher im eigenen KDP-Konto verwenden
- kleinste genannte Bildgröße: 150 × 300 px

**Standardmodul für technische Spezifikationen**

- Tabellenüberschrift setzt den Kontext
- bis zu 16 Zeilen
- geeignet für Buchlisten, Kurzbeschreibungen oder ergänzende Informationen

### Hintergrund des Autors / Charaktere

**Standardmodul mit Einzelbild und Seitenleiste**

- Autorenbild, Kurzbiografie, Q&A oder Charakterinformationen möglich
- hochwertige JPG-/PNG-Dateien verwenden

**Standardmodul mit Einzelbild auf der linken Seite**

- kleinste genannte Bildgröße: 600 × 180 px
- Amazon empfiehlt für hohe Auflösung 600 × 600 px

### Coverbild / Konzept

**Standardbild und Text-Overlay**

- geeignet als Banner mit Hintergrundbild und wenigen Textzeilen
- kleinste genannte Bildgröße: 970 × 300 px
- Amazon empfiehlt 1.940 × 600 px für hohe Auflösung
- Text nicht in das Hintergrundbild einbauen, sondern das Overlay-Feld verwenden
- Overlay ist optional und besitzt laut Beispielseite 70 % Deckkraft

### Leseprobe / Handlung

**Standardmodul mit drei Bildern und Text**

- kleinste genannte Bildgröße: 300 × 300 px
- Amazon empfiehlt 600 × 600 px
- Text möglichst nicht direkt in Bilder einbauen

**Standardmodul A mit mehreren Bildern**

- mehrere visuelle Elemente zur Handlung / Atmosphäre

**Standardtext zur Produktbeschreibung**

- bis zu 6.000 Zeichen
- linksbündiger Text
- keine eigene Überschriftenformatierung; erste Zeile kann hervorgehoben werden

## Bildanforderungen – operative Safe Rule

Amazon-Dokumente nennen je nach Seite unterschiedliche Grenzwerte. Die Beispielseite nennt teilweise **maximal 3 MB**, die A+-Inhaltsrichtlinien nennen **unter 2 MB pro Bilddatei**. Für `ABWEICHUNG` gilt deshalb als konservative Produktionsregel:

> **Jede A+-Bilddatei bleibt unter 2 MB.**

Weitere Regeln:

- JPG, BMP oder PNG
- RGB, **kein CMYK**
- keine GIFs / Animationen
- Zielauflösung: **300 DPI**
- Amazon bezeichnet Bilder unter 200 DPI als niedrige Auflösung
- keine unscharfen, pixeligen oder mit Wasserzeichen versehenen Bilder
- kein kleiner Text, der mobil nicht lesbar ist
- Alt-Text muss das Bild sachlich und screenreader-tauglich beschreiben
- A+-Bilder sollen einzigartige Aspekte ergänzen und nicht einfach die vorhandene Bildergalerie duplizieren
- nur eigene bzw. rechtlich nutzbare Bilder und Texte einsetzen

## Text- und Formatierungsregeln

- korrekte Rechtschreibung, Grammatik und Zeichensetzung
- Zahlen unter zehn ausschreiben
- keine unnötigen Großbuchstabenfolgen
- Fett/Kursiv sparsam und primär für Überschriften bzw. gezielte Hervorhebungen
- keine HTML-Tags oder Inhalte in einer anderen Sprache als der für den A+-Inhalt gewählten Sprache
- keine unnötigen oder wiederholten Informationen

## Nicht zulässige bzw. hochriskante Inhalte

### Preis / Verkauf

Nicht verwenden:

- Preise
- Rabatte oder Aktionen
- „günstig“, „billig“, „Bonus“, „kostenlos“
- „jetzt kaufen“, „in den Einkaufswagen“, „jetzt erhalten“ oder vergleichbare Kaufaufforderungen
- Versandinformationen

### Zeitbezug

Nicht verwenden:

- „jetzt“
- „neu“ / „neueste“
- „jetzt im Angebot“
- „das Beste bisher“
- Feiertagsbezüge
- Verweise auf Kindle Unlimited

### Rezensionen / Zitate

- keine Kundenrezensionen
- keine Aussagen von Privatpersonen
- maximal vier Zitate oder Empfehlungen
- nur aus bekannten Publikationen oder von öffentlich bekannten Personen
- Quelle, Autor, Datum und bei Publikationen Titel angeben

### Behauptungen / Auszeichnungen

- keine unbelegten Zertifizierungs-, Test-, Empfehlungs- oder Bestätigungsclaims
- Auszeichnungen/Empfehlungen mit Organisation und Datum belegen
- keine veralteten Auszeichnungen über zwei Jahre
- keine „Nr. 1“, „bestbewertet“, „100 % Zufriedenheit“ oder vergleichbare prahlerische Behauptungen

### Sonstige Beschränkungen

- keine Mitbewerber nennen oder vergleichen
- keine externen Links
- keine QR-Codes
- keine Telefonnummern, E-Mail-Adressen oder persönlichen Kontaktdaten
- keine Garantie-/Rückgabeinformationen außerhalb Amazon
- keine Nachahmung von Amazon-Logos, Detailseitenüberschriften oder Amazon-UI
- Vergleichstabellen ausschließlich für andere Bücher im eigenen KDP-Konto

## Marketplace-Regel

A+-Inhalte gelten jeweils für den Store, in dem sie veröffentlicht wurden. Für weitere Amazon-Stores müssen Inhalte separat veröffentlicht werden. Vorhandene Inhalte können als Entwurf dupliziert werden.

Für Amazon.de unterstützt Amazon laut bereitgestellter Dokumentation mehrere Sprachen, darunter Deutsch und Englisch. Für `ABWEICHUNG` ist der initiale Zielmarkt **Amazon.de / Deutsch**.

## Generative KI im A+-Manager

Amazon beschreibt eine **AI Ready**-Funktion für ausgewählte Module. Laut bereitgestellter Dokumentation ist sie derzeit nur:

- auf Englisch
- in den USA

verfügbar.

Unabhängig davon bleibt der Publisher für Richtigkeit und Richtlinienkonformität generierter Inhalte verantwortlich.

## Compliance-Check vor Einreichung

Vor jeder A+-Einreichung für `ABWEICHUNG` prüfen:

- [ ] maximal fünf Module
- [ ] Sprache konsistent Deutsch
- [ ] alle Bilder RGB
- [ ] jedes Bild unter 2 MB
- [ ] Zielauflösung 300 DPI
- [ ] richtige Pixelmaße je Modul
- [ ] keine Texte zu klein oder unleserlich im Bild
- [ ] Alt-Texte vorhanden und beschreibend
- [ ] keine Preise / Rabatte / Kaufaufforderungen
- [ ] keine Zeitangaben / KU-Hinweise
- [ ] keine Kundenrezensionen
- [ ] keine unbelegten Claims
- [ ] keine Mitbewerbervergleiche
- [ ] keine externen Links / QR-Codes / Kontaktdaten
- [ ] keine redundante Wiederholung der normalen Amazon-Bildergalerie
- [ ] Desktop-Vorschau geprüft
- [ ] Mobil-Vorschau geprüft
- [ ] verwendete ASINs gehören zum eigenen KDP-Konto

## Abgrenzung

Diese Datei beantwortet **was Amazon erlaubt und wie A+ technisch eingereicht wird**.

Sie beantwortet ausdrücklich noch nicht:

- welche fünf Module `ABWEICHUNG` konkret nutzen soll
- welche Story-/Marketingdramaturgie über die Module läuft
- welche Texte und Bilder erzeugt werden
- welche Module nach realer Vorschau funktionieren oder verworfen werden
- welche Regeln generalisierbar in das Buch-Framework gehören

Diese Entscheidungen folgen im nächsten Arbeitsschritt.
