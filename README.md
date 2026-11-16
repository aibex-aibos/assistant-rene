# assistant-rene

Assistent *Rene* von AIbex AIBOS, Version 0.2.0: Spezialist für Recherche. Sein erster Skill `rene-begriff` erfasst, was in der veröffentlichten Welt unter einem neuen Begriff verstanden wird. Jede Antwort beginnt mit „🕵🏻‍♂️ ".

## Holen

**Voraussetzung:** AIbex AIBOS v0.7 ist installiert, und der Vault ist an der Vault-Root mit `aibos --activate v0.7.<n>` gebunden (ein AIBOS-Workspace).

```bash
aibos --fetch assistant-rene
```

Zuordnen mit `/aibos-assistant Rene` im Projekt, in dem recherchiert wird. Rene und sein Skill wirken **ab dem nächsten Chat** in diesem Projekt. Die Recherche startest du mit `/rene-begriff <Begriff>` (Desktop-App) oder mit einem Satz wie „Was bedeutet der Begriff …?"; der Skill ist ein privater Skill von Rene und kein registrierter Befehl.

## Wie Rene arbeitet

Rene erfasst einen Begriff über **zwei Linsen**: die Merkmale, die die Verwender ihm zuschreiben, und das Problem, das das Bezeichnete lösen soll. Sein Skill `/rene-begriff <Begriff>` führt in **11 Schritten** vom Begriff zu einem belegten und gezählten Ergebnis-Memo im Projekt, mit einem Korpus der gelesenen Seiten in `@Corpus/`. Auf Vereinbarung **reflektiert** Rene danach über seine Methode und schreibt Vorschläge nach `@Improve/`; übernommen werden sie erst in einer neuen Version des Pakets.

## Voraussetzungen

Python 3 für die Skripte von `rene-begriff`, nur Standardbibliothek.

## Lizenz

Apache License 2.0 (`LICENSE`), Rechteinhaber AIbex KG (`NOTICE`). Die Marken „AIbex" und „AIbex AIBOS" sind nicht mitlizenziert.
