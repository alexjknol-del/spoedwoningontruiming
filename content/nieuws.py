# -*- coding: utf-8 -*-
from datetime import date

from build import dester, nl_date
from content.shared import contactbox, links_rail

CRUMB = {"/nieuws/": "Nieuws"}


def A(slug, d, h1, title, description, samenvatting, blocks):
    return {"url": "/nieuws/%s/" % slug, "date": d, "h1": h1, "title": title,
            "description": description, "samenvatting": samenvatting, "blocks": blocks}


ARTICLES = [
    A("afvalstoffenheffing-2026", date(2026, 8, 20),
      "Afvalstoffenheffing stijgt in 2026 met 3,6 procent",
      "Afvalstoffenheffing 2026 stijgt met 3,6 procent | SpoedWoningOntruiming.nl",
      "De gemeentelijke afvalstoffenheffing stijgt in 2026 minder hard dan in de twee jaren ervoor. Wat dat betekent voor wie een woning zelf leeghaalt.",
      "De heffing stijgt dit jaar met ongeveer 3,6 procent, tegen 5 procent in 2025 en 6 procent in 2024. De verschillen tussen gemeenten zijn groter dan de landelijke stijging.",
      [
          ("p", "Uit een steekproef van Vereniging Eigen Huis onder 106 gemeenten blijkt dat de afvalstoffenheffing in 2026 gemiddeld met ongeveer 3,6 procent stijgt. Dat is minder hard dan in 2025, toen de stijging op 5 procent uitkwam, en dan in 2024 met 6 procent."),
          ("p", "De landelijke gemiddelden zeggen weinig over een concrete situatie. In de steekproef loopt het bedrag per huishouden uiteen van iets meer dan tweehonderd euro in de laagste gemeente tot boven de vijfhonderdvijftig euro in de hoogste. Daarnaast rekenen veel gemeenten per keer of per kubieke meter voor grofvuil dat wordt opgehaald, en kennen milieustraten een beperkt aantal vrije bezoeken per jaar."),
          ("h2", "Waarom dit meetelt bij een ontruiming"),
          ("p", "Wie een woning zelf leeghaalt, bespaart manuren maar niet de afvoer. De afvalstoffenbelasting is per 1 januari 2026 verhoogd, en die verhoging werkt via de verwerkers door in de tarieven die zowel gemeenten als commerciële afvoerders rekenen."),
          ("p", "Voor een gemiddeld tweekamerappartement, vijftien tot vijfentwintig kubieke meter, betekent zelf afvoeren al snel meerdere ritten naar de milieustraat plus een of twee grofvuilrondes. Bij een eengezinswoning met dertig tot vijftig kubieke meter is een afvalcontainer meestal de enige werkbare route, en die kost inclusief plaatsen en verwerken tussen de driehonderd en vijfhonderd euro voor tien kubieke meter."),
          ("h2", "Wat het verschil maakt"),
          ("ul", [
              "Gescheiden aanbieden verlaagt het tarief per ton, omdat restafval de duurste stroom is.",
              "Bruikbare goederen naar een kringloopwinkel scheelt volume en dus containerkosten.",
              "Elektronica, tl-buizen en klein chemisch afval moeten sowieso apart, ook bij zelf afvoeren.",
              "Een container op de openbare weg vraagt in veel gemeenten een vergunning.",
          ]),
          ("p", "De rekensom tussen zelf doen en uitbesteden staat uitgewerkt op de pagina over %s."
           % '<a href="/kosten/zelf-doen-of-uitbesteden/">zelf doen of uitbesteden</a>'),
      ]),

    A("verklaring-van-erfrecht-2026", date(2026, 8, 5),
      "Verklaring van erfrecht in 2026: tarieven en de grenzen die banken hanteren",
      "Verklaring van erfrecht 2026: tarieven en bankgrenzen | SpoedWoningOntruiming.nl",
      "Wat een verklaring van erfrecht in 2026 kost, wanneer banken erom vragen en bij welke saldi zij een uitzondering maken.",
      "Notaristarieven voor een eenvoudige verklaring beginnen in 2026 rond de vierhonderd euro. Banken maken uitzonderingen tot honderdduizend euro voor een langstlevende partner.",
      [
          ("p", "Een verklaring van erfrecht is de notariële akte waarin staat wie is overleden, wie de erfgenamen zijn en wie namens hen mag handelen. Zonder dat document blijft een bankrekening geblokkeerd en kan een woning uit een nalatenschap niet worden overgedragen."),
          ("h2", "Tarieven"),
          ("p", "Notaristarieven zijn vrij. Voor een eenvoudige verklaring met een of twee erfgenamen liggen de bedragen in 2026 doorgaans vanaf ongeveer 395 tot 500 euro. Bij meerdere erfgenamen of een testament met een executeur loopt dat op naar 600 tot 900 euro, en bij buitenlandse erfgenamen of een onderneming in de nalatenschap naar duizend euro en hoger. De doorlooptijd is een tot drie weken, en die wordt vooral bepaald door hoe snel alle erfgenamen reageren."),
          ("h2", "Wanneer banken een uitzondering maken"),
          ("p", "Voor een langstlevende echtgenoot of geregistreerd partner vragen banken doorgaans geen verklaring wanneer het saldo niet boven de honderdduizend euro uitkomt. Voor andere erfgenamen ligt die grens lager, vaak rond tienduizend euro. In plaats van een verklaring vragen zij dan om een overlijdensakte, een identiteitsbewijs, een uittreksel uit het Centraal Testamentenregister en een vrijwaringsformulier."),
          ("p", "Altijd een verklaring vragen banken wanneer de overledene minderjarig was, onder curatele stond, in schuldsanering zat of failliet was verklaard, en bij complexere producten zoals een lopende hypotheek of een beleggingsrekening."),
          ("h2", "Volgorde bij een woning"),
          ("p", "Bij een koopwoning uit een nalatenschap kan de aanvraag al starten voordat de woning leeg is. Dat scheelt weken waarin hypotheekrente, verzekering en gemeentelijke heffingen doorlopen. De uitleg staat op de pagina over %s."
           % '<a href="/kennisbank/verklaring-van-erfrecht/">de verklaring van erfrecht</a>'),
      ]),

    A("meldingen-woningvervuiling-blijven-stijgen", date(2026, 7, 14),
      "Meldingen van hoarding en woningvervuiling blijven stijgen",
      "Meldingen hoarding en woningvervuiling nemen toe | SpoedWoningOntruiming.nl",
      "Gemeenten en GGD-regio's zien tussen 60 en 150 procent meer meldingen van woningvervuiling. Rotterdam ging van 200 naar 350 meldingen per jaar.",
      "De stijging loopt landelijk uiteen van 60 tot 150 procent. Onderzoekers leggen de link met eenzaamheid, ambulantisering en bezuinigingen in de zorg.",
      [
          ("p", "Rotterdam registreerde voor de coronaperiode ongeveer tweehonderd meldingen van woningvervuiling per jaar. Dat aantal liep op naar driehonderdvijftig en stijgt verder. Amsterdam telt jaarlijks rond de driehonderdvijftig ernstig vervuilde woningen, met een toename van klachten bij de ombudsman sinds 2023. Uit een uitvraag van GGD GHOR blijkt landelijk een stijging tussen zestig en honderdvijftig procent, met grote verschillen tussen gemeenten en regio's."),
          ("p", "Het onderzoek waar deze cijfers uit komen, is het rapport Als de zorgen boven het hoofd groeien van de Amsterdamse ombudsman. Daarin wordt hoarding beschreven als een signaal van bredere problemen, met een verband naar toenemende eenzaamheid, ambulantisering en bezuinigingen in de zorg. De ombudsman pleit voor een stedelijk expertisecentrum dat het overzicht houdt."),
          ("h2", "Wat dit betekent voor de uitvoering"),
          ("p", "Een ernstig vervuilde woning is geen zware schoonmaakklus maar een saneringstraject. Beschermingsmiddelen worden na afloop weggegooid, afvalstromen zijn duurder, ongediertebestrijding moet voor of tijdens de ontruiming plaatsvinden, en na afloop volgt vaak herstel van vloeren, wanden en plafonds. In de markt lopen de bedragen voor zwaar vervuilde panden op van ongeveer tweeduizendvijfhonderd tot zesduizend euro en hoger."),
          ("h2", "Ruimen alleen is niet genoeg"),
          ("p", "Zonder begeleiding staat een geruimde woning binnen een jaar regelmatig opnieuw vol. Corporaties koppelen een ontruiming daarom steeds vaker aan een zorgtraject via het wijkteam of de GGD. Hulp bij verzamelwoede is onder meer te vinden via https://www.legerdesheils.nl/hoarding."),
          ("p", "De praktische kant van dit werk staat beschreven op de pagina over %s."
           % '<a href="/ontruimen/vervuilde-woning/">het ontruimen van een vervuilde woning</a>'),
      ]),

    A("asbest-legt-ontruimingen-stil", date(2026, 6, 16),
      "Vloer eruit in een woning van voor 1994: asbest kan een ontruiming stilleggen",
      "Asbest bij ontruiming: wanneer het werk wordt stilgelegd | SpoedWoningOntruiming.nl",
      "Bij oudere woningen komt asbest vooral naar boven wanneer vloerbedekking of zeil eruit moet. Dat legt het werk stil tot er een inventarisatie is.",
      "Een ontruimingsbedrijf zonder certificaat mag geen asbest verwijderen. Wordt er asbestverdacht materiaal aangetroffen, dan volgt eerst een inventarisatie door een gecertificeerd bureau.",
      [
          ("p", "Asbest is in Nederland verboden sinds 1993, met een overgang naar 1994. In woningen van voor die tijd zit het op vaste plekken: vinylzeil met een viltachtige onderlaag, vloertegels uit de jaren zestig en zeventig, golfplaten op schuurdaken, standleidingen en plaatmateriaal rond de cv-ketel en de meterkast."),
          ("p", "Bij een ontruiming komt dat vooral aan het licht wanneer de vloer eruit moet. Zolang de vloerbedekking blijft liggen, gebeurt er niets. Zodra er getrokken en gesneden wordt, verandert de klus."),
          ("h2", "Wat de regels zeggen"),
          ("p", "Een particulier mag onder voorwaarden tot 35 vierkante meter asbesthoudend materiaal uit de eigen woning verwijderen: geschroefde hechtgebonden platen die heel blijven, vloertegels en niet-gelijmde vloerbedekking die in zijn geheel wordt verwijderd, en goed verpakte losse voorwerpen. Daarbuiten is een gecertificeerd bedrijf verplicht. Verwijdering vraagt een sloopmelding via het Omgevingsloket, minimaal een week vooraf, plus een startmelding minstens twee dagen voor het werk en een gereedmelding op de eerste werkdag erna."),
          ("p", "Voor huurwoningen geldt bovendien dat de huurder niet zelf mag verwijderen. Dat loopt via de verhuurder, die verantwoordelijk is voor asbest in het gehuurde."),
          ("h2", "Wat het betekent voor de planning"),
          ("p", "Een ontruimingsbedrijf zonder asbestcertificaat legt het werk stil zodra er asbestverdacht materiaal opduikt. Er volgt dan eerst een inventarisatie, die voor een woning tussen de vierhonderd en negenhonderd euro kost en enkele dagen in beslag neemt. Bij een strakke opleverdatum is dat het scenario dat het meeste schade aanricht."),
          ("p", "De praktische stap vooraf: bij woningen van voor 1994 de asbestinventarisatie van het complex opvragen bij de corporatie, of de vloeropbouw bij de opname laten beoordelen. Meer daarover staat op de pagina over %s."
           % '<a href="/kennisbank/asbest-in-de-woning/">asbest in de woning</a>'),
      ]),

    A("tachtigplussers-verdubbelen", date(2026, 5, 19),
      "Aantal 80-plussers verdubbelt richting 2045",
      "Vergrijzing: aantal 80-plussers verdubbelt richting 2045 | SpoedWoningOntruiming.nl",
      "Nederland telt ongeveer 900 duizend 80-plussers. Dat aantal groeit volgens het CBS naar 1,8 miljoen in 2045 en 2,1 miljoen in 2070.",
      "Sinds 2025 zijn er voor het eerst meer 65-plussers dan jongeren tot twintig jaar. De groep 80-plussers verdubbelt in twintig jaar tijd.",
      [
          ("p", "Begin 2025 telde Nederland 3,76 miljoen 65-plussers tegenover 3,72 miljoen jongeren tot twintig jaar. Dat was het eerste jaar waarin ouderen de jongeren in aantal overtroffen. Volgens de bevolkingsprognose van het CBS groeit de groep 65-plussers door naar 4,76 miljoen in 2040."),
          ("p", "De groep 80-plussers gaat harder. Nederland telt daar nu ongeveer negenhonderdduizend van. Die groep loopt naar verwachting op naar 1,8 miljoen in 2045 en 2,1 miljoen in 2070."),
          ("h2", "Wat dat praktisch betekent"),
          ("p", "Twee soorten woningverandering nemen daarmee toe: de verhuizing van een zelfstandige woning naar een zorginstelling of aanleunwoning, en het leeghalen van een woning na een overlijden. Beide gaan gepaard met een korte termijn, omdat huurovereenkomsten doorlopen en een woning die leegstaat geld kost."),
          ("p", "Bij een verhuizing naar een zorginstelling is de opzegtermijn van een maand meestal korter dan de tijd die familie nodig heeft om een woning van zestig jaar te sorteren. Bij een overlijden eindigt de huurovereenkomst van een alleenwonende huurder aan het eind van de tweede maand na het overlijden."),
          ("h2", "Ruimte in de woningvoorraad"),
          ("p", "Elke doorstroming van een eengezinswoning of een ruime seniorenwoning naar een zorgplek maakt een woning vrij. Corporaties sturen daarom strak op de opleverdatum: leegstand kost huurinkomsten en houdt een woningzoekende op."),
          ("p", "De praktische kant van zo'n verhuizing staat in de %s."
           % '<a href="/checklists/verhuizing-naar-zorginstelling/">checklist verhuizing naar een zorginstelling</a>'),
      ]),

    A("kringloop-hergebruik-63-procent", date(2026, 4, 22),
      "Kringloopsector hergebruikt 63 procent van wat binnenkomt",
      "Kringloopwinkels hergebruiken 63 procent van wat binnenkomt | SpoedWoningOntruiming.nl",
      "De aangesloten kringloopbedrijven hergebruikten in 2024 63 procent van de binnengekomen producten, tegen 56 procent een jaar eerder.",
      "62 leden met 242 winkels, gemiddeld 747.805 kilo per vestiging, en 339 miljoen kilo bespaarde CO2. Het aandeel hergebruik steeg met zeven procentpunten.",
      [
          ("p", "De aangesloten bedrijven van Branchevereniging Kringloop Nederland telden in 2024 62 leden met 242 winkels, tegen 66 organisaties met 248 winkels in 2023. Gemiddeld kwam er 747.805 kilo per vestiging binnen, ongeveer veertigduizend kilo minder dan het jaar ervoor, maar nog altijd veertigduizend kilo boven het niveau van voor de coronaperiode."),
          ("p", "Van alle binnengekomen producten werd 63 procent hergebruikt, tegen 56 procent in 2023. Daarnaast ging 22 procent naar recycling, 14 procent naar restafval en 1 procent naar export. De sector rekent voor dat daarmee 339 miljoen kilo CO2 is bespaard. De winkelomzet bedroeg 155,5 miljoen euro bij 16,7 miljoen betalende klanten. De kringloopbedrijven boden werk aan 18.659 mensen, van wie 46 procent uit een doelgroep met een afstand tot de arbeidsmarkt."),
          ("h2", "Wat dat betekent bij een ontruiming"),
          ("p", "Een groot deel van een gemiddelde inboedel is bruikbaar. Wat naar de kringloop gaat, telt niet mee in het volume dat naar de verwerker moet, en restafval is de duurste stroom per ton. Sorteren verlaagt daarmee zowel het volume als het tarief."),
          ("p", "De beperking zit in de tijd. Kringloopwinkels halen doorgaans gratis op vanaf een minimale hoeveelheid, met een wachttijd van dagen tot enkele weken. Bij een ontruiming met een korte deadline is dat vaak niet haalbaar, en verloopt de route via het ontruimingsbedrijf, dat bruikbare goederen naar dezelfde kanalen brengt."),
          ("p", "Wat kringloopwinkels wel en niet aannemen, staat op de pagina over %s."
           % '<a href="/kennisbank/hergebruik-en-kringloop/">hergebruik en kringloop</a>'),
      ]),

    A("cbs-173-duizend-overledenen-2025", date(2026, 3, 19),
      "CBS: 173 duizend mensen overleden in 2025, ruim de helft 80-plus",
      "CBS: 173 duizend overledenen in 2025 | SpoedWoningOntruiming.nl",
      "In 2025 overleden 173 duizend mensen in Nederland, 1,2 duizend meer dan in 2024. 57 procent was 80 jaar of ouder.",
      "De sterfte nam minder sterk toe dan het jaar ervoor. De levensverwachting steeg voor mannen en vrouwen met twee maanden.",
      [
          ("p", "In 2025 overleden in Nederland 173 duizend mensen, ongeveer 1,2 duizend meer dan in 2024. De toename was minder sterk dan een jaar eerder. Van alle overledenen was 57 procent 80 jaar of ouder, ongeveer 99 duizend mensen. Nog eens bijna 54 duizend was tussen de 65 en 80 jaar, en 12 procent was jonger dan 65."),
          ("p", "De levensverwachting steeg voor beide groepen met twee maanden, naar 80,68 jaar voor mannen en 83,47 jaar voor vrouwen."),
          ("h2", "Waarom deze cijfers hier staan"),
          ("p", "Achter elk van die 173 duizend overlijdens staat een woning die op enig moment leeg moet. Bij een alleenwonende huurder zonder medehuurder eindigt de huurovereenkomst aan het eind van de tweede maand na het overlijden. Erfgenamen kunnen die termijn verkorten tot het eind van de eerste maand, maar niet verlengen."),
          ("p", "Dat maakt het leeghalen van een woning een van de weinige onderdelen van een nalatenschap met een harde deadline. Voor de rest, van de aangifte erfbelasting tot de verdeling, is meer ruimte."),
          ("h2", "De volgorde"),
          ("p", "Eerst de keuze over de nalatenschap, dan pas de spullen. Wie waardevolle zaken meeneemt of verkoopt voordat die keuze is gemaakt, aanvaardt de erfenis zuiver en wordt persoonlijk aansprakelijk voor eventuele schulden. Ruimen, opslaan en afvoeren van zaken zonder waarde geldt als beheer en is wel toegestaan."),
          ("p", "De volledige volgorde staat in de %s."
           % '<a href="/checklists/na-overlijden/">checklist na een overlijden</a>'),
      ]),

    A("tweede-maand-na-overlijden", date(2026, 2, 17),
      "Waarom de tweede maand na een overlijden de echte deadline is",
      "Huurwoning na overlijden: de tweede maand is de deadline | SpoedWoningOntruiming.nl",
      "De huurovereenkomst van een alleenwonende huurder eindigt van rechtswege aan het eind van de tweede maand na het overlijden. Wat dat praktisch betekent.",
      "Artikel 7:268 lid 6 van het Burgerlijk Wetboek regelt het einde van de huur na een overlijden. Nabestaanden ontdekken die termijn vaak pas in de laatste week.",
      [
          ("p", "Woonde de overledene alleen en is er geen medehuurder of achterblijver met een duurzame gemeenschappelijke huishouding, dan eindigt de huurovereenkomst van rechtswege aan het eind van de tweede maand na het overlijden. Erfgenamen mogen de huur bovendien laten eindigen tegen het eind van de eerste maand. Dat staat in artikel 7:268 lid 6 van het Burgerlijk Wetboek."),
          ("p", "Concreet: bij een overlijden op 12 maart loopt de huur zonder actie door tot en met 31 mei, en met een opzegging door de erfgenamen tot en met 30 april. Op die datum moet de woning leeg zijn en opgeleverd volgens de eisen van de verhuurder."),
          ("h2", "Waar de tijd blijft"),
          ("p", "Van die twee maanden gaat de eerste vaak op aan de uitvaart, de administratie en de keuze over de nalatenschap. Wat overblijft is een paar weken voor de voorinspectie, het uitzoeken van persoonlijke zaken, het opvragen van offertes, de ontruiming zelf, herstelwerk en de eindinspectie."),
          ("p", "De voorinspectie is daarbij het scharnierpunt. Corporaties plannen die doorgaans binnen twee weken na de melding, en het rapport bepaalt wat er bij de ontruiming moet gebeuren: vloer eruit of niet, gaten dichten, sausen, tuin opruimen. Wie die inspectie pas in de laatste week aanvraagt, komt in de knel."),
          ("h2", "Wat er gebeurt bij overschrijding"),
          ("p", "De huurovereenkomst eindigt hoe dan ook. Staat de woning dan nog vol, dan kan de verhuurder de ontruiming zelf laten uitvoeren en de kosten indienen bij de nalatenschap. Voor erfgenamen die beneficiair hebben aanvaard of verworpen, levert dat geen persoonlijke aansprakelijkheid op. Bij zuivere aanvaarding wel."),
          ("h2", "Medehuurders en achterblijvers"),
          ("p", "Een medehuurder zet de huur voort als huurder en kan binnen zes maanden opzeggen. Iemand die geen medehuurder is maar wel hoofdverblijf had en een duurzame gemeenschappelijke huishouding voerde met de overledene, zet de huur zes maanden voort en kan binnen die termijn de rechter vragen om voortzetting daarna. Inwonende kinderen worden daar zelden onder geschaard."),
          ("p", "De volledige uitleg staat op de pagina over %s."
           % '<a href="/kennisbank/huur-opzeggen-na-overlijden/">huur opzeggen na overlijden</a>'),
      ]),
]


