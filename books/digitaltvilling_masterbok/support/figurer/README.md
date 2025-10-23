# Mappe for figurer til dt-boken

> Notat (2024-05-08): Opprettet struktur for kildesfiler og eksporterte figurer i forbindelse med illustrasjonsplanen.

Denne mappen organiserer arbeid med grafikk slik at alle figurer kan versjonskontrolleres.

- `kilder/` skal inneholde redigerbare originalfiler (for eksempel `.tikz`, `.svg`, `.afdesign`, `.drawio`).
- `eksport/` skal inneholde PDF/PNG/SVG-filer som brukes direkte i LaTeX-dokumentene.
- `metadata/` lagrer alt-tekst og figurinformasjon i tråd med malen beskrevet i `../illustrasjonsplan.md`.

Navngiv figurene etter mønsteret `kapXX-tema-versjon.ext`, der `versjon` oppdateres når layout eller innhold endres. Husk å legge ved kildefil hver gang en eksport oppdateres.

Lag tilhørende metadatafil `metadata/kapXX-tema-versjon.alt.md` når figuren er klar for fagfellelesing eller publisering. Referer til filen i kapittelteksen med en LaTeX-kommentar.
