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

## Evalueringsrubrikk (utdrag)
| Kriterium | Beskrivelse | Oppnådd nivå |
| --- | --- | --- |
| Modellforankring | Forklarer hvordan AR/VR-panelet henter data fra simuleringsmodeller og hvilke antakelser som vises til operatørene. | Klart dokumentert, delvis dokumentert, uklart |
| Beslutningsprosess | Viser tydelig hvilke roller som godkjenner tiltak og hvordan beslutningslogg oppdateres. | Tydelig ansvar og sporing, delvis ansvar, mangler ansvar |
| Tilgjengelighet | Beskriver tiltak for universell utforming (kontrast, tekstlesbarhet, alternative innspillingsmodi). | Fullstendig, delvis, utilstrekkelig |
| Risikohåndtering | Vurderer scenarier der AR/VR kan feile og foreslår kompenserende tiltak. | Helhetlig, begrenset, fraværende |

Rubrikken skal legges som vedlegg i læringsplattformen og speile vurderingskriteriene i kapittel 5 og 6.\
Storyboardet for figuren `kap04-immersiv-beslutning-v1` hentes direkte fra aktivitetens hovedscenario.
