# ABWEICHUNG

Erster echter Romanlauf mit `Satte882/Buch-Framework` v0.2.

## Aktueller Stand

**G0 APPROVED → G1 APPROVED → Szenenebene reviewt → Beat-Ebene reviewt → G2 APPROVED → PROSA FREIGEGEBEN**

- 18 Bausteine
- 54 Ereignisse
- 40 Szenen
- 253 Beats
- 6 plotrelevante Kernrollen
- 3 Informationsstränge: Outcome / Governance / Externalität
- R-06 medizinische Ankerfälle geschlossen
- Fresh-Context-Szenenreview: `CLEAN_FRESH_CONTEXT`, 0 Findings
- Same-Context-Beat-Review: 0 mandatory findings
- Fresh-Context-Beat-Review: `CLEAN_FRESH_CONTEXT`, 1 Finding
- BEAT-SR-001: bestätigt und auf Beat-Ebene korrigiert
- offene Story-/Szenen-/Beat-Blocker: none
- Human Gate G2 / Prose Ready: APPROVED
- Prosa darf jetzt beginnen

## Arbeitsprinzip

Die Story wird konsequent **vom Groben ins Feine** aufgebaut:

`Buchidee / Gesamtarchitektur → Baustein → Ereignisse → Szene → Beats → Prosa`

Dabei gilt:

> Erst eine Ebene über das gesamte Buch ausreichend schließen, dann die nächste Ebene ableiten.

Die Story ist jetzt bis auf Beat-Ebene horizontal geschlossen und freigegeben. Die Prosa ist die letzte Ebene und konkretisiert Sprache, Rhythmus, Dialog, Atmosphäre und Wahrnehmung. Sie darf keine neue relevante Storyentscheidung stillschweigend einführen.

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
    │       │   ├── BEATS.md
    │       │   └── PROSA.md
    │       └── 01_01_02_DER_SICHTBARE_ERFOLG/
    │           ├── SZENE.md
    │           ├── BEATS.md
    │           └── PROSA.md
    ├── 02_.../
    └── 18_.../
```

`PROSA.md` wird erst jetzt nach G2 erzeugt.

## Nächste Ebene

**Prosa.**

Die freigegebene Ableitungskette bleibt verbindlich:

`Baustein → Ereignisse → Szene → Beats → Prosa`

Wenn beim Schreiben eine echte Storyänderung notwendig erscheint, muss sie explizit auf die betroffene vorgelagerte Ebene zurückgeführt werden. Die Prosa darf die freigegebene Architektur nicht still umschreiben.

## Reihengedanke

Die Bücher sind keine klassische Fortsetzungsreihe mit denselben Figuren. Gemeinsam ist die dramaturgische Denkmaschine:

> Ein gesellschaftlich nachvollziehbares Problem trifft auf eine zunächst vernünftige Lösung. Die Lösung funktioniert. Gerade ihr Erfolg verschiebt schrittweise eine Grenze, bis etwas normal oder legitim erscheint, das zu Beginn kaum akzeptabel gewesen wäre.

## Thematischer Kern

**Thema:** KI + Entscheidungsmacht  
**Konflikt:** Ergebnisqualität vs. legitime menschliche Entscheidungsmacht

> **Wie lange darf ein Mensch eine schlechtere Entscheidung treffen, wenn eine Maschine nachweislich die bessere kennt?**

Kernumkehr:

> **Nicht mehr die Maschine muss beweisen, dass sie recht hat. Der Mensch muss beweisen, warum er von ihr abweichen darf.**
