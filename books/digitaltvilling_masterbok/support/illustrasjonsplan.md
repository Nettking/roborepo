# Illustrasjons- og grafikkplan

> Notat (2024-05-08): Utarbeidet plan for å løfte kladdeillustrasjoner til ferdige figurer og etablere felles stil på tvers av kapitlene.
> Notat (2024-05-10): Oppdatert etter gjennomgang av kapitteltekstene for å fange nye illustrasjonsbehov og avstemme ansvar.
> Notat (2024-07-15): Datapipeline-illustrasjonen i Kapittel 3 er oppdatert til definert fargepalett og alt-tekst er registrert som versjon 2.

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

## Oppdatert behov fra kapitlene (mai 2024)
- Kapittel 1 forsterker historiske milepæler og norske case, og trenger en tidslinje som viser internasjonale og nasjonale spor i samme figur.
- Kapittel 2 beholder systemkart og kausalsløyfe i Mermaid-kode; de må konverteres til TikZ med ikoner og tydelige dataetiketter.
- Kapittel 3 har en ny TikZ-figur for datapipeline som må harmoniseres med fargepalett, tekststørrelser og governance-callout.
- Kapittel 4 utdyper simuleringsmetoder, analyseprosesser og verktøystøtte, og krever matrise, prosessdiagram og oversiktsfigur for verktøy.
- Kapittel 5 beskriver en lukket sløyfe mellom læring, optimalisering og dataassimilering samt MLOps-oppdateringer; begge bør visualiseres.
- Kapittel 6 legger til usikkerhetsanalyse og etikk, noe som krever kontrolltårn-illustrasjon, usikkerhetskart og tillitsindikator.
- Kapittel 7 fremhever livssyklusfaser, governance-varianter og modenhetstrinn; disse må tegnes som egen figurserie.
- Kapittel 8 utvider sektorseksjoner og casemal, og trenger både casekart og infographic som viser malens byggesteiner.
- Kapittel 9 samler forskningsdrivere og teknologitrender, og trenger en roadmap samt trendradar for prioriteringer.
- Appendiks skal fortsatt få en ikonserie for ressurskategorier til digitale formater.

## Oversikt per kapittel og leveranse

