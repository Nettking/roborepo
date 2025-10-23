# Notat: Batteriverdikjede – Giga Arctic i Mo i Rana

## Hovedidé og læringsmål
- Vise hvordan en digital tvilling kan følge hele batteriverdikjeden fra råvarelogistikk til ferdig celle ved FREYR Battery sin Giga Arctic-fabrikk.
- Knytte kapittel 7 til gevinstrealisering og partnerskap mellom industripark, energiselskap og teknologiaktører.
- Støtte kapittel 8 sin casemal med oppdaterte KPI-er, datakilder og dataspace-krav.

## Datakilder og integrasjoner
- Prosessdata fra elektrodemiksing, coating og forming, eksponert via OPC UA og historikere.
- Energi- og effektdata fra Statkraft/Helgeland Kraft, samt lokale mikronettmålinger.
- Logistikk- og lagerdata fra ERP/MES (SAP S/4HANA, Siemens Opcenter) og transportpartnere i Mo Industripark.
- Kvalitets- og bærekraftdata knyttet til EU-batteriforordningen (pass, resirkulering, karbonfotavtrykk).

## KPI-er og gevinstindikatorer
| Dimensjon | KPI | Datakilde | Beslutningsfrekvens |
| --- | --- | --- | --- |
| Produksjon | First-pass yield (%) og syklusstabilitet etter 100 sykluser | Kvalitetslaboratorium + produksjonsdata | Daglig |
| Energi | Energiforbruk (kWh per GWh produsert) og peak load | Energi-overvåking og nettdata | Time og døgn |
| Logistikk | Ledetid for råvarepartier og lagerdager ferdig vare | ERP/MES og partnerportaler | Ukentlig |
| Bærekraft | CO$_2$-intensitet per celle og andel resirkulert materiale | Bærekraftsrapportering og leverandørdata | Månedlig |

## Dataspace-implikasjoner
- Fabrikken inngår i norsk batteridataspace der produsenter, energiselskaper og transportører deler dataprodukter med kontraktsstyrt tilgang.
- Krever integrasjon mellom lokale edge-noder (for prosesskontroll) og skybasert plattform (for analyse, AI og rapportering).
- Dataspace-policy bør speile EU-batteripass-krav og legge til rette for revisjon av karbonregnskapet.

## Kilder og videre lesing
- FREYR Battery (2024). «Giga Arctic Project Update». Tilgjengelig via https://www.freyrbattery.com/giga-arctic.
- Enova (2023). «Støtte til batteriproduksjon i Norge». https://www.enova.no/bedrift/transport/batteriproduksjon-i-norge/.
- Gaia-X AISBL (2023). «Gaia-X Architecture Document 22.10». https://gaia-x.eu/wp-content/uploads/2023/03/Gaia-X-Architecture-Document-22.10.pdf.
