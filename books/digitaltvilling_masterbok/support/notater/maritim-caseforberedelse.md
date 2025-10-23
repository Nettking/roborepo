# Forarbeid: Maritim caseprioritering

Dette notatet samler forberedende innsikt til utvidelsen av den maritime delen av Kapittel~8 og skal deles med sektorteamet før neste workshop.

> Oppdatert 2024-08-21: Lagt til casebrief for autonome ferger i Trondheimsfjorden basert på datagrunnlaget i tabellen under.

## Formål og scope
- Velge hvilke maritime case som skal løftes frem i kommende revisjon av kapittelet.
- Dokumentere hvilke dataressurser og samarbeidspartnere som er tilgjengelige.
- Koordinere leveranser mot fagfelleplanen (uke 4) og illustrasjonsplanen for kapittelgrafikk.

## Foreslåtte casekandidater
| Case | Beskrivelse | Data- og innsiktskilder | Mulige vinklinger |
| --- | --- | --- | --- |
| Offshore vedlikehold i Nordsjøen | Equinor og Aker BP samarbeider om prediktivt vedlikehold på plattformer med støtte fra Kongsberg Maritime. | Sanntids sensordata (vibrasjon, trykk), logistikkplaner, BarentsWatch- og AIS-feed for forsyningsfartøy, RNNP-rapporter fra Petroleumstilsynet. | Verdikjede for sikkerhet og effektivitet: koble driftssenter, leverandørkjede og regulatoriske rapporteringskrav. |
| Autonome ferger i Trondheimsfjorden | Zeabuz og Trondheim kommune tester autonom passasjerferge. | Navigasjonsdata, sensorstrømmer, Sjøfartsdirektoratets testtilatelser, lokale værdata (MET). | Byutvikling og mobilitet: integrasjon mot kollektivsystem og beredskap. |
| Digital havnlogistikk i Kristiansand | Kristiansand Havn og GCE Node digitaliserer kaioperasjoner med tvilling og automatisering. | Port Community System, losplanlegging, Kystverkets farledsdata, lokale energimålere. | Grønne havner: energiflyt, utslippsreduksjoner og koordinering av aktører. |

## Casebrief: Autonome ferger i Trondheimsfjorden

Denne casebriefen gir sektorteamet et utgangspunkt for å fylle casemalen i Kapittel~8 og koordinere leveranser mot illustrasjons- og fagfelleplanen.

### Beslutningskontekst og mål
- **Pilotarena:** Passasjerfergen ``Milliampere 2`` trafikkerer havnen i Trondheim som del av mobilitetsprogrammet til Trondheim kommune og Trøndelag fylkeskommune.
- **Strategisk hensikt:** Demonstrere hvordan en autonom fergetjeneste kan supplere byens kollektivsystem, redusere utslipp langs havnepromenaden og teste nye mobilitetsløsninger for korte krysninger.
- **Nøkkelbeslutninger:** Valg av operasjonelle scenarier (rutekart, værgrenser), organisering av beredskap (fjernoperatør, redningsressurser) og avklaringer mot Sjøfartsdirektoratets dispensasjoner.

### Datagrunnlag og teknologiplattform
- **Sensorikk:** Lidar, radar, kameraer og GNSS for navigasjon samt IMU for stabilitet. Dataene logges via Kongsberg Seatex-plattformen og tilgjengeliggjøres for analyse i skybasert datasjø.
- **Eksterne kilder:** Sanntids vær- og bølgeprognoser fra MET, AIS- og havneinformasjon via Kystverket samt vannstandsdata fra Kartverket for å planlegge kaioperasjoner.
- **Simulerings- og testmiljø:** Virtuell tvilling bygget på modellbibliotek fra NTNU/SINTEF brukes til å verifisere ruteplaner, avstandsregler og fjernstyringsprosedyrer før endringer tas i drift.
- **Integrasjonskrav:** Hendelser fra fartøyet strømmes til driftssenteret gjennom MQTT, mens historiske logger lastes til analyseplattformen for modelloppdatering og hendelsesanalyse.

