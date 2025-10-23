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
| DT-SUP-01 | Middels | Støtte | Utarbeid maler for prosjektkontrakt og koble rubrikker til kommende caseutvidelser. | Malutkast og oppdatert lærerveiledning. | `plan.md` (Støtte), `support/larerveiledning.tex` |
| DT-OPS-02 | Lav | Oppgavestruktur | Definer rutine for månedlig revisjon av oppgavetavle og task queue. | Rutinebeskrivelse og sjekkliste. | `support/oppgavetavle.md` |

## Pågår

*(ingen oppgaver for øyeblikket – oppdater tabellen når nye leveranser starter)*

## Ferdige oppgaver

| ID | Tema | Oppsummering | Leveranser |
| --- | --- | --- | --- |
| DT-09 | Kapittel 9 | FERDIG – Harmoniserte forskningskapitlet med dataspace-trender og oppdatert bibliografi etter fagfelleinnspill. | `chapters/kapittel09-fremtid.tex`, `support/referanser.bib`, `plan.md` |
| DT-08 | Kapittel 8 | FERDIG – Prioriterte pilotcase, etablerte dataspace-tilganger og oppdaterte sektoravsnitt etter fagfellefeedback. | `chapters/kapittel08-case.tex`, `support/notater/pilotundervisning-materiell.md`, `plan.md` |
| DT-07 | Kapittel 7 | FERDIG – Tegnet livssyklusdiagram, utarbeidet intervjuguide og koblet tiltak til pilotlogg. | `chapters/kapittel07-livssyklus.tex`, `plan.md`, `support/notater/pilotundervisning-materiell.md` |
| DT-06 | Kapittel 6 | FERDIG – Integrerte NIS2/IEC 62443-tiltak, oppdatert sjekklister og referanser. | `chapters/kapittel06-validering.tex`, `support/referanser.bib`, `plan.md` |
| DT-05 | Kapittel 5 | FERDIG – Innarbeidet generative og edge-baserte tiltak, utvidet vurderingsmatrise og pilotkrav. | `chapters/kapittel05-ai.tex`, `support/referanser.bib`, `plan.md` |
| DT-OPS-03 | Kvalitetssikring | FERDIG – Automatiserte LaTeX-kompileringstester i pytest slik at manus bygges og feiler ved faktiske kompilasjonsfeil. | `tests/test_latex_referanser.py` |
| DT-04 | Kapittel 4 | FERDIG – Kartlagt figurbehov, opprettet metadata og fagfellepakke for simulering og analyse. | `support/illustrasjonsplan.md`, `support/figurer/metadata/kap04-*.alt.md`, `support/notater/kap04-fagfellepakke.md` |


Se `completed_tasks.md` for hele historikken over ferdige oppgaver.
