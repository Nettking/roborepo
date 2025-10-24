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
| DT-21 | FERDIG | Middels | Kapittel 3 | Dokumenterte sanntidsobservabilitet i kraftnettet med metrikk- og hendelsestabell for driftssenteret. | Kapittelredaktør Kapittel 3 + dataarkitekt | `chapters/kapittel03-data.tex`, `plan.md` | Referanser til Statnett-kilder er aktivert og beredskapsseksjonen er oppdatert med kontrolltårn-fokus. |
| DT-20 | FERDIG | Høy | Kapittel 3 | Utarbeide seksjon om datakvalitetsstyring, kontrollpunkter og observabilitet i tvillingens datapipeline. | Kapittelredaktør Kapittel 3 + dataarkitekt | `chapters/kapittel03-data.tex`, `plan.md`, `support/notater/datastyringsforum-di03.md` | ISO-rammeverket er innarbeidet og sjekklisten er klar for pilotering i DI-03. |
| DT-12 | PÅGÅR | Kritisk | Kapittel 3 | Etablere nye seksjoner om dataspace-arkitektur, beredskap og bærekraftsindikatorer. | Kapittelredaktør Kapittel 3 + dataarkitekt | `plan.md`, `support/illustrasjonsplan.md`, `support/notater/datastyringsforum-di03.md` | Sikre koordinering med grafikkteam for nye dashboard-figurer og oppdatere API-eksempler. |
| DT-OPS-02 | FERDIG | Lav | Oppgavestruktur | Definere og teste månedlig revisjonsritual for task queue og oppgavetavle. | Redaksjonen + programleder | `task_queue.md`, `plan.md`, `support/oppgavetavle.md` | Rutine og sjekkliste publisert; evaluering loggføres etter første måned. |
| DT-SUP-01 | FERDIG | Middels | Støtte | Utarbeid maler for prosjektkontrakt og koble rubrikker til kommende caseutvidelser. | Programleder + kapittelredaktører Kapittel 4 og 8 | `plan.md`, `support/larerveiledning.tex` | Prosjektkontraktmal publisert og lærerveiledning/plan oppdatert med rubrikkkoblinger. |
| DT-10 | FERDIG | Middels | Kapittel 1 | Utvide verdikjedekart, modenhetsanalyse og etiske refleksjoner for norske case. | Kapittelredaktør Kapittel 1 + redaksjonen | `plan.md`, `support/illustrasjonsplan.md`, intervjunotater fra Equinor/Statnett | Tabell med verdikjedeledd, modenhetsmodell og etikkrammeverk publisert i kapittel og plan/statusfiler oppdatert. |
| DT-11 | FERDIG | Høy | Kapittel 2 | Bygge ut modelleringskapittelet med flerfidelitetscase, metodetabeller og dokumentasjonseksempler. | Kapittelredaktør Kapittel 2 + modelleringsteam | `plan.md`, `support/illustrasjonsplan.md` | Metodebibliotek, offshore-case og modelljournal-tabell publisert; klar for pilotering mot industripartnere. |
| DT-13 | FERDIG | Høy | Kapittel 4 | Integrere AR/VR-baserte beslutningsstøtteeksempler og utvidede simuleringscase. | Kapittelredaktør Kapittel 4 + grafikkteam | `plan.md`, `support/illustrasjonsplan.md`, `support/notater/kap04-fagfellepakke.md` | Kapittelet beskriver implementeringsløp, Statnett-case og scenariotabell for immersive kontrollrom. |
| DT-14 | FERDIG | Høy | Kapittel 5 | Utvide læringssløyfer med generative modeller, edge-implementering og vurderingsrubrikker. | Kapittelredaktør Kapittel 5 + programleder | `plan.md`, `support/larerveiledning.tex`, `support/referanser.bib` | Leveransen beskriver styringsramme for generativ dataflyt, ny kontrolltabell og oppdaterte plan-/statusfiler for kapittelet. |
| DT-15 | FERDIG | Middels | Kapittel 6 | Forsterke standardhenvisninger, usikkerhetsanalyse og kontrolltårn-case. | Kapittelredaktør Kapittel 6 + juridisk rådgiver | `plan.md`, `support/illustrasjonsplan.md` | Sertifiseringsløp og kvalitetsjournal er innarbeidet i kapittel og statusfiler oppdatert. |
| DT-19 | FERDIG | Middels | Kapittel 6 | Utvikle tillitsindikatorer, styringspanel og rapporteringsmal for kapittel 6. | Kapittelredaktør Kapittel 6 + kvalitetsteam | `chapters/kapittel06-validering.tex`, `plan.md`, `support/referanser.bib` | Tillitspanelet og indikatorene er publisert i kapittel 6 og synkronisert med plan- og statusfiler. |
| DT-16 | FERDIG | Høy | Kapittel 7 | Utvikle livssyklusfortellinger, governance-sammenligning og bærekraft-KPI-tabeller. | Kapittelredaktør Kapittel 7 + governance-team | `plan.md`, `support/illustrasjonsplan.md`, kommende intervjuguide | Livssyklusfortellingene har fått styringspunkttabell, hybrid styringssløyfer og modenhetssteg for bærekraft. |
| DT-17 | FERDIG | Høy | Kapittel 8 | Fordype klimacaser og bygge casemal-eksempler for undervisning. | Kapittelredaktør Kapittel 8 + sektorteam | `plan.md`, `support/appendiks-ressurser.tex`, `support/illustrasjonsplan.md` | Leveranseplan for klimacaser, workshopopplegg og felles milepæltabell publisert i kapittel og statusfiler. |
| DT-18 | FERDIG | Middels | Kapittel 9 | Oppdatere trendanalysen med roadmap, finansieringskilder og forskningsdesign. | Kapittelredaktør Kapittel 9 + forskningskoordinator | `plan.md`, `support/illustrasjonsplan.md`, `support/referanser.bib` | Veikartveiledning, finansieringstabell og milepælsoversikt er oppdatert; avtal fagfellegjennomgang for å validere krav og referanser. |
| DT-APP-01 | FERDIG | Middels | Appendiks – Ressurser | Kategorisere ressursbank og beskrive bruks-case for ulike modenhetsnivå. | Ressursteam + programleder | `plan.md`, `support/appendiks-ressurser.tex` | Ressursbanken har fått modenhetspakker og lisensoversikt for undervisningsteamet. |
| DT-APP-02 | FERDIG | Lav | Appendiks – Begrepsliste | Oppdatert ordlisten med dataspace-roller, modellverktøy og sikkerhets- og beredskapsbegrep. | Redaksjonen + terminologiansvarlig | `plan.md`, `support/ordliste.tex` | Ny sikkerhetsseksjon og observabilitetsbegrep lagt inn; avklarer videre innspill med kapittel 3, 5 og 6. |

