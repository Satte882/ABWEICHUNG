from __future__ import annotations

from pathlib import Path
import re

REPLACEMENTS = {
    "BAUSTEINE/02_KORA_FUNKTIONIERT/SZENEN/02_02_01_MORGENREVIEW/PROSA.md": [
        (
            "Das war der unangenehme Teil des Reviews. Es gab keinen technischen Haken, den sie herausziehen konnte. Keine fehlende Eingabe. Keine verspätete Aktualisierung. KORA hatte die Verschlechterung ihres Patienten gesehen und trotzdem einen anderen Patienten priorisiert.",
            "Es gab keinen technischen Haken, den sie herausziehen konnte. Keine fehlende Eingabe. Keine verspätete Aktualisierung. KORA hatte die Verschlechterung ihres Patienten gesehen und trotzdem einen anderen Patienten priorisiert.",
        ),
        (
            "Das machte den Fall einfacher.\n\nEva bemerkte es nicht als Entlastung. Noch nicht.",
            "Die verbundweite Gegenrechnung fehlte noch. Eva bemerkte diese Begrenzung nicht als Entlastung. Noch nicht.",
        ),
        (
            "Eva sah sie einen Moment an. Das war fast ihr eigener Satz. Vielleicht hatte Nele ihn von ihr.",
            "Eva sah sie einen Moment an. Der Satz klang fast wie einer von ihr. Vielleicht hatte Nele ihn übernommen.",
        ),
        (
            "Das war wichtig. Eva wollte nicht in einer Medizin arbeiten, in der gute Ergebnisse jede Entscheidung heiligten und schlechte Ergebnisse jede Entscheidung rückwirkend falsch machten.",
            "Eva wollte nicht in einer Medizin arbeiten, in der gute Ergebnisse jede Entscheidung heiligten und schlechte Ergebnisse jede Entscheidung rückwirkend falsch machten.",
        ),
        (
            "Die Runde brauchte dafür nur wenige Minuten.\n\nDas war der Normalfall.\n\nEva bemerkte, wie schnell er wieder aus ihrem Kopf verschwand.\n\nDer andere würde bleiben.",
            "Die Runde brauchte dafür nur wenige Minuten. Eva bemerkte, wie schnell dieser gewöhnliche Verlauf wieder aus ihrem Kopf verschwand.\n\nDer andere würde bleiben.",
        ),
    ],
    "BAUSTEINE/04_ERSTE_GOVERNANCE/SZENEN/04_04_02_FREITEXT/PROSA.md": [
        ("Eva nickte. Das war logisch.", "Eva nickte."),
        (
            "Das war der Teil, der Eva störte.\n\nVor dem Freitextfeld hatte eine Abweichung ebenfalls einen Namen getragen.",
            "Vor dem Freitextfeld hatte eine Abweichung ebenfalls einen Namen getragen.",
        ),
        (
            "Das machte schlechte Gründe sichtbarer.\n\nEs machte auch Ärzte vergleichbarer.",
            "Schlechte Gründe wurden damit sichtbarer, Ärzte zugleich vergleichbarer.",
        ),
    ],
    "BAUSTEINE/06_ZWEITFREIGABE_KONFLIKT/SZENEN/06_06_01_ZWEITE_UNTERSCHRIFT/PROSA.md": [
        (
            "Miriam öffnete auf dem Stationsrechner die Testansicht. Kein Foliensatz, keine Kennzahl. Vor ihnen lag Neles alter Fall in einer Trainingskopie, eingefroren am damaligen Entscheidungspunkt.",
            "Miriam öffnete auf dem Stationsrechner die Testansicht. Statt Foliensatz oder Kennzahl lag vor ihnen Neles alter Fall in einer Trainingskopie, eingefroren am damaligen Entscheidungspunkt.",
        ),
        (
            "Der Unterschied war klein genug, um auf einem Bildschirm banal auszusehen.\n\nAuf Station war er es nicht.",
            "Auf dem Bildschirm war nur ein zusätzliches Feld erschienen. Auf Station bedeutete es einen weiteren Arzt zwischen Entscheidung und Handlung.",
        ),
        (
            "Das war kein Reflex gegen Technik. Felix beschrieb den Preis ziemlich genau.",
            "Felix beschrieb den Preis der Regel ziemlich genau.",
        ),
        (
            "Ein einziger zusätzlicher Mensch zwischen Entscheidung und Handlung.\n\nDas war Reibung. Gewollte Reibung.\n\n„Der Pilot darf nicht daran gemessen werden, ob Ärzte KORA öfter folgen“, sagte Eva.",
            "Eva ließ den Status einen Moment stehen.\n\n„Der Pilot darf nicht daran gemessen werden, ob Ärzte KORA öfter folgen“, sagte Eva.",
        ),
        (
            "Eva mochte das nicht.\n\nDas reichte nicht mehr als Gegenargument.",
            "Eva mochte das nicht. Sie ließ die Trainingsansicht trotzdem unverändert und ging zurück auf Station.",
        ),
    ],
    "BAUSTEINE/08_FELIX_VERDACHT/SZENEN/08_08_01_ZU_WENIGE_KONFLIKTE/PROSA.md": [
        (
            "Das war mehr als Trotz.\n\nFelix hatte Angst vor einer Medizin, in der statistische Abweichung selbst zum Verdacht wurde.",
            "Hinter dem Trotz lag echte Angst vor einer Medizin, in der statistische Abweichung selbst zum Verdacht wurde.",
        ),
        (
            "Eva vertraute ihm in diesem Raum. Das machte die Zeile nicht weniger auffällig. Vielleicht war seine Erklärung vollständig.",
            "Eva vertraute ihm in diesem Raum. Die fast leere Zeile blieb trotzdem auffällig. Vielleicht war seine Erklärung vollständig.",
        ),
    ],
    "BAUSTEINE/09_MIDPOINT_EVAS_BILANZ/SZENEN/09_09_01_MEINE_FAELLE/PROSA.md": [
        (
            "Vielleicht war dort nichts Relevantes gewesen. Vielleicht doch. Genau das war die Frage.",
            "Ob dort etwas Relevantes geschehen war, wusste sie nicht.",
        ),
        (
            "Das war das Unangenehme.\n\nSie hatte erwartet, dass ihre Erfahrung gegen eine personenbezogene Statistik verteidigt werden müsste.",
            "Sie hatte erwartet, dass ihre Erfahrung gegen eine personenbezogene Statistik verteidigt werden müsste.",
        ),
    ],
    "BAUSTEINE/10_PERSONENBEZOGENE_GOVERNANCE/SZENEN/10_10_01_SCHWELLE_FUER_EVA/PROSA.md": [
        (
            "Das war genug für den Trainingsplatz.\n\nSie ließ Nele den nächsten Fall übernehmen.",
            "Für den Trainingsplatz ließ Eva es dabei.\n\nSie ließ Nele den nächsten Fall übernehmen.",
        ),
        (
            "Miriam sprach nicht wie jemand, der einen Sieg erklärte. Sie sprach wie jemand, der eine unangenehme Regel so eng wie möglich halten wollte.\n\nDas machte es für Eva schwerer.",
            "Miriam sprach nicht wie jemand, der einen Sieg erklärte. Sie sprach wie jemand, der eine unangenehme Regel so eng wie möglich halten wollte.\n\nGerade diese Sachlichkeit nahm Eva einen bequemen Gegner.",
        ),
        (
            "Kein dramatischer Satz.\n\nKeine Behauptung, Eva sei eine schlechte Ärztin.\n\nKeine automatische Übertragung auf andere Klassen, nachdem Miriam die Ergänzung eingearbeitet hatte.\n\nGerade die Begrenzung machte die Veränderung präzise.",
            "Die Begründung enthielt weder ein Urteil über Evas ärztliche Kompetenz noch eine automatische Übertragung auf andere Klassen; Miriam hatte die Begrenzung ausdrücklich eingearbeitet.\n\nGerade dadurch wurde die Veränderung präzise.",
        ),
        (
            "Nicht um die Regel zu testen. Sie wusste, dass sie funktionierte.\n\nSie wollte sehen, ob der Hinweis noch dieselbe Wirkung hatte, wenn niemand danebenstand.",
            "Sie wusste, dass die Regel funktionierte. Sie wollte nur sehen, ob der Hinweis noch dieselbe Wirkung hatte, wenn niemand danebenstand.",
        ),
    ],
    "BAUSTEINE/10_PERSONENBEZOGENE_GOVERNANCE/SZENEN/10_10_02_KEIN_GEGENBELEG/PROSA.md": [
        (
            "Da war die Regel.\n\nNicht als Eintrag in ihrem Profil. Nicht als abstrakte Verfahrensbeschreibung.\n\nZwischen ihr und einer konkreten Entscheidung.",
            "Die Regel stand jetzt zwischen ihr und einer konkreten Entscheidung, nicht mehr abstrakt in ihrem Profil oder einer Verfahrensbeschreibung.",
        ),
        (
            "Früher hätte ein Satz gereicht.\n\n*Patient klinisch stabiler als Risikobewertung.*\n\nOder:\n\n*Weitere Beobachtung bei engmaschiger Kontrolle vertretbar.*",
            "Früher hätte einer von zwei Sätzen gereicht: *Patient klinisch stabiler als Risikobewertung.* Oder: *Weitere Beobachtung bei engmaschiger Kontrolle vertretbar.*",
        ),
        (
            "Dann hielt sie inne.\n\n*Wirkt.*\n\nSie las das Wort noch einmal.",
            "Beim Wort *wirkt* hielt sie inne und las es noch einmal.",
        ),
        (
            "Wieder stoppte sie.\n\n*Der bisherige Verlauf.*\n\nWelcher Teil?",
            "Beim *bisherigen Verlauf* stoppte sie wieder. Welcher Teil genau?",
        ),
        (
            "Das ärgerte sie.\n\nNicht KORA zwang sie gerade zu etwas.\n\nEin Textfeld zwang sie, einen Impuls in einen überprüfbaren Grund zu verwandeln.",
            "Das ärgerte sie. KORA zwang sie gerade zu nichts; das Textfeld zwang sie, einen Impuls in einen überprüfbaren Grund zu verwandeln.",
        ),
        (
            "Eva stellte sich das Gespräch vor.\n\n*Was ist dein Gegenbeleg?*\n\nSie würde sagen:\n\n*Er sieht besser aus.*\n\nZu wenig.\n\n*Ich halte die Eskalation für verfrüht.*\n\nDas war keine neue Information.\n\n*Meine Erfahrung sagt mir, dass wir noch Zeit haben.*",
            "Eva stellte sich das Gespräch vor. *Was ist dein Gegenbeleg?* Ihre Antworten kamen sofort: *Er sieht besser aus.* Zu wenig. *Ich halte die Eskalation für verfrüht.* Keine neue Information. *Meine Erfahrung sagt mir, dass wir noch Zeit haben.*",
        ),
        (
            "Diesmal suchte sie ausdrücklich nach einem Gegenbeleg.\n\nNicht nach einem Grund, KORA zu mögen oder nicht zu mögen.\n\nNach etwas, das die Empfehlung in diesem konkreten Fall schwächte.",
            "Diesmal suchte sie ausdrücklich nach etwas, das die Empfehlung in diesem konkreten Fall schwächte, nicht nach einem Grund für oder gegen KORA.",
        ),
        (
            "Noch mehr ärgerte sie sich darüber, dass die Regel gerade funktionierte.\n\nNicht weil sie sie zwang, KORA zu folgen.\n\nNoch hatte niemand Nein gesagt.",
            "Noch mehr ärgerte sie sich darüber, dass die Regel gerade funktionierte, ohne sie technisch zu zwingen. Noch hatte niemand Nein gesagt.",
        ),
        (
            "Das Weil hatte nicht gehalten. Eva schloss den Fall. Das fühlte sich wie Machtverlust an. Und wie eine Hilfe.\n\nBeides gleichzeitig war schwerer auszuhalten als ein klares Verbot.",
            "Das Weil hatte nicht gehalten. Eva schloss den Fall. Der Machtverlust fühlte sich zugleich wie Hilfe an, und genau das war schwerer auszuhalten als ein klares Verbot.",
        ),
    ],
    "BAUSTEINE/11_LAURA_KONFRONTATION/SZENEN/11_11_02_WUERDEN_SIE_ES_WIEDER_TUN/PROSA.md": [
        (
            "Das war der Punkt. „Ich weiß es nicht“, sagte Eva.",
            "„Ich weiß es nicht“, sagte Eva.",
        ),
        (
            "Dann ging sie. Eva blieb im Raum zurück. Auf dem Tisch stand Lauras halbvolles Glas.\n\nDie Frage war geblieben.",
            "Dann ging sie. Eva blieb im Raum zurück. Auf dem Tisch stand Lauras halbvolles Glas.",
        ),
    ],
    "BAUSTEINE/12_WERT_KONTEXTAUSNAHME/SZENEN/12_12_02_DER_WERTERAUM/PROSA.md": [
        (
            "Der Patient hatte seine Grenze bereits gesetzt.\n\nNicht an diesem Morgen. Monate vorher.",
            "Der Patient hatte seine Grenze bereits Monate zuvor gesetzt.",
        ),
        (
            "Das war der Teil, den keine Statistik allein lösen konnte. Eine medizinisch bessere Prognose war nicht automatisch die einzige Größe, nach der ein Mensch behandelt werden wollte.",
            "Keine Statistik konnte allein beantworten, nach welchen Zielen dieser Patient behandelt werden wollte. Eine medizinisch bessere Prognose war dafür nicht automatisch die einzige Größe.",
        ),
        (
            "Das war keine Systemtreue. Es war eine präzisere Form von Verantwortung. Miriam speicherte den Entwurf.",
            "Miriam speicherte den Entwurf.",
        ),
    ],
    "BAUSTEINE/14_FELIX_UMGEHUNG/SZENEN/14_14_02_ZEITSTEMPEL/PROSA.md": [
        (
            "Felix. Sie öffnete einen Vergleichsfall. Der Patientenausgang war gut. Beim nächsten ebenfalls kein schwerer dokumentierter Schaden. Das war wichtig.\n\nDer Mechanismus durfte nicht erst durch den schlechten Ausgang des aktuellen Falls problematisch werden.",
            "Felix. Sie öffnete einen Vergleichsfall. Der Patientenausgang war gut. Beim nächsten ebenfalls kein schwerer dokumentierter Schaden.\n\nDer Mechanismus durfte nicht erst durch den schlechten Ausgang des aktuellen Falls problematisch werden.",
        ),
        (
            "Eva ließ die Formulierung stehen. Nicht: Felix hat manipuliert. Nicht: Felix hat den Schaden verursacht.\n\nNur: Die Schutzstufe griff an der faktischen Weiche nicht.",
            "Eva ließ die Formulierung stehen. Sie belegte weder Manipulation noch Schuld am Patientenausgang; sicher war nur, dass die Schutzstufe an der faktischen Weiche nicht gegriffen hatte.",
        ),
        (
            "Auf den Ausdrucken stand alles, was Eva für das Gespräch brauchte.\n\nNicht Felix' Motivation. Nicht die Schuld am Patientenausgang. Nur der Mechanismus. Diesmal war ihr Misstrauen kein Gefühl mehr.",
            "Auf den Ausdrucken stand alles, was Eva für das Gespräch brauchte. Sie belegten den Mechanismus, nicht Felix' Motivation oder die Schuld am Patientenausgang. Diesmal war ihr Misstrauen kein Gefühl mehr.",
        ),
    ],
    "BAUSTEINE/15_ENDGOVERNANCE/SZENEN/15_15_01_DREI_RISIKEN/PROSA.md": [
        (
            "Miriam wartete am zentralen Arbeitsplatz mit zwei Mitgliedern des Vorstands. Kein Konferenzraum. Keine Titelfolie. Hinter ihnen lief die Notaufnahme weiter, als hätte der Beschluss, den sie vorbereiteten, nichts mit ihr zu tun.",
            "Miriam wartete am zentralen Arbeitsplatz mit zwei Mitgliedern des Vorstands. Auf Konferenzraum und Titelfolie hatte sie verzichtet. Hinter ihnen lief die Notaufnahme weiter, als hätte der Beschluss, den sie vorbereiteten, nichts mit ihr zu tun.",
        ),
        (
            "Eva ließ die anonymisierte Spur laufen. Keine automatische Schuldzuweisung. Kein rotes Feld mit *Umgehung erkannt*.\n\nNur eine Zeitfolge, die eine frühere Frage ermöglichte.",
            "Eva ließ die anonymisierte Spur laufen. Es erschien kein rotes Feld mit *Umgehung erkannt*, nur eine Zeitfolge, die eine frühere Frage ermöglichte.",
        ),
        (
            "Eva hörte den Unterschied zu Felix sofort.\n\nDieselbe Oberfläche.\n\nFür Nele war sie Schutz vor dem eigenen Tunnel.\n\nFür Felix war sie eine fremde Hand auf seiner Entscheidung gewesen.",
            "Eva hörte den Unterschied zu Felix sofort. Nele sah in derselben Oberfläche Schutz vor dem eigenen Tunnel; Felix hatte darin eine fremde Hand auf seiner Entscheidung gesehen.",
        ),
        (
            "Kein zweiter Name. Sofortige Wirksamkeit. Persönliche Zuordnung. Automatisches Nachreview.",
            "Der Weg wirkte sofort, blieb Eva persönlich zugeordnet und löste automatisch ein Nachreview aus; ein zweiter Name war dafür nicht nötig.",
        ),
        (
            "Felix hatte eine Schutzstufe verschwinden lassen, weil er ihre Legitimität nicht akzeptierte.\n\nDer Break-glass tat das Gegenteil. Er ließ die Ausnahme ausdrücklich sichtbar werden.\n\nDas war für Eva der entscheidende Unterschied.",
            "Felix hatte eine Schutzstufe verschwinden lassen, weil er ihre Legitimität nicht akzeptierte. Beim Break-glass blieb die Ausnahme sichtbar und wurde Eva persönlich zugerechnet.",
        ),
        (
            "Miriam setzte die finale Freigabe im Dokument. Keine Folie mit **Beschluss**. Nur eine neue Versionsnummer und zwei Unterschriften.",
            "Miriam setzte die finale Freigabe im Dokument. Eine neue Versionsnummer und zwei Unterschriften genügten.",
        ),
        (
            "Sie kannte seine Argumente inzwischen gut genug, um sie selbst mit in die Regel zu schreiben.\n\nDas war kein Ersatz für ihn.",
            "Sie kannte seine Argumente inzwischen gut genug, um sie selbst mit in die Regel zu schreiben.\n\nDer Platz rechts neben Nele blieb trotzdem leer.",
        ),
    ],
    "BAUSTEINE/15_ENDGOVERNANCE/SZENEN/15_15_02_BREAK_GLASS/PROSA.md": [
        (
            "Der Patient auf dem Bildschirm existierte nicht. Das machte die Entscheidung leichter. Nur nicht harmlos.",
            "Der Patient auf dem Bildschirm existierte nicht. Die Entscheidung hatte keine unmittelbaren Folgen, die Logik dahinter schon.",
        ),
        (
            "Dann bestätigte sie. Der Behandlungspfad wechselte sofort. Kein Ladesymbol. Kein weiterer Name. Kein zweiter Dialog. Die Abweichung war wirksam.",
            "Dann bestätigte sie. Ohne Ladesymbol, weiteren Namen oder zweiten Dialog wechselte der Behandlungspfad sofort; die Abweichung war wirksam.",
        ),
        (
            "Kein anonymer Notfallmodus.\n\nKein technisches Schlupfloch, in dem später niemand mehr wusste, dass die Entscheidung allein getroffen worden war.\n\nAuch keine nachträgliche Genehmigung, die so tat, als hätte der zweite Blick vorher stattgefunden.",
            "Der Notfallmodus war nicht anonym. Später würde sichtbar bleiben, dass Eva allein entschieden hatte; eine nachträgliche Genehmigung konnte daraus keinen vorherigen zweiten Blick machen.",
        ),
        (
            "Nicht als moralischen Kommentar.\n\nAls unvermeidbaren Datensatz.",
            "Die Frage würde als unvermeidbarer Datensatz zurückkehren, nicht als moralischer Kommentar.",
        ),
    ],
    "BAUSTEINE/17_FINALE_ENTSCHEIDUNG/SZENEN/17_17_02_DER_KNOPF/PROSA.md": [
        (
            "Die Worte klangen falsch, sobald sie ausgesprochen waren. Es gab keine sichere Sekunde. Das war die Wahrheit. Die andere Wahrheit war, dass Zeitdruck jede Prüfung wie Zögern aussehen ließ.",
            "Die Worte klangen falsch, sobald sie ausgesprochen waren. Es gab keine sichere Sekunde; zugleich ließ Zeitdruck jede Prüfung wie Zögern aussehen.",
        ),
        (
            "Akut. Keine zweite Person verfügbar oder keine Zustimmung. Der Arzt konnte handeln. Sofort.",
            "Für die Akutlage brauchte es keine zweite Person und keine vorherige Zustimmung. Der Arzt konnte sofort handeln.",
        ),
        (
            "Eva hielt inne. Klinische Erfahrung. Höher gewichten. Das war wieder ein Prognosewiderspruch.",
            "Eva hielt inne. Klinische Erfahrung. Höher gewichten. Wieder widersprach sie damit KORAs Prognose.",
        ),
        (
            "Eva schloss die Augen. Der Satz war wahr. Er reichte nicht. Das war der Unterschied.",
            "Eva schloss die Augen. Der Satz war wahr und reichte trotzdem nicht.",
        ),
        (
            "Sie hatte keine Angst vor dem Review. Wenn sie einen tragfähigen Grund gehabt hätte, hätte sie gedrückt und später jeden Satz verteidigt. Die persönliche Markierung war nicht das Hindernis. Die Regel war nicht das Hindernis. Nele war nicht das Hindernis.",
            "Sie hatte keine Angst vor dem Review. Wenn sie einen tragfähigen Grund gehabt hätte, hätte sie gedrückt und später jeden Satz verteidigt. Weder die persönliche Markierung noch die Regel oder Nele hielten sie zurück.",
        ),
        (
            "Niemand hatte ihr die Entscheidung abgenommen. Das machte die Entscheidung nicht leichter. Es machte sie nur vollständig zu ihrer.",
            "Niemand hatte ihr die Entscheidung abgenommen. Sie gehörte vollständig ihr.",
        ),
    ],
}


def main() -> None:
    touched = 0
    changed = 0
    for raw_path, replacements in REPLACEMENTS.items():
        path = Path(raw_path)
        text = path.read_text(encoding="utf-8")
        original = text
        for old, new in replacements:
            count = text.count(old)
            if count != 1:
                raise SystemExit(f"{path}: expected exactly one occurrence, got {count}: {old[:90]!r}")
            text = text.replace(old, new, 1)
            changed += 1
        text = re.sub(r"^prose_status:\s*.*$", "prose_status: final_style_polish", text, count=1, flags=re.M)
        if text != original:
            path.write_text(text, encoding="utf-8")
            touched += 1

    all_prose = "\n".join(
        p.read_text(encoding="utf-8") for p in sorted(Path("BAUSTEINE").glob("*/SZENEN/*/PROSA.md"))
    )
    if "—" in all_prose:
        raise SystemExit("hard guard failed: em dash present")
    if re.search(r"\bsondern\b", all_prose, flags=re.I):
        raise SystemExit("hard guard failed: sondern present")

    print(f"final style polish applied: files={touched}, replacements={changed}")


if __name__ == "__main__":
    main()
