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
