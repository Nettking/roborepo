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
| DT-10 | Middels | Kapittel 1 | Utvide introduksjonskapittelet med verdikjedekart, modenhetsmatrise og etiske refleksjoner for norske case. | Oppdatert kapittelmanus med nye seksjoner og tabeller. | `plan.md` (Kapittel 1), `support/illustrasjonsplan.md` |
| DT-11 | Høy | Kapittel 2 | Bygge ut modelleringskapittelet med flerfidelitetscase, metodetabeller og dokumentasjonskrav. | Revidert tekst + tabeller for modellvalg og kalibrering. | `plan.md` (Kapittel 2), `support/oppgavetavle.md` |
| DT-13 | Høy | Kapittel 4 | Integrere AR/VR-baserte beslutningsstøtteeksempler, nye simuleringscase og vurderingsopplegg. | Utvidet kapittel med casebeskrivelser, storyboard-notater og figurreferanser. | `plan.md` (Kapittel 4), `support/illustrasjonsplan.md` |
| DT-14 | Høy | Kapittel 5 | Legge inn generative/edge-orienterte læringssløyfer, vurderingsrubrikker og nye industrireferanser. | Oppdatert manus med nye delkapitler og rubrikksammendrag. | `plan.md` (Kapittel 5), `support/larerveiledning.tex` |
| DT-15 | Middels | Kapittel 6 | Forsterke innhold om standarder, usikkerhetsanalyser og kontrolltårn-case. | Utvidet kapitteltekst + sjekklister for NIS2/IEC 62443. | `plan.md` (Kapittel 6), `support/illustrasjonsplan.md` |
| DT-16 | Høy | Kapittel 7 | Utvikle livssyklusfortellinger, governance-sammenligning og bærekraft-KPI-tabeller. | Nytt manusutkast med tabeller og caseintervjuplan. | `plan.md` (Kapittel 7), `support/illustrasjonsplan.md` |
| DT-17 | Høy | Kapittel 8 | Fordype sektorspesifikke case (havvind, landbruk, batteri) og bygge casemal-eksempler. | Revidert tekst, casemaler og kildebank. | `plan.md` (Kapittel 8), `support/appendiks-ressurser.tex` |
| DT-18 | Middels | Kapittel 9 | Oppdatere fremtidstrender med roadmap, finansieringskilder og forskningsdesign-eksempler. | Revidert kapittel med roadmap-tekst og tabeller. | `plan.md` (Kapittel 9), `support/illustrasjonsplan.md` |
| DT-APP-01 | Middels | Appendiks – Ressurser | Kategorisere ressursbanken etter modenhetsnivå og beskrive bruks-case. | Utvidet appendiks med kategoriserte tabeller og veiledning. | `plan.md` (Appendiks – Ressurser), `support/appendiks-ressurser.tex` |
| DT-APP-02 | Lav | Appendiks – Begrepsliste | Berike ordlisten med definisjoner, referanser og forkortelser. | Oppdatert ordliste med kildehenvisninger og tematiske grupper. | `plan.md` (Appendiks – Begrepsliste), `support/ordliste.tex` |

## Pågår

| ID | Prioritet | Tema | Oppgave | Hovedleveranse | Koblinger | Status |
| --- | --- | --- | --- | --- | --- | --- |
| DT-12 | Kritisk | Kapittel 3 | Utvide data- og integrasjonskapittelet med dataspace-arkitektur, beredskapsplan og bærekrafts-dashboard. | Revidert kapittelstruktur, nye seksjoner og tilhørende illustrasjonsbestillinger. | `plan.md` (Kapittel 3), `support/illustrasjonsplan.md`, `support/oppgavetavle.md` | PÅGÅR |

## Ferdige oppgaver

| ID | Tema | Oppsummering | Leveranser |
| --- | --- | --- | --- |
| DT-OPS-03 | Kvalitetssikring | FERDIG – Automatiserte LaTeX-kompileringstester i pytest slik at manus bygges og feiler ved faktiske kompilasjonsfeil. | `tests/test_latex_referanser.py` |
| DT-04 | Kapittel 4 | FERDIG – Kartlagt figurbehov, opprettet metadata og fagfellepakke for simulering og analyse. | `support/illustrasjonsplan.md`, `support/figurer/metadata/kap04-*.alt.md`, `support/notater/kap04-fagfellepakke.md` |


Se `completed_tasks.md` for hele historikken over ferdige oppgaver.
