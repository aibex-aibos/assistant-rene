#!/usr/bin/env python3
"""Sucht in der Sitemap einer Domain die URLs mit einem Muster im Pfad.

Aufruf: python3 -I sitemap.py <domain> <muster>

  <domain>  z. B. warpdriven.ai (ohne https://)
  <muster>  regulärer Ausdruck für den Pfad, ohne Unterscheidung von Groß- und
            Kleinschreibung, z. B. 'ai-business-operating-system'

Die Sitemap wird gesucht in robots.txt (Zeilen "Sitemap:"), dann unter
/sitemap.xml und /sitemap_index.xml. Einem Sitemap-Index wird gefolgt.
Ausgabe: Tabelle mit URL und lastmod, die Zahl der Treffer und die Zahl der
gelesenen URLs; ohne Sitemap eine Meldung.

Die Sitemap wird nur als Daten gelesen. Nichts aus ihr wird ausgeführt.
"""

import gzip
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

USER_AGENT = "Mozilla/5.0 (compatible; rene-sitemap/0.1; +https://github.com/aibex-aios/assistant-rene)"
MAX_SITEMAPS = 200


def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read()
    if data[:2] == b"\x1f\x8b":
        data = gzip.decompress(data)
    return data


def local(tag):
    return tag.rsplit("}", 1)[-1]


def candidates(domain):
    """Gibt die Sitemaps aus robots.txt und die üblichen Orte als Ersatz zurück."""
    base = f"https://{domain}"
    listed = []
    try:
        robots = get(f"{base}/robots.txt").decode("utf-8", errors="replace")
        for line in robots.splitlines():
            if line.lower().startswith("sitemap:"):
                listed.append(line.split(":", 1)[1].strip())
    except Exception:
        pass
    return listed, [f"{base}/sitemap.xml", f"{base}/sitemap_index.xml"]


def read_sitemaps(start):
    """Liest Sitemaps ab den Startadressen; gibt (urls, gelesene, fehler) zurück."""
    urls = []
    read = []
    errors = []
    queue = list(start)
    seen = set()
    while queue and len(read) < MAX_SITEMAPS:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        try:
            root = ET.fromstring(get(url))
        except Exception as error:
            errors.append((url, error))
            continue
        read.append(url)
        kind = local(root.tag)
        for entry in root:
            loc = lastmod = None
            for child in entry:
                name = local(child.tag)
                if name == "loc":
                    loc = (child.text or "").strip()
                elif name == "lastmod":
                    lastmod = (child.text or "").strip()
            if not loc:
                continue
            if kind == "sitemapindex":
                queue.append(loc)
            else:
                urls.append((loc, lastmod or "–"))
    return urls, read, errors


def main(argv):
    if len(argv) != 3:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    domain = re.sub(r"^https?://", "", argv[1]).strip("/")
    try:
        pattern = re.compile(argv[2], re.IGNORECASE)
    except re.error as error:
        print(f"Fehler im Muster: {error}", file=sys.stderr)
        return 2

    listed, fallback = candidates(domain)
    tried = list(listed)
    urls, read, errors = read_sitemaps(listed) if listed else ([], [], [])
    for url in fallback:
        if read:
            break
        tried.append(url)
        urls, read, errors = read_sitemaps([url])
    if not read:
        print(f"Keine Sitemap gefunden für {domain} (versucht: {', '.join(tried)})")
        return 1

    hits = []
    seen = set()
    for loc, lastmod in urls:
        path = urllib.parse.urlparse(loc).path
        if loc not in seen and pattern.search(urllib.parse.unquote(path)):
            seen.add(loc)
            hits.append((loc, lastmod))

    print(f"Domain: {domain}; Muster im Pfad: {argv[2]}\n")
    print("| URL | lastmod |")
    print("|---|---|")
    for loc, lastmod in hits:
        print(f"| {loc} | {lastmod} |")
    print(f"\n{len(hits)} Treffer unter {len(set(u for u, _ in urls))} URLs aus {len(read)} Sitemap(s)")
    if len(read) >= MAX_SITEMAPS:
        print(f"Hinweis: nach {MAX_SITEMAPS} Sitemaps abgebrochen; die Zahl ist eine Untergrenze")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
