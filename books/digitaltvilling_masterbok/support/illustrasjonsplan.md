# Illustrasjons- og grafikkplan


## Formål

Planen sikrer at alle figurer i dt-boken får en enhetlig visuell identitet, følger krav til tilgjengelighet og kan produseres effektivt av tverrfaglige bidragsytere. Dokumentet beskriver standarder for grafisk uttrykk, arbeidsflyt for produksjon og konkrete leveranser per kapittel.

## Felles stilprinsipper

### Format og filtyper
- Primærformat for vektorillustrasjoner er TikZ (kompilert via LaTeX) eller SVG eksportert til PDF. Rasterfiler (PNG) brukes kun for fotobasert materiale.
- Alle endelige filer skal lagres i `support/figurer/eksport` med opprinnelige kilder i `support/figurer/kilder`.
- Maks bredde i bokformatet er `\textwidth`. Standard høyde for horisontale figurer er 55–65 mm for å sikre lesbarhet i trykk.

### Fargepalett (WCAG AA-kontrast mot hvit bakgrunn)
| Navn | Hex | Bruk |
| --- | --- | --- |
| Dyp blå | `#1B4965` | Primærbokser og hovedstrømmer (f.eks. felt/arkitektur). |
| Petrol | `#2C7DA0` | Sekundære prosessbokser og edge-komponenter. |
| Havgrønn | `#00A896` | Integrasjons- og dataplattformer. |
| Solgul | `#F4D35E` | Brukergrensesnitt, beslutningspunkter, KPI-er. |
| Koral | `#EE6C4D` | Varsler, risiko og kontrollpunkter. |
| Grafitt | `#4F5D75` | Tekst, rammer og akselinjer. |
| Skygrå | `#E5E9EC` | Bakgrunnsfelt, callouts og hjelpelinjer. |

Fargene defineres i `main.tex` før bruk (`\definecolor{dypblaa}{HTML}{1B4965}` osv.) og gjenbrukes i alle TikZ-filer.

### Typografi og ikonografi
- Bruk Sans Serif (Helvetica/Arial via `\sffamily`) i figurer for å skille fra brødtekst i LaTeX.
- Linjetykkelse: 1.0 pt for hovedstrømmer, 0.6 pt for hjelpelinjer. Piler avsluttes med `>=Stealth` i TikZ.
- Ikoner hentes fra `FontAwesome5` via TikZ eller importeres som SVG for å sikre enhetlig stil.
- Unngå drop shadows; bruk heller kontrasterende bakgrunnsfelt.

### Tilgjengelighet
- Minimum 8 pt tekststørrelse i figurer; i tidslinjer 9 pt.
- Gi hver figur alternativtekst i LaTeX (`\caption` + `\label`, samt kort beskrivelse i kommentar for senere EPUB-produksjon).
- Sørg for at fargeinformasjon ikke er eneste bærer av betydning; kombiner farger med mønstre eller ikoner.

## Arbeidsflyt for ferdigstilling
1. **Brief og manus** – Fagansvarlig beskriver budskapet med referanse til kapitteltekst.
2. **Storyboard** – Designer lager enkel skisse (kan være Mermaid, håndtegning eller tabell) og lagrer i `kilder/`.
3. **Produksjon** – Endelig figur bygges i TikZ eller vektorverktøy. Fargepalett og typografi fra denne planen benyttes.
4. **Kvalitetssikring** – Dobbeltsjekk data, kilder og norsk terminologi. Test utskrift i gråtoner.
5. **Integrasjon** – Eksporter til PDF (evt. PNG @ 300 DPI) og oppdater kapittel med `\includegraphics` eller innebygd TikZ.
6. **Versjonslogg** – Kommenter endringer i kapittelfilen (dato + kort oppsummering). Lagre kildefil og eksport med samme versjonstagg.

Fagfellekommentarer loggføres i `support/fagfellelogg.csv` slik at grafikkendringer kan spores.

## Alt-tekst og metadata
Tilgjengelige figurer krever entydig alt-tekst og dokumentert kildeinformasjon. Alt-tekst beskriver funksjonen til illustrasjonen og skal gjøre det mulig for lesere med skjermleser å forstå figuren uten å se den. Metadatafilene brukes også som referanse når figurer revideres eller gjenbrukes i andre formater (EPUB, nettsider).

