# -*- coding: utf-8 -*-
from build import dester
from content.shared import hulpbox, contactbox, links_rail

CRUMB = {"/checklists/": "Checklists"}

ALL = [
    ("/checklists/ontruiming-voorbereiden/", "Ontruiming voorbereiden"),
    ("/checklists/oplevering-huurwoning/", "Oplevering huurwoning"),
    ("/checklists/na-overlijden/", "Na een overlijden"),
    ("/checklists/verhuizing-naar-zorginstelling/", "Verhuizing naar een zorginstelling"),
]


def _p(url, title, h1, description, intro, blocks, rail, prio="0.6"):
    return {"url": url, "title": title, "h1": h1, "description": description,
            "intro": intro, "blocks": blocks, "rail": rail, "priority": prio,
            "crumb_labels": CRUMB}


def _rail(exclude):
    return [links_rail("Checklists", [x for x in ALL if x[0] != exclude]),
            ("dark", "Rekenen", '<p>Volume en bandbreedte uitrekenen kan met de <a href="/tools/">tools</a>. Bedragen per woningtype staan op de <a href="/kosten/">kostenpagina</a>.</p>'),
            contactbox()]


def pages():
    out = []

    out.append(_p(
        "/checklists/",
        "Checklists bij een woningontruiming | SpoedWoningOntruiming.nl",
        "Checklists",
        "Vier checklists voor de praktijk: de ontruiming voorbereiden, een huurwoning opleveren, het traject na een overlijden en een verhuizing naar een zorginstelling.",
        "Vier lijsten die aflopen in de volgorde waarin de stappen zich in de praktijk aandienen. Bedoeld om af te vinken, niet om door te lezen.",
        [
            ("cards", [
                ("/checklists/ontruiming-voorbereiden/", "Ontruiming voorbereiden",
                 "Van het bepalen van de deadline tot de sleuteloverdracht, met de gegevens die een offerte compleet maken."),
                ("/checklists/oplevering-huurwoning/", "Oplevering huurwoning",
                 "Voorinspectie, herstelpunten, eindinspectie en het bewijs dat achteraf discussie voorkomt."),
                ("/checklists/na-overlijden/", "Na een overlijden",
                 "De eerste week, de eerste maand en de tweede maand, met de juridische keuzes op het juiste moment."),
                ("/checklists/verhuizing-naar-zorginstelling/", "Verhuizing naar een zorginstelling",
                 "Opzegtermijn, meeverhuizende spullen, Wmo-voorzieningen en het beperken van dubbele lasten."),
            ], 2),
            ("h2", "Hoe deze lijsten gebruikt worden"),
            ("p", "Elke lijst staat in chronologische volgorde en is bedoeld om uit te printen of naast het scherm te houden. Waar een stap juridische gevolgen heeft, staat er een verwijzing naar de uitleg in de kennisbank."),
        ],
        [links_rail("Checklists", ALL),
         ("dark", "Tools", '<p>De <a href="/tools/kostenindicatie/">kostenindicatie</a> en de <a href="/tools/inboedelvolume/">volumecalculator</a> rekenen in de browser, zonder dat er gegevens worden verstuurd.</p>'),
         contactbox()],
        prio="0.8",
    ))

    # ------------------------------------------------------------ voorbereiden
    out.append(_p(
        "/checklists/ontruiming-voorbereiden/",
        "Checklist: een woningontruiming voorbereiden | SpoedWoningOntruiming.nl",
        "Checklist ontruiming voorbereiden",
        "Stap voor stap van deadline tot sleuteloverdracht, inclusief de gegevens die een offerte compleet maken en de punten die achteraf tot meerwerk leiden.",
        "Deze lijst loopt van het moment dat duidelijk is dat de woning leeg moet tot het moment dat de sleutel is afgegeven.",
        [
            ("h2", "Stap 1: de deadline vaststellen"),
            ("check", [
                "Noteer de datum waarop de woning leeg moet zijn en wie die datum bepaalt.",
                "Reken twee werkdagen speling in voor tegenvallers.",
                "Controleer of er een voorinspectie gepland moet worden en wanneer die plaatsvindt.",
                "Ga na wie de sleutel heeft en wie hem in ontvangst neemt.",
            ]),
            ("h2", "Stap 2: de woning in kaart brengen"),
            ("check", [
                "Loop elke ruimte langs, ook zolder, kelder, berging, garage, balkon en tuin.",
                "Maak per ruimte foto's, ook van volle kasten, en een videorondje van twee minuten.",
                "Noteer of er vloerbedekking of laminaat uit moet en om hoeveel vierkante meter het gaat.",
                "Kijk of er zware of bijzondere zaken zijn: piano, kluis, aquarium, bad, cv-ketel.",
                "Controleer de bereikbaarheid: verdieping, lift, trapbreedte, parkeren voor de deur.",
                "Zoek naar bergingen of garageboxen op een ander adres.",
            ]),
            ("h2", "Stap 3: scheiden wat blijft"),
            ("check", [
                "Zet administratie, polissen, testamenten en eigendomsbewijzen apart.",
                "Zet sieraden, munten, horloges en klokken apart en fotografeer ze.",
                "Zet telefoons, laptops, tablets en externe schijven apart.",
                "Loop kleding, boeken en laden na op contant geld en enveloppen.",
                "Leg vast wie welke persoonlijke zaken krijgt, voordat er iets uit de woning verdwijnt.",
            ]),
            ("h2", "Stap 4: offertes"),
            ("check", [
                "Vraag twee of drie offertes op, bij voorkeur na een opname op locatie.",
                "Geef bij elke aanvrager dezelfde gegevens, anders zijn de bedragen niet vergelijkbaar.",
                "Controleer of alle ruimtes met naam in de offerte staan.",
                "Controleer of afvoer, stortkosten, bezemschoon en eventueel herstel inbegrepen zijn.",
                "Controleer of het bedrag inclusief of exclusief btw is.",
                "Vraag naar de aansprakelijkheidsverzekering en naar het KvK-nummer.",
            ]),
            ("h2", "Stap 5: de uitvoeringsdag"),
            ("check", [
                "Meld de ontruiming bij buren, corporatie of vereniging van eigenaren als de lift of het portiek gebruikt wordt.",
                "Regel een parkeerplaats of een ontheffing wanneer dat in de straat nodig is.",
                "Zorg dat de woning toegankelijk is en dat alle sleutels aanwezig zijn.",
                "Laat weten welke categorieën spullen apart gelegd moeten worden.",
                "Wees aanwezig bij de start, ook bij een sleutelafspraak, of laat iemand dat doen.",
            ]),
            ("h2", "Stap 6: afronden"),
            ("check", [
                "Loop de woning na op restanten in kasten, op zolder en in de berging.",
                "Maak foto's van elke lege ruimte, met datum.",
                "Noteer de meterstanden van gas, water en elektra.",
                "Zeg energiecontract, internet, verzekeringen en abonnementen op.",
                "Regel doorsturen van de post via https://www.postnl.nl.",
                "Geef de sleutel pas af na een ondertekend opleverformulier.",
                "Bewaar de factuur, de foto's en het opleverformulier bij elkaar.",
            ]),
            ("note", "De vier posten die achteraf opduiken",
             "<p>Een volle zolder die niet is bekeken, een gelijmde vloer, een tuin met schuur, en een garagebox op een ander adres. Wie die vier vooraf controleert, voorkomt vrijwel al het meerwerk.</p>"),
            ("partner", "Opname en vaste prijs",
             "<p>%s neemt de woning ter plaatse op en legt daarna een vaste prijs vast, zonder voorrijkosten. Zie %s.</p>"
             % (dester("/", kind="brand"), dester("/offerte/", kind="bare"))),
        ],
        _rail("/checklists/ontruiming-voorbereiden/"),
        prio="0.7",
    ))

    # ------------------------------------------------------------ oplevering
    out.append(_p(
        "/checklists/oplevering-huurwoning/",
        "Checklist: huurwoning opleveren zonder naheffing | SpoedWoningOntruiming.nl",
        "Checklist oplevering huurwoning",
        "Van het opzoeken van het opnameformulier tot de sleuteloverdracht, met de punten waar verhuurders bij de eindinspectie op letten.",
        "Deze lijst is gericht op het voorkomen van een rekening achteraf. De volgorde volgt het traject van huuropzegging tot sleuteloverdracht.",
        [
            ("h2", "Voorbereiding"),
            ("check", [
                "Zoek het opnameformulier of de beschrijving uit de begintijd van de huur op.",
                "Vraag bij de verhuurder een kopie op wanneer dat document ontbreekt.",
                "Zoek schriftelijke toestemmingen voor zelf aangebrachte voorzieningen op.",
                "Vraag de voorinspectie schriftelijk aan zodra de huur is opgezegd.",
                "Vraag het ZAV-reglement of het opleverbeleid van de corporatie op.",
            ]),
            ("h2", "Tijdens de voorinspectie"),
            ("check", [
                "Loop mee door elke ruimte en laat elk punt noteren.",
                "Vraag expliciet of vloerbedekking en laminaat mogen blijven liggen.",
                "Vraag welke muurkleuren hersteld moeten worden.",
                "Vraag of zelf geplaatste voorzieningen blijven, weg moeten of worden overgenomen.",
                "Vraag om het rapport op papier of per e-mail en controleer of alles erin staat.",
                "Vraag een indicatie van wat de verhuurder rekent wanneer een punt niet wordt hersteld.",
            ]),
            ("h2", "Herstelpunten die het vaakst terugkomen"),
            ("check", [
                "Schroeven en pluggen eruit, gaten dichten en bijwerken.",
                "Afwijkende muurkleuren dekkend overschilderen.",
                "Vloerbedekking of laminaat eruit, inclusief lijmresten en plinten.",
                "Beschadigde deuren, tegels en kozijnen herstellen.",
                "Silicone in badkamer en keuken vervangen wanneer die verkleurd of los is.",
                "Tuin onderhouden opleveren: onkruid weg, snoeiwerk gedaan, geen bouwafval.",
                "Berging, zolder en kruipruimte leeg.",
                "Rookmelders en verlichting aanwezig en werkend.",
            ]),
            ("h2", "De laatste dag"),
            ("check", [
                "Woning leeg, geveegd en toegankelijk, alle ruimtes open.",
                "Foto's van elke ruimte met datum, ook van de berging en de tuin.",
                "Meterstanden noteren en laten aftekenen.",
                "Alle sleutels tellen: voordeur, achterdeur, berging, brievenbus, centrale toegang.",
                "Het voorinspectierapport punt voor punt aflopen met de inspecteur.",
                "Ondertekend opleverformulier meenemen of per e-mail laten toesturen.",
            ]),
            ("h2", "Na afloop"),
            ("check", [
                "Bewaar foto's, opleverformulier en correspondentie minimaal een jaar.",
                "Controleer de eindafrekening van huur en servicekosten.",
                "Meld een adreswijziging bij gemeente, bank, verzekeraar en werkgever.",
                "Controleer of de huurtoeslag is stopgezet.",
            ]),
            ("note", "Als er toch een rekening komt",
             "<p>Vraag om onderbouwing met het inspectierapport en met facturen. Zonder voorinspectie kan een verhuurder in beginsel alleen de kosten vorderen die de huurder zelf zou hebben gemaakt. Meer daarover staat op de pagina over <a href=\"/kennisbank/oplevering-en-beschrijving/\">oplevering en beschrijving</a>.</p>"),
            ("partner", "Oplevering laten uitvoeren",
             "<p>%s levert op conform de eisen van de corporatie of makelaar, inclusief vloeren, herstel en schoonmaak. Zie %s.</p>"
             % (dester("/", kind="brand"), dester("/bezemschoon-opleveren/", kind="bare"))),
        ],
        _rail("/checklists/oplevering-huurwoning/"),
        prio="0.7",
    ))

    # ------------------------------------------------------------ na overlijden
    out.append(_p(
        "/checklists/na-overlijden/",
        "Checklist: woning en nalatenschap na een overlijden | SpoedWoningOntruiming.nl",
        "Checklist na een overlijden",
        "Wat er in de eerste week, de eerste maand en de tweede maand geregeld moet worden rond de woning, de nalatenschap en de oplevering.",
        "Deze lijst gaat over de praktische en juridische kant rond de woning. De uitvaart zelf blijft buiten beschouwing.",
        [
            ("h2", "De eerste week"),
            ("check", [
                "Overlijdensakte aanvragen bij de gemeente van overlijden, meerdere exemplaren.",
                "Controleren of er een testament is via het Centraal Testamentenregister, https://www.centraaltestamentenregister.nl.",
                "De woning afsluiten en nagaan wie er sleutels heeft.",
                "Administratie, polissen, sieraden en digitale apparaten veiligstellen.",
                "Verhuurder informeren met een kopie van de overlijdensakte.",
                "Banken en verzekeraars informeren.",
                "Post laten doorsturen zodat de brievenbus niet vol raakt.",
            ]),
            ("h2", "De eerste maand"),
            ("check", [
                "Keuze maken over de nalatenschap: zuiver aanvaarden, beneficiair aanvaarden of verwerpen.",
                "Bij twijfel over schulden: beneficiair aanvaarden bij de griffie van de rechtbank.",
                "Nagaan of een verklaring van erfrecht nodig is en die eventueel aanvragen.",
                "Huur laten eindigen tegen het eind van de eerste maand wanneer dat gunstiger uitvalt.",
                "Voorinspectie aanvragen bij de verhuurder en het rapport opvragen.",
                "Abonnementen, energiecontract, internet en verzekeringen opzeggen per de opleverdatum.",
                "Waardevolle spullen laten taxeren, maar nog niets verkopen.",
            ]),
            ("warn", "Nog niet verkopen of verdelen",
             "<p>Het verkopen of verdelen van waardevolle spullen geldt als een beschikkingshandeling en leidt tot zuivere aanvaarding, met persoonlijke aansprakelijkheid voor schulden. Ruimen, opslaan en afvoeren van zaken zonder waarde mag wel. Zie <a href=\"/kennisbank/erfenis-aanvaarden/\">erfenis aanvaarden of verwerpen</a>.</p>"),
            ("h2", "De tweede maand"),
            ("check", [
                "Offertes voor de ontruiming opvragen, bij voorkeur na opname op locatie.",
                "Familie een dag geven om persoonlijke zaken te kiezen, met de verdeling op papier.",
                "Ontruiming laten uitvoeren, inclusief herstelpunten uit de voorinspectie.",
                "Eindschoonmaak en foto's van de lege woning.",
                "Eindinspectie, meterstanden en sleuteloverdracht.",
                "Facturen bewaren voor de afwikkeling van de nalatenschap en de aangifte erfbelasting.",
            ]),
            ("h2", "Waarom de tweede maand telt"),
            ("p", "Woonde de overledene alleen en is er geen medehuurder, dan eindigt de huurovereenkomst aan het eind van de tweede maand na het overlijden. Erfgenamen kunnen die termijn verkorten tot het eind van de eerste maand. Dat volgt uit artikel 7:268 lid 6 van het Burgerlijk Wetboek en staat uitgelegd op de pagina over %s."
             % '<a href="/kennisbank/huur-opzeggen-na-overlijden/">huur opzeggen na overlijden</a>'),
            ("h2", "Bij een koopwoning"),
            ("check", [
                "Verklaring van erfrecht aanvragen, want zonder dat document kan er niet worden overgedragen.",
                "Opstalverzekering aanhouden zolang de woning niet is verkocht.",
                "Doorlopende lasten in beeld brengen: hypotheekrente, heffingen, energie en servicekosten.",
                "Woning leeghalen voordat de bezichtigingen starten.",
                "Makelaar of taxateur inschakelen voor de vraagprijs.",
            ]),
            ("partner", "Ontruiming na overlijden",
             "<p>%s werkt op sleutelbasis, houdt gevonden documenten en waardevolle zaken apart en levert bezemschoon op. Zie %s.</p>"
             % (dester("/", kind="brand"), dester("/woning-na-overlijden/", kind="bare"))),
        ],
        _rail("/checklists/na-overlijden/"),
        prio="0.7",
    ))

    # ------------------------------------------------------------ zorg
    out.append(_p(
        "/checklists/verhuizing-naar-zorginstelling/",
        "Checklist: verhuizing naar een zorginstelling | SpoedWoningOntruiming.nl",
        "Checklist verhuizing naar een zorginstelling",
        "Van opnamedatum tot sleuteloverdracht: opzegtermijn, meeverhuizende spullen, Wmo-voorzieningen en het beperken van dubbele lasten.",
        "Bij een opname in een verpleeghuis of aanleunwoning loopt alles tegelijk. Deze lijst zet de stappen op volgorde, met de dubbele lasten als leidraad.",
        [
            ("h2", "Direct na de opnamedatum"),
            ("check", [
                "Huur opzeggen, doorgaans met een opzegtermijn van een maand.",
                "Voorinspectie aanvragen bij de verhuurder.",
                "Nagaan of er een volmacht, bewind of curatele is voor het regelen van zaken.",
                "Adreswijziging doorgeven aan gemeente, bank, zorgverzekeraar en pensioenfonds.",
                "Contact opnemen met het CAK over de eigen bijdrage, https://www.hetcak.nl.",
            ]),
            ("h2", "De nieuwe kamer"),
            ("check", [
                "De kamer opmeten en de indeling tekenen voordat er wordt ingepakt.",
                "Navragen wat de instelling standaard levert, en of eigen meubels aan brandveiligheidseisen moeten voldoen.",
                "Vijf tot tien persoonlijke voorwerpen kiezen die zeker meegaan.",
                "Kleding merken wanneer de instelling dat vraagt in verband met de was.",
                "Een fotoboek maken van de oude woning, zodat het beeld blijft zonder de spullen.",
            ]),
            ("h2", "De oude woning"),
            ("check", [
                "Wmo-voorzieningen melden bij de gemeente zodat de leverancier ze ophaalt.",
                "Nagaan of berging, garagebox of parkeerplaats apart opgezegd moet worden.",
                "Familie een dag geven om te kiezen, met de verdeling op papier.",
                "Waardevolle spullen apart zetten en laten taxeren.",
                "Offertes opvragen voor de ontruiming, inclusief het verwijderen van de vloer.",
                "Ontruiming plannen ruim voor de opleverdatum, niet in de laatste week.",
            ]),
            ("h2", "Financieel"),
            ("check", [
                "De periode met dubbele lasten in beeld brengen en zo kort mogelijk houden.",
                "Huurtoeslag stopzetten per de einddatum van de huur.",
                "Bij een koopwoning: nagaan wat de verkoop betekent voor de eigen bijdrage.",
                "Automatische incasso's van de oude woning beëindigen.",
                "Energiecontract, internet en verzekeringen opzeggen per de opleverdatum.",
            ]),
            ("note", "Het tempo bepaalt de ervaring",
             "<p>Wanneer familie eerst rustig kiest en een bedrijf daarna het zware werk doet, blijft de emotionele kant gescheiden van het sjouwen. Dat is bij dit soort verhuizingen belangrijker dan het verschil van enkele honderden euro's tussen offertes.</p>"),
            ("partner", "Seniorenwoning ontruimen",
             "<p>%s ontruimt seniorenwoningen met ruimte voor familie om eerst te kiezen wat blijft. Zie %s.</p>"
             % (dester("/", kind="brand"), dester("/seniorenwoning-ontruimen/", kind="bare"))),
        ],
        _rail("/checklists/verhuizing-naar-zorginstelling/"),
    ))

    return out
