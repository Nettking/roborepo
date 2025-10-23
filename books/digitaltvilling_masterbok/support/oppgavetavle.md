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
| DT-04 | TODO | Høy | Kapittel 4 | Identifisere supplerende figurer til simuleringseksemplet og forberede fagfellepakke med vurderingsspørsmål. | Kapittelredaktør Kapittel 4 + grafikkteam | `support/illustrasjonsplan.md`, fagfellemal i `support/notater` | Samordne med kapittel 3 slik at dataflyt og simulering beskrives konsistent. |
| DT-05 | TODO | Høy | Kapittel 5 | Samle nye referanser om AI-drevne tvillinger, oppdatere rubrikk i lærerveiledningen og sette opp fagfelleoppsummering. | Kapittelredaktør Kapittel 5 + programleder | `support/larerveiledning.tex`, `support/referanser.bib` | Avklar hvilke norske case som bør refereres for å styrke praksisdelen. |
| DT-06 | TODO | Middels | Kapittel 6 | Kvalitetssikre henvisninger til standarder og metodeverk, og planlegge støttefigurer for valideringsløpet. | Kapittelredaktør Kapittel 6 | `support/illustrasjonsplan.md`, `plan.md` | Koordiner innspill fra juristene som omtales i leseplanen uke 5. |
| DT-07 | TODO | Høy | Kapittel 7 | Lage visualisering av livssyklusmodellen og plan for intervjuer med norske caseeiere. | Kapittelredaktør Kapittel 7 + grafikkteam | `support/illustrasjonsplan.md`, intervjuguide i `support/notater` (må etableres) | Sikre at RACI-eksemplet i kapittelet kobles til visualiseringen. |
| DT-08 | TODO | Høy | Kapittel 8 | Prioritere hvilke bransjecase som skal utdypes og samle kildegrunnlag for hver sektor, inkludert krav til figurer. | Redaksjonen for Kapittel 8 | `support/appendiks-ressurser.tex`, `support/referanser.bib` | Bruk vurderingsmatrisen fra Kapittel 8 for å begrunne utvalget. |
| DT-09 | TODO | Middels | Kapittel 9 | Harmoniser referanser til forskningsfronten og vurder behov for tabeller eller figurer som oppsummerer trendene. | Kapittelredaktør Kapittel 9 | `support/referanser.bib`, `plan.md` | Stem av med fagfelle fra akademia før utsendelse. |
| DT-SUP-01 | TODO | Middels | Støtte | Utarbeide maler for prosjektkontrakt og knytte rubrikker til planlagte caseutvidelser i lærerveiledningen. | Programleder + undervisningsteam | `support/larerveiledning.tex`, eksisterende rubrikker | Malen skal kunne deles med studentgrupper i pilotundervisningen. |
| DT-OPS-02 | TODO | Lav | Oppgavestruktur | Beskrive rutine for månedlig revisjon av oppgavelisten, inkludert sjekkliste for å synkronisere plan, tavle og fagfellelogg. | Redaksjonen | `task_queue.md`, `plan.md`, `support/fagfellelogg.csv` | Foreslå hvem som leder månedlig standup og hvordan endringer varsles. |

## Vedlikeholdssyklus
1. **Oppdater tavlen samtidig som `task_queue.md`.** Når status endres i arbeidslisten,
   juster tabellen over slik at begge filene viser samme status.
2. **Synkroniser med `plan.md` og `fagfellelogg`.** Når en oppgave påvirker progresjon
   eller fagfelleløp, noter endringen i planen eller loggen samme dag.
3. **Bruk notatene aktivt.** Feltet «Notater» skal beskrive hva som er viktig å huske til
   neste innsjekk, for eksempel koordinering med andre kapitler eller behov for beslutninger.