### Obligatoriske felt
| Felt | Beskrivelse | Eksempel |
| --- | --- | --- |
| `figur` | Filnavn uten endelse og med versjon (`kap04-analyseflyt-v1`). | `kap03-datapipeline-v2` |
| `tittel` | Kort visningsnavn som kan brukes i figurregister. | «Datapipeline fra felt til styringssystemer» |
| `alttekst` | 2–3 setninger som beskriver hovedbudskap, aktører og hva pilene/aksene viser. | «Figuren viser fem steg fra feltsensorer via edge og integrasjonslag til analyseplattformer og dashboards, med egen styringsboks for sikkerhet og logging.» |
| `kilde` | Kapittelreferanse eller ekstern kilde som figuren bygger på. | `Kapittel 3, seksjon «Dataflyt og pipeline-design»` |
| `forfatter` | Navn på ansvarlig designer/forfatter. | `Ahmed Solheim` |
| `dato` | ISO-format (`YYYY-MM-DD`) for siste oppdatering. | `2024-05-10` |
| `relaterte_kapitler` | (Valgfritt) Liste over kapittelnummer der figuren brukes. | `["3", "6"]` |

### Mal for metadatafil
Alt-tekst og metadata lagres som Markdown med YAML-frontmatter i `support/figurer/metadata/`. Filnavnet følger mønsteret `kapXX-tema-vY.alt.md`. Innholdet skal bruke malen under:

```markdown
---
figur: kap04-analyseflyt-v1
tittel: Analyseflyt for digitale tvillinger
alttekst: >-
  Figuren viser en prosess med fem steg fra datainnsamling via modellering til visualisering,
  og fremhever hvordan beslutningspunkter og feedbacksløyfer er koblet på hvert trinn.
kilde: Kapittel 4, seksjon «Analysemetoder»
forfatter: Nora Aas
dato: 2024-05-10
relaterte_kapitler:
  - 4
  - 5
notater: >-
  Oppdatert etter fagfellekommentar DI-03 for å tydeliggjøre governance-callout.
---
```

`alttekst`-feltet kan være flere avsnitt ved behov; bruk `>-`-syntaksen for å håndtere linjeskift. `notater` brukes til kort endringslogg (for eksempel referanse til fagfellekommentar eller Jira-sak). Når figuren oppdateres, kopieres metadatafilen og versjonsnummeret økes i både filnavn og `figur`-felt.

## Oppdatert behov fra kapitlene (august 2024)
- Kapittel 1 trenger både tidslinje og en ny verdikjede-/modenhetsfigur som kobler norske case til gevinstindikatorer.
- Kapittel 2 beholder systemkart og kausalsløyfe i Mermaid-kode; de må fortsatt konverteres til TikZ med enhetlig ikonsett og dataetiketter.
- Kapittel 3 skal i tillegg til datapipeline vise et dataspace-samhandlingskart og en beredskapstavle som dekker NIS2-krav og bærekraftsindikatorer.
- Kapittel 4 utvider simuleringskapittelet med AR/VR-baserte beslutningsrom og trenger storyboard for immersive oppsett i tillegg til matrise, prosessdiagram og verktøystakk.
- Kapittel 5 får nye delkapitler om generative og edge-baserte tvillinger, og trenger visuelle sløyfer for både generativ pipeline og edge-operasjoner.
- Kapittel 6 skal visualisere kontrolltårn, usikkerhetskart og et beredskapsscenario som viser koblingen til NIS2/IEC 62443-krav.
- Kapittel 7 må suppleres med governance-serie og et bærekraft-/gevinstdashboard som støtter nye KPI-tabeller.
- Kapittel 8 utvider casene med klima- og sektorsammenligninger, og trenger en casemal-infografikk samt en komparativ klimacase-matrise.
- Kapittel 9 skal vise roadmap og trendradar, og kompletteres med en finansierings-/programmatrise for forsknings- og innovasjonsløp.
- Appendiks trenger fortsatt ikonserie, men også en ressursnavigator som viser hvordan verktøy, kurs og nettverk henger sammen.

## Oversikt per kapittel og leveranse

