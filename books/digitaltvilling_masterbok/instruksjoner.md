# Instruksjoner for arbeid med «Digitale tvillinger i praksis for masterstudenter»

Denne filen beskriver hvordan neste oppgave skal velges og hvordan bidrag organiseres.

## Arbeidsflyt

1. **Åpne `task_queue.md`.** Oppgavene er listet i prioritert rekkefølge. Hver oppgave har en status (`TODO`, `PÅGÅR`, `FERDIG`).
2. **Finn første oppgave merket `TODO`.** Dette er «neste oppgave». Når du som bidragsyter blir bedt om å "ta neste oppgave på dt-boken", skal du velge denne.
3. **Oppdater status til `PÅGÅR`** før du starter arbeidet, slik at andre ser at oppgaven er under arbeid.
4. **Utfør oppgaven** ved å redigere de relevante filene i denne mappen (eller underordnede mapper).
5. **Dokumenter resultatet.**
   - Legg til korte notater i kapittel- eller støttefilen du har endret (for eksempel et sammendrag av hva som ble lagt til).
   - Oppdater eventuelle referanser i `plan.md` hvis strukturen eller progresjonen endres.
6. **Marker oppgaven som `FERDIG`.** Flytt ferdige oppgaver til seksjonen «Ferdige oppgaver» nederst i `task_queue.md` for historikk.
7. **Legg til nye oppgaver ved behov.** Når du identifiserer oppfølgingselementer, opprett nye `TODO`-oppgaver under «Aktive oppgaver».

## Stil og formatering

- Bruk norsk bokmål.
- Kapittelfiler og frontmatter skrives i LaTeX (`.tex`) og inkluderes via `main.tex`.
- Strukturér kapitler med `\chapter{...}`, `\section{...}` og `\subsection{...}`. Bruk `\begin{itemize}`/`\begin{enumerate}` for lister og `\begin{tabular}` for tabeller.
- Hvert kapittel bør inneholde læringsmål, hovedinnhold og forslag til øvingsoppgaver eller refleksjonsspørsmål.
- Kontroller at nye pakker eller kommandoer er kompatible med den eksisterende LaTeX-oppsettet i `main.tex`.
- Ikke legg inn datostemplede «Notat»-/«Oppdatert»-kommentarer i LaTeX- eller Markdown-filer. Historikk håndteres gjennom Git og `task_queue.md`; dokumenter endringer direkte i teksten eller i strukturerte logger uten dato-kommentarer.

## Siteringspraksis og referansehåndtering

- Alle kilder skal registreres i BibTeX-filen `support/referanser.bib`. Bruk beskrivende nøkler (for eksempel `forfatterÅrTema`).
- Sett inn kilder i teksten med `\citet{}` når forfatteren skal være en del av setningen og `\citep{}` for parentesreferanser. Begge kommandoene støttes av `natbib`-oppsettet som er aktivert i `main.tex`.
- Inkluder DOI eller URL der det finnes, og merk rapporter fra norsk industri og offentlig sektor som `@report` eller `@misc` med tydelige institusjonsnavn.
- Når nye kapitler ferdigstilles, gjennomgå bibliografien samlet for å sikre at alle kilder er konsistente og følger valgt stil (`apalike`).

## Oppdatering av plan

`plan.md` gir en samlet oversikt over bokas struktur og anbefalt progresjon for lesere og forfattere. Dersom du endrer strukturen, introduserer nye kapitler eller justerer læringsmål, oppdater `plan.md` samtidig.

## Tips for videreutvikling

- Inkluder casestudier fra norsk industri og offentlig sektor for relevans.
- Knyt teori til praksis med konkrete verktøy (simulatorer, IoT-plattformer, dataintegrasjon).
- Husk å dekke etiske og juridiske aspekter ved bruk av digitale tvillinger.

## Nye tematiske prioriteringer og innholdsforslag

For å fylle boken med ferske perspektiver og holde stoffet oppdatert, skal kommende oppgaver hente inn følgende temaer. Opprett egne `TODO`-oppgaver i `task_queue.md` når du starter hvert initiativ, og oppdater `plan.md` når strukturen justeres.

### Temaer som må innarbeides i kapittelteksene

- **Sirkulærøkonomi og bærekraftindikatorer:** Beskriv hvordan digitale tvillinger støtter materialgjenvinning, energioptimalisering og klimaregnskap i norske verdikjeder (industri, bygg, kommuner). Foreslå måltall og dashboards for kapittel 3, 4 og 7.
- **Digitale tvillinger for beredskap og sikkerhet:** Utdyp scenarioanalyse for kritisk infrastruktur, inkludert cyber-fysisk sikkerhet, nøkkelstandarder (NIS2, IEC 62443) og beredskapsøvelser. Koble innholdet til kapittel 3, 6 og 7.
- **Menneske–maskin-samhandling og visualisering:** Legg inn stoff om AR/VR, beslutningsstøtte og operatøropplæring. Sett av plass til norske pilotprosjekter (f.eks. offshore, helse) og vurder hvordan det kan integreres i kapittel 4, 5 og 8.
- **Datasamarbeid og digitale dataspace-modeller:** Forklar Gaia-X, IDSA og norske dataøkosystem (f.eks. MobilityLab, HealthData). Angi hvordan datasamarbeid påvirker datadeling, kontrakter og styring i kapittel 3 og 7.
- **Tverrsektorielle klimacaser:** Planlegg nye caser for havvind, landbruk og batteriverdikjeden som komplementerer dagens industri-, transport- og helseeksempler i kapittel 8.
- **Fremvoksende teknologier og AI-verktøy:** Oppdater kapittel 5 og 9 med bruk av foundation-modeller, generativ simulering, agentbasert AI og digitale tvillinger som kjører på kant/edge.

### Elementer som kan berike bokas støtteapparat

- **Øvingsbank og prosjektmaler:** Utvid støttefilene med komplette prosjektoppgaver (data, vurderingskriterier, forslag til presentasjoner) som bygger på hvert nytt tema.
- **Intervjuer og ekspertkommentarer:** Planlegg korte tekstbokser eller marginalkommentarer med sitater fra norske fagfolk (energi, bygg, helse, mobilitet) for å gi autentiske stemmer.
- **Figur- og dataressurser:** Opprett illustrasjonsplaner for nye caser, inkludert krav til 3D-modeller, tidsserier og sanntidsdashboards. Registrer alt-tekst og metadata i `support/figurer/` samtidig.
- **Regelverksoppsummeringer:** Lag tabeller i appendiks som sammenligner lover, standarder og tilsynsmyndigheter per sektor (personvern, sikkerhet, miljø). Referer til relevant kapittel når tabellen oppdateres.
- **Verktøykasser for implementering:** Sammensett sjekklister, modenhetsmålinger og gevinstrealiseringsplaner som kan legges inn i kapittel 7, appendiks og lærerveiledningen.

Med denne strukturen kan du enkelt be assistenten om å «ta neste oppgave på dt-boken». Assistenten vil da lese `task_queue.md`, plukke første `TODO`-oppgave og utføre den.
