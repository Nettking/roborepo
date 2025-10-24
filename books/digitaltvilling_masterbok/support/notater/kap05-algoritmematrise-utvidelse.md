# Kapittel 5 – Algoritmematrise for immersiv AI-lab

## Formål
Dette notatet utvider algoritmematrisen i kapittelteksten med fokus på multimodale datasett og operatørsamhandling i AR/VR-miljøer. Tabellen brukes både som beslutningsstøtte i prosjektoppgaven og som grunnlag for evalueringen av laboratorieøvingene.

## Utvidet algoritmematrise
| Datakilde/Modalitet | Anbefalt algoritme | Støtteverktøy og modeller | Dokumenterte kontrollpunkter |
| --- | --- | --- | --- |
| Streaming av tidsserier + 3D-mesh fra inspeksjonsdrone | Temporal Fusion Transformer kombinert med grafnevrale nett (GNN) for geometriske avvik. | PyTorch Forecasting, DGL + ONNX for eksport til edge. | Sørg for konfidensbånd i dashboardet; valider mot feltmålinger hver uke. |
| Taleinstruksjoner fra operatører (norsk) + sensordata | Multimodal transformer (ASR + tabulære embeddings) med aktiv læring for nye uttrykk. | HuggingFace Whisper + TabNet, MLflow for versjonskontroll. | Loggfør alle manuelle korreksjoner; dokumenter språkmodellens usikkerhet i tiltaksløypen. |
| Haptiske input (AR-hansker) + simulert responstid | Bayesiansk optimalisering for parameterjustering av simuleringsmodeller. | BoTorch, AnyLogic API, Azure ML pipelines. | Definer sikkerhetsgrenser for taktile tilbakemeldinger; stress-test med latensscenarier. |
| Videostrøm fra operatørkamera + vedlikeholdslogg | Spatio-temporal CNN med selvtilsyn (contrastive learning). | OpenCV, PyTorch Lightning, Data Version Control (DVC). | Sørg for anonymisering av persondata; registrer avvik i kontrolltårnreferansen i Kapittel 6. |

## Evalueringsrubrikk for laboratorieøving
| Kriterium | Poeng (0–3) | Beskrivelse |
| --- | --- | --- |
| Datasamsvar | 0–3 | Kartlegger hvordan hver modalitet forankres i dataplattformen og beskriver sanntidskrav. |
| Algoritmevalg | 0–3 | Argumenterer med referanse til matrisen over og dokumenterer hvordan modellene valideres. |
| Operatøropplevelse | 0–3 | Viser hvordan forklaringer og tiltak presenteres i AR/VR-panelet, inkludert fallback-løsninger. |
| Etterlevelse | 0–3 | Beskriver hvordan tiltakene harmoniseres med \citet{iec62443-2-1} og \citet{eu2022nis2}. |
| Refleksjon | 0–3 | Diskuterer forbedringer etter laboratorieprøven og peker på videre arbeid i kapittel 6 og 7. |

En poengsum på 12 eller mer regnes som «godkjent». Rubrikken publiseres sammen med laboratorieinstruksen og brukes av både faglærer og medstudent som fagfelle.

## Implementasjonsnotater
- Matrisen skal deles som eget vedlegg (PDF/LaTeX-tabell) til kapittel 5 og lenkes fra læringsplattformen.
- Prosjektteamet dokumenterer hvilke rader som er relevante for deres case i fagfelleloggen og refererer til dette i prosjektpresentasjonen.
- Når modellen driftes, må oppdateringer i algoritmevalg loggføres i samsvar med kontrolltårn-prosedyren i Kapittel 6 og governance-strukturen i Kapittel 7.

## Operatørreise og styringspunkter
1. **Flerkanals datainntak:** Kombiner sanntidsstrømmer, historikk og syntetiske scenarioer. Bruk metadatafelt som beskriver modalitet, versjon og kvalitetsflagger slik at laboratorierubrikken kan verifisere datasamsvar.
2. **Algoritmeallokering:** Velg modell per modalitet fra tabellen ovenfor, og angi måltall og kontrollpunkter i prosjektloggen. Husk å begrunne eventuelle avvik i fagfelleloggen.
3. **Operatørdialog:** Prototyp AR/VR-panelet med forklaringer, taktile tilbakemeldinger og mulighet for what-if-simuleringer. Registrer dialogen slik at operatøropplevelsen kan evalueres.
4. **Tiltaksoppfølging:** Lever beslutningslogg til kontrolltårnet, koble tiltakene til \citet{iec62443-2-1} og \citet{eu2022nis2}, og oppdater plan for neste iterasjon.

## Kobling til vurderingsrubrikken
- **Datasamsvar og kvalitet:** Bruk metadataark og versjonskontroll for å vise at hver datapakke har sporbarhet. Marker syntetiske bidrag og lagre kontrollrapporter i læringsplattformen.
- **Algoritmevalg og begrunnelse:** Dokumenter hyperparametere, ytelsesmål og hvorfor valg av algoritme passer modaliteten. Sett opp alarmgrenser for konseptdrift.
- **Operatøropplevelse og forklaringer:** Beskriv hvordan operatøren kan be om forklaringer, pause anbefalinger og logge tiltak. Legg ved skjermbilder fra AR/VR-panelet.
- **Edge--sky-samspill:** Tegn oppdateringssløyfen mellom edge-noder og sky, og vis hvordan fallback aktiveres. Registrer latensmålinger.
- **Etterlevelse, refleksjon og forbedring:** Oppsummer hvilke standarder som er brukt, hvordan revisjon skjer over tid, og hvilke forbedringer som planlegges neste sprint.
