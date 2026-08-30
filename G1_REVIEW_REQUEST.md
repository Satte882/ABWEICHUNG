# G1 Review Request – ABWEICHUNG

status: READY_FOR_HUMAN_G1
review_type: Human Gate G1 – Story-Architektur
basis: `STORY_PACKAGE.md`; `STORY_BLOCKS.md`; `EVENTS.md`; `CHARACTERS.md`; `RESEARCH_REGISTER.md`; `G1_FRESH_CONTEXT_RESULT.md`

## Architektur in Kurzform

- 18 Story Blocks
- 54 Events
- 6 plotrelevante Figuren/Funktionsrollen
- 3 durchgehende Informationsstränge: O = Outcome/Performance, G = Governance/Macht, X = Externalität/Sichtbarkeit
- 3 zentrale Beziehungsbögen: Eva↔Miriam, Eva↔Felix, Eva↔Nele
- Cold Open und Finale spiegeln denselben Ressourcenkonflikt mit unterschiedlicher Informationslage
- Midpoint-Reversal: Evas eigene high-confidence Override-Bilanz ist schlechter als KORA; ihr lokaler Erfolgsbias wird sichtbar
- Wert-/Kontextabweichungen bleiben legitimer menschlicher Entscheidungsraum, sind aber vor dem Finale auf benennbare patientenspezifische Gründe begrenzt; bloße Nähe/Behandlerbindung reicht im verbundweiten Ressourcenkonflikt nicht
- Felix' Umgehung ist im konkreten Schadensfall kausal mit der ausgeschalteten Zweitfreigabe verbunden; kein sicherer kontrafaktischer Patientenausgang wird behauptet
- Finale: echter Break-glass bleibt vorhanden, Eva nutzt ihn mangels medizinischen Gegenbelegs **und** mangels zulässigen patientenspezifischen Wert-/Kontextgrunds nicht
- keine böse KI, kein Herstellerkomplott, kein späterer Technikfehler als Ausweg

## Research-Status

R-01 bis R-05: resolved / `blocking_now: no`.

R-06 – konkrete medizinische Falldetails: open / `blocking_now: no` für G1. Vor medizinisch konkreten G2-Beats/Szenenkarten wird R-06 blockierend geschlossen.

## Same-Context-Review

`SEMANTIC_G1_SELF_REVIEW.md` ist abgeschlossen, zählt aber ausdrücklich **nicht** als unabhängiger Review.

## Fresh-Context-Review

`G1_FRESH_CONTEXT_TASK.md` wurde in einem neuen Chat ausgeführt.

Ergebnis: `CLEAN_FRESH_CONTEXT`, 2 Findings.

Disposition in `G1_FRESH_CONTEXT_RESULT.md`:

1. **G1-SR-001 confirmed** – fehlende Grenze Wert-/Kontextabweichung vs. Finale → Story-Architektur korrigiert.
2. **G1-SR-002 confirmed** – Felix-Schaden war noch nicht kausal an die konkrete Umgehung gekoppelt → Event-/Block-Kette korrigiert.

Beide Befunde wurden umgesetzt; keine G0-Entscheidung wurde verändert und keine neue Plotidee hinzugefügt.

## G1-Prüffragen für den Human Gate

1. Trägt Eva Riedel als Protagonistin zwischen evidenzorientierter Medizin und ärztlicher Letztentscheidung?
2. Trägt Miriam als legitime Gegenkraft, ohne zur autoritären Strohfrau zu werden?
3. Trägt die Eskalation der Governance von freiem Override bis Break-glass als schrittweise Folge realer Probleme?
4. Trägt der Midpoint, dass nicht KORA, sondern Evas eigene high-confidence Abweichungsbilanz ihr Selbstbild beschädigt?
5. Ist die Wert-/Kontextausnahme ausreichend real, aber zugleich so begrenzt, dass das Finale nicht über ein spontanes „Duty-to-care“-Schlupfloch gelöst wird?
6. Ist Felix' Grenzüberschreitung kausal genug, ohne ihn zum Bösewicht oder den Patientenausgang kontrafaktisch sicher zu machen?
7. Trägt das Finale: Nele verweigert die Zweitfreigabe nach bereits gesetzten Kriterien; Eva könnte Break-glass nutzen, tut es aber nicht?
8. Ist die zentrale Frage weiterhin unverändert sichtbar: **Wie lange darf ein Mensch eine schlechtere Entscheidung treffen, wenn eine Maschine nachweislich die bessere kennt?**

## Human Gate

- `G1-APPROVE` – Story-Architektur wird kanonisch; danach horizontale Beat-Ebene und G2-Vorbereitung.
- `G1-REWORK` – Architektur vor G1-Freigabe weiter überarbeiten.
- `G1-STOP` – Romanlauf stoppen.

**Noch keine G1-Entscheidung wurde im Repository eingetragen.**