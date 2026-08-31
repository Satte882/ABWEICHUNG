# Full-Manuscript Self Review – ABWEICHUNG

status: HARDENING_COMPLETE_INDEPENDENT_REVIEW_REQUIRED
review_scope: prose S001–S040
hardened_prose_target: `1937fec17d283613a31e30e3346d4b521fc61176`
independent_review: required

## Zweck

Same-Context-Selbstprüfung und anschließender Manuskript-Hardening-Pass des vollständigen Prosa-Drafts nach G3. Diese Datei ist **keine unabhängige Qualitätsfreigabe** und darf von einem späteren Fresh-Context-Reviewer nicht als Evidenzquelle verwendet werden.

## Vollständigkeit

- 18 Bausteine vorhanden
- 54 Ereignisse vorhanden
- 40 Szenen vorhanden
- 253 Beats vorhanden
- 40/40 Szenen besitzen `PROSA.md`
- davon 3 G3-freigegebene Stilreferenzen: S001, S019, S023
- 37 weitere Szenen nach G3 in derselben Stilrichtung ausformuliert

## Mechanische / profilbezogene Prüfung

### Harter Guard `sondern = 0`

- G3-Stichprobe S001/S019/S023: bereits vor G3 geprüft, 0 Treffer
- Prosa-Batch S002–S009: 0 Treffer
- Prosa-Batch S010–S018: 0 Treffer
- Prosa-Batch S020–S027: 0 Treffer
- Prosa-Batch S028–S035: 0 Treffer
- Prosa-Batch S036–S040: 0 Treffer
- die nachfolgenden Hardening-Reworks führen das verbotene Wort ebenfalls nicht neu ein

Ergebnis: **PASS** für `forbidden_sondern`.

## Erster Same-Context-Pass – korrigierte Prosa-Fehler

1. **S020:** interner Produktionsbegriff `Cold-Open-Fall` aus dem Fließtext entfernt.
2. **S037:** interner Produktionsbegriff `Cold Open` aus dem Fließtext entfernt.
3. **S037:** Tippfehler `überdeckckte` → `überdeckte`.
4. **S020/S037/S038/S039:** klar erkennbare Negationsketten sprachlich geglättet, ohne Inhalt zu ändern.
5. **S028:** Feststellung des schweren hypoxischen Schadens in den weiteren Verlauf verschoben, damit die Prosa nicht suggeriert, der endgültige Schaden sei bereits in der unmittelbaren Notfallminute abschließend diagnostiziert worden.

## Whole-Manuscript-Hardening nach Gesamtlektüre

Eine anschließende Gesamtlektüre über S001–S040 machte Muster sichtbar, die ein szenenweiser Scanner nicht zuverlässig erkennt. Die Befunde wurden gegen den tatsächlichen Branch geprüft und wie folgt dispositioniert.

### 1. Interne Produktionslabels

Bestätigt und korrigiert:

- **S008:** `Cold-Open-Nacht` → natürliche Rückreferenz auf die frühere Nacht.
- **S020:** `Cold-Open-Fall` war bereits korrigiert.
- **S035:** internes Architektur-Label `B13` entfernt; die Erinnerung referenziert nur noch Laura und die im Roman etablierte Regel.
- **S037:** `Cold Open` war bereits korrigiert.

Der Audit der ursprünglichen fünf Schreib-Batches fand keine weitere Instanz dieser bekannten Labelklassen.

### 2. Manuskriptweites Dialog-Pingpong

Befund: Kurze Frage-Antwort-Ketten waren über viele Governance-/Analyse-Szenen hinweg zu ähnlich verteilt. Lokal waren sie jeweils plausibel; in der Summe entstand ein Monotonierisiko.

Gezielt reworked:

- **S004:** Jan präsentiert die Evidenz zunächst zusammenhängend; Eva prüft anschließend die Tragfähigkeit.
- **S014:** Evas Hypothese wird als markierter Analyseauftrag statt als Fragekaskade vermittelt.
- **S015:** Low-/High-Confidence-Evidenz bekommt zusammenhängenden Raum; Prüfungsdialog stark reduziert.
- **S018:** Eva bietet ihre eigenen Fälle aktiv als Gegenprobe an und definiert die Analyse in einem zusammenhängenden Argument.
- **S027:** Regelverhandlung wird über konkrete Textarbeit am Entwurf und längere Begründung geführt statt über repetitive Kurzfragen.
- **S008:** zusätzlich rhythmisch neu gefasst, da die Szene besonders stark aus Ja/Nein-Prüffragen bestand.

Bewusst nicht pauschal entfernt:

- S003 bleibt als früher, knapper Morgenreview vergleichsweise stakkato.
- Echtzeit-/Prüfungsszenen wie S010, S021, S029 und S035 dürfen kurze Fragen behalten, wenn die Form aus klinischer Arbeit, Audit oder Zweitfreigabe entsteht.

Ziel war **Verteilungsvariation**, nicht die Eliminierung eines grundsätzlich funktionierenden Stilmittels.

### 3. Wiederkehrender Szenentyp „Daten zeigen → Rückfragen → Klärung“

Der Befund wurde als real akzeptiert, aber ohne G2-Backtrack behandelt. Die freigegebenen Szenenfunktionen blieben unverändert. Variation entstand ausschließlich auf Prosaebene durch unterschiedliche Träger:

