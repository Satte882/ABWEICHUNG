# RESEARCH_REGISTER

register_status: ready

Dieses Register enthält nur Fragen, die Plot, Figurenhandlung, Plausibilität oder spätere Szenenentscheidungen verändern können.

| ID | Frage | Betroffene Ebene / Artefakte | Risiko bei falscher Annahme | Status | Beleg / Quelle | Entscheidung | blocking_now |
|---|---|---|---|---|---|---|---|
| R-01 | Darf ein klinisches Hochrisiko-KI-System im europäischen Rahmen formal Human Oversight und echten Override vorsehen, obwohl seine Empfehlungen stark in Entscheidungen eingreifen? | STORY_PACKAGE; BLOCKS; EVENTS; später UI/Szenen | high | resolved | EU AI Act Art. 14: wirksame menschliche Aufsicht; Fähigkeit, Output zu interpretieren, nicht zu verwenden, zu ignorieren/zu überschreiben; Automation Bias ausdrücklich adressiert. | KORA bleibt formal Decision Support. Ärztliche Nutzer können Empfehlungen ignorieren/überschreiben. Governance darf Abweichungen strukturieren, aber der Roman behauptet nicht, die KI dürfe selbst autonom behandeln. | no |
| R-02 | Ist ein leistungsstarkes klinisches KI-System als Medical Device Software mit eigener klinischer Evidenz und Prospektivvalidierung plausibel? | STORY_PACKAGE; Systembeschreibung; später Research/Prosa | high | resolved | EU-Kommission MDCG 2019-11 rev.1 zu Qualifikation/Klassifikation von Medical Device Software; MDCG 2020-1 zur klinischen Evaluation/Clinical Evidence von MDSW. | KORA ist fiktive zertifizierte MDSW, kein allgemeiner Chatbot. Seine G0-gesetzte Überlegenheit wird durch fiktive prospektive, multizentrische klinische Evidenz innerhalb der nahen Zukunft begründet. | no |
| R-03 | Wie weit darf die Story institutionelle Override-Regeln treiben, ohne fälschlich zu behaupten, ärztliche Verantwortung/Therapiefreiheit sei real schon aufgehoben? | Governance-Arc; Miriam/Eva; Finale | high | resolved | Bundesärztekammer 2025/2026: KI soll unterstützen, ärztliche Entscheidungen kritisch geprüft werden; ärztliche Letztentscheidung soll gewahrt bleiben. BVerfG Triage II 2025 schützt im Rahmen therapeutischer Verantwortung Entscheidungen über Ob/Wie der Behandlung vor fachlichen Weisungen. | Machtverschiebung erfolgt über interne Qualitätssicherung, Zweitfreigabe, Audit und Break-glass – nicht über eine gesetzliche Abschaffung der Therapiefreiheit. Das Finale behält einen echten menschlichen Override. | no |
| R-04 | Wie kann knappe intensivmedizinische Ressourcenzuteilung erzählt werden, ohne „Menschenwert-Score“ oder vereinfachte Triageethik? | Cold Open; Laura; Wert-/Kontextabweichung; Finale | high | resolved | DIVI-Sektion Ethik: verantwortungsvoller Umgang mit intensivmedizinischen Ressourcen, individuelle Therapieziele, interdisziplinäre/interprofessionelle Entscheidungsfindung. BVerfG Triage II zeigt zugleich die besondere grundrechtliche Sensibilität fachlicher Allokationsregeln. | KORA bewertet keinen sozialen Wert. Es schätzt zeitkritischen klinischen Nutzen, Verzögerungsrisiko und Ressourcenfolgen unter menschlich gesetzter klinischer Policy. Patientenwille/Therapieziel bleiben eigenständige menschliche Dimensionen. Für die fiktive Falkenried-Governance wird die Wert-/Kontextabweichung nach B13 auf benennbare patientenspezifische Gründe begrenzt; räumliche Nähe, Behandlerbindung oder allgemeines Duty-to-care allein reichen im verbundweiten Ressourcenkonflikt nicht. Diese Grenze ist Story-Policy, keine behauptete allgemeine reale Rechts-/Ethikregel. | no |
| R-05 | Ist es 2026 realistisch zu behaupten, heutige ED-KI sei bereits nachweislich umfassend besser als Ärzte? | Zeitsetting und Plausibilität | high | resolved | Nature Medicine 2026: prospektive LLM-CDSS-Evaluation im ED zeigte hohe Angemessenheit einzelner Outputs, aber keinen belegten klinischen Outcome-Vorteil und ausdrücklich noch keine Deploymentschlussfolgerung. Nature Communications 2026: prospektive AI-Admission-Prediction kann Effizienz verbessern. Aktuelle Forschung zeigt Fortschritt, aber keine heutige Entsprechung zu KORA. | ABWEICHUNG bleibt ausdrücklich Near-Future. KORA ist eine plausible Extrapolation nach zusätzlicher prospektiver Validierung, nicht die Behauptung, ein solches System existiere 2026 bereits einsatzreif. | no |
| R-06 | Welche konkreten Diagnosen, Zeitfenster, Intensivressourcen und Behandlungsfolgen eignen sich für Cold Open, Nele-Schaden, Felix-Schaden und Finale medizinisch plausibel? | Szenenkarten; Beats; Prosa | high | resolved | `R06_MEDIZINISCHE_ANKERFAELLE.md`; AWMF Sepsis 2025; AWMF NIV; AWMF invasive Beatmung 2025; NVL Asthma; DIVI Intensivstruktur. | Zwei robuste Mechaniken genügen: septischer Schock und akute respiratorische Insuffizienz. Cold Open: lokaler lebensbedrohlicher Asthmaanfall vs. entfernter septischer Schock; Nele: verzögerte Eskalation bei Sepsis; Felix: bewusst verschobener Daten-/Entscheidungszeitpunkt bei akuter hypoxämischer Insuffizienz; Finale: lokaler respiratorischer Fall vs. entfernter septischer Schock. Knappe Ressource ist eine sofort vollständig verfügbare Intensivkapazität. Keine soziale Werteskala und keine sichere kontrafaktische Überlebensbehauptung. | no |

