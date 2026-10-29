#!/usr/bin/env python3
"""Lädt eine Seite und legt ihren Text im Korpus eines Rechercheprojekts ab.

Aufruf: python3 -I corpus.py <projekt> <kurzname> <url> <art>

  <projekt>   Ordner des Rechercheprojekts; der Korpus liegt in <projekt>/@Corpus/
  <kurzname>  Name der Quelle: Kleinbuchstaben, Ziffern, Bindestriche
  <url>       http- oder https-Adresse der Seite
  <art>       selbst | fremd | anwender
              (Selbstbeschreibung, Fremdbeschreibung, Anwenderstimme)

Ergebnis:
  @Corpus/<kurzname>.txt  Kopf (Titel, URL, Ladedatum, Text) und Text der Seite:
                          der Haupttext aus <main> oder <article>, sonst der
                          ganze Text ohne Skripte, Styles und Navigation
  @Corpus/sources.md      eine neue Zeile je Ladevorgang
  HTML-Datei              in einem eigenen, leeren Ordner im temporären
                          Verzeichnis (TMPDIR), nicht im Projekt

Die Seite wird nur als Text gelesen. Nichts aus ihr wird ausgeführt.
"""

import datetime
import os
import re
import sys
import tempfile
import urllib.request
from html.parser import HTMLParser

ARTEN = {
    "selbst": "Selbstbeschreibung",
    "fremd": "Fremdbeschreibung",
    "anwender": "Anwenderstimme",
}

# Inhalt dieser Elemente gehört nie zum Text
SKIP = {"script", "style", "noscript", "template", "svg", "canvas", "iframe",
        "object", "head"}
# Navigation und Rahmen der Seite
FRAME = {"nav", "header", "footer", "aside", "form"}
# Elemente, nach denen eine neue Zeile beginnt
BLOCK = {"p", "div", "section", "article", "main", "br", "li", "ul", "ol",
         "h1", "h2", "h3", "h4", "h5", "h6", "tr", "table", "blockquote",
         "pre", "dd", "dt", "dl", "figure", "figcaption", "hr"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}

USER_AGENT = "Mozilla/5.0 (compatible; rene-corpus/0.1; +https://github.com/aibex-aios/assistant-rene)"


class TextParser(HTMLParser):
    """Sammelt den Titel, den Text in <main> bzw. <article> und den ganzen Text."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.title = []
        self.main = []
        self.article = []
        self.whole = []

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            if tag in BLOCK:
                self._add("\n")
            return
        self.stack.append(tag)
        if tag in BLOCK:
            self._add("\n")

    def handle_startendtag(self, tag, attrs):
        if tag in BLOCK:
            self._add("\n")

    def handle_endtag(self, tag):
        if tag in VOID or tag not in self.stack:
            return
        while self.stack:
            top = self.stack.pop()
            if top == tag:
                break
        if tag in BLOCK:
            self._add("\n")

    def handle_data(self, data):
        if "title" in self.stack and "svg" not in self.stack:
            self.title.append(data)
            return
        self._add(data)

    def _add(self, text):
        if any(t in SKIP for t in self.stack):
            return
        if any(t in FRAME for t in self.stack):
            return
        self.whole.append(text)
        if "main" in self.stack:
            self.main.append(text)
        if "article" in self.stack:
            self.article.append(text)


def clean(parts):
    text = "".join(parts)
    lines = [re.sub(r"[ \t\r\f\v\xa0]+", " ", line).strip() for line in text.split("\n")]
    out = []
    for line in lines:
        if line or (out and out[-1]):
            out.append(line)
    return "\n".join(out).strip()


def extract(html):
    """Gibt (titel, text, art_des_texts) zurück."""
    parser = TextParser()
    parser.feed(html)
    parser.close()
    title = re.sub(r"\s+", " ", "".join(parser.title)).strip()
    for parts, label in ((parser.main, "Haupttext (<main>)"),
                         (parser.article, "Haupttext (<article>)")):
        text = clean(parts)
        if len(text.split()) >= 50:
            return title, text, label
    return title, clean(parser.whole), "ganzer Text"


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = response.read()
        charset = response.headers.get_content_charset()
    if not charset:
        match = re.search(rb"<meta[^>]+charset=[\"']?([\w-]+)", raw[:4096], re.I)
        charset = match.group(1).decode("ascii") if match else "utf-8"
    try:
        return raw, raw.decode(charset, errors="replace")
    except LookupError:
        return raw, raw.decode("utf-8", errors="replace")


def add_source(corpus, kurzname, url, date, art, label):
    path = os.path.join(corpus, "sources.md")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("# Quellen des Korpus\n\n"
                    "| Kurzname | URL | Ladedatum | Art | Text |\n"
                    "|---|---|---|---|---|\n")
    with open(path, "a", encoding="utf-8") as f:
        f.write(f"| {kurzname} | {url} | {date} | {art} | {label} |\n")


def main(argv):
    if len(argv) != 5:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    projekt, kurzname, url, art = argv[1:]
    if not os.path.isdir(projekt):
        print(f"Fehler: Projekt {projekt} nicht gefunden", file=sys.stderr)
        return 2
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", kurzname):
        print("Fehler: Kurzname nur aus Kleinbuchstaben, Ziffern und Bindestrichen", file=sys.stderr)
        return 2
    if not re.match(r"https?://", url):
        print("Fehler: nur http- und https-Adressen", file=sys.stderr)
        return 2
    if art not in ARTEN:
        print(f"Fehler: Art muss eine von {', '.join(ARTEN)} sein", file=sys.stderr)
        return 2

    try:
        raw, html = fetch(url)
    except Exception as error:  # Netzfehler, HTTP-Fehler, Zeitüberschreitung
        print(f"Fehler beim Laden von {url}: {error}", file=sys.stderr)
        return 1

    html_dir = tempfile.mkdtemp(prefix=f"rene-html-{kurzname}-")
    with open(os.path.join(html_dir, f"{kurzname}.html"), "wb") as f:
        f.write(raw)

    title, text, label = extract(html)
    date = datetime.date.today().isoformat()
    corpus = os.path.join(projekt, "@Corpus")
    os.makedirs(corpus, exist_ok=True)
    target = os.path.join(corpus, f"{kurzname}.txt")
    replaced = os.path.exists(target)
    with open(target, "w", encoding="utf-8") as f:
        f.write(f"Titel: {title}\nURL: {url}\nGeladen: {date}\nText: {label}\n\n{text}\n")
    add_source(corpus, kurzname, url, date, ARTEN[art], label)

    words = len(text.split())
    print(f"{kurzname}: {label}, {words} Wörter -> {target}"
          + (" (ersetzt, neue Zeile in sources.md)" if replaced else ""))
    print(f"HTML: {html_dir}/{kurzname}.html")
    if label == "ganzer Text":
        print("Hinweis: kein <main> oder <article> mit Text gefunden; ganzer Text ohne Skripte, Styles und Navigation genommen")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