### Organisering og governance
- **Roller:** Zeabuz drifter fartøymodulene og kontrollprogramvaren, Trondheim kommune koordinerer tjenesten mot øvrig kollektivtransport, mens NTNU og SINTEF følger opp forskningsspørsmål og sikkerhetstesting.
- **Styringsfora:** Prosjektets endringsråd møtes annenhver uke for å godkjenne oppdateringer i autonominivå, beredskapsplan og datadeling. Hendelser rapporteres inn til både kommunen og Sjøfartsdirektoratet for etterprøving.
- **Datastyring:** Tilgangsstyring følger zero-trust-prinsipper med segmenterte nettverk mellom fartøy, kontrollsenter og analyseplattform. Loggdata versjoneres og merkes med scenario-ID slik at tvillingen kan reproduseres i simulator.

### Gevinster, måleindikatorer og læringspunkter
- **KPI-er:** Punktlighet, energibruk per tur, antall automatiserte dokkingssykluser uten manuell overstyring og responstid ved hendelser.
- **Gevinsthypoteser:** Redusert ventetid for myke trafikanter, lavere driftskostnader sammenlignet med tradisjonell ferge, samt økt kunnskap om autonome systemer for norske havner.
- **Læringspunkter:** Behov for robust vær- og bølgeprediksjon, standardisering av grensesnitt mot landinfrastruktur og tydelig kommunikasjon av beredskapsrutiner til publikum.

### Videre arbeid og koblinger til boken
- Dokumenter case i tråd med casemalen i Kapittel~8 med eksplisitte referanser til datakilder i \autoref{sec:maritimressurser}.
- Planlegg illustrasjon i `support/illustrasjonsplan.md` som viser samspill mellom fartøy, fjernoperatør og byens mobilitetssystem (bruk ikonbiblioteket definert i planen).
- Foreslå øving der studenter analyserer logger fra pilotperioder for å identifisere forbedringer i rutevalg og beredskap; koble til Kapittel~3 (datapipeline) og Kapittel~6 (tillit og sikkerhet).
- Oppdater `support/fagfellelogg.csv` etter hver workshop med status på datatilgang, regulatoriske avklaringer og illustrasjonsleveranser.

## Kritiske datakilder
- Se den nye ressursoversikten i `support/appendiks-ressurser.tex` (seksjonen «Maritime og offshore-ressurser») for lenker til BarentsWatch, skipsregisterdata, dybdemodeller og miljøserier.
- Vurder behov for skjermede datasett (f.eks. detaljerte sensorer fra offshore-operasjoner) og planlegg pseudonymiserte eksempler til undervisningsbruk.
- Koble datakildene til læringsmålene i Kapittel~3 (dataflyt) og Kapittel~6 (tillit og etterlevelse) for å sikre gjenbruk i øvingsopplegg.

## Arbeidsoppgaver før neste sektorworkshop
1. Lag korte casebriefs (maks én side) for kandidatene over med fokus på beslutningssituasjoner, roller og teknisk scope.
2. Kartlegg hvilke illustrasjoner som trengs (f.eks. logistikkflyt for forsyningsfartøy, oversikt over havneoperasjoner) og registrer behovet i `support/illustrasjonsplan.md`.
3. Oppdater `support/fagfellelogg.csv` med eventuelle avklaringer som må innhentes fra industripartnere eller myndigheter.

## Koordinering og oppfølging
- Ingrid Lunde fasiliterer beslutningsmøte i uke 3 for å velge hovedcase og definere tekstleveranser.
- Ahmed Solheim kvalitetssikrer tekniske beskrivelser og avklarer datadeling med plattformteamene.
- Leif Ødegaard sikrer at governance- og gevinstperspektivet knyttes til Kapittel~7, inkludert RACI-tilpasninger.

Notatet oppdateres etter workshop-resultater og refereres i kapittelkommentaren når sektorseksjonen revideres.
