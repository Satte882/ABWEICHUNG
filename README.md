# ABWEICHUNG

Erster echter Romanlauf mit `Satte882/Buch-Framework` v0.2.

## Aktueller Stand

**G0 APPROVED → G1 APPROVED → nächste Ebene: SZENEN**

- 18 Bausteine: freigegeben
- 54 Ereignisse: freigegeben
- 6 plotrelevante Kernrollen
- 3 Informationsstränge: Outcome / Governance / Externalität
- Fresh-Context-G1-Review durchgeführt; 2/2 Findings bestätigt und korrigiert
- Szenen, Beats und Prosa noch nicht begonnen

## Arbeitsprinzip

Die Story wird konsequent **vom Groben ins Feine** aufgebaut:

`Buchidee / Gesamtarchitektur → Baustein → Ereignisse → Szene → Beats → Prosa`

Dabei gilt:

> Erst eine Ebene über das gesamte Buch ausreichend schließen, dann die nächste Ebene ableiten.

Prosa ist die letzte Ebene. Sie beginnt erst, wenn die Story bis auf Szenen- und Beat-Ebene so granular festgelegt ist, dass beim Schreiben keine relevante Storyentscheidung mehr erfunden werden muss.

## Repo-Struktur

```text
ABWEICHUNG/
├── BOOK_IDEA.md
├── STORY_PACKAGE.md
├── CHARACTERS.md
├── RESEARCH_REGISTER.md
├── gates/
└── BAUSTEINE/
    ├── 01_COLD_OPEN/
    │   ├── BAUSTEIN.md
    │   └── EREIGNISSE/
    │       └── EREIGNISSE.md
    ├── 02_.../
    └── 18_.../
```

Die nächste horizontale Ebene sind die Szenen. Eine konkrete Szene erhält später genau diese Struktur:

```text
SZENEN/
└── 01_01_01/
    ├── SZENE.md
    ├── BEATS.md
    └── PROSA.md   # erst nach vollständiger Beat-Ebene und den nachfolgenden Gates
```

Keine parallelen Root-Ordner für Events, Beats oder Prosa. Figuren und Research bleiben als Querschnitt auf Meta-Ebene.

## Reihengedanke

Die Bücher sind keine klassische Fortsetzungsreihe mit denselben Figuren. Gemeinsam ist die dramaturgische Denkmaschine:

> Ein gesellschaftlich nachvollziehbares Problem trifft auf eine zunächst vernünftige Lösung. Die Lösung funktioniert. Gerade ihr Erfolg verschiebt schrittweise eine Grenze, bis etwas normal oder legitim erscheint, das zu Beginn kaum akzeptabel gewesen wäre.

## Thematischer Kern

**Thema:** KI + Entscheidungsmacht  
**Konflikt:** Ergebnisqualität vs. legitime menschliche Entscheidungsmacht

> **Wie lange darf ein Mensch eine schlechtere Entscheidung treffen, wenn eine Maschine nachweislich die bessere kennt?**

Kernumkehr:

> **Nicht mehr die Maschine muss beweisen, dass sie recht hat. Der Mensch muss beweisen, warum er von ihr abweichen darf.**
