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
- LaTeX-kompilering er ikke tilgjengelig i dagens miljø (`latexmk`/`pdflatex` mangler);
  noter behovet før nye kompileringstester planlegges.

## Aktive oppgaver (TODO)

| ID | Prioritet | Tema | Oppgave | Hovedleveranse | Koblinger |
| --- | --- | --- | --- | --- | --- |
| DT-SUP-01 | Middels | Støtte | Utarbeid maler for prosjektkontrakt og koble rubrikker til kommende caseutvidelser. | Malutkast og oppdatert lærerveiledning. | `plan.md` (Støtte), `support/larerveiledning.tex` |
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
| DT-04 | Høy | Kapittel 4 | Reåpnet – ferdigstille immersivt beslutningsrom og laboratoriepakke for simulering. | Storyboard for `kap04-immersiv-beslutning-v1` og labbeskrivelse. | `support/illustrasjonsplan.md`, `support/notater/kap04-immersiv-case.md` | PÅGÅR |
| DT-05 | Høy | Kapittel 5 | Reåpnet – utvide analyseeksempel og algoritme-/rubrikkstøtte for AI-lab. | Storyboard for `kap05-operator-coach-v1`, algoritmematrise og rubrikknotat. | `support/illustrasjonsplan.md`, `support/notater/kap05-algoritmematrise-utvidelse.md` | PÅGÅR |
| DT-12 | Kritisk | Kapittel 3 | Utvide data- og integrasjonskapittelet med dataspace-arkitektur, beredskapsplan og bærekrafts-dashboard. | Revidert kapittelstruktur, nye seksjoner og tilhørende illustrasjonsbestillinger. | `plan.md` (Kapittel 3), `support/illustrasjonsplan.md`, `support/oppgavetavle.md` | PÅGÅR |

## Ferdige oppgaver