| Kapittel/element | Kladd/status i dag | Tiltak for ferdigstilling | Format og filnavn | Ansvar og tidslinje |
| --- | --- | --- | --- | --- |
| Kap. 1 – Historisk tidslinje | Tekstlig oversikt over milepæler i kapittel 1, ingen grafikk | Lage to-spors tidslinje (internasjonalt vs. Norge) med ikonmarkering av sektorer og korte tekstbobler | `figurer/kap01-tidslinje-v1.tikz` (+ PDF) | Ingrid Lunde (manus) + grafiker; storyboard uke 1, ferdig leveranse uke 3 |
| Kap. 2 – Systemkart for produksjonslinje | Mermaid-kode i manus | Konvertere til TikZ med palett, ikonsett for sensorer/aktører og datapiler merket med datatyper | `figurer/kap02-systemkart-v1.tikz/pdf` | Ahmed Solheim leder, skisse oppdatert uke 1, ferdigstillelse uke 2 |
| Kap. 2 – Kausalsløyfe vedlikehold–energi | Mermaid-kode i manus | Redesign som sirkulær kausalfigur med positive/negative koblinger, tidsforsinkelsesikon og legendetekst | `figurer/kap02-kausal-v1.tikz/pdf` | Ahmed Solheim + fagekspert; storyboard uke 1, produksjon uke 2 |
| Kap. 3 – Datapipeline (Figur~\ref{fig:kap3-datapipeline}) | TikZ oppdatert til versjon 2 (2024-07-15) med definert palett og governance-callout | Visuell QA mot øvrige kapitler; metadata publisert i `metadata/kap03-datapipeline-v2.alt.md` | Oppdatere `kapittel03-data.tex` + `figurer/kap03-datapipeline-v2.tikz/pdf` | Ahmed Solheim + Nora Aas; revisjon uke 2, alt-tekst uke 2 |
| Kap. 4 – Simuleringsmetodematrise | Mangler figur | Lage 2×2 matrise (deterministisk/stokastisk × diskret/kontinuerlig) med norske eksempler og metodeikon | `figurer/kap04-matrise-v1.svg/pdf` | Nora Aas; skisse uke 2, ferdiggjøring uke 3 |
| Kap. 4 – Analyseflyt | Mangler figur | Tegne prosess med trinnene datainntak → modellering → simulering → analyse → visualisering, inkludert referanse til scenario-/sensitivitetsarbeid | `figurer/kap04-analyseflyt-v1.tikz` | Nora Aas; storyboard uke 2, levering uke 3 |
| Kap. 4 – Verktøystakk | Ingen eksisterende grafikk | Visualisere lagdelt verktøystøtte (modellering, data/integrasjon, automasjon, ytelsesmiljø) med eksempler fra teksten | `figurer/kap04-verktoystakk-v1.tikz/pdf` | Nora Aas + grafisk designer; skisse uke 2, ferdig uke 4 |
| Kap. 5 – Læringssløyfe (ML–optimalisering–assimilering) | Ingen figur | Illustrere lukket sløyfe mellom dataassimilering, ML-modeller, optimalisering og operasjonelle dashboards med usikkerhetsindikator | `figurer/kap05-laeringssloyfe-v1.tikz/pdf` | Nora Aas; storyboard uke 2, ferdig uke 4 |
| Kap. 5 – MLOps-oppdateringsløp | Ikke planlagt tidligere | Lage flytskjema for dataopptak, kvalitetskontroll, trening, registrering og utrulling med alarm for konseptdrift | `figurer/kap05-mlops-v1.tikz/pdf` | Nora Aas + DevOps-team; struktur uke 3, levering uke 5 |
| Kap. 6 – Valideringsrammeverk («kontrolltårn») | Ingen grafikk ennå | Utforme vertikal kontrolltårn-figur som viser verifikasjon, validering, beslutningsportaler og revisjonsspor | `figurer/kap06-validering-v1.svg/pdf` | Leif Ødegaard; arbeidsmøte uke 3, ferdig uke 5 |
| Kap. 6 – Usikkerhetskart | Nytt behov fra kapittelet | Lage oversikt (2×2 eller spektrum) som plasserer aleatorisk vs. epistemisk usikkerhet, metoder og tiltak | `figurer/kap06-usikkerhet-v1.svg/pdf` | Leif Ødegaard + data scientist; skisse uke 3, ferdig uke 4 |
| Kap. 6 – Tillitspanel | Ikke tidligere planlagt | Visualisere indikatorpanel med sporbarhet, etikk og revisjonsspor, koblet til dashboard-eksempler | `figurer/kap06-tillitspanel-v1.tikz/pdf` | Leif Ødegaard + designressurs; storyboard uke 4, levering uke 5 |
| Kap. 7 – Livssyklusdiagram | Mangler figur | Bygge sirkel/tidslinje med fasene initiativ, design, drift, avvikling og tilhørende leveranser, inkl. RACI-callout | `figurer/kap07-livssyklus-v1.tikz/pdf` | Leif Ødegaard; gapanalyse uke 2, ferdig uke 3 |
| Kap. 7 – Governance-modeller | Nytt behov | Diagram som sammenligner sentralisert, føderert og produktlinje-modell med ansvarslinjer og beslutningsfora | `figurer/kap07-governance-v1.svg/pdf` | Leif Ødegaard + Ingrid Lunde; workshop uke 3, ferdig uke 4 |
| Kap. 7 – Modenhetsstige | Uadressert i tidligere plan | Lage modenhetsstige (ad hoc → pilot → styrt → integrert → kontinuerlig forbedring) med kriterier per trinn | `figurer/kap07-modenhet-v1.tikz/pdf` | Leif Ødegaard + programteam; skisse uke 4, ferdig uke 5 |
| Kap. 8 – Caseoversikt | Ingen figur ennå | Kart/matrise med sektorer (industri, energi, maritim, bygg, helse) og nøkkelindikatorer; markere geografisk plassering i Norge | `figurer/kap08-casekart-v1.svg/pdf` | Ingrid Lunde + sektorteam; datainnsamling uke 3, ferdig uke 4 |
| Kap. 8 – Casemal infographic | Nytt behov fra maltekst | Infographic som viser hovedseksjoner i casemalen (sammendrag, mål, datagrunnlag, modeller, resultater, overføringsverdi) med ikoner | `figurer/kap08-casemal-v1.tikz/pdf` | Ingrid Lunde + grafiker; storyboard uke 4, levering uke 5 |
| Kap. 9 – FoU-roadmap | Ingen figur ennå | Roadmap som kobler internasjonale drivere, norske satsinger og studentprosjektideer med tidshorisont (0–2/2–5/5+ år) | `figurer/kap09-roadmap-v1.tikz/pdf` | Leif Ødegaard + forskningskoordinator; skisse uke 4, ferdig uke 5 |
| Kap. 9 – Trendradar | Ikke planlagt tidligere | Trendradar eller spindeldiagram som grupperer semantiske tvillinger, immersive arbeidsflater og bærekraft/regulering etter modenhet | `figurer/kap09-trendradar-v1.svg/pdf` | Leif Ødegaard + trendteam; datainnsamling uke 5, levering uke 6 |
| Appendiks – Ressursikoner | Fortsatt uadressert | Utvikle ikonsett for ressurskategorier (datasett, verktøy, kurs, nettverk) til digital distribusjon | `figurer/app-ressurser-ikoner-v1.svg/pdf` | Astrid Hauge; starter etter hovedfigurer, ferdig uke 6 |

## Leveranse- og kvalitetskriterier
- Hver figur skal ha versjonslogg i commit-melding og i kapittelfilens kommentarblokk.
- Alt-tekst og metadata lagres i `support/figurer/metadata/kapXX-tema-vY.alt.md` og lenkes fra kapittelfilen med kommentar (`% Alt-tekst: kapXX-tema-vY.alt.md`).
- Ved bruk av data, legg ved kildehenvisning i figurtekst og i `referanser.bib`.
- Fagansvarlig signerer av for faglig korrekthet; grafisk ansvarlig for layout; prosjektleder for helhetlig stil.

## Neste steg
1. Koordinere storyboard-arbeid for kapittel 1–3 i uke 1 (tidslinje, systemkart og kausalsløyfe) sammen med fagansvarlige og grafisk ressurs.
2. Revidere eksisterende TikZ-filer til felles palett og etablere delte stiler for kontrolltårn, læringssløyfe og dashboard-elementer før kapittel 5–6-produksjon.
3. Planlegge uke 3–5 workshops med grafisk team for governance-/modenhetsfigurer, casekart og trendradar, samt sikre at nødvendige data- og ikonbibliotek legges i `support/figurer/kilder`.