| Kapittel/element | Kladd/status i dag | Tiltak for ferdigstilling | Format og filnavn | Ansvar og tidslinje |
| --- | --- | --- | --- | --- |
| Kap. 1 – Historisk tidslinje | Tekstlig oversikt over milepæler i kapittel 1, ingen grafikk | Lage to-spors tidslinje (internasjonalt vs. Norge) med ikonmarkering av sektorer og korte tekstbobler | `figurer/kap01-tidslinje-v1.tikz` (+ PDF) | Ingrid Lunde (manus) + grafiker; storyboard uke 1, ferdig leveranse uke 3 |
| Kap. 1 – Verdikjede og modenhet | Ingen eksisterende grafikk; omtale kun i tekst | Utvikle verdikjedekart med modenhetsnivåer (initielt, styrt, optimalisert) og tilhørende KPI-er per sektor | `figurer/kap01-verdikjede-v1.tikz/pdf` | Ingrid Lunde + governance-team; research uke 2, storyboard uke 3, ferdig levering uke 5 |
| Kap. 2 – Systemkart for produksjonslinje | TikZ versjon 2 med ikonsett og metadata (2024-07-18) | Visuell QA og eksport til PDF ved behov | `figurer/kap02-systemkart-v2.tikz/pdf` | Ahmed Solheim leder, ferdig levert uke 2 |
| Kap. 2 – Kausalsløyfe vedlikehold–energi | Mermaid-kode i manus | Redesign som sirkulær kausalfigur med positive/negative koblinger, tidsforsinkelsesikon og legendetekst | `figurer/kap02-kausal-v1.tikz/pdf` | Ahmed Solheim + fagekspert; storyboard uke 1, produksjon uke 2 |
| Kap. 3 – Datapipeline (Figur~\ref{fig:kap3-datapipeline}) | TikZ oppdatert til versjon 2 (2024-07-15) med definert palett og governance-callout | Visuell QA mot øvrige kapitler; metadata publisert i `metadata/kap03-datapipeline-v2.alt.md`; koordinere fagfelleinnspill (DI-03) og referanser i `plan.md` | Oppdatere `kapittel03-data.tex` + `figurer/kap03-datapipeline-v2.tikz/pdf` | Ahmed Solheim + Nora Aas; revisjon uke 2, alt-tekst uke 2 |
| Kap. 3 – Dataspace-samhandlingskart | Ikke planlagt tidligere | Designe kart som viser roller (produsent, konsument, koordinator), dataspace-tjenester og policystrømmer | `figurer/kap03-dataspace-v1.tikz/pdf` | Ahmed Solheim + dataarkitekt; storyboard uke 3, produksjon uke 4, metadata `metadata/kap03-dataspace-v1.alt.md` |
| Kap. 3 – Beredskapstavle | Ingen eksisterende grafikk | Utvikle beredskapstavle som illustrerer NIS2-krav, responsteam, alarmer og eskalering | `figurer/kap03-beredskapstavle-v1.svg/pdf` | Nora Aas + sikkerhetsteam; risikoworkshop uke 3, ferdig leveranse uke 5 |
| Kap. 4 – Simuleringsmetodematrise | Mangler figur | Lage 2×2 matrise (deterministisk/stokastisk × diskret/kontinuerlig) med norske eksempler og metodeikon | `figurer/kap04-matrise-v1.svg/pdf` | Nora Aas; skisse uke 2, ferdiggjøring uke 3 |
| Kap. 4 – Analyseflyt | Mangler figur | Tegne prosess med trinnene datainntak → modellering → simulering → analyse → visualisering, inkludert referanse til scenario-/sensitivitetsarbeid | `figurer/kap04-analyseflyt-v1.tikz` | Nora Aas; storyboard uke 2, levering uke 3 |
| Kap. 4 – Verktøystakk | Ingen eksisterende grafikk | Visualisere lagdelt verktøystøtte (modellering, data/integrasjon, automasjon, ytelsesmiljø) med eksempler fra teksten | `figurer/kap04-verktoystakk-v1.tikz/pdf` | Nora Aas + grafisk designer; skisse uke 2, ferdig uke 4 |
| Kap. 4 – AR/VR beslutningsrom | Ikke planlagt tidligere | Vise immersive beslutningsrom med kobling mellom simuleringsmodeller, sensorer og operatørroller | `figurer/kap04-arvr-beslutning-v1.svg/pdf` | Nora Aas + AR/VR-team; storyboard uke 3, testing uke 4, ferdigstillelse uke 5 |
| Kap. 5 – Læringssløyfe (ML–optimalisering–assimilering) | Ingen figur | Illustrere lukket sløyfe mellom dataassimilering, ML-modeller, optimalisering og operasjonelle dashboards med usikkerhetsindikator | `figurer/kap05-laeringssloyfe-v1.tikz/pdf` | Nora Aas; storyboard uke 2, ferdig uke 4 |
| Kap. 5 – MLOps-oppdateringsløp | Ikke planlagt tidligere | Lage flytskjema for dataopptak, kvalitetskontroll, trening, registrering og utrulling med alarm for konseptdrift | `figurer/kap05-mlops-v1.tikz/pdf` | Nora Aas + DevOps-team; struktur uke 3, levering uke 5 |
| Kap. 5 – Generativ tvilling-pipeline | Nytt behov | Illustrere hvordan generative modeller brukes til scenariobygging, syntetiske data og menneske-i-løkken-godkjenning | `figurer/kap05-generativ-v1.tikz/pdf` | Nora Aas + AI-lab; storyboard uke 4, grafikk uke 5, metadata `metadata/kap05-generativ-v1.alt.md` |
| Kap. 5 – Edge-operasjonskart | Ingen grafikk ennå | Vise distribusjon mellom edge-noder, sky, modelloppdateringer og overvåkingsdashboards | `figurer/kap05-edge-v1.svg/pdf` | DevOps-team + programleder; arkitekturworkshop uke 4, levering uke 6 |
| Kap. 6 – Valideringsrammeverk («kontrolltårn») | Ingen grafikk ennå | Utforme vertikal kontrolltårn-figur som viser verifikasjon, validering, beslutningsportaler og revisjonsspor | `figurer/kap06-validering-v1.svg/pdf` | Leif Ødegaard; arbeidsmøte uke 3, ferdig uke 5 |
| Kap. 6 – Usikkerhetskart | Nytt behov fra kapittelet | Lage oversikt (2×2 eller spektrum) som plasserer aleatorisk vs. epistemisk usikkerhet, metoder og tiltak | `figurer/kap06-usikkerhet-v1.svg/pdf` | Leif Ødegaard + data scientist; skisse uke 3, ferdig uke 4 |
| Kap. 6 – Tillitspanel | Ikke tidligere planlagt | Visualisere indikatorpanel med sporbarhet, etikk og revisjonsspor, koblet til dashboard-eksempler | `figurer/kap06-tillitspanel-v1.tikz/pdf` | Leif Ødegaard + designressurs; storyboard uke 4, levering uke 5 |
| Kap. 6 – Beredskapsscenario (NIS2) | Nytt behov | Scenariofigur som viser deteksjon, respons, kommunikasjon og etterlevelse per NIS2-krav | `figurer/kap06-beredskap-v1.svg/pdf` | Leif Ødegaard + sikkerhetsteam; scenarioworkshop uke 4, ferdig uke 6 |
| Kap. 7 – Livssyklusdiagram | Mangler figur | Bygge sirkel/tidslinje med fasene initiativ, design, drift, avvikling og tilhørende leveranser, inkl. RACI-callout | `figurer/kap07-livssyklus-v1.tikz/pdf` | Leif Ødegaard; gapanalyse uke 2, ferdig uke 3 |
| Kap. 7 – Governance-modeller | Nytt behov | Diagram som sammenligner sentralisert, føderert og produktlinje-modell med ansvarslinjer og beslutningsfora | `figurer/kap07-governance-v1.svg/pdf` | Leif Ødegaard + Ingrid Lunde; workshop uke 3, ferdig uke 4 |
| Kap. 7 – Modenhetsstige | Uadressert i tidligere plan | Lage modenhetsstige (ad hoc → pilot → styrt → integrert → kontinuerlig forbedring) med kriterier per trinn | `figurer/kap07-modenhet-v1.tikz/pdf` | Leif Ødegaard + programteam; skisse uke 4, ferdig uke 5 |
| Kap. 7 – Bærekraft- og gevinstdashboard | Ny leveranse | Utvikle dashboard med KPI-er for sirkulærøkonomi, sikkerhet og gevinstrealisering koblet til livssyklusfasene | `figurer/kap07-dashboard-v1.svg/pdf` | Leif Ødegaard + bærekraftsteam; datainnsamling uke 4, design uke 5, ferdig uke 6 |
| Kap. 8 – Caseoversikt | Ingen figur ennå | Kart/matrise med sektorer (industri, energi, maritim, bygg, helse) og nøkkelindikatorer; markere geografisk plassering i Norge | `figurer/kap08-casekart-v1.svg/pdf` | Ingrid Lunde + sektorteam; datainnsamling uke 3, ferdig uke 4 |
| Kap. 8 – Casemal infographic | Nytt behov fra maltekst | Infographic som viser hovedseksjoner i casemalen (sammendrag, mål, datagrunnlag, modeller, resultater, overføringsverdi) med ikoner | `figurer/kap08-casemal-v1.tikz/pdf` | Ingrid Lunde + grafiker; storyboard uke 4, levering uke 5 |
| Kap. 8 – Klimacase-komparator | Ikke planlagt tidligere | Tabell/diagram som sammenligner havvind, landbruk og batteri på mål, data, verktøy og gevinst | `figurer/kap08-klimacase-v1.svg/pdf` | Ingrid Lunde + sektorteam; datainnsamling uke 4, design uke 5, ferdig uke 6 |
| Kap. 9 – FoU-roadmap | Ingen figur ennå | Roadmap som kobler internasjonale drivere, norske satsinger og studentprosjektideer med tidshorisont (0–2/2–5/5+ år) | `figurer/kap09-roadmap-v1.tikz/pdf` | Leif Ødegaard + forskningskoordinator; skisse uke 4, ferdig uke 5 |
| Kap. 9 – Trendradar | Ikke planlagt tidligere | Trendradar eller spindeldiagram som grupperer semantiske tvillinger, immersive arbeidsflater og bærekraft/regulering etter modenhet | `figurer/kap09-trendradar-v1.svg/pdf` | Leif Ødegaard + trendteam; datainnsamling uke 5, levering uke 6 |
| Kap. 9 – Finansierings- og programmatrise | Nytt behov | Matrise som kobler forsknings- og innovasjonsprogram (nasjonalt/internasjonalt) med tidslinjer og tema | `figurer/kap09-finansiering-v1.tikz/pdf` | Leif Ødegaard + forskningskoordinator; kartlegging uke 5, design uke 6, ferdig uke 7 |
| Appendiks – Ressursikoner | Fortsatt uadressert | Utvikle ikonsett for ressurskategorier (datasett, verktøy, kurs, nettverk) til digital distribusjon | `figurer/app-ressurser-ikoner-v1.svg/pdf` | Astrid Hauge; starter etter hovedfigurer, ferdig uke 6 |
| Appendiks – Ressursnavigator | Ikke planlagt tidligere | Diagram som viser koblinger mellom verktøy, kurs, nettverk og lisenskategorier | `figurer/app-ressursnavigator-v1.svg/pdf` | Astrid Hauge + programleder; kartlegging uke 5, design uke 6, ferdigstillelse uke 7 |

