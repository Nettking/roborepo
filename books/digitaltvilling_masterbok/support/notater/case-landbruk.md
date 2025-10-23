# Notat: Landbrukscase – Presisjonsjordbruk i Trøndelag

## Hovedidé og læringsmål
- Utforske hvordan en digital tvilling av gårdsdrift kan kombinere sanntidsdata fra felt, maskiner og klimamodeller for å redusere utslipp og øke avlinger.
- Knytte kapittel 7 til styring av samarbeid mellom bønder, rådgivere og teknologileverandører.
- Utvide kapittel 8 med et landbrukscase som viser verdien av datadeling mellom landbruksforetak, NIBIO og fôrprodusenter.

## Datakilder og integrasjoner
- Sensorer i jord og plantebestand (fukt, næringsinnhold, NDVI) koblet via LoRaWAN eller 5G edge-gatewayer.
- Maskindata fra traktorer og redskap (ISO 11783/ISOBUS) med telematikk fra produsenter som John Deere Operations Center.
- Offentlige datakilder: NIBIOs arealressurskart (AR5), Meteorologisk institutt (Frost API), Landbruksdirektoratets søknads- og tilskuddsdata.
- Markedspriser på korn og melk fra SSB/landbrukskooperativer for å koble agronomi til økonomi.

## KPI-er og gevinstindikatorer
| Dimensjon | KPI | Datakilde | Beslutningsfrekvens |
| --- | --- | --- | --- |
| Agronomi | Avlingsprognose (kg/daa) og avvik mot målsatt nivå | Feltdata + historiske avlinger | Ukentlig i vekstsesong |
| Ressurseffektivitet | Nitrogenutnyttelse (%) og drivstoff per hektar | Gjødselplan + maskintelematikk | Månedlig |
| Bærekraft | Klimagassutslipp per produsert enhet (CO$_2$-ekv./kg) | Klimakalkulator + produksjonsdata | Sesongvis |
| Samhandling | Delingsgrad av data i dataspace (antall aktive dataprodukter) | Dataspace-logg | Kvartalsvis |

## Dataspace-implikasjoner
- Landbruket trenger tillitstjenester som lar gårdbrukere kontrollere deling av feltdata med leverandører og forskningsmiljøer.
- Dataproduktene bør følge IDSA-kontrakter som regulerer bruk av rådata, agronomiske anbefalinger og avregningsgrunnlag.
- Edge-prosessering på maskiner reduserer behov for å sende rådata, men tvillingen må synkronisere aggregater i skyen for analyse og rapportering.

## Kilder og videre lesing
- NIBIO (2023). «Dataflyt for smartere agronomi». Tilgjengelig via https://www.nibio.no/tema/teknologi/presisjonsjordbruk/dataflyt-for-smartere-agronomi.
- Landbruksdirektoratet (2023). «Digitaliseringsstrategi for landbruket». https://www.landbruksdirektoratet.no/nb/strategier/digitaliseringsstrategi-for-landbruket.
- ETSI (2023). «Multi-access Edge Computing (MEC); Framework and Reference Architecture» (ETSI GS MEC 003). https://www.etsi.org/deliver/etsi_gs/MEC/001_099/003/03.01.01_60/gs_mec003v030101p.pdf.
