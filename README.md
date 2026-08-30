# ABWEICHUNG

Erster echter Romanlauf mit `Satte882/Buch-Framework` v0.2.

## Aktueller Stand

**G0 APPROVED → G1 APPROVED → Szenenebene reviewt → Beat-Ebene vollständig geplant → AWAITING_FRESH_CONTEXT_BEAT_REVIEW**

- 18 Bausteine
- 54 Ereignisse
- 40 Szenen
- 253 Beats
- 6 plotrelevante Kernrollen
- 3 Informationsstränge: Outcome / Governance / Externalität
- R-06 medizinische Ankerfälle geschlossen
- Fresh-Context-Szenenreview: `CLEAN_FRESH_CONTEXT`, 0 Findings
- Same-Context-Beat-Review: 0 mandatory findings
- Prosa bewusst noch nicht begonnen

## Arbeitsprinzip

Die Story wird konsequent **vom Groben ins Feine** aufgebaut:

`Buchidee / Gesamtarchitektur → Baustein → Ereignisse → Szene → Beats → Prosa`

Dabei gilt:

> Erst eine Ebene über das gesamte Buch ausreichend schließen, dann die nächste Ebene ableiten.

Prosa ist die letzte Ebene. Sie beginnt erst, wenn die Story bis auf Szenen- und Beat-Ebene so granular festgelegt und geprüft ist, dass beim Schreiben keine relevante Storyentscheidung mehr erfunden werden muss.

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
    │       │   ├── SZENE.md
    │       │   └── BEATS.md
    │       └── 01_01_02_DER_SICHTBARE_ERFOLG/
    │           ├── SZENE.md
    │           └── BEATS.md
    ├── 02_.../
    └── 18_.../
```

Die Storywahrheit ist damit bis auf Beat-Ebene horizontal über den gesamten Roman heruntergebrochen. `PROSA.md` wird weiterhin **nicht vorgezogen**.

## Nächster Prüfpunkt

Die vollständige Beat-Ebene wird einmal unabhängig im Fresh Context geprüft (`BEAT_FRESH_CONTEXT_TASK.md`).

Wenn dieser Review keine offenen Blocker ergibt, folgt der Human Gate **G2 / Prose Ready**. Erst nach G2 beginnt die Prosaebene.

## Reihengedanke

Die Bücher sind keine klassische Fortsetzungsreihe mit denselben Figuren. Gemeinsam ist die dramaturgische Denkmaschine:

> Ein gesellschaftlich nachvollziehbares Problem trifft auf eine zunächst vernünftige Lösung. Die Lösung funktioniert. Gerade ihr Erfolg verschiebt schrittweise eine Grenze, bis etwas normal oder legitim erscheint, das zu Beginn kaum akzeptabel gewesen wäre.

## Thematischer Kern

**Thema:** KI + Entscheidungsmacht  
**Konflikt:** Ergebnisqualität vs. legitime menschliche Entscheidungsmacht

> **Wie lange darf ein Mensch eine schlechtere Entscheidung treffen, wenn eine Maschine nachweislich die bessere kennt?**

Kernumkehr:

> **Nicht mehr die Maschine muss beweisen, dass sie recht hat. Der Mensch muss beweisen, warum er von ihr abweichen darf.**