- zusammenhängende Präsentation,
- markierter Analyseauftrag,
- konkrete Fallserien,
- Whiteboard-/Regelarbeit,
- direkte Textredaktion,
- aktive Gegenprobe durch Eva.

Status nach Hardening: **kein nachgewiesener Bedarf für Szenen-/Beat-Rework; unabhängige Gesamtlektüre muss die Wirkung erneut beurteilen.**

### 4. Übergangsfloskeln `Eva sah / nickte / schwieg`

Befund: Über das Gesamtmanuskript häuften sich diese Formeln als Absatzscharniere.

Gezielt reduziert in **S002, S005 und S006** sowie indirekt durch die größeren Reworks S004/S014/S015/S018/S027. Nicht jede Blickbewegung wurde ersetzt: Wo Eva tatsächlich zwischen Patient, Daten und Oberfläche prüft, bleibt Wahrnehmung funktional und soll nicht durch künstliche Synonymrotation ersetzt werden.

### 5. Wiederkehrende Kontrastformeln

Der G3-Watchpoint in S019 bleibt als Stilreferenz unangetastet. Die ähnliche Formel in **S033** (`Nicht derselbe Patient. Nicht dieselbe Diagnose. Aber dieselbe Form.`) wurde in eine fließende Spiegelung umgebaut, damit das Muster nicht als wiederkehrende Signatur über das Manuskript erscheint.

## Kritische Architekturketten – Same-Context-Check nach Hardening

### Nele S010/S011

- S010: Nele entscheidet und dokumentiert den Override selbst.
- Eva gibt keine Vorabfreigabe und erfährt die Entscheidung erst im weiteren Verlauf.
- S011: Eva erkennt Kultur-/Mentoring-Verantwortung, nicht direkte Mitentscheidung.

Status: **konsistent**.

### Midpoint S018/S019

- Eva fordert die personenbezogene Auswertung selbst an.
- S018 wurde rhythmisch verändert, die Initiative Evas bleibt vollständig erhalten.
- S019 bricht Evas unvollständige Gewichtung sichtbarer und unsichtbarer Folgen; KORAs reale Grenzen bleiben erhalten.

Status: **konsistent**.

### Wert-/Kontextregel S024–S027

- Trennung Prognosewiderspruch vs. akzeptierte Prognose + patientenspezifischer Wert-/Kontextgrund wird vor dem Finale aufgebaut.
- S026 zeigt Missbrauch/Umdeklaration.
- S027 setzt weiterhin explizit: räumliche Nähe, Behandlerbeziehung und allgemeines unmittelbares Verantwortungsgefühl reichen allein nicht.

Status: **konsistent**.

### Felix S028–S030

- S028 zeigt Schadensfall und Anlass für Audit.
- S029 beweist die umgangene Schutzstufe, **nicht** Felix' Absicht und **nicht** einen sicheren alternativen Patientenausgang.
- S030 bestätigt Felix' Absicht erst durch seine eigene Nichtbestreitung/Rechtfertigung.

Status: **konsistent**.

### Finale S033–S040

- S033 wurde nur rhythmisch geglättet; der Spiegel zum Ausgangskonflikt bleibt erhalten.
- S035 enthält kein internes `B13` mehr, prüft aber weiterhin exakt die vorher etablierten zwei zulässigen Abweichungswege; Nele verweigert eigenständig.
- S036: Solo-Break-glass bleibt technisch real; Eva nutzt ihn freiwillig nicht, weil sie keinen tragfähigen Grund findet.
- S037: lokaler Patient stirbt ohne nachträglichen Rettungstrick.
- S038: entfernter Patient überlebt; kein Beweis allgemeiner KORA-Unfehlbarkeit.
- S039: Institution bewertet Human Oversight als gewahrt; Eva übernimmt diese Erfolgserzählung nicht vollständig.
- S040 endet offen mit `Was sieht KORA nicht?` vor Antwort/Entscheidung.

Status: **konsistent**.

## Nicht durch Same-Context-Hardening freigegeben

Diese Punkte benötigen bewusst einen unabhängigen Gesamtmanuskriptblick auf den gehärteten Stand:

- Gesamtpacing und Gewichtung über alle 40 Szenen
- ausreichende Romanlänge / Erlebnisdichte statt bloßer Architektur-Abarbeitung
- ob Dialogrhythmus und Meeting-/Analyse-Szenen **nach** dem Rework ausreichend variiert sind
- verbleibende wiederkehrende Übergangs- oder Kontrastformeln über große Distanz
- ausreichende Differenzierung der Stimmen von Eva, Miriam, Felix, Nele, Jan und Laura
- Expositionsdichte in Governance-/Daten-Szenen
- semantische Anti-KI-Muster wie Erklärungsechos und rhetorische Über-Symmetrie
- emotionale Tragfähigkeit des Finales über den Gesamtroman hinweg

## Ergebnis

Same-Context-Status: **HARDENING_PASS_WITH_INDEPENDENT_REVIEW_REQUIRED**

Der gehärtete Prosa-Draft auf `1937fec17d283613a31e30e3346d4b521fc61176` darf jetzt in einen bewusst entkoppelten Fresh-Context-Gesamtmanuskriptreview gehen. Kein Human Gate G4 wurde durch diese Selbstprüfung vorweggenommen.
