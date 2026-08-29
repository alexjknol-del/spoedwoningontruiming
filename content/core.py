# -*- coding: utf-8 -*-
from build import dester, nl_date, render_blocks, EMAIL, BUILD_DATE
from content.shared import contactbox, links_rail


def home(articles):
    laatste = sorted(articles, key=lambda a: a["date"], reverse=True)[:4]
    nieuwsitems = "".join(
        '<li><time datetime="%s">%s</time><a href="%s">%s</a></li>'
        % (a["date"].isoformat(), nl_date(a["date"]), a["url"], a["h1"]) for a in laatste)

    situaties = render_blocks([("cards", [
        ("/ontruimen/spoedontruiming/", "Spoedontruiming",
         "De woning moet binnen een of twee dagen leeg zijn. Wat er dan haalbaar is en welke toeslag daarbij hoort."),
        ("/ontruimen/na-overlijden/", "Ontruiming na overlijden",
         "Eerst de erfenis, dan de spullen. De termijn van twee maanden en de handelingen die risico geven."),
        ("/ontruimen/seniorenwoning/", "Seniorenwoning ontruimen",
         "Verhuizing naar een zorginstelling, met dubbele lasten en een opzegtermijn van een maand."),
        ("/ontruimen/vervuilde-woning/", "Vervuilde woning ontruimen",
         "Woningvervuiling en hoarding, met bestrijding, sanering en herstel van vloeren en wanden."),
        ("/ontruimen/huurwoning-opleveren/", "Huurwoning opleveren",
         "Voorinspectie, eindinspectie en het verschil tussen bezemschoon en de staat volgens de beschrijving."),
        ("/ontruimen/inboedel-opkoop/", "Inboedel verkopen",
         "Wat een inboedel werkelijk opbrengt, hoe opkopers rekenen en welke voorwerpen het verschil maken."),
    ], 3)])

    verdieping = render_blocks([("cards", [
        ("/kennisbank/", "Kennisbank",
         "Erfrecht, huurrecht, oplevering, asbest, afvalregels en een begrippenlijst met zevenendertig termen."),
        ("/checklists/", "Checklists",
         "Vier lijsten om af te vinken: voorbereiding, oplevering, na een overlijden en verhuizing naar zorg."),
        ("/tools/", "Rekentools",
         "Een kostenindicatie en een volumeberekening, beide rekenend in de browser zonder gegevensverwerking."),
    ], 3)])

    kostentabel = render_blocks([("table", ["Type woning", "Bandbreedte 2026"], [
        ["Zorgkamer of studio", "250 tot 750 euro"],
        ["Twee- of driekamerappartement", "550 tot 1.250 euro"],
        ["Tussenwoning", "1.000 tot 1.800 euro"],
        ["Hoekwoning of twee-onder-een-kap", "1.500 tot 2.500 euro"],
        ["Vrijstaande woning", "2.000 tot 4.000 euro en hoger"],
        ["Zwaar vervuilde woning", "2.500 tot 6.000 euro en hoger"],
    ])])

    faq = render_blocks([("faq", [
        ("Wat kost een woningontruiming?",
         "<p>Voor een tweekamerappartement ligt de bandbreedte in 2026 tussen 550 en 950 euro, voor een tussenwoning tussen 1.000 en 1.800 euro. De vaste prijs volgt uit een opname op locatie. Zie de <a href=\"/kosten/\">kostenpagina</a>.</p>"),
        ("Hoe snel kan een woning ontruimd worden?",
         "<p>Veel bedrijven kunnen binnen 24 tot 48 uur, met een toeslag van tien tot dertig procent. Zonder spoed is een of twee weken vooruit gebruikelijk.</p>"),
        ("Hoe lang loopt de huur door na een overlijden?",
         "<p>Zonder medehuurder eindigt de huurovereenkomst aan het eind van de tweede maand na het overlijden. Erfgenamen kunnen dat verkorten tot het eind van de eerste maand.</p>"),
        ("Mag de woning leeggehaald worden voordat de erfenis is aanvaard?",
         "<p>Ja, zolang het bij beheer blijft: ruimen, opslaan en afvoeren van zaken zonder waarde. Verkopen of verdelen van waardevolle spullen geldt als zuivere aanvaarding.</p>"),
        ("Wat betekent bezemschoon opleveren?",
         "<p>Leeg, geveegd en vrij van losse rommel. Ramen lappen en het ontvetten van de oven vallen daarbuiten, dat hoort bij een eindschoonmaak.</p>"),
        ("Kan een ontruiming kosteloos zijn omdat de inboedel meegaat?",
         "<p>Alleen wanneer de inboedel voldoende waarde vertegenwoordigt. Bij een gemiddelde inboedel leidt verrekening tot een lagere rekening, niet tot een nulrekening.</p>"),
        ("Moet er iemand aanwezig zijn tijdens de ontruiming?",
         "<p>Niet per se. Veel bedrijven werken op sleutelbasis. Leg dan vooraf schriftelijk vast welke categorieën spullen apart gelegd worden.</p>"),
        ("Wie betaalt de ontruiming na een overlijden?",
         "<p>De nalatenschap. Is die negatief en hebben de erfgenamen beneficiair aanvaard of verworpen, dan blijven de kosten bij de verhuurder of de boedel.</p>"),
    ])])

    body = """
<div class="hero"><div class="wrap">
<h1>Een woning leeghalen: wat het kost, wat er moet en in welke volgorde</h1>
<p class="lead">SpoedWoningOntruiming.nl is een onafhankelijke gids over woningontruiming in Nederland. Prijsbandbreedtes voor 2026, de termijnen uit het huurrecht en erfrecht, en checklists die aflopen in de volgorde waarin het zich in de praktijk aandient.</p>
<div class="cta">
<a class="btn" href="/kosten/">Wat kost een ontruiming</a>
<a class="btn ghost" href="/checklists/ontruiming-voorbereiden/">Checklist voorbereiding</a>
</div>
</div></div>

<main id="inhoud">

<section class="band wash"><div class="wrap">
<div class="usp">
<div><strong>Bandbreedtes per woningtype</strong><p>Prijzen voor 2026 per type woning, met de losse posten en de toeslagen erbij.</p></div>
<div><strong>Termijnen uit de wet</strong><p>Huurrecht en erfrecht met de artikelnummers, zodat het na te lezen is.</p></div>
<div><strong>Checklists en rekentools</strong><p>Lijsten om af te vinken en twee rekentools die in de browser werken.</p></div>
<div><strong>Geen bemiddeling</strong><p>Deze gids verkoopt niets, bemiddelt niet en verzamelt geen aanvragen.</p></div>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>Waar het om gaat</h2>
<p>Woningontruiming is een verzamelnaam voor situaties die inhoudelijk sterk verschillen. Wat ze gemeen hebben is een datum die vastligt: de dag waarop de sleutel binnen moet zijn bij de corporatie, of de dag van de overdracht bij de notaris. Uit die datum volgt alles.</p>
%s
<p style="margin-top:22px"><a class="btn" href="/ontruimen/">Alle negen situaties</a></p>
</div></section>

<section class="band wash"><div class="wrap">
<div class="grid g2" style="align-items:start">
<div>
<h2>Kosten in 2026</h2>
<p>De bedragen hieronder gelden voor een complete ontruiming inclusief afvoer en bezemschoon opleveren, exclusief btw en zonder herstelwerk. Waar een concrete woning binnen de bandbreedte valt, hangt af van volume, bereikbaarheid en de gevraagde eindstaat.</p>
%s
<p><a href="/kosten/">Volledige kostenpagina met alle posten</a></p>
</div>
<div class="newsbox">
<h2>Nieuws</h2>
<p class="muted">Cijfers, regels en signalen die het ontruimen van een woning raken.</p>
<ul class="newslist">%s</ul>
<a class="btn" href="/nieuws/">Alle artikelen</a>
</div>
</div>
</div></section>

<section class="band"><div class="wrap">
<h2>Uitzoeken en voorbereiden</h2>
%s
</div></section>

<section class="band wash"><div class="wrap">
<h2>Wie voert het werk uit</h2>
<p>Deze gids voert zelf geen ontruimingen uit en bemiddelt niet in opdrachten. Voor wie een uitvoerende partij zoekt: %s werkt landelijk, rekent geen voorrijkosten en legt de prijs vooraf vast na een opname op locatie. Bezemschoon opleveren zit in het tarief, en het bedrijf werkt ook in de avonden en het weekend.</p>
<p>Aparte pagina's per situatie: %s, %s, %s, %s en %s. De tarieven per woningtype staan op %s.</p>
<p><a class="btn" href="/ontruimen/">Vergelijk eerst de situatie</a></p>
</div></section>

<section class="band"><div class="wrap">
<h2>Veelgestelde vragen</h2>
%s
</div></section>

</main>
""" % (situaties, kostentabel, nieuwsitems, verdieping,
       dester("/", kind="brand"),
       dester("/spoedontruiming/", kind="bare"),
       dester("/woning-na-overlijden/", kind="bare"),
       dester("/seniorenwoning-ontruimen/", kind="bare"),
       dester("/vervuilde-woning-ontruimen/", kind="bare"),
       dester("/bedrijfspand-ontruimen/", kind="bare"),
       dester("/kosten/", kind="bare"),
       faq)

    return {
        "url": "/",
        "title": "Woningontruiming: kosten, regels en checklists | SpoedWoningOntruiming.nl",
        "h1": "Een woning leeghalen: wat het kost, wat er moet en in welke volgorde",
        "og_title": "SpoedWoningOntruiming.nl",
        "description": "Onafhankelijke gids over woningontruiming in Nederland: prijsbandbreedtes voor 2026, termijnen uit het huurrecht en erfrecht, checklists en rekentools.",
        "full": True,
        "body": body,
        "priority": "1.0",
    }


