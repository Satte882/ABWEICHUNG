# G1 Review Request – ABWEICHUNG

status: APPROVED
review_type: Human Gate G1 – Story-Architektur
decision: G1-APPROVE
decided_by: human
date: 2026-08-30
gate_record: `gates/G1.md`

## Freigegebene Architektur

- 18 Story-Bausteine
- 54 Ereignisse
- 6 plotrelevante Figuren/Funktionsrollen
- 3 durchgehende Informationsstränge: O = Outcome/Performance, G = Governance/Macht, X = Externalität/Sichtbarkeit
- 3 zentrale Beziehungsbögen: Eva↔Miriam, Eva↔Felix, Eva↔Nele
- Cold Open und Finale spiegeln denselben Ressourcenkonflikt mit unterschiedlicher Informationslage
- Midpoint-Reversal: Evas eigene high-confidence Override-Bilanz ist schlechter als KORA; ihr lokaler Erfolgsbias wird sichtbar
- Wert-/Kontextabweichungen bleiben legitimer menschlicher Entscheidungsraum, sind aber vor dem Finale auf benennbare patientenspezifische Gründe begrenzt
- Felix' Umgehung ist im konkreten Schadensfall kausal mit der ausgeschalteten Zweitfreigabe verbunden
- Finale: echter Break-glass bleibt vorhanden; Eva nutzt ihn mangels zulässigem Gegenbeleg nicht
- keine böse KI, kein Herstellerkomplott, kein späterer Technikfehler als Ausweg

## Struktur

Die freigegebene G1-Storywahrheit liegt hierarchisch unter `BAUSTEINE/`:

`Baustein → Ereignisse → später Szene → Beats → Prosa`

Basis:

- `STORY_PACKAGE.md`
- `BAUSTEINE/**/BAUSTEIN.md`
- `BAUSTEINE/**/EREIGNISSE/EREIGNISSE.md`
- `CHARACTERS.md`
- `RESEARCH_REGISTER.md`
- `G1_FRESH_CONTEXT_RESULT.md`

## Review-Historie

`SEMANTIC_G1_SELF_REVIEW.md` wurde durchgeführt, zählt aber nicht als unabhängiger Review.

Der Fresh-Context-Review war `CLEAN_FRESH_CONTEXT` und lieferte zwei Findings. Beide wurden bestätigt und vor dem Human Gate korrigiert.

## Research-Status

R-01 bis R-05: resolved / `blocking_now: no`.

R-06 – konkrete medizinische Falldetails – bleibt offen, war kein G1-Blocker und muss vor medizinisch konkreter Szenen-/Beat-Festlegung geschlossen werden.

## Ergebnis

Human `G1-APPROVE` erteilt.

Die nächste horizontale Arbeitsebene ist die **Szenenarchitektur über den gesamten Roman**. Beats und Prosa bleiben bis zum Abschluss ihrer jeweils vorgelagerten Ebene gesperrt.
