# Kapittel 6 – Sikkerhetsstandarder og caseoppgave

## Formål
Dette notatet dokumenterer caseoppgaven som støtter den nye seksjonen om sikkerhetsstandarder i kapittel 6. Studentene skal koble standardkrav til en digital tvilling i drift og beskrive hvordan tekniske og organisatoriske tiltak følges opp.

## Casebeskrivelse
- **Scenario:** «VestKraft Nett» drifter et regionalt kraftnett med digital tvilling for tilstandsbasert vedlikehold og planlegging.
- **Utfordring:** Selskapet skal etterleve både \citet{iec62443-2-1} og \citet{eu2022nis2} før en ny operatørportal tas i bruk.
- **Oppdrag til studentene:**
  1. Kartlegg hvordan tvillingens komponenter (dataplattform, modellbibliotek, operatørportal) mappes mot soner og konduiter i IEC 62443.
  2. Prioriter tiltak ved hjelp av en risikomatrise (sannsynlighet × konsekvens) og foreslå kontrollmekanismer.
  3. Definer nøkkelindikatorer og revisjonsrutiner som dokumenterer etterlevelse, inkludert roller fra governance-modellen i Kapittel 7.

## Arbeidsflyt i laboratorieøving
1. **Forstudie:** Studentene analyserer en logg over avvik og patch-nivå (tilgjengelig som CSV i læringsplattformen) og identifiserer hvilke hendelser som omfattes av NIS2 artikkel 23.
2. **Workshop:** Gruppa fyller ut et «compliance canvas» med seks felt: standardreferanse, teknisk tiltak, organisatorisk tiltak, ansvarlig rolle, dokumentasjon og oppfølging.
3. **Rapport:** Lever en tre-siders vurdering inkludert diagrammer for soner/konduiter og en tabell over indikatorer med målefrekvens.

## Evalueringsrubrikk (utdrag)
| Kriterium | Poeng (0–3) | Beskrivelse |
| --- | --- | --- |
| Standardforståelse | 0–3 | Viser korrekt kobling mellom kravene i IEC 62443-2-1 og NIS2 og tvillingens arkitektur. |
| Risikohåndtering | 0–3 | Begrunner prioritering i risikomatrisen og foreslår passende kontrolltiltak. |
| Dokumentasjon | 0–3 | Leverer tydelig plan for revisjon, logging og sporbarhet. |
| Tverrfaglig koordinering | 0–3 | Viser hvordan tiltak fordeles på roller fra Kapittel 7 og hvordan de følges opp i driftsprosesser. |

En totalscore på 10 eller mer kreves for å bestå øvingen. Sensor bruker rubrikken i kombinasjon med ALTAI-sjekkpunktene fra Kapittel 5 for å sikre helhetlig vurdering.
