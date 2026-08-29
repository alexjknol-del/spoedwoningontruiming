# -*- coding: utf-8 -*-
from build import dester
from content.shared import ONTRUIM_LINKS, hulpbox, contactbox, links_rail

CRUMB = {"/kosten/": "Kosten"}


def _p(url, title, h1, description, intro, blocks, rail, prio="0.7"):
    return {"url": url, "title": title, "h1": h1, "description": description,
            "intro": intro, "blocks": blocks, "rail": rail, "priority": prio,
            "crumb_labels": CRUMB}


PRIJSTABEL = ["Type woning of ruimte", "Bandbreedte", "Waar het verschil in zit"], [
    ["Zorgkamer of verzorgingskamer", "250 tot 550 euro", "Weinig volume, vaak een lift en korte looplijn"],
    ["Studio of eenkamerappartement", "350 tot 750 euro", "Een halve dag werk, meestal een ritje afvoer"],
    ["Tweekamerappartement", "550 tot 950 euro", "Verdieping, lift of trap, hoeveelheid kastruimte"],
    ["Driekamerappartement", "750 tot 1.250 euro", "Berging en balkon tellen mee, vloer eruit is een aparte post"],
    ["Tussenwoning", "1.000 tot 1.800 euro", "Zolder, schuur en tuin bepalen het volume"],
    ["Hoekwoning of twee-onder-een-kap", "1.500 tot 2.500 euro", "Meer bergruimte, vaak een garage"],
    ["Vrijstaande woning", "2.000 tot 4.000 euro en hoger", "Meerdere ritten, twee dagen werk, buitenruimte"],
    ["Zwaar vervuilde woning", "2.500 tot 6.000 euro en hoger", "Bestrijding, sanering, herstel en dure afvalstromen"],
]


