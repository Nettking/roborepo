# Metadata for figurer

Denne mappen inneholder alt-tekst og supplerende metadata for figurer i dt-boken. Filene brukes både til universell utforming og for å spore hvilken versjon av figuren som er brukt i kapittelteksen.

## Struktur
- Hver fil navngis `kapXX-tema-vY.alt.md`, i tråd med filnavnene til kilde- og eksportfilene.
- Metadata lagres som YAML-frontmatter etterfulgt av en kort kommentar dersom det er behov.
- Legg filen i samme commit som figuren eller den oppdaterte kapittelteksen.

## Mal

```markdown
---
figur: kap04-analyseflyt-v1
tittel: Analyseflyt for digitale tvillinger
alttekst: >-
  Figuren viser en prosess med fem steg fra datainnsamling via modellering til visualisering,
  og fremhever hvordan beslutningspunkter og feedbacksløyfer er koblet på hvert trinn.
kilde: Kapittel 4, seksjon «Analysemetoder»
forfatter: Nora Aas
dato: 2024-05-10
relaterte_kapitler:
  - 4
  - 5
notater: >-
  Oppdatert etter fagfellekommentar DI-03 for å tydeliggjøre governance-callout.
---
```

### Retningslinjer for innhold
- **Alt-tekst** beskriver hovedbudskapet og viktige grafiske elementer; unngå rene opplistinger av farger og former uten sammenheng.
- **Kilde** viser til kapittel og seksjon eller ekstern referanse som figuren bygger på.
- **Notater** brukes til å peke på fagfellekommentarer eller Jira-saker som førte til oppdateringer.
- Feltet `relaterte_kapitler` brukes når samme figur gjenbrukes flere steder.

Se `../illustrasjonsplan.md` for flere detaljer om arbeidsflyt og kvalitetskriterier.
