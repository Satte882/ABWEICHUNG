#!/usr/bin/env python3
"""Targeted dialogue-rhythm rework after external XR-002 review.

This pass is intentionally narrow. It does not change story events, causal claims,
scene order, or the G1/G2 architecture. It only rewrites a small set of verified
question/short-answer chains that survived the scene-shape rework.
"""

from __future__ import annotations

from pathlib import Path


def apply_replacement(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old in text:
        text = text.replace(old, new, 1)
        path.write_text(text, encoding="utf-8", newline="\n")
        return
    if new in text:
        return
    raise SystemExit(f"expected dialogue block missing in {path}")


def mark_status(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for old in (
        "prose_status: final_rhythm_rework",
        "prose_status: external_major_rework",
    ):
        if old in text:
            text = text.replace(old, "prose_status: external_major_dialogue_rework", 1)
            path.write_text(text, encoding="utf-8", newline="\n")
            return
    if "prose_status: external_major_dialogue_rework" in text:
        return
    raise SystemExit(f"prose_status missing in {path}")


P005 = Path("BAUSTEINE/03_UNSICHTBARE_GEGENRECHNUNG/SZENEN/03_03_01_DIE_BETTENKETTE/PROSA.md")
P006 = Path("BAUSTEINE/03_UNSICHTBARE_GEGENRECHNUNG/SZENEN/03_03_02_DER_ZWEITE_AUSGANG/PROSA.md")
P010 = Path("BAUSTEINE/05_NELES_OVERRIDE_SCHADEN/SZENEN/05_05_01_NELES_FALL/PROSA.md")
P011 = Path("BAUSTEINE/05_NELES_OVERRIDE_SCHADEN/SZENEN/05_05_02_ZU_SPAET/PROSA.md")
P022 = Path("BAUSTEINE/11_LAURA_KONFRONTATION/SZENEN/11_11_01_DIE_CHRONOLOGIE/PROSA.md")
P039 = Path("BAUSTEINE/18_NACHHALL_BEWEISLAST/SZENEN/18_18_01_HUMAN_OVERSIGHT/PROSA.md")

# S005: keep the confrontation, remove protocol-like alternating confirmations.
apply_replacement(
    P005,
    """„KORA bewertet verbundweit.“\n\n„Genau.“\n\n„KORA trägt den Patienten nicht.“\n\n„Nein.“\n\nMiriam verschob die Ansicht erneut. Jetzt standen Evas klinische Notizen direkt neben den Daten aus Nord.\n\n„Aber vielleicht sieht es Dinge, die ein Mensch am Bett zwangsläufig nicht gleichzeitig sehen kann.“""",
    """„KORA bewertet verbundweit“, sagte Eva. „Aber KORA trägt den Patienten nicht.“\n\nMiriam verschob die Ansicht erneut. Jetzt standen Evas klinische Notizen direkt neben den Daten aus Nord. „Nein. Aber vielleicht sieht es Dinge, die ein Mensch am Bett zwangsläufig nicht gleichzeitig sehen kann.“""",
)
apply_replacement(
    P005,
    """„Wenn ich Nord gesehen hätte, hätte ich trotzdem entscheiden müssen.“\n\n„Natürlich.“\n\n„Und vielleicht genauso.“\n\n„Vielleicht.“\n\nMiriam sagte es ohne Provokation. Gerade das störte Eva.""",
    """„Wenn ich Nord gesehen hätte, hätte ich trotzdem entscheiden müssen“, sagte Eva. „Vielleicht genauso.“\n\nMiriam nickte nur. „Vielleicht.“ Gerade die fehlende Provokation störte Eva.""",
)
apply_replacement(
    P005,
    """„Ich will nicht, dass daraus eine Moralgeschichte wird.“\n\n„Welche?“\n\n„Lokaler Arzt egoistisch, System objektiv.“\n\n„Das ist nicht meine Geschichte.“\n\n„Welche dann?“\n\nMiriam wandte sich wieder dem Bildschirm zu. „Dass du eine vernünftige Entscheidung getroffen haben kannst und sie trotzdem einen Preis hatte, den du in dem Moment kaum sehen konntest.“""",
    """„Ich will nicht, dass daraus eine Moralgeschichte wird. Lokaler Arzt egoistisch, System objektiv.“\n\nMiriam wandte sich wieder dem Bildschirm zu. „Das ist nicht meine Geschichte. Meine ist: Du kannst eine vernünftige Entscheidung treffen und trotzdem einen Preis erzeugen, den du in dem Moment kaum sehen kannst.“""",
)

# S006: causal uncertainty remains, but is no longer delivered as a review transcript.
apply_replacement(
    P006,
    """„Er ist nach der Verzögerung gestorben.“\n\n„Ja.“\n\n„Du sagst gerade dasselbe mit anderen Worten.“\n\n„Nein.“\n\nMiriam zog die Akte näher zu sich, nicht als Schutz, eher um den relevanten Abschnitt zwischen ihnen zu platzieren.\n\n„Wir können belegen, dass deine Ressourcenentscheidung seine definitive Intensivversorgung verzögert hat. Wir können nicht belegen, dass er bei früherer Aufnahme überlebt hätte.“""",
    """„Er ist nach der Verzögerung gestorben“, sagte Eva. „Für mich klingt das wie dasselbe mit anderen Worten.“\n\nMiriam zog die Akte näher zu sich, nicht als Schutz, eher um den relevanten Abschnitt zwischen ihnen zu platzieren. „Ist es nicht. Wir können belegen, dass deine Ressourcenentscheidung seine definitive Intensivversorgung verzögert hat. Wir können nicht belegen, dass er bei früherer Aufnahme überlebt hätte.“""",
)
apply_replacement(
    P006,
    """„Und wenn er sofort den Platz bekommen hätte?“\n\n„KORA berechnet uns keine alternative Vergangenheit.“\n\n„Das System macht Prognosen.“\n\n„Prospektiv. Nicht als Beweis für einen nicht eingetretenen Einzelfall.“""",
    """„Und wenn er sofort den Platz bekommen hätte? Das System macht Prognosen.“\n\nMiriam schüttelte den Kopf. „Prospektiv. Es berechnet uns keine alternative Vergangenheit und beweist keinen nicht eingetretenen Einzelfall.“""",
)
apply_replacement(
    P006,
    """„Und wenn er so oder so gestorben wäre?“\n\n„Dann wäre die Verzögerung trotzdem passiert.“\n\n„Aber ohne Schaden.“\n\n„Ohne nachweisbaren zusätzlichen individuellen Todesschaden. Die Ressourcenfolge bliebe.“""",
    """„Und wenn er so oder so gestorben wäre? Dann hätten wir eine Verzögerung ohne nachweisbaren zusätzlichen Todesschaden.“\n\n„Richtig“, sagte Miriam. „Die Ressourcenfolge bliebe.“""",
)

# S010: clinical supervision stays concrete, but clustered checklist dialogue becomes prose.
apply_replacement(
    P010,
    """„KORA wollte hoch.“\n\n„Ich weiß.“\n\n„High confidence.“\n\n„Auch das.“""",
    """Eva deutete auf den Konflikteintrag. „KORA wollte hoch. High confidence.“\n\n„Ich weiß“, sagte Nele.""",
)
apply_replacement(
    P010,
    """„Und das Laktat?“\n\n„Ist noch hoch.“\n\n„Tendenz?“\n\n„Noch nicht gut genug für eine Aussage.“\n\n„Vasopressor?“\n\nNele nannte die aktuelle Unterstützung.\n\nEva sah auf die Zeitpunkte.\n\n„Wann hast du zuletzt selbst untersucht?“\n\n„Vor zwölf Minuten.“\n\n„Neurologisch?“\n\n„Wach. Orientiert. Spricht normal.“\n\n„Diurese?“\n\nNele beantwortete auch das.""",
    """Eva fragte nach dem Laktat, seiner Tendenz und der aktuellen Vasopressorunterstützung. Das Laktat war noch hoch; für eine Richtung war es zu früh. Nele nannte die laufende Unterstützung.\n\nEva ging die Zeitpunkte weiter durch. Nele hatte den Patienten vor zwölf Minuten selbst untersucht: wach, orientiert, normale Sprache. Auch zur Diurese hatte sie eine aktuelle Antwort.""",
)
apply_replacement(
    P010,
    """„Noch stabil?“\n\nNele drehte sich um.\n\n„Im Moment ja.“\n\n„Neues Laktat?“\n\n„Noch nicht da.“""",
    """„Noch stabil? Neues Laktat?“\n\nNele drehte sich um. „Im Moment ja. Das Laktat ist noch nicht da.“""",
)

# S011: preserve Nele's ownership; reduce forensic cross-examination cadence.
apply_replacement(
    P011,
    """„KORA hat früher zur Intensiveskalation geraten.“\n\n„Ja.“\n\n„High confidence.“\n\n„Ja.“\n\n„Und ich habe gewartet.“""",
    """Nele sah auf ihre Hände. „KORA hat früher zur Intensiveskalation geraten. High confidence. Und ich habe gewartet.“""",
)
apply_replacement(
    P011,
    """„Was war dein Gegenbeleg?“\n\nNele antwortete nicht sofort.\n\n„Er hatte sich gebessert.“\n\n„Was genau hatte sich gebessert?“\n\nNele nannte die Veränderungen.\n\n„Und was blieb ungünstig?“\n\nNele sah auf die damaligen Werte.\n\n„Die Gesamtlage. Mehrere Risikosignale. Die Unsicherheit.“\n\n„Hatte KORA die vorübergehende Stabilisierung?“\n\n„Ja.“\n\n„Gab es einen relevanten Befund, den KORA nicht hatte?“\n\nNele schüttelte den Kopf.\n\n„Eine Datenlücke?“\n\n„Nein.“\n\n„Ein patientenspezifisches Therapieziel, das gegen die Eskalation sprach?“\n\n„Nein.“""",
    """„Sag mir deinen Gegenbeleg noch einmal vollständig“, sagte Miriam.\n\nNele brauchte einen Moment. „Er hatte sich gebessert. Druck, Herzfrequenz, klinischer Eindruck.“\n\nMiriam ließ sie ausreden. „Die Stabilisierung hatte KORA. Was blieb ungünstig?“\n\nNele sah auf die damaligen Werte. „Die Gesamtlage. Mehrere Risikosignale. Die Unsicherheit.“\n\n„Also kein relevanter Befund außerhalb der Systemdaten, keine Datenlücke und kein patientenspezifisches Therapieziel gegen die Eskalation?“\n\nNele schüttelte den Kopf. „Nein.“""",
)

# S022: one blunt 'Ja' remains where it carries emotional weight; repeated confirmations are collapsed.
apply_replacement(
    P022,
    """„Das ist mein Vater.“\n\n„Ja.“\n\n„Und KORA hat gesagt, er soll den Platz bekommen.“\n\n„Ja.“\n\n„Mit hoher Sicherheit.“\n\nEva spürte den Impuls, sofort zu korrigieren. Sie ließ eine Sekunde vergehen.\n\n„Mit hoher Konfidenz.“""",
    """Laura ließ den Finger auf der Zeile. „Das ist mein Vater. KORA hat gesagt, er soll den Platz bekommen. Mit hoher Sicherheit.“\n\nEva spürte den Impuls, sofort zu korrigieren. Sie ließ eine Sekunde vergehen. „Mit hoher Konfidenz.“""",
)
apply_replacement(
    P022,
    """„Sie haben das gesehen.“\n\n„Ja.“\n\n„Bevor Sie entschieden haben.“\n\n„Ja.“\n\n„Sie wussten, dass das System meinen Vater priorisiert.“\n\n„Ja.“\n\nLaura zog die Hand zurück.""",
    """„Sie haben das gesehen, bevor Sie entschieden haben. Sie wussten, dass das System meinen Vater priorisiert.“\n\n„Ja.“\n\nLaura zog die Hand zurück.""",
)
apply_replacement(
    P022,
    """„Bei Ihrem Patienten kannten Sie das Gesicht.“\n\n„Ja.“\n\n„Sie wussten, wie er atmet.“\n\n„Ja.“\n\n„Sie konnten ihn anfassen.“\n\nEva spürte die Erinnerung an die feuchte Haut unter ihrer Hand, bevor sie antwortete.\n\n„Ja.“""",
    """„Bei Ihrem Patienten kannten Sie das Gesicht. Sie wussten, wie er atmet. Sie konnten ihn anfassen.“\n\nEva spürte die Erinnerung an die feuchte Haut unter ihrer Hand, bevor sie antwortete.\n\n„Ja.“""",
)

# S039: keep the philosophical disagreement, remove alternating yes/no cadence.
apply_replacement(
    P039,
    """„Also beeinflusst die Governance.“\n\n„Natürlich.“\n\n„Dann ist die Freiheit nicht dieselbe wie vorher.“\n\n„Nein. Das habe ich nie behauptet.“\n\n„Institutionell klingt es oft so.“\n\n„Institutionen mögen klare Sätze.“""",
    """„Also beeinflusst die Governance. Dann ist die Freiheit nicht dieselbe wie vorher.“\n\nMiriam nickte. „Natürlich beeinflusst sie. Und nein, die Freiheit ist nicht dieselbe. Das habe ich nie behauptet.“\n\n„Institutionell klingt es oft so.“\n\n„Institutionen mögen klare Sätze.“""",
)
apply_replacement(
    P039,
    """„Und wer entscheidet das?“\n\n„Wir.“\n\n„Das ist keine beruhigende Antwort.“\n\n„Sollte es auch nicht sein.“""",
    """„Und wer entscheidet, ob dieser Einfluss legitim ist?“\n\n„Wir“, sagte Miriam. „Und nein, das ist keine beruhigende Antwort. Sollte es auch nicht sein.“""",
)

for path in (P005, P006, P010, P011, P022, P039):
    mark_status(path)

# Local hard guards for the touched material.
for path in (P005, P006, P010, P011, P022, P039):
    text = path.read_text(encoding="utf-8")
    if "—" in text:
        raise SystemExit(f"em dash hard guard failed in {path}")
    if "sondern" in text.lower().split():
        raise SystemExit(f"forbidden prose token hard guard failed in {path}")

print("Targeted external-dialogue rework applied/verified.")