def pages():
    out = []

    cards = []
    for a in ARTICLES:
        cards.append((a["url"], a["h1"], nl_date(a["date"]) + ". " + a["samenvatting"]))

    out.append({
        "url": "/nieuws/",
        "title": "Nieuws over woningontruiming, erfrecht en oplevering | SpoedWoningOntruiming.nl",
        "h1": "Nieuws",
        "description": "Actuele artikelen over woningontruiming, nalatenschappen, huurrecht, afvalregels en hergebruik, met de cijfers en bronnen erbij.",
        "intro": "Ontwikkelingen die het ontruimen van een woning raken: cijfers van het CBS, regels rond huur en erfrecht, tarieven voor afvoer en signalen uit de praktijk.",
        "blocks": [("cards", cards, 2)],
        "rail": [links_rail("Onderwerpen", [("/ontruimen/", "Soorten ontruimingen"),
                                            ("/kosten/", "Kosten"),
                                            ("/kennisbank/", "Kennisbank"),
                                            ("/checklists/", "Checklists")]),
                 ("dark", "RSS", '<p>De artikelen zijn te volgen via <a href="/rss.xml">de RSS-feed</a>.</p>'),
                 contactbox()],
        "priority": "0.8",
        "crumb_labels": CRUMB,
    })

    for i, a in enumerate(ARTICLES):
        overige = [(x["url"], x["h1"]) for x in ARTICLES if x is not a][:5]
        blocks = list(a["blocks"])
        blocks.append(("partner", "Uitvoering",
                       "<p>Deze gids voert zelf geen ontruimingen uit. Wie een uitvoerende partij zoekt: %s werkt landelijk met een vaste prijs vooraf. Zie %s.</p>"
                       % (dester("/", kind="brand"), dester("/", kind="bare"))))
        out.append({
            "url": a["url"],
            "title": a["title"],
            "h1": a["h1"],
            "description": a["description"],
            "intro": a["samenvatting"],
            "meta": "Nieuws &middot; " + nl_date(a["date"]),
            "blocks": blocks,
            "rail": [links_rail("Meer nieuws", overige),
                     ("dark", "Overzicht", '<p>Alle artikelen staan op de <a href="/nieuws/">nieuwspagina</a>.</p>'),
                     contactbox()],
            "priority": "0.6",
            "date": a["date"],
            "is_article": True,
            "crumb_labels": CRUMB,
        })

    return out
