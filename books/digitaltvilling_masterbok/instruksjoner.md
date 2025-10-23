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

Med denne strukturen kan du enkelt be assistenten om å «ta neste oppgave på dt-boken». Assistenten vil da lese `task_queue.md`, plukke første `TODO`-oppgave og utføre den.
