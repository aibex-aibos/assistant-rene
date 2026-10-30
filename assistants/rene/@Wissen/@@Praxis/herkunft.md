# Praxis — Herkunft

Lies dieses Dokument, wenn du Wurzeln, Vorgänger oder die Zeitachse suchst (Schritt 8 von `rene-begriff`; die Bestandteile entstehen schon in Schritt 1).

Die Herkunft beantwortet, **was am Begriff neu ist**: das Problem, die Begründung oder nur das Etikett. Dafür gibt es drei Blickwinkel.

## Wurzeln nach Namen

1. In Schritt 1 zerlegst du den Begriff in seine **Bestandteile** und merkst dir die, die selbst Fachbegriffe sind.
2. In Schritt 8 schlägst du für jeden die **etablierte Bedeutung** nach: Wikipedia, Fachlexika, Standardwerke, frühe wissenschaftliche Arbeiten.
3. Du hältst fest, welche Wurzel bei welchen Verwendern überwiegt.

Tabelle *Wurzeln*: Wurzel, älterer Begriff, Herkunft mit Datum, was der Bestandteil dort bedeutet, Verwender, bei denen sie überwiegt.

## Vorgänger nach Zweck

Die Wurzeln findest du über den Namen. Begriffe mit **anderem Namen, aber demselben Zweck** findest du so nicht. Deshalb fragst du nach der Problemfrage (`kategorien-und-zuordnung.md`) für jedes häufige Problem: Welche älteren Begriffe oder Produktkategorien haben schon versprochen, es zu lösen?

Tabelle *Vorgänger*: Problem, älterer Begriff oder Kategorie, seit wann, was er versprach, was der neue Begriff anders begründet.

## Zeitachse

Jede Angabe nennt ihre **Datumsquelle**. Nimm sie in dieser Reihenfolge:

| # | Datumsquelle | Wie |
|---|---|---|
| 1 | Veröffentlichungsdatum in den Metadaten der Seite | `article:published_time`, JSON-LD `datePublished` im HTML der Seite (im Arbeitsordner von `corpus.py`) |
| 2 | `lastmod` aus der Sitemap | `sitemap.py` |
| 3 | Anlagedatum der Domain | RDAP-Abfrage der Domain |
| 4 | Datum von Repos und Paketen | GitHub-API (`created_at`), Paketregister |
| 5 | Wayback Machine | erste archivierte Fassung; Vorkommen in alten Fassungen |

Für Datumsquelle 1 suchst du in den HTML-Dateien, deren Ordner `corpus.py` meldet, mit absoluten Pfaden, ohne `cd`:

```bash
for f in <tmp>/rene-html-*/*.html; do echo "$f"; grep -o -E '"datePublished" *: *"[^"]+"|article:published_time" content="[^"]+"' "$f" | head -2; done
```

Ein Datum aus einem Suchergebnis ist die schwächste Quelle und heißt so („laut Suchergebnis"). Der früheste Beleg ist nur der früheste **gefundene**: Sag, dass ältere Belege nicht ausgeschlossen sind.

## Was neu ist

Am Ende steht ein Satz: Ist das **Problem** neu, die **Begründung** (z. B. KI macht ein altes Versprechen einlösbar) oder nur das **Etikett**? Er stützt sich auf Wurzeln, Vorgänger und Zeitachse.

## Beispiel aus der Testfrage

- **Wurzeln** (RA, Memo 03): der Management-Begriff „Business Operating System" (Toyota Production System 1948–1975, Danaher, EOS) und die Computer-Metapher „AI Operating System" (arXiv 2312.03815, Dezember 2023). Gefunden eher zufällig über einen Wikipedia-Artikel; in Memo 01 und 02 fehlten sie.
- **Vorgänger nach Zweck** (RA, Memo 04): Die Zersplitterung von Werkzeugen und Daten wollten schon ERP und Integrationsplattformen lösen. Weder „ERP" noch „Integration" steckt im Namen.
- **Zeitachse** (RA, Memo 03): Für 10 von 12 geprüften Seiten hatte die Wayback Machine keine Fassung. Der früheste datierte Beleg der exakten Phrase stammte aus dem März 2026, und das nur laut Suchergebnis.

## Herkunft

MAR-Rene, Memo 02 (*Schwächen*: nur eine Momentaufnahme), Memo 07 (Schritte 1 und 8); `@Improve/01`, `@Improve/05`, `@Improve/09`; RA, Memo 03 (*Zwei Wurzeln*, *Zeitachse*), Memo 04 (*Problem der Wurzeln und Nachbarn*).
