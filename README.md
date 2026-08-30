# ABWEICHUNG

Erster echter Romanlauf mit `Satte882/Buch-Framework` v0.2.

## Aktueller Stand

**G0 APPROVED → G1 APPROVED → Szenenebene reviewt → Beat-Ebene reviewt → G2 APPROVED → G3-PROSA-STICHPROBE BEREIT**

- 18 Bausteine
- 54 Ereignisse
- 40 Szenen
- 253 Beats
- 3 repräsentative Prosa-Szenen für G3
- 37 Szenen bis G3 bewusst noch ohne Prosa
- 6 plotrelevante Kernrollen
- 3 Informationsstränge: Outcome / Governance / Externalität
- R-06 medizinische Ankerfälle geschlossen
- Fresh-Context-Szenenreview: `CLEAN_FRESH_CONTEXT`, 0 Findings
- Fresh-Context-Beat-Review: `CLEAN_FRESH_CONTEXT`, 1 Finding; bestätigt und korrigiert
- offene Story-/Szenen-/Beat-Blocker: none
- Human Gate G2 / Prose Ready: APPROVED
- aktueller Prüfpunkt: Human Gate G3 / Prosa-Stil

## Arbeitsprinzip

Die Story wird konsequent **vom Groben ins Feine** aufgebaut:

`Buchidee / Gesamtarchitektur → Baustein → Ereignisse → Szene → Beats → Prosa`

Dabei gilt:

> Erst eine Ebene über das gesamte Buch ausreichend schließen, dann die nächste Ebene ableiten.

Die Story ist bis auf Beat-Ebene horizontal geschlossen und durch G2 freigegeben. Vor der Vollskalierung testet G3 einen kleinen repräsentativen Prosa-Batch. Erst nach G3-APPROVE wird die Prosa auf die übrigen Szenen skaliert.

## Aktueller G3-Batch

- `S001 – Die letzte Kapazität`: akuter medizinischer Druck
- `S019 – Die Bilanz`: analytischer Midpoint
- `S023 – Würden Sie es wieder tun?`: persönliche Konfrontation

Nur diese drei Szenen tragen aktuell `prose_allowed: yes` und besitzen eine `PROSA.md`.

## Repo-Struktur

```text
ABWEICHUNG/
├── BOOK_IDEA.md
├── STORY_PACKAGE.md
├── CHARACTERS.md
├── RESEARCH_REGISTER.md
├── R06_MEDIZINISCHE_ANKERFAELLE.md
├── G3_REVIEW_REQUEST.md
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
    │           └── BEATS.md
    ├── 02_.../
    └── 18_.../
```

## Prosa-Regel

Prosa konkretisiert Sprache, Rhythmus, Dialog, Atmosphäre und Wahrnehmung. Sie darf keine neue relevante Storyentscheidung stillschweigend einführen.

Wenn beim Schreiben eine echte Storyänderung notwendig erscheint, muss sie explizit auf die betroffene vorgelagerte Ebene zurückgeführt werden.

## Nächster Prüfpunkt

Human Gate **G3 / Prosa-Stil** über `G3_REVIEW_REQUEST.md`.

Freigabetoken:

- `G3-APPROVE`
- `G3-REWORK`
- `G3-STOP`

Bis zur G3-Entscheidung wird keine weitere Szene in Prosa geschrieben.

## Reihengedanke

Die Bücher sind keine klassische Fortsetzungsreihe mit denselben Figuren. Gemeinsam ist die dramaturgische Denkmaschine:

> Ein gesellschaftlich nachvollziehbares Problem trifft auf eine zunächst vernünftige Lösung. Die Lösung funktioniert. Gerade ihr Erfolg verschiebt schrittweise eine Grenze, bis etwas normal oder legitim erscheint, das zu Beginn kaum akzeptabel gewesen wäre.

## Thematischer Kern

**Thema:** KI + Entscheidungsmacht  
**Konflikt:** Ergebnisqualität vs. legitime menschliche Entscheidungsmacht

> **Wie lange darf ein Mensch eine schlechtere Entscheidung treffen, wenn eine Maschine nachweislich die bessere kennt?**

Kernumkehr:

> **Nicht mehr die Maschine muss beweisen, dass sie recht hat. Der Mensch muss beweisen, warum er von ihr abweichen darf.**
