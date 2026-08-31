# ABWEICHUNG

Erster echter Romanlauf mit `Satte882/Buch-Framework` v0.2.

## Aktueller Stand

**G0 APPROVED → G1 APPROVED → G2 APPROVED → G3 APPROVED → 40/40 PROSA → MANUSKRIPT-REWORK/ADJUDIKATION → G4 APPROVED → PRODUCTION BUILD PASS → READY_FOR_HUMAN_G5**

- 18 Bausteine
- 54 Ereignisse
- 40 Szenen
- 253 Beats
- 40/40 Szenen mit `PROSA.md`
- kanonischer G4-Manuskriptstand: `78222a7e99c80378c35379ad42684ee332a412a6`
- offene bestätigte G4-Blocker/Majors: 0
- nicht blockierende G4-Residual-/Minor-Risiken: 2
- Human `G4-APPROVE`: 2026-08-31
- `main` enthält den vollständigen G4-Stand
- Framework-Lessons-Learned aus Issue #17 umgesetzt; Issue #17 geschlossen
- Production Build Run #1 / ID `33366125536`: **PASS**
- Produktionsartefakt: `abweichung-production-v01`
- konsolidierte Fassung: `ABWEICHUNG_v01.md` + `ABWEICHUNG_v01.html`
- vollständiger G4-Umfang: **16.527 Wörter**
- Human Gate G5: **READY_FOR_HUMAN_G5 – Produktumfang muss bewusst entschieden werden**

## G4

Human `G4-APPROVE` akzeptiert den vollständigen Manuskriptstand

`78222a7e99c80378c35379ad42684ee332a412a6`

als kanonisches Manuskript.

Gate-Record: `gates/G4.md`

Weitere Änderungen am Roman nach G4 dürfen keine neue Storyentscheidung stillschweigend einführen.

## Produktion

Der Produktionsbuilder `scripts/build_production.py` liest ausschließlich den festen G4-Commit und erzeugt deterministisch:

1. `ABWEICHUNG_v01.md` – konsolidierte Manuskriptfassung
2. `ABWEICHUNG_v01.html` – standalone Lese-/Druckfassung
3. `BUILD_INFO.json` – Quellen-/Hashnachweis

Kanonischer Build:

- Workflow: `Production Build`
- Run #1 / ID: `33366125536`
- Ergebnis: PASS
- Artifact-ID: `9748335150`
- ZIP SHA-256: `b6d6fde371e14d9f2f03b5e4a5839ff1e85e72f03345ab508c31373bb3e0d765`
- Markdown SHA-256: `9c00cb0632b0729f43bf0d74f565573d52a794de4d6227eac06a3cf966ff478d`
- HTML SHA-256: `debc8a08023ca793c4ab4b35c2e5c428d3eb94f4d9ce97dcbd6bdfe3e12b4be4`
- 40/40 Szenen, S001–S040 lückenlos
- `sondern = 0`

Details: `production/BUILD_MANIFEST.md`

## Produktumfang vor G5

Der Produktionsbuild hat erstmals den vollständigen Umfang exakt gemessen:

**16.527 Wörter bei 40 Szenen.**

Vor G4 war kein verbindlicher Ziel-Wortumfang definiert. Deshalb wird die Zahl nicht rückwirkend als automatischer G4-Fehler behandelt.

G5 muss den Produkt-Scope nun bewusst entscheiden:

- `G5-APPROVE` – aktuellen Umfang und Produktionsstand akzeptieren,
- `G5-REWORK` – Manuskript/Product Scope wieder öffnen,
- `G5-STOP` – Produktion stoppen.

Gate-Anforderung: `G5_REVIEW_REQUEST.md`

## Lessons Learned

Der Pilot hat insbesondere bestätigt:

- Whole-Book Scene-Shape-Verteilung vor G2 prüfen,
- G3 zusätzlich mit zusammenhängendem Mittelteil-Run prüfen,
- globale statt nur lokale Wiederholungsmuster bewerten,
- bei wiederholtem bestätigtem Manuskript-Major kontrolliert upstream backtracken,
- Raw-Reviews vor Rework evidenzbasiert adjudizieren.

Diese Punkte wurden nach G4 in `Satte882/Buch-Framework` umgesetzt.

## Thematischer Kern

**Thema:** KI + Entscheidungsmacht  
**Konflikt:** Ergebnisqualität vs. legitime menschliche Entscheidungsmacht

> **Wie lange darf ein Mensch eine schlechtere Entscheidung treffen, wenn eine Maschine nachweislich die bessere kennt?**

Kernumkehr:

> **Nicht mehr die Maschine muss beweisen, dass sie recht hat. Der Mensch muss beweisen, warum er von ihr abweichen darf.**
