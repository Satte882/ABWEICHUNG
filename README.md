# ABWEICHUNG

Erster echter Romanlauf mit `Satte882/Buch-Framework` v0.2.

## Aktueller Stand

**G0 APPROVED → G1 Story-Architektur vollständig → READY_FOR_HUMAN_G1**

- 18 Bausteine B01–B18
- 54 Events
- 6 plotrelevante Kernrollen
- 3 Informationsstränge: Outcome / Governance / Externalität
- Fresh-Context-G1-Review durchgeführt; 2/2 Findings bestätigt und korrigiert
- Szenen, Beats und Prosa bewusst noch nicht begonnen

## Verbindliche Arbeitsstruktur

Die Story wird **vom Groben ins Feine** aufgebaut. Die Ebenen stehen nicht parallel nebeneinander.

```text
ABWEICHUNG/
├── README.md
├── BOOK_IDEA.md
├── STORY_PACKAGE.md
├── CHARACTERS.md
├── RESEARCH_REGISTER.md
├── gates/
│
└── BAUSTEINE/
    ├── B01/
    │   ├── BAUSTEIN.md
    │   ├── EVENTS.md
    │   └── SZENEN/
    │       └── S001/
    │           ├── SZENE.md
    │           ├── BEATS.md
    │           ├── CHARACTER_STATES.md
    │           └── PROSA.md
    ├── B02/
    │   └── ...
    └── B18/
        └── ...
```

Die Ordner `SZENEN/` und die darunterliegenden Dateien entstehen erst, wenn die jeweilige Ebene fachlich erreicht ist. Git hält keine leeren Ordner vor.

## Ableitungsregel

`Buchidee / Story Package → Baustein → Events / Sequenzen → Szenen → Beats → Prosa`

Dabei gilt horizontal:

> Erst eine Ebene über das gesamte Buch ausreichend schließen, dann die nächste Ebene ableiten.

Das bedeutet insbesondere:

- erst alle Bausteine und ihre Eventketten schließen,
- dann Szenen über das gesamte Buch ableiten,
- dann jede Szene in Beats präzisieren,
- erst wenn G2 bestätigt, dass keine relevante Storyentscheidung mehr beim Schreiben erfunden werden muss, entsteht Prosa.

**Prosa ist die unterste Ebene und niemals ein paralleler Arbeitsstrang.**

## Source of Truth

Meta-Ebene im Root:

- `BOOK_IDEA.md` – Konzept
- `STORY_PACKAGE.md` – Gesamtarchitektur
- `CHARACTERS.md` – Figurenkern / Beziehungen
- `RESEARCH_REGISTER.md` – Rechercheabhängigkeiten
- `gates/` – Human-Gate-Records

Story-Hierarchie:

- `BAUSTEINE/Bxx/BAUSTEIN.md` – kanonischer Baustein
- `BAUSTEINE/Bxx/EVENTS.md` – kanonische Event-/Sequenzebene dieses Bausteins
- später `BAUSTEINE/Bxx/SZENEN/Sxxx/...` – Szene → Beats/States → Prosa

Die Root-Dateien `STORY_BLOCKS.md` und `EVENTS.md` bleiben vorerst als **abgeleitete Gesamt-/Checker-Sicht** erhalten. Sie sind nicht die primäre Arbeitsquelle und dürfen nicht unabhängig von `BAUSTEINE/` weiterentwickelt werden.

## Reihengedanke

Die Bücher sind keine klassische Fortsetzungsreihe mit denselben Figuren. Gemeinsam ist die dramaturgische Denkmaschine:

> Ein gesellschaftlich nachvollziehbares Problem trifft auf eine zunächst vernünftige Lösung. Die Lösung funktioniert. Gerade ihr Erfolg verschiebt schrittweise eine Grenze, bis etwas normal oder legitim erscheint, das zu Beginn kaum akzeptabel gewesen wäre.

Die Gefahr entsteht nicht primär durch ein System, das versagt, sondern durch eines, das **funktioniert**.

## Thematischer Kern

**Thema:** KI + Entscheidungsmacht  
**Konflikt:** Ergebnisqualität vs. legitime menschliche Entscheidungsmacht

> **Wie lange darf ein Mensch eine schlechtere Entscheidung treffen, wenn eine Maschine nachweislich die bessere kennt?**

Kernumkehr:

> **Nicht mehr die Maschine muss beweisen, dass sie recht hat. Der Mensch muss beweisen, warum er von ihr abweichen darf.**

Der konkrete, G0-freigegebene Romanansatz steht in [`BOOK_IDEA.md`](BOOK_IDEA.md).