# ABWEICHUNG

Erster echter Romanlauf mit `Satte882/Buch-Framework` v0.2.

## Aktueller Stand

**G0 APPROVED → G1 APPROVED → Szenenebene vollständig geplant**

- 18 Bausteine
- 54 Ereignisse
- 40 Szenen
- 6 plotrelevante Kernrollen
- 3 Informationsstränge: Outcome / Governance / Externalität
- R-06 medizinische Ankerfälle für die Szenenebene geschlossen
- Beats und Prosa bewusst noch nicht begonnen

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
├── R06_MEDIZINISCHE_ANKERFAELLE.md
├── gates/
└── BAUSTEINE/
    ├── 01_COLD_OPEN/
    │   ├── BAUSTEIN.md
    │   ├── EREIGNISSE/
    │   │   └── EREIGNISSE.md
    │   └── SZENEN/
    │       ├── 01_01_01_DIE_LETZTE_KAPAZITAET/
    │       │   └── SZENE.md
    │       └── 01_01_02_DER_SICHTBARE_ERFOLG/
    │           └── SZENE.md
    ├── 02_.../
    └── 18_.../
```

Die Szenenebene ist jetzt über den gesamten Roman vorhanden. Jede Szene enthält zunächst nur `SZENE.md`. `BEATS.md` und `PROSA.md` werden **nicht vorgezogen**.

## Nächste Ebene

Nach Review der vollständigen Szenenfolge folgt horizontal die **Beat-Ebene** über alle 40 Szenen.

Erst danach wird G2 / Prose Ready geprüft. Prosa beginnt nicht vorher.

## Reihengedanke

Die Bücher sind keine klassische Fortsetzungsreihe mit denselben Figuren. Gemeinsam ist die dramaturgische Denkmaschine:

> Ein gesellschaftlich nachvollziehbares Problem trifft auf eine zunächst vernünftige Lösung. Die Lösung funktioniert. Gerade ihr Erfolg verschiebt schrittweise eine Grenze, bis etwas normal oder legitim erscheint, das zu Beginn kaum akzeptabel gewesen wäre.

## Thematischer Kern

**Thema:** KI + Entscheidungsmacht  
**Konflikt:** Ergebnisqualität vs. legitime menschliche Entscheidungsmacht

> **Wie lange darf ein Mensch eine schlechtere Entscheidung treffen, wenn eine Maschine nachweislich die bessere kennt?**

Kernumkehr:

> **Nicht mehr die Maschine muss beweisen, dass sie recht hat. Der Mensch muss beweisen, warum er von ihr abweichen darf.**