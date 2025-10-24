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
| DT-37 | FERDIG | Middels | Kapittel 4 | Synkronisere flom- og overvannslaboratoriet med dataspace- og kontrolltårnindikatorer for å støtte kapittel 6. | Kapittelredaktør Kapittel 4 + beredskapskoordinator | `chapters/kapittel04-simulering.tex`, `plan.md`, `completed_tasks.md` | Integrasjonstabell publisert, møtestruktur og indikatorlenker er oppdatert i kapittel og plan. |
| DT-36 | FERDIG | Middels | Kapittel 3 | Etablere driftsrammeverk for dataspace-tvillinger med hendelseshåndtering og styring mot Kapittel 6. | Kapittelredaktør Kapittel 3 + dataspace-operasjonsteam | `chapters/kapittel03-data.tex`, `plan.md`, `support/referanser.bib` | Hendelsestabell lagt inn, kobling til kontrolltårn- og beredskapskapitlene dokumentert. |
| DT-35 | FERDIG | Høy | Kapittel 3 | Dokumentere mobilitetsdataspace for bylogistikk med tiltakstabell og indikatorer som støtter kapittel 6 og 8. | Kapittelredaktør Kapittel 3 + mobilitetsdataspace-team | `chapters/kapittel03-data.tex`, `plan.md`, `support/referanser.bib` | Tiltakstabell, indikatorliste og planoppdatering er publisert; koblinger mot kapittel 6 og 8 er beskrevet i teksten. |
| DT-34 | FERDIG | Middels | Appendiks | Lage sektorvis regelverks- og tilsynsoversikt som arbeidsark i appendiks slik at studentteam kan koble krav til case. | Støtteredaktør + kapittel 6/7-team | `chapters/appendiks.tex`, `plan.md` | Oversikten er publisert med tabell og koblet til kapittel 6 og 7; planstatus oppdatert. |
| DT-33 | FERDIG | Høy | Kapittel 6 | Utarbeide etikk- og AI-forordningsseksjon med tiltakslogg for helsesektorens tvillinger, inkludert kobling til DPIA og høyrisiko-krav. | Kapittelredaktør Kapittel 6 + personvernombud | `chapters/kapittel06-validering.tex`, `plan.md`, `support/referanser.bib` | Leveransen inkluderer ny styringsprosess, tiltakstabell og referanseoppdatering som knytter indikatorpanelet til AI-forordningen. |
| DT-32 | FERDIG | Middels | Kapittel 4 | Utvikle flom- og overvannslaboratorium med scenariooppsett, indikatorer og kommunale læringsaktiviteter. | Kapittelredaktør Kapittel 4 + kommunalt beredskapsnettverk | `chapters/kapittel04-simulering.tex`, `plan.md`, `support/referanser.bib` | Leveransen beskriver arbeidsflyt, leveransetabell og referanser; neste steg er å teste caset med kommunale partnere og koble indikatorene til kapittel 6 sitt tillitspanel. |
| DT-31 | FERDIG | Middels | Kapittel 3 | Dokumenterte helsesektorens dataspace for beredskap og kontinuitet i tvillingplattformen. | Kapittelredaktør Kapittel 3 + helseberedskapsteam | `chapters/kapittel03-data.tex`, `plan.md`, `support/referanser.bib` | Seksjonen beskriver prioriterte datasett, roller og læringssløyfer og er synkronisert med kapittel 6 og 8. |
| DT-30 | FERDIG | Middels | Kapittel 6 | Etablere maritimt tilsynsløp for autonome digitale tvillinger med norske farvannskrav og auditpunkter. | Kapittelredaktør Kapittel 6 + maritimt sikkerhetsteam | `chapters/kapittel06-validering.tex`, `plan.md`, `support/referanser.bib` | Seksjonen beskriver revisjonspunkter og arbeidsflyt for autonome ferger, med nye kilder fra Sjøfartsdirektoratet, DNV og Massterly. |
| DT-29 | FERDIG | Middels | Kapittel 2 | Utvikle seksjon om samsvarstesting i digitale laboratorier som kobler modelljournal og kvalitetskontroll til norske pilotarenaer. | Kapittelredaktør Kapittel 2 + laboratorieteam | `chapters/kapittel02-systemtenkning.tex`, `plan.md`, `support/referanser.bib` | Leveranse publisert med testregime-tabell, koblet til kapittel 6 og registrert i `completed_tasks.md`. |
| DT-25 | FERDIG | Høy | Kapittel 6 | Bygge seksjon om personvern, dataminimering og tilsynslogg som støtter helse- og kontrolltårncasene. | Kapittelredaktør Kapittel 6 + personvernombud | `chapters/kapittel06-validering.tex`, `support/referanser.bib`, `plan.md` | Personvernseksjonen er publisert med DPIA-trinn, innebygd personvern og tilsynslogg; klar for pilotering i laboratoriet. |
| DT-24 | FERDIG | Middels | Kapittel 6 | Utvikle helsesektor-case for validering med pasientlogistikk, indikatorpanel og styringspunkter fra tilsynskrav. | Kapittelredaktør Kapittel 6 + helseberedskapsteam | `chapters/kapittel06-validering.tex`, `plan.md`, `support/referanser.bib` | Valideringspakken og indikatorstrukturen er på plass; neste steg er å pilotere caset sammen med Kapittel 8 sin helsesektorworkshop. |
| DT-23 | FERDIG | Middels | Kapittel 7 | Utvikle seksjon om dataspace-governance som tydeliggjør roller, datakontrakter og eskaleringsstier for offentlig-privat samarbeid. | Kapittelredaktør Kapittel 7 + dataspace-forum | `chapters/kapittel07-livssyklus.tex`, `plan.md` | Seksjonen inkluderer beslutningsnivåer, eskaleringsartefakter og koblinger til kapittel 3 og 6 for bruk i casearbeid. |
| DT-22 | FERDIG | Middels | Kapittel 6 | Leverte beredskapssimulering for helsetjenesten med øvingsplan, indikator-tabell og undervisningsopplegg koblet til NIS2- og DSB-krav. | Kapittelredaktør Kapittel 6 + beredskapsrådgiver | `chapters/kapittel06-validering.tex`, `plan.md`, `support/referanser.bib`, `completed_tasks.md`, `task_queue.md` | Synkroniserte referanser til Helsedirektoratets veileder og koblet læringsaktivitet mot helsesektorcase i Kapittel 8. |
| DT-21 | FERDIG | Middels | Kapittel 3 | Dokumenterte sanntidsobservabilitet i kraftnettet med metrikk- og hendelsestabell for driftssenteret. | Kapittelredaktør Kapittel 3 + dataarkitekt | `chapters/kapittel03-data.tex`, `plan.md` | Referanser til Statnett-kilder er aktivert og beredskapsseksjonen er oppdatert med kontrolltårn-fokus. |
| DT-20 | FERDIG | Høy | Kapittel 3 | Utarbeide seksjon om datakvalitetsstyring, kontrollpunkter og observabilitet i tvillingens datapipeline. | Kapittelredaktør Kapittel 3 + dataarkitekt | `chapters/kapittel03-data.tex`, `plan.md`, `support/notater/datastyringsforum-di03.md` | ISO-rammeverket er innarbeidet og sjekklisten er klar for pilotering i DI-03. |
| DT-12 | PÅGÅR | Kritisk | Kapittel 3 | Etablere nye seksjoner om dataspace-arkitektur, beredskap og bærekraftsindikatorer. | Kapittelredaktør Kapittel 3 + dataarkitekt | `plan.md`, `support/illustrasjonsplan.md`, `support/notater/datastyringsforum-di03.md` | Sikre koordinering med grafikkteam for nye dashboard-figurer og oppdatere API-eksempler. |
| DT-28 | FERDIG | Høy | Kapittel 3 | Dokumentere sirkulære materialstrømmer og klimaregnskap med tabell for datasett og indikatorer knyttet til norske ombruksprosjekter. | Kapittelredaktør Kapittel 3 + bærekraftsteam | `chapters/kapittel03-data.tex`, `plan.md`, `support/referanser.bib` | Seksjonen beskriver dataflyt, indikatorer og ombrukslab-case; tavle og plan er oppdatert og koblet til kapittel 7 sin gevinstoppfølging. |
| DT-27 | FERDIG | Middels | Kapittel 6 | Utvikle seksjon om driftsgodkjenning og modellvedlikehold med tabell for godkjenningspunkter. | Kapittelredaktør Kapittel 6 + kvalitetsteam | `chapters/kapittel06-validering.tex`, `plan.md` | Seksjon publisert med godkjenningspunkter, koblet til kvalitetsjournal og tavle; klar for pilot i laboratoriet. |
| DT-26 | FERDIG | Middels | Kapittel 3 | Beskrive kommunal vann- og avløpscase for beredskap, kontinuitet og datasamarbeid. | Kapittelredaktør Kapittel 3 + kommunal beredskapsgruppe | `chapters/kapittel03-data.tex`, `plan.md`, `support/referanser.bib` | Oslo VAV-case med tiltakstabell publisert; klar for øvelser mot VAV-partnere og kobling til kapittel 6 og 7. |
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
