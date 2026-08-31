from pathlib import Path
import argparse
import re

TITLES = [
    'Die letzte Kapazität',
    'Der sichtbare Erfolg',
    'Am Morgen danach',
    'Die besseren Zahlen',
    'Die Bettenkette',
    'Was Eva nicht sah',
    'Laura Berg',
    'Ein Grund',
    'Freitext',
    'Neles Entscheidung',
    'Zu spät',
    'Zweite Unterschrift',
    'Schutz oder Gehorsam',
    'Getrennte Daten',
    'Wo KORA irrt',
    'Zu wenig Widerspruch',
    'Der Zeitpunkt',
    'Meine Fälle',
    'Die Bilanz',
    'Die neue Schwelle',
    'Kein Gegenbeleg',
    'Die Chronologie',
    'Würden Sie es wieder tun?',
    'Zwei Wege',
    'Was nicht in den Daten steht',
    'Zu viele Ausnahmen',
    'Nähe zählt nicht',
    'Unter der Schwelle',
    'Zeitstempel',
    'Felix',
    'Drei Risiken',
    'Break Glass',
    'Alles belegt',
    'Beide Patienten',
    'Du siehst ihn nicht',
    'Der Knopf',
    'Vor ihr',
    'Der andere Patient',
    'Human Oversight',
    'Was sieht KORA nicht?',
]

FRONT = (
    '# ABWEICHUNG\n\n'
    '*Wenn die Maschine recht hat*\n\n'
    '> Du darfst widersprechen.  \n'
    '> Die Beweislast liegt bei dir.\n\n'
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', required=True)
    parser.add_argument('--output', default='ABWEICHUNG_FINAL.md')
    args = parser.parse_args()

    src = Path(args.source).read_text(encoding='utf-8')
    if not src.startswith('# ABWEICHUNG\n'):
        raise SystemExit('Unexpected canonical manuscript title')

    body = src[len('# ABWEICHUNG\n'):].lstrip('\n')
    seen = []

    def replace_heading(match: re.Match[str]) -> str:
        number = int(match.group(1))
        if not 1 <= number <= 40:
            raise SystemExit(f'Unexpected chapter number: {number}')
        seen.append(number)
        return f'## Kapitel {number} – {TITLES[number - 1]}'

    body = re.sub(r'^## Kapitel (\d+)$', replace_heading, body, flags=re.M)
    if seen != list(range(1, 41)):
        raise SystemExit(f'Chapter sequence mismatch: {seen}')

    out = Path(args.output)
    out.write_text(FRONT + body, encoding='utf-8')
    print(f'Built {out} ({out.stat().st_size} bytes)')


if __name__ == '__main__':
    main()
