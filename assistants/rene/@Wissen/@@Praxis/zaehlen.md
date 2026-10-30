# Praxis — Zählen

Lies dieses Dokument, wenn du zählst, eine Sitemap liest oder eine Untergrenze angibst (Schritte 3 und 5 von `rene-begriff`). Es wendet die Regel *Zahlen in Memos* auf Web-Recherchen an: Zahlen werden gezählt, nicht geschätzt.

## Was zählbar ist und was nicht

| Größe | Wie | Was es ist |
|---|---|---|
| Vorkommen auf einer Seite | `corpus.py`, dann `count.py` mit genanntem Muster | gezählt |
| Seiten einer Domain mit dem Begriff im Pfad | `sitemap.py` | gezählt, soweit die Sitemap vollständig ist |
| Verwender, Fremdbeschreibungen, Anwenderstimmen | Tabellen des Memos auszählen | gezählt, aber nur unter dem Gefundenen: **Untergrenze** |
| Treffer im ganzen Web | nicht zählbar; die Websuche liefert keine Trefferzahlen | höchstens Untergrenze, sonst „nicht ermittelt" |
| Verbreitung über die Zeit | ohne SEO-Werkzeug nicht zählbar | „nicht ermittelt"; Belege einzeln in der Zeitachse |

Eine Zahl, die weder gezählt noch Untergrenze ist, heißt „etwa" oder „geschätzt" und nennt, worauf sie beruht.

## Muster

- Das Muster nennst du im Memo wörtlich, z. B. `ai[\s-]+business[\s-]+operating[\s-]+systems?`: ohne Groß- und Kleinschreibung, mit Bindestrich und Plural.
- Exakte Phrase und Kurzform zählst du mit getrennten Mustern.
- `count.py` gleicht Leerraum und Zeilenwechsel an, ein Muster findet die Phrase also auch über einen Zeilenumbruch.

## Haupttext und Titel

`corpus.py` legt den **Haupttext** ab: den Text in `<main>` oder `<article>` (ab 50 Wörtern), ohne Navigation, Kopf, Fußzeile, Seitenleisten und Formulare. Gibt es keinen, nimmt es den ganzen Text ohne Skripte, Styles und Navigation und meldet das. `count.py` zählt im Text unter dem Kopf der Datei und weist den **Titel** getrennt aus (ja/nein).

Rohes HTML enthält einen Begriff oft vielfach in Metadaten und Skripten (Softomate: 70-mal im HTML, 15-mal im sichtbaren Text). Gezählt wird deshalb nie im HTML.

**Hilfsbefehle ohne `cd`:** Für einen schnellen Blick auf den Korpus setzt du den Ordner in eine Variable, statt hineinzuwechseln:

```bash
C="<projekt>/@Corpus"; wc -w "$C"/*.txt; grep -l -i "<muster>" "$C"/*.txt
```

Gezählt wird trotzdem mit `count.py`; `grep` und `wc` dienen nur zum Auswählen und Prüfen.

## Das Abruf-Werkzeug zählt nicht

Das Werkzeug zum Abruf einer Seite fasst sie mit einem kleinen Modell zusammen. Seine Zahlen schwanken: In RA, Memo 03, wich es bei 8 von 13 vergleichbaren Seiten um 1 bis 5 von der eigenen Zählung ab. Nutz es nur für Inhalte (Merkmale, Sitz, Definition).

## Zählweisen der Testfrage

Die Durchläufe 2 und 3 (RA, Memos 03, 04) zählten im **ganzen sichtbaren Text mit Titel**, einschließlich Navigation und Fußzeile. `count.py` zählt im **Haupttext ohne Titel**. Auf denselben 15 Seiten ergab das bei der Probe des Pakets (MAR-Rene, Memo 20):

| Zählweise | Summe der 15 Seiten | Beispiel Pharen |
|---|---|---|
| ganzer Text mit Titel (wie RA) | 90 | 5 |
| `count.py`, Haupttext | 67 | 1 |

Die Werte sind deshalb nicht direkt vergleichbar. Nenne beim Vergleich mit früheren Durchläufen die Zählweise, und vergleiche Vorkommen nur innerhalb derselben Zählweise.

## Sitemap

- `sitemap.py <domain> '<muster>'` sucht die Sitemap über `robots.txt`, `/sitemap.xml` und `/sitemap_index.xml` und folgt einem Sitemap-Index.
- Es zählt URLs mit dem Muster **im Pfad**. Eine Seite, die den Begriff nur im Text trägt, findet es nicht; wo es nötig ist, lädst du die Seiten und zählst im Text.
- `lastmod` ist eine Datumsquelle für die Zeitachse (`herkunft.md`).
- Fehlt die Sitemap, bleibt es bei der Suche, und das Memo sagt das. Die Zahl ist dann eine Untergrenze.

Beispiel: Die Sitemap von WarpDriven enthält 9 URLs mit „ai-business-operating-system" im Pfad, die Websuche fand 8.

## Herkunft

Regel *Zahlen in Memos*; MAR-Rene, Memo 01 (*Praxis-Themen*: Zählen), Memo 02 (*Schwächen*: Zahlen ungeprüft), Memo 08 (Skripte), Memo 20 (Probe der Skripte); `@Improve/02`, `@Improve/04`, `@Improve/12`; RA, Memo 03 (*Zählung — eigene Nachprüfung*).