| ID | Tema | Oppsummering | Leveranser |
| --- | --- | --- | --- |
| DT-BUG-04 | Kapittel 1–3 | FERDIG – Rettet figurstiene slik at `main.tex` finner TikZ-filene når kapitlene inkluderes, og verifiserte at kompileringstesten går grønt. | `chapters/kapittel01-introduksjon.tex`, `chapters/kapittel02-systemtenkning.tex`, `chapters/kapittel03-data.tex`, `support/figurer/kilder/*`, `plan.md`, `completed_tasks.md` |
| DT-BUG-02 | Kapittel 1–3 | FERDIG – Gjenopprettet kapitteltegningenes TikZ-stier til `../support/figurer/kilder/` slik at figurene kompileres fra kapittelmappene. | `chapters/kapittel01-introduksjon.tex`, `chapters/kapittel02-systemtenkning.tex`, `chapters/kapittel03-data.tex` |
| DT-BUG-01 | Kapittel 1–3 | FERDIG – Rettet TikZ-stier for kapittel 1–3 slik at figurfilene hentes fra `support/figurer/kilder/`. | `chapters/kapittel01-introduksjon.tex`, `chapters/kapittel02-systemtenkning.tex`, `chapters/kapittel03-data.tex`, `support/referanser.bib`, `task_queue.md`, `completed_tasks.md` |
| DT-FIG-01 | Kapittel 1 | FERDIG – Tidslinjefiguren er produsert som to-spors TikZ-grafikk med sektorikoner og legende for fagfellepakke. | `support/figurer/kilder/kap01-tidslinje-v1.tikz`, `plan.md`, `completed_tasks.md` |
| DT-OPS-02 | Oppgavestruktur | FERDIG – Etablerte månedlig revisjonsrutine for tavle og arbeidsliste med sjekkliste og fasetidslinje. | `support/oppgavetavle.md`, `plan.md`, `completed_tasks.md` |
| DT-11 | Kapittel 2 | FERDIG – Utvidet modelleringskapittelet med flerfidelitetscase, metodetabeller og dokumentasjonskrav. | `chapters/kapittel02-systemtenkning.tex`, `plan.md`, `support/referanser.bib` |
| DT-08 | Kapittel 8 | FERDIG – Prioriterte pilotcase, etablerte dataspace-tilganger og oppdaterte sektoravsnitt etter fagfellefeedback. | `chapters/kapittel08-case.tex`, `support/notater/pilotundervisning-materiell.md`, `plan.md` |
| DT-06 | Kapittel 6 | FERDIG – Integrerte NIS2/IEC 62443-tiltak, oppdatert sjekklister og referanser. | `chapters/kapittel06-validering.tex`, `support/referanser.bib`, `plan.md` |
| DT-05 | Kapittel 5 | FERDIG – Innarbeidet generative og edge-baserte tiltak, utvidet vurderingsmatrise og pilotkrav. | `chapters/kapittel05-ai.tex`, `support/referanser.bib`, `plan.md` |
| DT-09 | Kapittel 9 | FERDIG – Harmoniserte forskningskapitlet med generativ AI, edge-native tvillinger, dataspace-regulering og forsknings-KPI-tabell, og oppdaterte bibliografien i både manus og `plan.md`. | `chapters/kapittel09-fremtid.tex`, `support/referanser.bib`, `plan.md` |
| DT-08C | Kapittel 8 | FERDIG – Prioriterte batteriverdikjede-case, oppdaterte KPI-er og dataspace-krav, og la inn støtte-notat. | `chapters/kapittel08-case.tex`, `support/notater/case-batteri.md` |
| DT-08B | Kapittel 8 | FERDIG – Dokumenterte landbrukscase med KPI-tabell, dataspace-implikasjoner og kildeoversikt. | `chapters/kapittel08-case.tex`, `support/notater/case-landbruk.md` |
| DT-08A | Kapittel 8 | FERDIG – Utdypet havvind-caset med KPI-er, dataspace-arkitektur og nye kilder i kapittel og støttefil. | `chapters/kapittel08-case.tex`, `support/notater/case-havvind.md` |
| DT-07 | Kapittel 7 | FERDIG – Tegnet livssyklusdiagram, utarbeidet intervjuguide, koblet tiltak til pilotlogg og la inn RACI-S-variant, gevinstplan samt dataspace-arkitektur i kapittel og appendiks. | `chapters/kapittel07-livssyklus.tex`, `plan.md`, `support/notater/pilotundervisning-materiell.md`, `support/appendiks-ressurser.tex` |
| DT-10 | Kapittel 1--3 | FERDIG – Kartla tomrom i første tre kapitler og utvidet manus med historiske milepæler, politiske rammer, sirkulærøkonomi og nye caser før fagfelleløp. | `chapters/kapittel01-introduksjon.tex`, `chapters/kapittel02-systemtenkning.tex`, `chapters/kapittel03-data.tex`, `plan.md`, `support/referanser.bib`, `support/figurer/metadata/*` |
| DT-APP-10 | Appendiks | FERDIG – Arbeidsark, lærerveiledning og ordliste oppdatert for å støtte fagfelleklarering og prosjektarbeid. | `chapters/appendiks.tex`, `support/larerveiledning.tex`, `support/ordliste.tex`, `plan.md`, `support/fagfellelogg.csv` |
| DT-OPS-03 | Kvalitetssikring | FERDIG – Automatiserte LaTeX-kompileringstester i pytest slik at manus bygges og feiler ved faktiske kompilasjonsfeil. | `tests/test_latex_referanser.py` |
| DT-04 | Kapittel 4 | FERDIG – Kartlagt figurbehov, opprettet metadata og fagfellepakke for simulering og analyse. | `support/illustrasjonsplan.md`, `support/figurer/metadata/kap04-*.alt.md`, `support/notater/kap04-fagfellepakke.md` |


Se `completed_tasks.md` for hele historikken over ferdige oppgaver.