## Vedlikeholdssyklus
1. **Oppdater tavlen samtidig som `task_queue.md`.** Når status endres i arbeidslisten,
   juster tabellen over slik at begge filene viser samme status.
2. **Synkroniser med `plan.md` og `fagfellelogg`.** Når en oppgave påvirker progresjon
   eller fagfelleløp, noter endringen i planen eller loggen samme dag.
3. **Bruk notatene aktivt.** Feltet «Notater» skal beskrive hva som er viktig å huske til
   neste innsjekk, for eksempel koordinering med andre kapitler eller behov for beslutninger.

## Månedlig revisjonsrutine
For å sikre at arbeidsstrømmen er oppdatert før hver fagfelle- og pilotrunde gjennomføres
en fast revisjon den første hele uken i hver måned. Programleder kaller inn redaksjonen til
et 45-minutters tavlemøte hvor beslutninger fattes og oppfølgingspunkter loggføres.

### Fasetidslinje
1. **Dag 1 – Forberedelse:** Gjennomgå endringslogg i `git` og siste kommentarer i
   `support/fagfellelogg.csv`. Marker kandidater for nye oppgaver eller oppdateringer.
2. **Dag 2 – Datavask:** Sammenlign `task_queue.md` og denne tavlen, fjern duplikater og
   noter uavklarte eiere. Oppdater `plan.md` med statusendringer som påvirker fremdrifts-
   eller leseplanen.
3. **Dag 3 – Beslutning:** Hold tavlemøte for å fastsette prioriteringer, avklare
   avhengigheter og tildele ansvar. Registrer eventuelle figurbestillinger i
   `support/illustrasjonsplan.md`.
4. **Dag 4 – Publisering:** Send kort sammendrag til fagfelle- og pilotteam, oppdater
   `completed_tasks.md` ved behov og forbered eventuelle kommunikasjonsinnlegg.

### Sjekkliste for månedsoppfølging
- [ ] Datohjul oppdatert i kalenderen til programleder og kapittelredaktører.
- [ ] Statusfelt i `task_queue.md` og `support/oppgavetavle.md` samsvarer.
- [ ] `plan.md` inneholder oppdatert «Neste steg» for kapitler som har fått nye tiltak.
- [ ] Nye eller endrede oppgaver har tydelig ansvarlig og koblinger til relevante støttefiler.
- [ ] Eventuelle kildebehov eller referanser lagt til i `support/referanser.bib`.
