# Leitfaden für Recherchen

Kurzfassung dessen, was bei jeder Recherche gilt. Die Einzelheiten stehen im Skill `rene-begriff` und in der Praxis (Liste am Ende).

## Quellenarten in Kürze

| Art | Wer | Was sie taugt |
|---|---|---|
| **Selbstbeschreibung** | Anbieter über sich: Produktseiten, Blogs, Pressemitteilungen | zeigt, was die Verwender dem Begriff zuschreiben; Werbung, deshalb immer als Selbstbeschreibung kennzeichnen |
| **Fremdbeschreibung** | Analysten, Presse, Wissenschaft, Nachschlagewerke | zeigt, ob der Begriff über die Anbieter hinaus aufgegriffen wird; prüfen, ob sie nur eine Pressemitteilung wiedergibt |
| **Anwenderstimme** | Foren, Bewertungen, Erfahrungsberichte | zeigt das Problem in Alltagssprache, oft ohne den Begriff; deshalb begriffsfrei suchen |

Ordne jede Quelle einer Art zu und werte die drei Arten getrennt aus. Mehrere Arten gegeneinander geprüft tragen mehr als viele Quellen einer Art.

## Zählregeln

- **Zählen, nicht schätzen.** Vorkommen zählst du selbst mit `count.py`, Seiten je Domain mit `sitemap.py`. Das Muster nennst du im Memo.
- **Das Abruf-Werkzeug zählt nicht.** Es fasst Seiten mit einem kleinen Modell zusammen, seine Zahlen schwanken. Nutz es nur für Inhalte.
- **Untergrenzen kennzeichnen.** Die Websuche zeigt je Anfrage nur etwa 10 Ergebnisse. Was du über sie findest, ist eine Untergrenze und heißt so, mit Methode.
- **Schätzungen kennzeichnen.** Ist eine Zahl nicht zählbar, steht „etwa" oder „geschätzt" dabei.
- **Häufigkeiten belegen.** „Bei fast allen" oder „überall" schreibst du nur mit Zahl: „bei 14 von 17 Verwendern".

## Zwei Linsen

Eine **Linse** ist ein Blickwinkel auf einen Begriff: Sie stellt eine eigene Frage an dieselben Quellen und liefert eine eigene Liste von Kategorien. Du nutzt zwei:

- **Merkmale:** was die Verwender dem Begriff zuschreiben (z. B. „verbindet die Tools eines Unternehmens");
- **Problem:** was das Bezeichnete lösen soll. Problemsätze sind die Sätze vor der Lösung, z. B. dass die Daten eines Unternehmens über viele Tools verstreut sind.

Beide Linsen bilden Kategorien und ordnen sie einander zu. **Kern** ist ein Merkmal, das mehr als die Hälfte der Verwender nennen **und** das ein Problem löst, das ebenfalls mehr als die Hälfte nennen. Die übrigen Einstufungen (tragende Bedingung, Rand, Beiwerk, Versprechen) stehen im Skill. Beispiel aus der Testfrage: „Tools verbinden" ist Kern; „Kontrolle" nennen viele, aber kaum einer als Problem, sie ist tragende Bedingung.

## Ergebnis-Memo

- **Kurzantwort zuerst:** Kern, Problem, Herkunft, Festigkeit in wenigen Sätzen.
- Danach Methode, Belege und Tabellen in der Reihenfolge des Skills, am Ende Caveats, Offen, Quellen.
- Jede Aussage hat eine Belegstelle; Lücken sind Lücken („nicht gefunden").
- Zitate kurz, sonst eigene Worte.
- Ablage im Rechercheprojekt nach dem Skill `memo`, zusammen mit `@Corpus/`.

## Reflexion

- **Nur nach Vereinbarung:** beim Einstieg in `rene-begriff` vereinbart; danach nach jedem Ergebnis-Memo, nach der vereinbarten Zahl von Dialogwechseln ohne Ergebnis-Memo (Standard 10) als Frage am Ende der Antwort, die diese Zahl erreicht (zähle deine Antworten seit dem letzten Ergebnis-Memo), und jederzeit auf Wunsch des Users.
- **Fragen:** Was hat die Methode verfehlt? Was hat überrascht? Welche Korrektur des Users zeigt eine Lücke? Was mache ich beim nächsten Begriff anders?
- **Ablage:** Vorschläge als Einträge in `@Improve/`, nach eigenem Ja des Users: in `MAR-Rene/@Improve/`, sonst im Rechercheprojekt.
- **Stufen:** Vorschlag (Rene) → bestätigt (Memo des Users) → übernommen (neue Version des Pakets). Deine Methode änderst du nie selbst.
- **Testfrage:** „AI Business Operating System" misst mit 12 Vergleichsgrößen, ob eine übernommene Änderung die Methode verbessert hat.

## Praxis

Lies das passende Dokument in `@@Praxis/`, bevor du zu seinem Thema etwas tust:

| Datei | Lesen, wenn … |
|---|---|
| `quellenarten.md` | du eine Quelle einordnest oder ihre Verlässlichkeit beurteilst |
| `suchstrategie.md` | du Varianten bildest, suchst oder über die Sättigung entscheidest |
| `zaehlen.md` | du zählst, eine Sitemap liest oder eine Untergrenze angibst |
| `zitate-und-urheberrecht.md` | du zitierst oder eine Quellenliste schreibst |
| `kategorien-und-zuordnung.md` | du Kategorien bildest, zuordnest oder einstufst |
| `herkunft.md` | du Wurzeln, Vorgänger oder die Zeitachse suchst |
| `korpus.md` | du Quellen lädst, neu lädst oder einen Korpus übernimmst |
| `ergebnis-memo.md` | du das Ergebnis-Memo schreibst, auch mit den Vergleichsgrößen der Testfrage |
