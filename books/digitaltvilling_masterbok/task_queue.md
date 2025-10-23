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
| DT-06 | Middels | Kapittel 6 | Verifiser standardhenvisninger og vurder støttefigurer for kvalitetsprosesser. | Revidert kapittelavsnitt og figurplan. | `plan.md` (Kapittel 6), `support/illustrasjonsplan.md` |
| DT-07 | Høy | Kapittel 7 | Utvikle grafisk livssyklus og planlegg caseintervjuer. | Grafikkutkast og intervjuliste. | `plan.md` (Kapittel 7), `support/illustrasjonsplan.md` |
| DT-08 | Høy | Kapittel 8 | Prioriter hvilke case som skal utdypes, samle kildegrunnlag og skissere visuelle elementer. | Prioritert caseliste og kildeoppsummering. | `plan.md` (Kapittel 8), `support/appendiks-ressurser.tex` |
| DT-09 | Middels | Kapittel 9 | Harmoniser referanser og avklar behov for tabell- eller figurtilegg. | Oppdatert referanseoversikt og leveranseplan. | `plan.md` (Kapittel 9), `support/referanser.bib` |
| DT-SUP-01 | Middels | Støtte | Utarbeid maler for prosjektkontrakt og koble rubrikker til kommende caseutvidelser. | Malutkast og oppdatert lærerveiledning. | `plan.md` (Støtte), `support/larerveiledning.tex` |
| DT-OPS-02 | Lav | Oppgavestruktur | Definer rutine for månedlig revisjon av oppgavetavle og task queue. | Rutinebeskrivelse og sjekkliste. | `support/oppgavetavle.md` |

## Pågår

| ID | Prioritet | Tema | Oppgave | Hovedleveranse | Koblinger |
| --- | --- | --- | --- | --- | --- |
| DT-04 | Høy | Kapittel 4 | Reåpnet – ferdigstille immersivt beslutningsrom og laboratoriepakke for simulering. | Storyboard for `kap04-immersiv-beslutning-v1` og labbeskrivelse. | `support/illustrasjonsplan.md`, `support/notater/kap04-immersiv-case.md` |
| DT-05 | Høy | Kapittel 5 | Reåpnet – utvide analyseeksempel og algoritme-/rubrikkstøtte for AI-lab. | Storyboard for `kap05-operator-coach-v1`, algoritmematrise og rubrikknotat. | `support/illustrasjonsplan.md`, `support/notater/kap05-algoritmematrise-utvidelse.md` |

## Ferdige oppgaver

| ID | Tema | Oppsummering | Leveranser |
| --- | --- | --- | --- |
| DT-OPS-03 | Kvalitetssikring | FERDIG – Automatiserte LaTeX-kompileringstester i pytest slik at manus bygges og feiler ved faktiske kompilasjonsfeil. | `tests/test_latex_referanser.py` |
| DT-04 | Kapittel 4 | FERDIG – Kartlagt figurbehov, opprettet metadata og fagfellepakke for simulering og analyse. | `support/illustrasjonsplan.md`, `support/figurer/metadata/kap04-*.alt.md`, `support/notater/kap04-fagfellepakke.md` |


Se `completed_tasks.md` for hele historikken over ferdige oppgaver.
