# Kapittel 4 – Immersivt beslutningsrom

## Oversikt
Dette notatet beskriver hvordan AR/VR-beslutningsstøtte skal integreres i kapitteltekst, laboratorieaktivitet og figurproduksjon. Målet er å vise hvordan operatører i et norsk kontrollrom kan kombinere simuleringer, sensordata og samarbeidsverktøy for å teste tiltak før de settes i drift.

## Caseoppgave for studenter
- **Bakgrunn:** Fjernvarmesentralen «NordEnergi» ønsker å bruke en immersiv tvilling for å planlegge lastbalansering under kuldeperioder.
- **Oppgave:** Lag en kort «operatørhistorie» (5–7 steg) som viser hvordan teamet bruker AR-briller til å inspisere komponenter, trigge simuleringer og se KPI-er i konteksten.
- **Datagrunnlag:** Bruk datastrømmer for temperatur, trykk og energiflyt fra øvingsdatasettet i kapittel 3. Suppler med scenarioer fra sensitivitetsanalysen i kapittel 4.
- **Leveranser:**
  1. Storyboard med skjermbilder eller skisser av tre visningsflater (primær dashboard, hendelsespanel og samarbeidsnotat).
  2. Kort beslutningslogg som viser hvordan tiltak godkjennes og hvilke KPI-er som overvåkes.
  3. Risikoanalyse for menneske-maskin-samhandling (maks én side) der tiltakene knyttes til kontrolltiltak i Kapittel 6.

## Laboratorieopplegg
1. **Forberedelse (uke 3):** Studenter får en kort video (3 minutter) som viser hvordan AR-panelet er strukturert. De analyserer loggen fra forrige driftsdøgn og definerer tre hypotese-scenarioer som skal testes.
2. **I laben:**
   - Gruppevis gjennomføring på 90 minutter med AnyLogic/Modelica som simuleringsmotor og en delt VR-vegg (CAVE) med strømming av sanntidsdata.
   - Hver gruppe dokumenterer hvilke sensorer som blir «festet» til AR-objekter, og hvordan alarmer vises for ulike aktører.
   - Instruktører sjekker at fallback-prosedyrene (swap til tradisjonelle dashboards) er definert.
3. **Etterarbeid:** Studentene leverer en to-siders refleksjon i læringsplattformen der de beskriver hvordan immersiv visualisering påvirket beslutningene, og foreslår forbedringer.

## Teknisk oppsett
- **Maskinvare:** To HoloLens 2 (eller tilsvarende) for operatørroller, én VR-rigg (HTC Vive Pro 2) koblet til kraftig GPU-stasjon, samt 3×55" veggskjermer for felles visning i kontrollromsmodus.
- **Programvare:** AnyLogic/Modelica for simulering, Kognitwin Live Operations eller Equinor OMNIA som dataplattform, Azure Digital Twins som mellomlagring, samt Teams/OneNote for samtidige notater.
- **Datakilder:** Historiske temperatur- og trykklogger (15 min intervall), sanntidsstrøm fra SCADA (MQTT), syntetisk scenariobank fra sensitivitetstabellen i kapittel 4 og hendelseslogg fra beredskapsøvelsen.
- **Integrasjon:** Data distribueres via en Kafka-broker som håndterer både sanntidsfeeds og «replay» av historikk. Edge-gateway på fjernvarmesentralen tar hånd om første filtrering før datastrømmen går inn i skyplattformen.

## Datastrømmer og roller
| Datastrøm | Formål | Ansvarlig rolle |
| --- | --- | --- |
| Sensorbuffer (historikk + sanntid) | Sikrer at simuleringene kan kalibreres fortløpende og at AR-overlegg har ferske verdier. | Driftstekniker |
| Simuleringsresultat via REST API | Gjør det mulig å «pinne» scenarioutfall i AR-panelet og eksportere til beslutningslogg. | Data scientist |
| Alarm- og hendelseskø | Fordeler varsler til riktige brukerprofiler, og trigges av IEC 62443-tilpasset regelsett. | Beredskapsleder |
| Beslutningslogg (Teams/OneNote) | Dokumenterer tiltak, ansvar og tidspunkter. Eksporteres som vedlegg til evalueringsrubrikken. | Operasjonsleder |

Tabellen brukes som sjekkliste når laben rigges. Hver rolle må signere på at datastrømmen er testet i forkant av økten.

## Sikkerhet og beredskap
- Følg kravene i IEC 62443-2-1 for endringskontroll; simuleringsmodellen og AR-konfigurasjon lagres i Git med tagging per øvelse.
- Loggfør alle tilgangsforespørsler til immersive enheter. Tilgang gis gjennom Azure AD med tidsbegrensede pass.
- Gjennomfør en «tabletop»-øvelse før første lab for å validere varslings- og fallback-prosedyrene sammen med beredskapsleder.
- Etter laben: Eksporter hendelsesloggen til fagteamet for vurdering opp mot DSBs øvelsesveileder og oppdater risikoregisteret i støttefilen for kapittel 6.

## Evalueringsrubrikk (utdrag)
| Kriterium | Beskrivelse | Oppnådd nivå |
| --- | --- | --- |
| Modellforankring | Forklarer hvordan AR/VR-panelet henter data fra simuleringsmodeller og hvilke antakelser som vises til operatørene. | Klart dokumentert, delvis dokumentert, uklart |
| Beslutningsprosess | Viser tydelig hvilke roller som godkjenner tiltak og hvordan beslutningslogg oppdateres. | Tydelig ansvar og sporing, delvis ansvar, mangler ansvar |
| Tilgjengelighet | Beskriver tiltak for universell utforming (kontrast, tekstlesbarhet, alternative innspillingsmodi). | Fullstendig, delvis, utilstrekkelig |
| Risikohåndtering | Vurderer scenarier der AR/VR kan feile og foreslår kompenserende tiltak. | Helhetlig, begrenset, fraværende |

Rubrikken skal legges som vedlegg i læringsplattformen og speile vurderingskriteriene i kapittel 5 og 6.\
Storyboardet for figuren `kap04-immersiv-beslutning-v1` hentes direkte fra aktivitetens hovedscenario.