### Kapittel 4 – detaljert figurbehov (DT-04)

| Figur | Hovedbudskap | Plassering i manus | Kilder og data | Status og ansvar |
| --- | --- | --- | --- | --- |
| Simuleringsmetodematrise (`kap04-simuleringsmatrise-v1`) | Vise hvordan deterministiske/stokastiske og diskrete/kontinuerlige modeller kombineres i praksis med norske eksempler (fjernvarme, produksjonslinje, trafikk). | Etter \subsection{Kopling mot sanntidsdata} for å oppsummere modelltypene. | Kapitteltekst i seksjonen «Typer simulering», faglige innspill fra NTNU-pilot (2023), lenker til Modelica og AnyLogic-dokumentasjon. | Storyboard og alt-tekst utarbeides av Nora Aas (uke 2). Grafikkproduksjon koordineres med grafiker Ida Holmen i uke 3. Metadatafil: `support/figurer/metadata/kap04-simuleringsmatrise-v1.alt.md`. |
| Analyseflyt for digitale tvillinger (`kap04-analyseflyt-v1`) | Forklare arbeidsflyten fra datainntak via modellering og simulering til visualisering og beslutningsstøtte, inkludert kontrollsløyfer for kvalitet. | I starten av \section{Analysemetoder} som visuell introduksjon. | Avsnittene om sensitivitetsanalyse, optimalisering og visualisering; prosessbeskrivelse fra `support/notater/datastyringsforum-di03.md`. | Storyboard i uke 2 ved Nora Aas, detaljdesign i samarbeid med Ahmed Solheim (uke 3). Alt-tekst klargjort i metadatafil `support/figurer/metadata/kap04-analyseflyt-v1.alt.md`. |
| Verktøystakk for simulering (`kap04-verktoystakk-v1`) | Illustrere lagdelt verktøystøtte fra modellering til ytelsesmiljø med eksempler på norske plattformer (Kongsberg Kognitwin, Equinor OMNIA). | Etter punktlisten i \section{Verktøy og arbeidsflyt}. | Kapitteltekst, vendor-notater fra Kongsberg Digital og Equinor workshops (finnes i redaksjonsarkivet), referanser i `support/referanser.bib`. | Strukturutkast av Nora Aas (uke 2), grafiker ferdigstiller uke 4. Metadatafil: `support/figurer/metadata/kap04-verktoystakk-v1.alt.md`. |
| Immersivt beslutningsrom (`kap04-immersiv-beslutning-v1`) | Vise hvordan AR/VR-flater kombinerer sanntidsdata, simuleringer og samarbeidsverktøy i et norsk kontrollrom. | I den nye \subsection{Immersiv AR/VR-beslutningsstøtte} rett etter omtalen av visualisering. | Støttenotat `support/notater/kap04-immersiv-case.md`, erfaringer fra Equinor OMNIA og Kongsberg Digital demoer, samt \citep{palmarini2018augmented} for metodikk. | Storyboard og alt-tekst utarbeides av Nora Aas (uke 2) med grafiker Ida Holmen; metadatafil `support/figurer/metadata/kap04-immersiv-beslutning-v1.alt.md`. |
| Fjernvarmecase – simulering til gevinst (`kap04-fjernvarmecase-v1`) | Koble casebeskrivelsen til konkrete data- og beslutningspunkter (temperaturmålere, pumpesettpunkt, KPI for energitopper) og vise hvordan simuleringstypene spiller sammen. | Mot slutten av \section{Praksiseksempel: Digital tvilling for fjernvarmenett}. | Casebeskrivelse i kapittel 4, energirapport fra Enova (2022) og kundedata brukt i pilotprosjektet (tilgjengelig via prosjektleder). | Ny figur bestilles uke 3; manusforfatter utarbeider storyboard og alt-tekst (Nora Aas). Metadata utarbeides i fil `support/figurer/metadata/kap04-fjernvarmecase-v1.alt.md`. |

