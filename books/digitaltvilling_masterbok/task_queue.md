# Arbeidsliste for dt-boken

Arbeidslisten er omstrukturert til en lett kanban-tavle med identifiserbare oppgavekort.
Bruk tabellen under for å se hvilke leveranser som står for tur, og slå opp i
`support/oppgavetavle.md` for detaljerte beskrivelser.

## Bruksnotater
- Oppgaver får en kort ID (for eksempel `DT-07`) slik at diskusjoner og commiter kan
  peke på samme leveranse.
- Alle nye oppgaver legges inn i tabellen under som `TODO` og flyttes til seksjonen
  «Pågår» ved å endre status til `PÅGÅR` før arbeidet starter.
- Når oppgaven er ferdig, flytt raden til «Ferdige oppgaver» og dokumenter resultatet
  i de berørte filene samt i `completed_tasks.md`.

## Aktive oppgaver (TODO)

| ID | Prioritet | Tema | Oppgave | Hovedleveranse | Koblinger |
| --- | --- | --- | --- | --- | --- |
| DT-05 | Høy | Kapittel 5 | Samle tilleggsreferanser, koble vurderingsrubrikk og forberede fagfelleløp. | Oppdatert kildebank og rubrikknotat. | `plan.md` (Kapittel 5), `support/larerveiledning.tex` |
| DT-06 | Middels | Kapittel 6 | Verifiser standardhenvisninger og vurder støttefigurer for kvalitetsprosesser. | Revidert kapittelavsnitt og figurplan. | `plan.md` (Kapittel 6), `support/illustrasjonsplan.md` |
| DT-09 | Middels | Kapittel 9 | Harmoniser referanser og avklar behov for tabell- eller figurtilegg. | Oppdatert referanseoversikt og leveranseplan. | `plan.md` (Kapittel 9), `support/referanser.bib` |
| DT-SUP-01 | Middels | Støtte | Utarbeid maler for prosjektkontrakt og koble rubrikker til kommende caseutvidelser. | Malutkast og oppdatert lærerveiledning. | `plan.md` (Støtte), `support/larerveiledning.tex` |
| DT-OPS-02 | Lav | Oppgavestruktur | Definer rutine for månedlig revisjon av oppgavetavle og task queue. | Rutinebeskrivelse og sjekkliste. | `support/oppgavetavle.md` |

## Pågår

*(ingen oppgaver for øyeblikket – endre status til `PÅGÅR` i tabellen over når arbeid starter)*

## Ferdige oppgaver

| ID | Tema | Oppsummering | Leveranser |
| --- | --- | --- | --- |
| DT-09 | Kapittel 9 | FERDIG – Harmoniserte forskningskapitlet med generativ AI, edge-native tvillinger, dataspace-regulering og forsknings-KPI-tabell. | `chapters/kapittel09-fremtid.tex`, `support/referanser.bib` |
| DT-08C | Kapittel 8 | FERDIG – Prioriterte batteriverdikjede-case, oppdaterte KPI-er og dataspace-krav, og la inn støtte-notat. | `chapters/kapittel08-case.tex`, `support/notater/case-batteri.md` |
| DT-08B | Kapittel 8 | FERDIG – Dokumenterte landbrukscase med KPI-tabell, dataspace-implikasjoner og kildeoversikt. | `chapters/kapittel08-case.tex`, `support/notater/case-landbruk.md` |
| DT-08A | Kapittel 8 | FERDIG – Utdypet havvind-caset med KPI-er, dataspace-arkitektur og nye kilder i kapittel og støttefil. | `chapters/kapittel08-case.tex`, `support/notater/case-havvind.md` |
| DT-07 | Kapittel 7 | FERDIG – La inn RACI-S-variant, gevinstplan og dataspace-arkitektur i kapittel og appendiks. | `chapters/kapittel07-livssyklus.tex`, `support/appendiks-ressurser.tex` |
| DT-OPS-03 | Kvalitetssikring | FERDIG – Automatiserte LaTeX-kompileringstester i pytest slik at manus bygges og feiler ved faktiske kompilasjonsfeil. | `tests/test_latex_referanser.py` |
| DT-04 | Kapittel 4 | FERDIG – Kartlagt figurbehov, opprettet metadata og fagfellepakke for simulering og analyse. | `support/illustrasjonsplan.md`, `support/figurer/metadata/kap04-*.alt.md`, `support/notater/kap04-fagfellepakke.md` |


Se `completed_tasks.md` for hele historikken over ferdige oppgaver.