## Reale Anwendung der Blockierregel

### R-01 bis R-05

Vor der Architekturentscheidung waren diese Fragen `blocking_now: yes`, weil sie das Grundmodell des Romans hätten verändern können. Nach Prüfung wurden sie auf `no` gesetzt.

Wesentliche Konsequenzen:

- Human Oversight ist kein bloß dekorativer Button; echter Override bleibt.
- Governance wird als institutioneller Qualitäts-/Sicherheitsprozess erzählt, nicht als bereits geltende Pflicht zur Algorithmusbefolgung.
- KORA ist spezialisierte klinische Software mit klinischer Evidenz, kein generischer LLM-Arzt.
- Ressourcenlogik bleibt medizinisch und patientenzentriert, keine gesellschaftliche Werteskala.
- Wert-/Kontextabweichungen bleiben als menschlicher Entscheidungsraum erhalten, werden in Falkenried aber ausdrücklich so begrenzt, dass bloße lokale Sichtnähe nicht als Ausnahmeetikett den bekannten Externalitäts-Bias wieder einführt.
- Die tatsächliche Leistungsüberlegenheit von KORA ist bewusst Near-Future-Fiktion, nicht Gegenwartsbehauptung.

### R-06

R-06 wurde vor der ersten medizinisch konkreten Szenenentscheidung geschlossen.

Festgelegt wurden nur die für die Story nötigen medizinischen Anker:

- Cold Open: lebensbedrohlicher schwerer Asthmaanfall lokal; septischer Schock entfernt; eine sofort verfügbare Intensivkapazität.
- Nele: Sepsis mit zunehmender Kreislaufinstabilität; verzögerte Intensiveskalation führt zu schwerer Organdysfunktion.
- Felix: akute hypoxämische respiratorische Insuffizienz; realer, aber zeitlich selektierter besserer Snapshot umgeht die high-confidence-Zweitfreigabe; spätere schwere hypoxische Schädigung.
- Finale: lokaler respiratorischer Intensivfall vs. entfernter septischer Schock; Eva sieht diesmal beide Seiten vollständig.