### Kapittel 5 – detaljert figurbehov (DT-05)

| Figur | Hovedbudskap | Plassering i manus | Kilder og data | Status og ansvar |
| --- | --- | --- | --- | --- |
| AI-coach i immersivt kontrollrom (`kap05-operator-coach-v1`) | Illustrere hvordan operatører bruker AR/VR-baserte assistenter som kombinerer simulering, maskinlæring og samskriving av tiltak. | I den nye \section{Utvidet analyseeksempel: Immersiv AI-coach} etter omtalen av samspill mellom læring, optimalisering og assimilering. | `support/notater/kap05-algoritmematrise-utvidelse.md`, pilotdata fra Cognite InField, \citep{palmarini2018augmented} og \citep{iec62443-2-1}. | Storyboard og metadata utarbeides av Nora Aas (uke 2) i samarbeid med Ahmed Solheim; grafiker ferdigstiller uke 4. Metadatafil: `support/figurer/metadata/kap05-operator-coach-v1.alt.md`. |

Til hver figur følger et kort sett med kontrollspørsmål til fagfeller (se `support/notater/kap04-fagfellepakke.md`) og forslag til hvordan figuren kan brukes i undervisningsopplegg. Fargepalett og typografi følger prinsippene i dette dokumentet, og alle metadatafiler opprettes samtidig med storyboard for å sikre konsistent alt-tekst.