def pages(articles):
    out = [home(articles)]

    out.append({
        "url": "/over/",
        "title": "Over SpoedWoningOntruiming.nl | Onafhankelijke gids",
        "h1": "Over deze gids",
        "description": "Wat SpoedWoningOntruiming.nl is, hoe de informatie tot stand komt, welke bronnen worden gebruikt en hoe de site zichzelf bekostigt.",
        "intro": "SpoedWoningOntruiming.nl is een onafhankelijke gids over het leeghalen en opleveren van woningen en bedrijfspanden in Nederland.",
        "priority": "0.7",
        "blocks": [
            ("h2", "Waarom deze site bestaat"),
            ("p", "Wie voor het eerst met een ontruiming te maken krijgt, komt online vooral aanbieders tegen. Dat is logisch, maar het levert een informatieprobleem op: de vragen die vooraf spelen gaan zelden over een bedrijf. Ze gaan over termijnen, over wat een verhuurder mag eisen, over wat er met de spullen van een overledene mag gebeuren en over de vraag of een bedrag redelijk is."),
            ("p", "Deze gids beantwoordt die vragen op een plek waar niets verkocht wordt. Er staat geen aanvraagformulier op, er worden geen offertes verzameld en er wordt niet bemiddeld tussen bezoeker en bedrijf."),
            ("h2", "Wat hier staat"),
            ("ul", [
                "Negen soorten ontruimingen, met per situatie de regels, de doorlooptijd en de kostenposten.",
                "Prijsbandbreedtes voor 2026 per woningtype, met de losse posten en de toeslagen erbij.",
                "Een kennisbank met de wetsartikelen die van toepassing zijn, in gewone taal uitgelegd.",
                "Vier checklists die aflopen in de volgorde waarin de stappen zich aandienen.",
                "Twee rekentools die volledig in de browser werken.",
                "Nieuwsartikelen over cijfers en regels die dit onderwerp raken.",
            ]),
            ("h2", "Hoe de informatie tot stand komt"),
            ("p", "De juridische uitleg is gebaseerd op de wetteksten zelf, met vermelding van het artikelnummer, zodat iedereen kan nalezen wat er staat. Cijfers komen uit openbare publicaties van het CBS, brancheorganisaties, gemeenten en onderzoeksrapporten, met vermelding van het jaar waarop ze betrekking hebben."),
            ("p", "Prijsbandbreedtes zijn afgeleid van gepubliceerde tarieven van Nederlandse ontruimingsbedrijven en van wat in de markt gangbaar is. Het zijn bandbreedtes en geen offertes: de werkelijke prijs volgt uit een opname op locatie."),
            ("note", "Geen juridisch advies",
             "<p>De uitleg op deze site is algemeen van aard. Bij een concrete zaak met een verhuurder, een schuldeiser of tussen erfgenamen is advies van een jurist of notaris op zijn plaats. Het Juridisch Loket, https://www.juridischloket.nl, biedt kosteloze eerste hulp.</p>"),
            ("h2", "Hoe de site zichzelf bekostigt"),
            ("p", "Op een aantal pagina's staat een verwijzing naar %s, een landelijk werkend ontruimingsbedrijf. Die verwijzingen zijn als zodanig herkenbaar en staan onderaan een pagina, niet in de uitleg zelf. De inhoud van de gids verandert er niet door: prijsbandbreedtes, termijnen en regels staan er los van."
             % dester("/", kind="brand")),
            ("p", "Er staat geen advertentienetwerk op de site, er worden geen persoonsgegevens verzameld en er is geen tracking. Zie het %s."
             % '<a href="/privacybeleid/">privacybeleid</a>'),
            ("h2", "Wat hier niet gebeurt"),
            ("ul", [
                "Geen bemiddeling of doorverwijzing van aanvragen naar bedrijven.",
                "Geen contactformulier waarin gegevens van bezoekers terechtkomen.",
                "Geen vergelijkingsscores of ranglijsten van bedrijven.",
                "Geen beoordelingen of ervaringsverhalen van derden.",
            ]),
            ("h2", "Correcties en aanvullingen"),
            ("p", 'Wetgeving verandert, tarieven veranderen en de praktijk verandert. Een fout of een verouderd bedrag kan gemeld worden via <a href="mailto:%s">%s</a>. Meldingen worden nagelopen en, wanneer terecht, verwerkt.' % (EMAIL, EMAIL)),
            ("p", "Laatste inhoudelijke actualisatie: %s." % nl_date(BUILD_DATE)),
        ],
        "rail": [links_rail("Naar de inhoud", [("/ontruimen/", "Soorten ontruimingen"),
                                               ("/kosten/", "Kosten"),
                                               ("/kennisbank/", "Kennisbank"),
                                               ("/checklists/", "Checklists"),
                                               ("/tools/", "Rekentools"),
                                               ("/nieuws/", "Nieuws")]),
                 contactbox()],
    })

    out.append({
        "url": "/contact/",
        "title": "Contact | SpoedWoningOntruiming.nl",
        "h1": "Contact",
        "description": "Contactgegevens van SpoedWoningOntruiming.nl. Vragen, correcties en aanvullingen gaan per e-mail, er is geen contactformulier.",
        "intro": "Vragen over de inhoud van deze gids, correcties en aanvullingen gaan per e-mail.",
        "priority": "0.5",
        "blocks": [
            ("h2", "E-mail"),
            ("p", '<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL)),
            ("p", "Er staat bewust geen contactformulier op deze site. Een e-mail komt rechtstreeks binnen, zonder tussenpartij en zonder dat er gegevens in een systeem worden vastgelegd."),
            ("h2", "Waarvoor dit adres bedoeld is"),
            ("check", [
                "Correcties op teksten, bedragen of wetsverwijzingen.",
                "Aanvullingen op de begrippenlijst of de checklists.",
                "Vragen over de herkomst van een cijfer of een bron.",
                "Meldingen van kapotte links of technische problemen.",
            ]),
            ("h2", "Waarvoor niet"),
            ("p", "Deze gids voert geen ontruimingen uit, geeft geen offertes af en bemiddelt niet. Een aanvraag voor een ontruiming kan niet via dit adres worden ingediend en wordt niet doorgestuurd."),
            ("p", "Wie een uitvoerende partij zoekt, kan rechtstreeks contact opnemen met een ontruimingsbedrijf. Zo werkt %s landelijk en is de contactpagina van dat bedrijf te vinden op %s."
             % (dester("/", kind="brand"), dester("/contact/", kind="url"))),
            ("h2", "Juridische of financiële vragen"),
            ("p", "Bij een geschil met een verhuurder of tussen erfgenamen is advies op maat nodig. Het Juridisch Loket, https://www.juridischloket.nl, helpt kosteloos bij een eerste beoordeling. Voor huurgeschillen in de sociale sector is de Huurcommissie het adres, https://www.huurcommissie.nl. Voor erfrechtelijke vragen is een notaris de aangewezen route, te vinden via https://www.notaris.nl."),
        ],
        "rail": [links_rail("Veelgevraagd", [("/kosten/", "Wat kost een ontruiming"),
                                             ("/kennisbank/erfenis-aanvaarden/", "Erfenis aanvaarden"),
                                             ("/kennisbank/huur-opzeggen-na-overlijden/", "Huur na overlijden"),
                                             ("/checklists/", "Checklists")]),
                 ("dark", "Onafhankelijk", "<p>Deze gids verkoopt niets, bemiddelt niet en verzamelt geen aanvragen. Zie <a href=\"/over/\">over deze gids</a>.</p>")],
    })

    out.append({
        "url": "/privacybeleid/",
        "title": "Privacybeleid | SpoedWoningOntruiming.nl",
        "h1": "Privacybeleid",
        "description": "Welke gegevens SpoedWoningOntruiming.nl verwerkt, welke niet, en hoe het zit met logbestanden, e-mail en externe links.",
        "intro": "Deze site verzamelt zo min mogelijk gegevens. Hieronder staat precies wat er wel en niet gebeurt.",
        "priority": "0.3",
        "blocks": [
            ("h2", "Wie verantwoordelijk is"),
            ("p", 'SpoedWoningOntruiming.nl is verantwoordelijk voor de verwerking van gegevens op deze website. Contact loopt via <a href="mailto:%s">%s</a>.' % (EMAIL, EMAIL)),
            ("h2", "Wat er niet gebeurt"),
            ("ul", [
                "Er staat geen contactformulier op de site, dus er worden langs die weg geen gegevens verzameld.",
                "Er is geen nieuwsbrief en er worden geen e-mailadressen opgeslagen voor verzending.",
                "Er staat geen advertentienetwerk op de site.",
                "Er wordt geen bezoekersstatistiek met persoonsgegevens bijgehouden en er zijn geen trackingpixels.",
                "Er worden geen gegevens verkocht of gedeeld met derden voor commerciële doeleinden.",
            ]),
            ("h2", "Logbestanden van de server"),
            ("p", "De hostingpartij verwerkt technische gegevens die bij elk bezoek aan een website ontstaan, zoals het opgevraagde adres, het tijdstip, de statuscode en het IP-adres van de bezoeker. Die gegevens dienen uitsluitend voor beveiliging en het oplossen van storingen, en worden na een korte periode automatisch verwijderd. De grondslag is het gerechtvaardigd belang van een werkende en veilige website."),
            ("h2", "E-mail"),
            ("p", "Wie een e-mail stuurt, deelt daarmee een e-mailadres en de inhoud van het bericht. Die gegevens worden gebruikt om de vraag te beantwoorden en niet voor iets anders. Correspondentie wordt bewaard zolang dat nodig is voor de afhandeling en daarna verwijderd."),
            ("h2", "Rekentools"),
            ("p", "De kostenindicatie en de volumeberekening werken volledig in de browser. De ingevoerde waarden worden niet verstuurd, niet opgeslagen en niet gedeeld."),
            ("h2", "Links naar andere websites"),
            ("p", "Op deze site staan verwijzingen naar andere websites, waaronder die van een ontruimingsbedrijf en van overheidsinstanties. Zodra een bezoeker daarheen doorklikt, geldt het privacybeleid van die partij. SpoedWoningOntruiming.nl heeft geen invloed op wat daar gebeurt."),
            ("h2", "Rechten"),
            ("p", "Iedereen heeft het recht om in te zien welke gegevens over hem of haar worden verwerkt, en om die te laten corrigeren of verwijderen. Gezien de aard van deze site zal dat in de praktijk alleen om e-mailcorrespondentie gaan. Een verzoek kan naar het bovengenoemde adres. Er bestaat daarnaast het recht om een klacht in te dienen bij de Autoriteit Persoonsgegevens, https://www.autoriteitpersoonsgegevens.nl."),
            ("h2", "Wijzigingen"),
            ("p", "Dit privacybeleid kan worden aangepast wanneer de opzet van de site verandert. De versie op deze pagina is de geldende. Laatst bijgewerkt: %s." % nl_date(BUILD_DATE)),
        ],
        "rail": [links_rail("Juridisch", [("/cookiebeleid/", "Cookiebeleid"),
                                          ("/over/", "Over deze gids"),
                                          ("/contact/", "Contact")])],
    })

    out.append({
        "url": "/cookiebeleid/",
        "title": "Cookiebeleid | SpoedWoningOntruiming.nl",
        "h1": "Cookiebeleid",
        "description": "Deze website plaatst geen cookies en gebruikt geen lokale opslag. Uitleg over wat dat betekent en waarom er geen cookiemelding is.",
        "intro": "Deze website plaatst geen cookies, gebruikt geen lokale opslag en laadt geen scripts van derden.",
        "priority": "0.3",
        "blocks": [
            ("h2", "Geen cookies"),
            ("p", "Een cookie is een klein bestand dat een website op een apparaat achterlaat om iets te onthouden of om gedrag te volgen. Deze site plaatst er geen. Er staat geen statistiekpakket op, geen advertentienetwerk en geen sociale mediaknoppen die meekijken."),
            ("h2", "Geen lokale opslag"),
            ("p", "Ook van localStorage, sessionStorage en vergelijkbare technieken wordt geen gebruik gemaakt. De rekentools op deze site werken in het geheugen van de browser en onthouden niets tussen bezoeken."),
            ("h2", "Waarom er geen cookiemelding staat"),
            ("p", "Een toestemmingsmelding is verplicht wanneer een website cookies plaatst of gegevens uitleest die niet strikt noodzakelijk zijn. Omdat hier niets wordt geplaatst en niets wordt uitgelezen, is die melding niet aan de orde. Dat scheelt de bezoeker een klik."),
            ("h2", "Externe links"),
            ("p", "Wie doorklikt naar een andere website, komt daar wel cookies tegen. Op die websites geldt hun eigen beleid. Er staan op deze site geen ingesloten video's, kaarten of lettertypen van externe partijen, dus tot dat moment worden er geen verzoeken naar derden gedaan."),
            ("h2", "Technische verzoeken"),
            ("p", "De server van de hostingpartij legt bij elk bezoek technische gegevens vast, zoals het opgevraagde adres en het tijdstip. Dat is geen cookie maar een serverlog, en het staat beschreven in het %s."
             % '<a href="/privacybeleid/">privacybeleid</a>'),
            ("p", "Laatst bijgewerkt: %s." % nl_date(BUILD_DATE)),
        ],
        "rail": [links_rail("Juridisch", [("/privacybeleid/", "Privacybeleid"),
                                          ("/over/", "Over deze gids"),
                                          ("/contact/", "Contact")])],
    })

    out.append({
        "url": "/404.html",
        "title": "Pagina niet gevonden | SpoedWoningOntruiming.nl",
        "h1": "Pagina niet gevonden",
        "description": "Deze pagina bestaat niet of is verplaatst. Hieronder staan de belangrijkste onderdelen van de site.",
        "intro": "Deze pagina bestaat niet of is verplaatst. Hieronder staan de belangrijkste onderdelen.",
        "head": '<meta name="robots" content="noindex, follow">\n',
        "blocks": [
            ("cards", [
                ("/ontruimen/", "Soorten ontruimingen", "Negen situaties, met per situatie de regels en de kostenposten."),
                ("/kosten/", "Kosten", "Bandbreedtes per woningtype voor 2026 en de losse posten."),
                ("/kennisbank/", "Kennisbank", "Erfrecht, huurrecht, oplevering, asbest en afvalregels."),
                ("/checklists/", "Checklists", "Vier lijsten om af te vinken."),
                ("/tools/", "Rekentools", "Kostenindicatie en volumeberekening."),
                ("/nieuws/", "Nieuws", "Cijfers en regels die dit onderwerp raken."),
            ], 3),
            ("p", 'Een kapotte link melden kan via <a href="mailto:%s">%s</a>.' % (EMAIL, EMAIL)),
        ],
        "rail": [],
    })

    return out