def pages():
    out = []

    out.append(_p(
        "/kosten/",
        "Wat kost een woningontruiming in 2026? Prijzen per woningtype | SpoedWoningOntruiming.nl",
        "Wat kost een woningontruiming",
        "Prijsbandbreedtes per woningtype voor 2026, de opbouw van de rekening, de vaste toeslagen en de vragen die de prijs bepalen.",
        "Een ontruiming wordt bijna altijd als vaste prijs afgesproken na een opname op locatie. Hieronder staan de bandbreedtes die in 2026 in de Nederlandse markt gangbaar zijn, en de factoren die bepalen waar een concrete woning binnen die bandbreedte valt.",
        [
            ("h2", "Bandbreedtes per woningtype"),
            ("p", "De bedragen hieronder gaan uit van een complete ontruiming inclusief afvoer en bezemschoon opleveren, exclusief btw. Ze gelden voor een normaal gevulde woning zonder vervuiling en zonder herstelwerk."),
            ("table", PRIJSTABEL[0], PRIJSTABEL[1]),
            ("p", "Ter vergelijking: %s publiceert dezelfde indeling met vergelijkbare bandbreedtes op %s, inclusief de meerprijs voor losse onderdelen."
             % (dester("/", kind="brand"), dester("/kosten/", kind="url"))),
            ("h2", "Wat er los bij komt"),
            ("table", ["Onderdeel", "Indicatie", "Toelichting"], [
                ["Vloerbedekking of laminaat verwijderen", "3 tot 7 euro per vierkante meter",
                 "Gelijmd zeil of tapijt kost meer dan los liggend laminaat"],
                ["Stortkosten", "100 tot 300 euro",
                 "Afhankelijk van gewicht en van het tarief van de verwerker"],
                ["Eindschoonmaak na de ontruiming", "150 tot 500 euro",
                 "Meer dan bezemschoon: keuken, sanitair en ramen"],
                ["Schroeven, pluggen en gaten", "50 tot 150 euro",
                 "Standaardpunt bij de eindinspectie van een huurwoning"],
                ["Grofvuiltransport", "100 tot 400 euro",
                 "Losse ritten wanneer niet de hele woning wordt ontruimd"],
                ["Spoed binnen 48 uur", "10 tot 30 procent opslag",
                 "Afhankelijk van hoeveel er in de planning verschuift"],
            ]),
            ("h2", "De zeven vragen die de prijs bepalen"),
            ("ol", [
                "Hoeveel kubieke meter moet eruit? Dit is de belangrijkste factor en de reden dat foto's zo veel schelen.",
                "Op welke verdieping, en is er een lift? Drie hoog zonder lift verdubbelt de tijd per kubieke meter.",
                "Kan er voor de deur geparkeerd worden? Vijftig meter sjouwen naar de wagen telt door bij elke rit.",
                "Moet de vloer eruit? Dit is de grootste losse post bij een gemiddelde woning.",
                "Is er sprake van vervuiling, ongedierte of schimmel? Dat verandert de klus fundamenteel.",
                "Wat is de gevraagde eindstaat: bezemschoon, eindschoonmaak of inclusief herstelwerk?",
                "Zit er waarde in de inboedel die verrekend kan worden?",
            ]),
            ("note", "Voorrijkosten en btw",
             "<p>Landelijk werkende bedrijven rekenen doorgaans geen voorrijkosten. Bij particuliere opdrachtgevers wordt het btw-tarief van 21 procent meestal in het genoemde bedrag verwerkt. Bij zakelijke opdrachtgevers staat het bedrag vrijwel altijd exclusief btw in de offerte, dus vergelijk offertes altijd op hetzelfde uitgangspunt.</p>"),
            ("h2", "Wat een ontruiming duurder maakt dan verwacht"),
            ("ul", [
                "Een volle zolder of kruipruimte die bij de opname niet is bekeken.",
                "Een tuin met schuur, tegels en een verwilderde beplanting.",
                "Een gelijmde vloer die alleen met een vloerenfrees los te krijgen is.",
                "Bouwafval, verf, accu's of gasflessen die als gevaarlijk afval apart moeten.",
                "Een garagebox op een ander adres die pas op de dag zelf ter sprake komt.",
            ]),
            ("h2", "Kosten van zelf afvoeren"),
            ("p", "Wie zelf ruimt, betaalt geen manuren maar wel afvoerkosten. De gemeentelijke afvalstoffenheffing stijgt in 2026 met ongeveer 3,6 procent, na 5 procent in 2025 en 6 procent in 2024, blijkt uit een steekproef van Vereniging Eigen Huis onder 106 gemeenten. De spreiding is groot: van ruim tweehonderd euro per huishouden in de laagste gemeente tot boven de vijfhonderdvijftig euro in de hoogste. Bovenop die heffing rekenen veel gemeenten per keer of per kubieke meter voor grofvuil dat opgehaald wordt."),
            ("p", "De rekensom om zelf te doen of uit te besteden staat op de pagina over %s."
             % '<a href="/kosten/zelf-doen-of-uitbesteden/">zelf doen of uitbesteden</a>'),
            ("h2", "Veelgestelde vragen"),
            ("faq", [
                ("Wat kost het ontruimen van een woning per vierkante meter?",
                 "<p>Die eenheid wordt in de praktijk zelden gebruikt, omdat de vulling meer bepaalt dan het oppervlak. Een lege woning van honderd vierkante meter is in een uur klaar, een volle van zestig kost een dag. Alleen bij vloerverwijdering wordt per vierkante meter gerekend, doorgaans 3 tot 7 euro.</p>"),
                ("Kan een woningontruiming kosteloos?",
                 "<p>Alleen wanneer de inboedel voldoende waarde vertegenwoordigt om de kosten te dekken. Dat komt voor bij woningen met edelmetaal, design of complete verzamelingen, en zelden bij een gemiddelde inboedel. Zie de pagina over <a href=\"/ontruimen/ontruimen-in-ruil-voor-inboedel/\">ontruimen in ruil voor de inboedel</a>.</p>"),
                ("Zit schoonmaak bij de prijs in?",
                 "<p>Bezemschoon opleveren zit meestal in het tarief. Een volledige eindschoonmaak is een aparte post van doorgaans 150 tot 500 euro.</p>"),
                ("Zijn er kosten achteraf?",
                 "<p>Bij een vaste prijsafspraak op basis van een opname op locatie niet. Bij een telefonische schatting wel, want dan is meerwerk bijna onvermijdelijk.</p>"),
                ("Wie betaalt bij een ontruiming na overlijden?",
                 "<p>De nalatenschap. Is die negatief en hebben de erfgenamen beneficiair aanvaard of verworpen, dan blijven de kosten bij de verhuurder of bij de boedel.</p>"),
                ("Hoe snel kan een ontruiming plaatsvinden?",
                 "<p>Veel bedrijven kunnen binnen 24 tot 48 uur, met een toeslag. Zonder spoed is een of twee weken vooruit gebruikelijk.</p>"),
            ]),
            ("partner", "Vaste prijs vooraf",
             "<p>%s werkt met een vaste prijsafspraak na een opname op locatie, zonder voorrijkosten en met bezemschoon opleveren in het tarief. De kostenpagina met tarieven per woningtype staat op %s.</p>"
             % (dester("/", kind="brand"), dester("/kosten/", kind="bare"))),
        ],
        [links_rail("Kosten", [("/kosten/kostenposten/", "Waar de rekening uit bestaat"),
                               ("/kosten/offertes-vergelijken/", "Offertes vergelijken"),
                               ("/kosten/zelf-doen-of-uitbesteden/", "Zelf doen of uitbesteden")]),
         ("dark", "Indicatie", '<p>De <a href="/tools/kostenindicatie/">kostenindicatie</a> rekent een bandbreedte uit voor een concrete situatie. Alles gebeurt in de browser, er wordt niets verstuurd.</p>'),
         links_rail("Situaties", ONTRUIM_LINKS[:4])],
        prio="0.9",
    ))

    # ------------------------------------------------------------ kostenposten
    out.append(_p(
        "/kosten/kostenposten/",
        "Waar de rekening van een ontruiming uit bestaat | SpoedWoningOntruiming.nl",
        "Waar de rekening uit bestaat",
        "De vijf posten achter de prijs van een woningontruiming: manuren, transport, verwerking, materiaal en herstel, met de verhoudingen ertussen.",
        "Een offerte noemt meestal een bedrag en niet de opbouw. Wie de vijf posten kent, ziet meteen waarom de ene woning het dubbele kost van een andere die er even vol uitziet.",
        [
            ("h2", "Post 1: manuren"),
            ("p", "De grootste post. Een ploeg van drie tot vier mensen kost inclusief werkgeverslasten, verzekering en materieel een aanzienlijk bedrag per dag. Wat de manuren opdrijft is zelden het volume zelf, maar de looplijn: derde verdieping zonder lift, een smalle trap, parkeren om de hoek, een portiek met een deur die dichtvalt."),
            ("p", "Praktische vuistregel uit de branche: drie hoog zonder lift kost ruwweg het dubbele aan tijd per kubieke meter vergeleken met de begane grond."),
            ("h2", "Post 2: transport"),
            ("p", "Een bakwagen neemt ongeveer twintig kubieke meter mee. Elke extra rit betekent laden, rijden, lossen, wachten bij de verwerker en terugrijden, wat bij een gemiddelde afstand al snel twee uur is. Daarom is het verschil tussen vijftien en vijfentwintig kubieke meter in de prijs groter dan het volumeverschil suggereert."),
            ("h2", "Post 3: verwerking"),
            ("p", "Afvalverwerkers rekenen per ton en per stroom. Restafval is de duurste, gescheiden hout, metaal en puin zijn goedkoper of leveren zelfs iets op. Elektronica, koelapparatuur, tl-buizen en gevaarlijk afval gaan tegen aparte tarieven. De afvalstoffenbelasting is per 1 januari 2026 verhoogd, wat via de verwerkers doorwerkt in de tarieven."),
            ("table", ["Stroom", "Effect op de rekening"], [
                ["Herbruikbare goederen", "Drukt de kosten, gaan naar kringloop of handel"],
                ["Hout, metaal en puin gescheiden", "Lager tarief per ton dan restafval"],
                ["Restafval", "Hoogste tarief, en de stroom die het meeste weegt"],
                ["Elektronica en witgoed", "Apart tarief, verplichte inzameling"],
                ["Gevaarlijk afval", "Hoogste tarief per eenheid, kleine volumes"],
            ]),
            ("h2", "Post 4: materiaal en middelen"),
            ("p", "Dozen, folie, dekens, handschoenen en gereedschap zijn bij een gewone ontruiming een kleine post. Bij een vervuilde woning is het dat niet: overalls, ademmaskers, handschoenen en soms schoenovertrekken worden na afloop weggegooid, en dat per persoon per dag."),
            ("h2", "Post 5: herstel en schoonmaak"),
            ("p", "Vloeren eruit, gaten dichten, wanden sausen, tuin opruimen en de eindschoonmaak. Dit is bij een huurwoning zelden optioneel, omdat het voorinspectierapport het voorschrijft. Bij een koopwoning hangt het af van de koopakte."),
            ("h2", "Hoe de posten zich verhouden"),
            ("p", "Bij een gemiddelde woningontruiming zonder bijzonderheden zitten manuren en transport samen op het grootste deel van de rekening. Verwerking is de tweede post, en herstel de derde. Bij een vervuilde woning verschuift dat: verwerking en beschermingsmiddelen worden dan relatief veel zwaarder, en herstel wordt een hoofdpost in plaats van een bijpost."),
            ("note", "Wat dit betekent voor het beperken van kosten",
             "<p>De posten waar een opdrachtgever zelf invloed op heeft, zijn volume en herstel. Waardevolle en bruikbare spullen eruit halen verkleint het volume en levert soms verrekening op. Zelf gaten dichten en de tuin opruimen haalt de herstelpost omlaag. Aan manuren en verwerkingstarieven valt weinig te doen.</p>"),
            ("h2", "Btw en facturatie"),
            ("p", "Particuliere opdrachtgevers krijgen een bedrag inclusief 21 procent btw. Zakelijke opdrachtgevers, corporaties en makelaars krijgen exclusief. Bij een ontruiming uit een nalatenschap wordt de factuur op naam van de nalatenschap of van een gemachtigde erfgenaam gesteld, wat later van belang is bij de verdeling en bij de aangifte erfbelasting."),
            ("h2", "Veelgestelde vragen"),
            ("faq", [
                ("Waarom scheelt een verdieping zo veel?",
                 "<p>Omdat elke kubieke meter met de hand naar beneden moet. Zonder lift loopt de tijd per kubieke meter ruwweg naar het dubbele.</p>"),
                ("Wordt gescheiden afvoeren doorberekend?",
                 "<p>Ja, maar in het voordeel van de opdrachtgever. Gescheiden stromen zijn goedkoper te verwerken dan restafval, en dat verschil zit in de vaste prijs verwerkt.</p>"),
                ("Kan de opdrachtgever zelf de stortkosten betalen?",
                 "<p>Dat kan bij sommige bedrijven, maar het levert weinig op. Bedrijven hebben tarieven bij verwerkers die particulieren niet krijgen.</p>"),
            ]),
        ],
        [links_rail("Kosten", [("/kosten/", "Wat kost een ontruiming"),
                               ("/kosten/offertes-vergelijken/", "Offertes vergelijken"),
                               ("/kosten/zelf-doen-of-uitbesteden/", "Zelf doen of uitbesteden")]),
         hulpbox("/kosten/", "kosten en tarieven"),
         contactbox()],
    ))

    # ------------------------------------------------------------ offertes
    out.append(_p(
        "/kosten/offertes-vergelijken/",
        "Offertes voor een woningontruiming vergelijken | SpoedWoningOntruiming.nl",
        "Offertes vergelijken",
        "Waar een offerte voor een ontruiming aan hoort te voldoen, welke elf punten erin moeten staan en welke signalen wijzen op nawerk of naberekening.",
        "Twee offertes die honderden euro's schelen, gaan meestal niet over dezelfde klus. Het verschil zit in wat er niet in staat. Deze elf punten maken offertes vergelijkbaar.",
        [
            ("h2", "Wat er in een offerte hoort te staan"),
            ("check", [
                "Alle ruimtes met naam: woonkamer, slaapkamers, keuken, badkamer, zolder, kelder, berging, garage, balkon en tuin.",
                "De eindstaat: leeg, bezemschoon of leeg plus eindschoonmaak, met een omschrijving van wat dat inhoudt.",
                "Of vloerbedekking, laminaat en ondervloer verwijderd worden, en of de lijmresten eraf moeten.",
                "Of gaten, schroeven en pluggen worden hersteld, en of er gesausd wordt.",
                "Of afvoer, stortkosten en verwerkingstarieven inbegrepen zijn.",
                "Of er voorrijkosten worden gerekend.",
                "Of het bedrag inclusief of exclusief btw is.",
                "De uitvoeringsdatum, de starttijd en het aantal mensen.",
                "Wat er gebeurt met waardevolle spullen en gevonden documenten.",
                "Of de inboedel wordt verrekend en zo ja, met welk bedrag.",
                "Betalingsvoorwaarden: vooraf, achteraf of in termijnen, en de vervaltermijn.",
            ]),
            ("h2", "Signalen die op naberekening wijzen"),
            ("table", ["Signaal", "Wat er meestal achter zit"], [
                ["Prijs per telefoon zonder foto's", "Een schatting die achteraf wordt bijgesteld"],
                ["Het woord vanaf in de offerte", "Het genoemde bedrag is een ondergrens, niet de prijs"],
                ["Geen benoeming van zolder, schuur of tuin", "Die ruimtes vallen buiten de opdracht en worden meerwerk"],
                ["Alleen mobiel nummer, geen KvK-nummer", "Moeilijk verhaal te halen bij schade of een geschil"],
                ["Volledige vooruitbetaling", "In deze branche ongebruikelijk, meestal wordt achteraf gefactureerd"],
                ["Geen algemene voorwaarden meegestuurd", "Onduidelijk wie aansprakelijk is bij schade aan het pand"],
            ]),
            ("h2", "Aansprakelijkheid en verzekering"),
            ("p", "Bij het uitdragen van een bank door een trappenhuis gaat er weleens iets stuk. Vraag daarom of het bedrijf een aansprakelijkheidsverzekering voor bedrijven heeft en of schade aan het pand daaronder valt. Bij een huurwoning is dat extra belangrijk, omdat schade aan het trappenhuis of de lift bij de corporatie terechtkomt en vervolgens bij de opdrachtgever."),
            ("h2", "Het opnamemoment zelf"),
            ("p", "Een opname op locatie duurt twintig minuten en levert de betrouwbaarste prijs. Wat een goede opnemer doet: elke ruimte in, kasten open, zolderluik open, schuur in, tuin bekijken, de looplijn naar de wagen lopen en vragen naar de gewenste eindstaat. Wie alleen in de woonkamer blijft staan, komt achteraf terug met meerwerk."),
            ("note", "Drie offertes is genoeg",
             "<p>Meer offertes leveren zelden een beter beeld op, maar kosten wel dagen. Bij een harde deadline zijn twee offertes met een opname op locatie beter dan vijf telefonische schattingen.</p>"),
            ("h2", "Vergelijken op gelijke voet"),
            ("p", "Zet de offertes naast elkaar en corrigeer eerst voor de verschillen: btw, vloer eruit ja of nee, schoonmaak wel of niet, en of de zolder is meegenomen. Pas daarna zegt het bedrag iets. In de praktijk verdwijnt het grootste deel van het prijsverschil in die correctie."),
            ("h2", "Veelgestelde vragen"),
            ("faq", [
                ("Kost een offerte op locatie geld?",
                 "<p>Bij de meeste bedrijven niet, ook niet wanneer er geen opdracht uit volgt.</p>"),
                ("Mag een bedrijf de prijs achteraf verhogen?",
                 "<p>Alleen wanneer er sprake is van meerwerk buiten de omschreven opdracht, en dat hoort vooraf gemeld en akkoord bevonden te zijn.</p>"),
                ("Wat als de woning voller blijkt dan op de foto's?",
                 "<p>Bij een prijs op basis van foto's is dat het risico van de opdrachtgever. Bij een opname op locatie ligt dat risico bij het bedrijf.</p>"),
                ("Hoort een offerte een geldigheidstermijn te hebben?",
                 "<p>Ja, meestal veertien tot dertig dagen. Daarna kunnen verwerkingstarieven veranderd zijn.</p>"),
            ]),
            ("partner", "Offerte op locatie",
             "<p>%s neemt de woning ter plaatse op en legt daarna een vaste prijs vast. De offertepagina staat op %s.</p>"
             % (dester("/", kind="brand"), dester("/offerte/", kind="bare"))),
        ],
        [links_rail("Kosten", [("/kosten/", "Wat kost een ontruiming"),
                               ("/kosten/kostenposten/", "Waar de rekening uit bestaat"),
                               ("/kosten/zelf-doen-of-uitbesteden/", "Zelf doen of uitbesteden")]),
         ("dark", "Checklist", '<p>De <a href="/checklists/ontruiming-voorbereiden/">checklist voorbereiding</a> bevat dezelfde punten in de volgorde waarin ze aan bod komen.</p>'),
         contactbox()],
    ))

    # ------------------------------------------------------------ zelf doen
    out.append(_p(
        "/kosten/zelf-doen-of-uitbesteden/",
        "Zelf ontruimen of uitbesteden: de rekensom | SpoedWoningOntruiming.nl",
        "Zelf doen of uitbesteden",
        "Wat zelf ontruimen werkelijk kost aan bus, containers, stortkosten en dagen, en bij welke omvang uitbesteden gunstiger uitvalt.",
        "Zelf ruimen scheelt manuren, maar niet de afvoer. Deze rekensom zet de werkelijke kosten van beide routes naast elkaar, inclusief de posten die in een eerste inschatting meestal ontbreken.",
        [
            ("h2", "Wat zelf ontruimen kost"),
            ("table", ["Post", "Indicatie", "Toelichting"], [
                ["Bestelbus huren", "70 tot 120 euro per dag", "Exclusief brandstof en kilometers boven de vrije limiet"],
                ["Afvalcontainer 10 kubieke meter", "300 tot 500 euro", "Plaatsen, huur, ophalen en verwerken samen"],
                ["Milieustraat", "Vaak enkele bezoeken per jaar vrij, daarna per keer of per kubieke meter", "Alleen voor particulieren, en niet elke stroom is toegestaan"],
                ["Grofvuil laten ophalen", "0 tot 60 euro per keer", "Sterk verschillend per gemeente, met een maximum aantal stuks"],
                ["Vloerverwijdering", "Machinehuur 60 tot 120 euro per dag", "Alleen nodig bij gelijmde vloeren"],
                ["Verhuisdozen en materiaal", "50 tot 150 euro", "Dozen, folie, tape, handschoenen, afvalzakken"],
                ["Eigen tijd", "Twee tot zes dagen", "Voor een gemiddelde woning, met twee tot drie mensen"],
            ]),
            ("p", "Voor een tweekamerappartement komt dat vaak uit tussen vierhonderd en zevenhonderd euro plus twee tot drie dagen werk. Voor een eengezinswoning tussen achthonderd en vijftienhonderd euro plus vier tot zes dagen. Bij een korte deadline valt die tijd niet altijd te vinden."),
            ("h2", "Waar zelf doen vastloopt"),
            ("ul", [
                "De milieustraat neemt geen ongelimiteerde hoeveelheden aan en is voor particulieren, niet voor volledige woninginhouden.",
                "Grofvuil ophalen kent per gemeente een maximum aantal stuks of kubieke meters per keer, en een wachttijd tot de eerstvolgende ronde.",
                "Een container in een straat met betaald parkeren of een smal profiel vereist een gemeentelijke vergunning.",
                "Zware zaken zoals een piano, een kluis, een cv-ketel of een verhoogd bad vragen materieel dat niet te huren is bij een bouwmarkt.",
                "Bij drie hoog zonder lift is het sjouwwerk de beperkende factor, niet de wil.",
            ]),
            ("h2", "Wanneer uitbesteden gunstiger uitvalt"),
            ("check", [
                "De woning moet binnen een week leeg zijn.",
                "Het gaat om meer dan ongeveer vijfentwintig kubieke meter.",
                "De woning ligt hoger dan de eerste verdieping zonder lift.",
                "Er moet vloerbedekking uit, of er is herstelwerk nodig.",
                "Er is sprake van vervuiling, ongedierte of schimmel.",
                "De betrokkenen wonen ver weg of hebben geen fysieke mogelijkheid om te sjouwen.",
                "Er staat dubbele huur of doorlopende hypotheeklasten tegenover elke week uitstel.",
            ]),
            ("h2", "De tussenvorm"),
            ("p", "Veel mensen kiezen een combinatie: familie zoekt zelf de persoonlijke spullen uit en haalt de kasten leeg, en een bedrijf doet in een dag het zware werk, de afvoer en de oplevering. Dat drukt de prijs, omdat het volume kleiner is en de ploeg niet hoeft te sorteren, en het houdt de emotionele kant in eigen hand."),
            ("note", "Reken de doorlopende lasten mee",
             "<p>Bij een huurwoning loopt de huur door tot de opleverdatum, bij een koopwoning lopen hypotheekrente, verzekering en heffingen door. Een maand uitstel kost daardoor vaak meer dan het verschil tussen zelf doen en uitbesteden.</p>"),
            ("h2", "Veelgestelde vragen"),
            ("faq", [
                ("Mag een volledige woninginhoud naar de milieustraat?",
                 "<p>Nee. Milieustraten zijn bedoeld voor huishoudelijk grofvuil van particulieren, met limieten per bezoek. Een complete woninginhoud valt daarbuiten.</p>"),
                ("Is een container goedkoper dan een ontruimingsbedrijf?",
                 "<p>Alleen wanneer de manuren gratis zijn en er tijd is. Bij een container komt het vullen, sorteren en sjouwen er nog bij.</p>"),
                ("Kan een deel worden uitbesteed?",
                 "<p>Ja. Bedrijven doen ook losse onderdelen, zoals alleen de afvoer of alleen het verwijderen van de vloer.</p>"),
            ]),
        ],
        [links_rail("Kosten", [("/kosten/", "Wat kost een ontruiming"),
                               ("/kosten/kostenposten/", "Waar de rekening uit bestaat"),
                               ("/kosten/offertes-vergelijken/", "Offertes vergelijken")]),
         ("dark", "Volume schatten", '<p>De <a href="/tools/inboedelvolume/">volumecalculator</a> geeft een schatting in kubieke meters en het aantal ritten dat daarbij hoort.</p>'),
         links_rail("Kennisbank", [("/kennisbank/grofvuil-en-milieustraat/", "Grofvuil en milieustraat"),
                                   ("/kennisbank/hergebruik-en-kringloop/", "Hergebruik en kringloop")])],
    ))

    return out