## Leveranse- og kvalitetskriterier
- Hver figur skal ha versjonslogg i commit-melding og i kapittelfilens kommentarblokk.
- Alt-tekst og metadata lagres i `support/figurer/metadata/kapXX-tema-vY.alt.md` og lenkes fra kapittelfilen med kommentar (`% Alt-tekst: kapXX-tema-vY.alt.md`).
- Ved bruk av data, legg ved kildehenvisning i figurtekst og i `referanser.bib`.
- Fagansvarlig signerer av for faglig korrekthet; grafisk ansvarlig for layout; prosjektleder for helhetlig stil.

## Neste steg
1. Koordinere storyboard-arbeid for kapittel 1–3 i uke 1–3 (tidslinje, verdikjedekart, dataspace og beredskapstavle) sammen med fagansvarlige og grafisk ressurs.
2. Etablere felles stiler for AR/VR-rammer, generative pipelines og edge-operasjonskart i TikZ/SVG-biblioteket før kapittel 4–5-produksjon starter.
3. Planlegge uke 4–6 workshops for governance-, bærekraft- og klimacase-illustrasjoner (kapittel 7–8) samt finansieringsmatrise (kapittel 9); sikre data- og ikonbibliotek i `support/figurer/kilder`.
4. Synkronisere `plan.md`, `task_queue.md` og `support/fagfellelogg.csv` etter hver milepæl slik at fagfeller og grafikkteam deler oppdatert status og metadata.
