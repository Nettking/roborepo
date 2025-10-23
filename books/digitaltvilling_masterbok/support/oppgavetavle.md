# Oppgavetavle for dt-boken

Denne tavlen utfyller `task_queue.md` med mer kontekst om hver oppgave. Når nye
oppgaver opprettes i arbeidslisten, skal de også beskrives her med samme ID.

## Hvordan lese tavlen
- **Status** følger `TODO`, `PÅGÅR` eller `FERDIG` slik at tavlen speiler
  kanban-strukturen i `task_queue.md`.
- **Prioritet** brukes for å styre rekkefølgen. Vurder høy prioritet når oppgaven
  er tidskritisk for kommende fagfelleløp eller pilotundervisning.
- **Ansvar** viser hvem eller hvilket team som bør følge opp. Roller kan være
  kapittelredaktør, grafikkteam, programleder eller redaksjonen samlet.
- **Avhengigheter** peker på filer eller prosesser som må være på plass før
  oppgaven kan fullføres.

## Prioritert backlog

| ID | Status | Prioritet | Tema | Beskrivelse | Ansvar | Avhengigheter | Notater |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DT-12 | PÅGÅR | Kritisk | Kapittel 3 | Etablere nye seksjoner om dataspace-arkitektur, beredskap og bærekraftsindikatorer. | Kapittelredaktør Kapittel 3 + dataarkitekt | `plan.md`, `support/illustrasjonsplan.md`, `support/notater/datastyringsforum-di03.md` | Sikre koordinering med grafikkteam for nye dashboard-figurer og oppdatere API-eksempler. |
| DT-10 | TODO | Middels | Kapittel 1 | Utvide verdikjedekart, modenhetsanalyse og etiske refleksjoner for norske case. | Kapittelredaktør Kapittel 1 + redaksjonen | `plan.md`, `support/illustrasjonsplan.md`, intervjunotater fra Equinor/Statnett | Krever avklaringer om hvilke case som skal fremheves i hovedfortellingen. |
| DT-11 | TODO | Høy | Kapittel 2 | Bygge ut modelleringskapittelet med flerfidelitetscase, metodetabeller og dokumentasjonseksempler. | Kapittelredaktør Kapittel 2 + modelleringsteam | `plan.md`, `support/illustrasjonsplan.md` | Harmoniser språk og symbolbruk med kapittel 1 og 3 for å sikre røde tråder. |
| DT-13 | TODO | Høy | Kapittel 4 | Integrere AR/VR-baserte beslutningsstøtteeksempler og utvidede simuleringscase. | Kapittelredaktør Kapittel 4 + grafikkteam | `plan.md`, `support/illustrasjonsplan.md`, `support/notater/kap04-fagfellepakke.md` | Planlegg AR/VR-workshop og sikre datagrunnlag til nye figurer. |
| DT-14 | TODO | Høy | Kapittel 5 | Utvide læringssløyfer med generative modeller, edge-implementering og vurderingsrubrikker. | Kapittelredaktør Kapittel 5 + programleder | `plan.md`, `support/larerveiledning.tex`, `support/referanser.bib` | Avklar datasett og pilotpartnere som kan deles i ressursbanken. |
| DT-15 | TODO | Middels | Kapittel 6 | Forsterke standardhenvisninger, usikkerhetsanalyse og kontrolltårn-case. | Kapittelredaktør Kapittel 6 + juridisk rådgiver | `plan.md`, `support/illustrasjonsplan.md` | Krever input fra personvernteamet omtalt i leseplan uke 5. |
| DT-16 | TODO | Høy | Kapittel 7 | Utvikle livssyklusfortellinger, governance-sammenligning og bærekraft-KPI-tabeller. | Kapittelredaktør Kapittel 7 + governance-team | `plan.md`, `support/illustrasjonsplan.md`, kommende intervjuguide | Samordne med caseintervjuplan og KPI-sett fra kapittel 3. |
| DT-17 | TODO | Høy | Kapittel 8 | Fordype klimacaser og bygge casemal-eksempler for undervisning. | Kapittelredaktør Kapittel 8 + sektorteam | `plan.md`, `support/appendiks-ressurser.tex`, `support/illustrasjonsplan.md` | Trenger avtaler om datadeling fra havvind-, landbruks- og batteriprosjekter. |
| DT-18 | TODO | Middels | Kapittel 9 | Oppdatere trendanalysen med roadmap, finansieringskilder og forskningsdesign. | Kapittelredaktør Kapittel 9 + forskningskoordinator | `plan.md`, `support/illustrasjonsplan.md`, `support/referanser.bib` | Koordiner med fagfelle fra akademia og sørg for konsistens med kapittel 5. |
| DT-APP-01 | TODO | Middels | Appendiks – Ressurser | Kategorisere ressursbank og beskrive bruks-case for ulike modenhetsnivå. | Ressursteam + programleder | `plan.md`, `support/appendiks-ressurser.tex` | Avklar med undervisningsteam hvilke lisensbegrensninger som må beskrives. |
| DT-APP-02 | TODO | Lav | Appendiks – Begrepsliste | Berike ordlisten med definisjoner, forkortelser og referanser. | Redaksjonen + terminologiansvarlig | `plan.md`, `support/ordliste.tex` | Trenger koordinering mot nye begrep som innføres i kapittel 3, 5 og 7. |

## Vedlikeholdssyklus
1. **Oppdater tavlen samtidig som `task_queue.md`.** Når status endres i arbeidslisten,
   juster tabellen over slik at begge filene viser samme status.
2. **Synkroniser med `plan.md` og `fagfellelogg`.** Når en oppgave påvirker progresjon
   eller fagfelleløp, noter endringen i planen eller loggen samme dag.
3. **Bruk notatene aktivt.** Feltet «Notater» skal beskrive hva som er viktig å huske til
   neste innsjekk, for eksempel koordinering med andre kapitler eller behov for beslutninger.
