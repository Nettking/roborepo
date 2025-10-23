# Illustrasjons- og grafikkplan

> Notat (2024-05-08): Utarbeidet plan for å løfte kladdeillustrasjoner til ferdige figurer og etablere felles stil på tvers av kapitlene.

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

## Oversikt per kapittel og leveranse

| Kapittel/element | Kladd/status i dag | Tiltak for ferdigstilling | Format og filnavn | Ansvar og tidslinje |
| --- | --- | --- | --- | --- |
| Kap. 1 – Introduksjon: historisk tidslinje | Tekstlig beskrivelse av milepæler, ingen figur | Utarbeide horisontal tidslinje med norske milepæler, markere industrisektorer med ikoner | `figurer/kap01-tidslinje-v1.tikz` (+ PDF) | Ingrid Lunde klargjør manus, grafiker ferdigstiller innen uke 2 før fagfellelesing |
| Kap. 2 – Figur 2.1 systemkart | Mermaid-kode i kapitteltekst | Gjenskape i TikZ med definert palett, legge til ikon for hvert aktør-lag og tydelige dataetiketter; exportere både farge og gråtoneversjon | `figurer/kap02-systemkart-v1.tikz` og `-v1.pdf` | Ahmed Solheim leder produksjon, førsteutkast uke 1, review med Ingrid |
| Kap. 2 – Figur 2.2 kausalsløyfe | Mermaid-kode i kapitteltekst | Redesign som sirkulær diagram i TikZ; markere positive/negative koblinger med ikon + stiplet linje | `figurer/kap02-kausal-v1.tikz` | Ahmed Solheim + temaekspert; ferdig uke 1 |
| Kap. 3 – Datapipeline (Figur~\ref{fig:kap3-datapipeline}) | TikZ-figur eksisterer, men fargekoder og tekst varierer fra ønsket standard | Refaktorere til felles palett, justere tekststørrelser til 8/9 pt, legge inn ikon for governance-blokk og eksportere versjonert PDF | Oppdatere `kapittel03-data.tex` + `figurer/kap03-datapipeline-v2.tikz/pdf` | Ahmed Solheim ferdigstiller uke 2, kvalitetssjekk av Nora Aas |
| Kap. 4 – Simuleringsmetodematrise | Ingen figur; behov uttrykt i kapittel og plan | Lage 2x2 matrise som kartlegger deterministisk/stokastisk vs. diskret/kontinuerlig, med eksempler fra tekst | `figurer/kap04-matrise-v1.svg` (+ PDF) | Nora Aas utarbeider skisse, grafiker leverer uke 3 |
| Kap. 4 – Analyseflyt | Tekst beskriver arbeidsflyt | Utforme prosessdiagram (input–modell–analyse–visualisering) som kan gjenbrukes i undervisning | `figurer/kap04-analyseflyt-v1.tikz` | Nora Aas, ferdigstilles uke 3 |
| Kap. 5 – ML/optimalisering samspill | Ingen figur | Lage lagdelt arkitekturfigur som viser ML-moduler koblet mot optimalisering og datakilder | `figurer/kap05-mlflow-v1.tikz` | Nora Aas initierer storyboard uke 2, ferdig uke 4 |
| Kap. 6 – Valideringsrammeverk | Tekst refererer til rammeverk og kontrollpunkter | Skape «kontrolltårn»-illustrasjon som viser modellversjoner, datasett og beslutningsportaler | `figurer/kap06-validering-v1.svg` | Leif Ødegaard fasiliterer, ferdig uke 4 |
| Kap. 7 – Livssyklusdiagram | Planen etterspør grafisk fremstilling | Produsere sirkel/timeline med faser og governance-artefakter; markere RACI-eksempel som callout | `figurer/kap07-livssyklus-v1.tikz` | Leif Ødegaard, ferdig uke 2 før intervjuer |
| Kap. 8 – Caseoversikt | Kapittel beskriver sektorseksjoner | Lage matrix/galleri med sektorer og nøkkelindikatorer; eventuelt kart over Norge med case | `figurer/kap08-casekart-v1.svg` | Ingrid Lunde + sektoreiere, ferdig uke 4 |
| Kap. 9 – FoU-roadmap | Kapittel omtaler trender og prosjektforslag | Designe roadmap med kortsiktige/langsiktige initiativ og tilhørende aktører | `figurer/kap09-roadmap-v1.tikz` | Leif Ødegaard, ferdig uke 4 |
| Appendiks – Ressurser | Tabeller eksisterer, ingen grafikk | Valgfri ikonserie for ressurskategorier for bruk i digitale versjoner | `figurer/app-ressurser-ikoner-v1.svg` | Astrid Hauge, levering etter hovedfigurer (uke 5) |

## Leveranse- og kvalitetskriterier
- Hver figur skal ha versjonslogg i commit-melding og i kapittelfilens kommentarblokk.
- Alt-tekst dokumenteres i kapittelkommentar eller egen `.alt`-fil i `figurer/kilder`.
- Ved bruk av data, legg ved kildehenvisning i figurtekst og i `referanser.bib`.
- Fagansvarlig signerer av for faglig korrekthet; grafisk ansvarlig for layout; prosjektleder for helhetlig stil.

## Neste steg
1. Definere farger i `main.tex` (egen PR).
2. Starte med konvertering av Kapittel 2-figurene (Mermaid → TikZ) og refaktorering av Kapittel 3-figuren.
3. Forberede storyboardmal (PowerPoint eller LaTeX) for nye figurer og lagre i `support/figurer/kilder`.
