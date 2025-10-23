# Notat: Havvind-case – Sørlige Nordsjø II og Hywind Tampen

## Hovedidé og læringsmål
- Vise hvordan flytende havvind kan støttes av en digital tvilling som koordinerer produksjon, vedlikehold og energiintegrasjon mot norsk sokkel.
- Knytte kapittel 7 til styrings- og dataspace-prinsipper for flere rettighetshavere.
- Utvide kapittel 8 med et konkret fornybar-case som speiler nasjonale klimamål og elektrifisering av sokkelen.

## Datakilder og integrasjoner
- Sanntids produksjons- og tilstandsmålinger fra turbiner, eksportkabler og understasjoner (SCADA og edge-noder).
- Vær- og bølgeprognoser fra Meteorologisk institutt (Frost API) og operasjonelle havdata fra BarentsWatch.
- Vedlikeholdslogger fra operatør (Equinor) koblet til logistikkdata for servicefartøy.
- Regulering og lisensdata fra NVE, inkludert områdeallokering og nettverkskapasitet.

## KPI-er og gevinstindikatorer
| Dimensjon | KPI | Datakilde | Beslutningsfrekvens |
| --- | --- | --- | --- |
| Produksjon | Kapasitetsfaktor (%) og energileveranse (MWh per uke) | Turbin- og nettdata (SCADA) | Daglig og ukentlig |
| Vedlikehold | Antall korrigerende oppdrag vs. planlagte kampanjer | Vedlikeholdssystem og logistikkplan | Ukentlig |
| Sikkerhet | Registrerte HSE-observasjoner og værvinduer under terskel | HSE-rapport og værvarsling | Månedlig |
| Klimanytte | Redusert dieselbruk på sokkelen (tonn CO$_2$) | Kombinasjon av produksjonsdata og utslippsfaktorer | Kvartalsvis |

## Dataspace-implikasjoner
- Havvindoperatører må samhandle med TSO (Statnett), olje- og gassinstallasjoner og myndigheter.
- Bruk Gaia-X/IDSA-prinsipper for å sikre dataprodukter med tydelige policyer (tilgangsnivå, konfidensialitet, ansvar).
- Krever identitets- og tilgangstjenester som støtter både offshore drift og leverandørkjeder.

## Kilder og videre lesing
- NVE (2023). «Fakta om havvind i Norge». Tilgjengelig via https://www.nve.no/energi/energisystem/offshore-vindkraft/fakta-om-havvind/. 
- Equinor (2023). «Hywind Tampen». Tilgjengelig via https://www.equinor.com/energy/hywind-tampen.
- International Data Spaces Association (2023). «IDS Reference Architecture Model 4.0». https://internationaldataspaces.org/use/dataspace-architecture/.