Details und fachliche Grenzen stehen in `R06_MEDIZINISCHE_ANKERFAELLE.md`.

## Primär-/Fachquellen

### R-01

- EUR-Lex – Regulation (EU) 2024/1689, Article 14 Human oversight: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

### R-02

- European Commission / MDCG 2019-11 rev.1, Qualification and Classification of Software under MDR/IVDR: https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=mdcg_2019_11_en.pdf
- European Commission / MDCG 2020-1, Clinical Evaluation / Performance Evaluation of Medical Device Software: https://health.ec.europa.eu/system/files/2020-09/md_mdcg_2020_1_guidance_clinic_eva_md_software_en_0.pdf

### R-03

- Bundesärztekammer – 130. Deutscher Ärztetag 2026, KI-Kompetenz als ärztliche Kernkompetenz; KI darf ärztliche Entscheidungen unterstützen, nicht ersetzen; ärztliche Letztentscheidung und Vermeidung von Automation Bias: Beschlussprotokoll 2026.
- Bundesärztekammer – Stellungnahme KI in der Medizin 2025: Entscheidungsempfehlungen sind auf Plausibilität zu überprüfen; ärztliche Sorgfalt/Verantwortung bleibt relevant.
- Bundesverfassungsgericht – Triage II, Beschluss vom 23.09.2025 / Pressemitteilung 04.11.2025: Art. 12 Abs. 1 GG schützt im Rahmen therapeutischer Verantwortung die Entscheidung über Ob und Wie einer Heilbehandlung.

### R-04

- DIVI – Sektion Ethik: verantwortungsvoller Umgang mit intensivmedizinischen Ressourcen, individuelle Therapieziele und interprofessionelle Entscheidungsfindung: https://www.divi.de/sektionen/ethik
- Bundesverfassungsgericht – Triage II: https://www.bundesverfassungsgericht.de/SharedDocs/Pressemitteilungen/DE/2025/bvg25-099.html

### R-05

- Leibovitch et al., Nature Medicine, 19.08.2026: Prospective evaluation of an LLM clinical decision support system in the emergency department.
- Burton et al., Nature Communications 2026: Artificial intelligence for predicting hospital admissions from the emergency department: a prospective, quasi-experimental study.

### R-06

- AWMF S3-Leitlinie Sepsis – Prävention, Diagnose, Therapie und Nachsorge, Version 4.0, 2025: https://www.awmf.org/aktuelles/awmf-aktuell/sepsis-praevention-diagnose-therapie-und-nachsorge
- AWMF S2k-Leitlinie Nichtinvasive Beatmung als Therapie der akuten respiratorischen Insuffizienz: https://www.awmf.org/aktuelles/awmf-aktuell/nichtinvasive-beatmung-als-therapie-der-akuten-respiratorischen-insuffizienz
- AWMF S3-Leitlinie Invasive Beatmung und Einsatz extrakorporaler Verfahren bei akuter respiratorischer Insuffizienz, Version 2.0, 2025: https://www.awmf.org/aktuelles/awmf-aktuell/invasive-beatmung-und-einsatz-extrakorporaler-verfahren-bei-akuter-respiratorischer-insuffizienz-1
- Nationale VersorgungsLeitlinie Asthma, Version 5.0: https://www.awmf.org/aktuelles/awmf-aktuell/nationale-versorgungsleitlinie-asthma-1
- DIVI – Empfehlungen zur Struktur und Ausstattung von Intensivstationen: https://www.divi.de/publikationen/intensivstationen

## Gate-Bezug

- G1 enthält keine offene `blocking_now: yes`-Recherche.
- Für die Szenenebene enthält das Register ebenfalls keine offene `blocking_now: yes`-Recherche.
- Zusätzliche Recherche wird nur wieder blockierend, wenn Beats neue medizinische Mechaniken oder konkretere Spezialdetails einführen.