#!/usr/bin/env python3
"""Zählt die Vorkommen eines Musters in Dateien des Korpus.

Aufruf: python3 -I count.py <muster> <datei>...

  <muster>  regulärer Ausdruck, ohne Unterscheidung von Groß- und Kleinschreibung,
            z. B. 'ai[\\s-]+business[\\s-]+operating[\\s-]+systems?'
  <datei>   Textdateien aus @Corpus/ (von corpus.py); bei Dateien ohne Kopf
            zählt der ganze Inhalt als Text

Ausgabe: Tabelle mit den Vorkommen im Text und ob das Muster im Titel steht,
je Datei, dazu die Summe. Leerraum und Zeilenwechsel gelten als ein Leerzeichen,
damit ein Muster auch über einen Zeilenwechsel hinweg gefunden wird.
"""

import os
import re
import sys

HEADER_KEYS = ("Titel", "URL", "Geladen", "Text")


def read(path):
    """Gibt (titel, text) zurück; titel ist None, wenn die Datei keinen Kopf hat."""
    with open(path, encoding="utf-8", errors="replace") as f:
        content = f.read()
    head, sep, body = content.partition("\n\n")
    lines = head.split("\n")
    if sep and lines and all(line.split(":", 1)[0] in HEADER_KEYS for line in lines):
        title = next((line.split(":", 1)[1].strip() for line in lines
                      if line.startswith("Titel:")), "")
        return title, body
    return None, content


def main(argv):
    if len(argv) < 3:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    try:
        pattern = re.compile(argv[1], re.IGNORECASE)
    except re.error as error:
        print(f"Fehler im Muster: {error}", file=sys.stderr)
        return 2

    print(f"Muster: {argv[1]} (ohne Groß- und Kleinschreibung)\n")
    print("| Datei | Text | im Titel |")
    print("|---|---|---|")
    total = 0
    in_title = 0
    for path in argv[2:]:
        if not os.path.isfile(path):
            print(f"| {path} | nicht gefunden | – |")
            continue
        title, text = read(path)
        n = len(pattern.findall(re.sub(r"\s+", " ", text)))
        total += n
        if title is None:
            title_mark = "–"
        elif pattern.search(title):
            title_mark = "ja"
            in_title += 1
        else:
            title_mark = "nein"
        print(f"| {os.path.basename(path)} | {n} | {title_mark} |")
    print(f"| **Summe** | **{total}** | {in_title} mit Muster im Titel |")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
