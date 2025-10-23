# Delingsnotat: Datastyringsforum (DI-03)

Dette notatet underbygger tiltaksplanen for fagfellekommentar **DI-03** og brukes som felles referanse for
kapittelteamet, dataplattformgruppen og sikkerhetsansvarlige. Dokumentet kan distribueres direkte til fagfeller
sammen med kapittelutdraget fra Kapittel~3.

## Mål og scope
- Sikre en samordnet praksis for datastyring på tvers av tvillinginitiativ.
- Dokumentere indikatorer, responssløyfer og personverntiltak som må være på plass før neste fagfellerunde.
- Knytte tiltakene eksplisitt til tekst og illustrasjoner i Kapittel~3 og Kapittel~6.

## Arbeidsflyt og roller
| Rolle | Hovedansvar | Leveranser |
| --- | --- | --- |
| Produkteier for digital tvilling | Prioritere tiltak og forankre beslutninger i gevinstplanene (Kapittel~7). | Tiltakslogg, beslutningsnotater |
| Data steward | Overvåke datakvalitet, utløse korrigerende tiltak og koordinere med endringsstyret. | Ukentlig kvalitetsrapport, oppdaterte datakontrakter |
| Teknisk plattformteam | Forvalte overvåkingsdashbord, teste distribuerte oppdateringer og drifte hendelseshåndtering. | Dashboard-konfigurasjoner, hendelseslogg |
| Sikkerhets- og personvernrådgiver | Validerer tilgangsstyring, behandlingsgrunnlag og logging i henhold til Normen og GDPR. | Personvernsjekkliste, revisjonslogger |

Forumet gjennomfører ukentlige møter i innføringsfasen. Agendaen skal alltid inneholde status på indikatorene under, åpne
hendelser og planlagte endringer i integrasjonsgrensesnitt.

## Indikatorpakke for datakvalitetsdashbord
| Indikator | Definisjon | Varslingsgrense | Tiltak ved avvik |
| --- | --- | --- | --- |
| Fullstendighet per datastrøm | Andel registreringer som oppfyller forventet frekvens de siste 24 timene. | < 98 % over to måleperioder | Trigger fallback-strategi (buffersynk) og varsle plattformteam. |
| Tidsforsinkelse | Median forsinkelse fra felt til integrasjonslag. | > 90 sekunder i mer enn tre påfølgende målinger | Initiere root cause-analyse og vurdere midlertidig prioritering av ressursbruk. |
| Valideringsfeil | Antall meldinger som bryter regler for datatyper, måleområder eller semantikk. | > 5 feil pr. time i kritiske strømmer | Midlertidig stoppe automatisert modelloppdatering og aktivere manuell kontroll. |
| Sikkerhetsavvik | Antall hendelser relatert til tilgangsbrudd eller uautoriserte integrasjoner. | > 1 hendelse pr. uke | Varsle sikkerhetsansvarlig, revurdere tilgangspolicy og oppdatere logging. |

Målemetodene for indikatorene dokumenteres i dashboard-konfigurasjonen og refereres i Kapittel~3 (seksjonen «Operasjonelle
kontrollpunkter»).

## Hendelseshåndtering og læringssløyfe
1. **Registrering:** Alle avvik loggføres i samme løsning som sikkerhetshendelser.
2. **Klassifisering:** Produkteier, data steward og plattformteam vurderer alvorlighetsgrad innen to timer.
3. **Tiltaksvalg:** Ved høy risiko aktiveres fallback-modeller eller manuelt kontrollsteg beskrevet i Kapittel~6.
4. **Tilbakerapportering:** Resultatet dokumenteres i fagfelleloggen (DI-03) og gjennomgås i kvartalsvise retrospektiv.
5. **Forbedring:** Læringspunkter omsettes til oppdaterte datakontrakter, opplæringsmateriell og eventuelle justeringer i
   illustrasjonen av datapipelinen.

## Personvern og etikk
- Hver ny datakilde skal risikovurderes i tråd med Helsedirektoratets veiledere og Normen før produksjonssetting.
- Behandlingsgrunnlag registreres i datakatalogen med lenke til ansvarlig person og forventet slettetidspunkt.
- Sensitive datasett tagges med tilgangsnivå som gjenspeiler zero-trust-prinsippene, og det føres revisjonslogg over alle
  oppslag i sanntidsdashbord.
- Forumet bekrefter kvartalsvis at tiltakene harmonerer med etikk- og tillitskravene i Kapittel~6.

## Videre oppfølging
- Del notatet med fagfeller sammen med utdrag fra Kapittel~3 innen 22.05.
- Oppdater `support/fagfellelogg.csv` når tiltakene er levert og dokumenter eventuelle nye anbefalinger.
- Evaluer indikatorene etter pilotperioden og foreslå justeringer i kapitteltekst eller dashboard-oppsett.
