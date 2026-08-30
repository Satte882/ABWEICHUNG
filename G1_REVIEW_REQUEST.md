# G1 Review Request – ABWEICHUNG

status: READY_FOR_HUMAN_G1
review_type: Human Gate G1 – Story-Architektur
basis: `STORY_PACKAGE.md`; `BAUSTEINE/**/BAUSTEIN.md`; `BAUSTEINE/**/EREIGNISSE/EREIGNISSE.md`; `CHARACTERS.md`; `RESEARCH_REGISTER.md`; `G1_FRESH_CONTEXT_RESULT.md`

## Architektur in Kurzform

- 18 Story-Bausteine
- 54 Ereignisse
- 6 plotrelevante Figuren/Funktionsrollen
- 3 durchgehende Informationsstränge: O = Outcome/Performance, G = Governance/Macht, X = Externalität/Sichtbarkeit
- 3 zentrale Beziehungsbögen: Eva↔Miriam, Eva↔Felix, Eva↔Nele
- Cold Open und Finale spiegeln denselben Ressourcenkonflikt mit unterschiedlicher Informationslage
- Midpoint-Reversal: Evas eigene high-confidence Override-Bilanz ist schlechter als KORA; ihr lokaler Erfolgsbias wird sichtbar
- Wert-/Kontextabweichungen bleiben legitimer menschlicher Entscheidungsraum, sind aber vor dem Finale auf benennbare patientenspezifische Gründe begrenzt; bloße Nähe/Behandlerbindung reicht im verbundweiten Ressourcenkonflikt nicht
- Felix' Umgehung ist im konkreten Schadensfall kausal mit der ausgeschalteten Zweitfreigabe verbunden; kein sicherer kontrafaktischer Patientenausgang wird behauptet
- Finale: echter Break-glass bleibt vorhanden, Eva nutzt ihn mangels medizinischen Gegenbelegs **und** mangels zulässigen patientenspezifischen Wert-/Kontextgrunds nicht
- keine böse KI, kein Herstellerkomplott, kein späterer Technikfehler als Ausweg

## Struktur

Die G1-Storywahrheit liegt jetzt hierarchisch unter `BAUSTEINE/`:

`Baustein → Ereignisse → später Szene → Beats → Prosa`

Szenen, Beats und Prosa existieren noch nicht. Sie werden erst nach G1 horizontal über das gesamte Buch abgeleitet.

## Research-Status

R-01 bis R-05: resolved / `blocking_now: no`.

R-06 – konkrete medizinische Falldetails: open / `blocking_now: no` für G1. Vor medizinisch konkreten G2-Szenen/Beats wird R-06 blockierend geschlossen.

## Reviews

`SEMANTIC_G1_SELF_REVIEW.md` ist abgeschlossen, zählt aber ausdrücklich nicht als unabhängiger Review.

`G1_FRESH_CONTEXT_TASK.md` wurde in einem neuen Chat ausgeführt. Ergebnis: `CLEAN_FRESH_CONTEXT`, 2 Findings. Beide wurden in `G1_FRESH_CONTEXT_RESULT.md` bestätigt und korrigiert.

## G1-Prüffragen für den Human Gate

1. Trägt Eva Riedel als Protagonistin zwischen evidenzorientierter Medizin und ärztlicher Letztentscheidung?
2. Trägt Miriam als legitime Gegenkraft, ohne zur autoritären Strohfrau zu werden?
3. Trägt die Eskalation der Governance von freiem Override bis Break-glass als schrittweise Folge realer Probleme?
4. Trägt der Midpoint, dass nicht KORA, sondern Evas eigene high-confidence Abweichungsbilanz ihr Selbstbild beschädigt?
5. Ist die Wert-/Kontextausnahme ausreichend real, aber zugleich so begrenzt, dass das Finale nicht über ein spontanes Duty-to-care-Schlupfloch gelöst wird?
6. Ist Felix' Grenzüberschreitung kausal genug, ohne ihn zum Bösewicht oder den Patientenausgang kontrafaktisch sicher zu machen?
7. Trägt das Finale: Nele verweigert die Zweitfreigabe nach bereits gesetzten Kriterien; Eva könnte Break-glass nutzen, tut es aber nicht?
8. Ist die zentrale Frage weiterhin unverändert sichtbar: **Wie lange darf ein Mensch eine schlechtere Entscheidung treffen, wenn eine Maschine nachweislich die bessere kennt?**

## Human Gate

- `G1-APPROVE` – Story-Architektur wird kanonisch; danach Szenen- und Beat-Ebene sowie G2-Vorbereitung.
- `G1-REWORK` – Architektur vor G1-Freigabe weiter überarbeiten.
- `G1-STOP` – Romanlauf stoppen.

**Noch keine G1-Entscheidung wurde im Repository eingetragen.**
