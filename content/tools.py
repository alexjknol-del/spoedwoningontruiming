# -*- coding: utf-8 -*-
from build import dester
from content.shared import contactbox, links_rail

CRUMB = {"/tools/": "Tools"}


def _p(url, title, h1, description, intro, blocks, rail, prio="0.6"):
    return {"url": url, "title": title, "h1": h1, "description": description,
            "intro": intro, "blocks": blocks, "rail": rail, "priority": prio,
            "crumb_labels": CRUMB}


KOSTEN_FORM = """
<div class="calc">
  <div class="row">
    <div class="field">
      <label for="type">Type woning of ruimte</label>
      <select id="type">
        <option value="250,550">Zorgkamer of verzorgingskamer</option>
        <option value="350,750">Studio of eenkamerappartement</option>
        <option value="550,950" selected>Tweekamerappartement</option>
        <option value="750,1250">Driekamerappartement</option>
        <option value="1000,1800">Tussenwoning</option>
        <option value="1500,2500">Hoekwoning of twee-onder-een-kap</option>
        <option value="2000,4000">Vrijstaande woning</option>
      </select>
    </div>
    <div class="field">
      <label for="vulling">Hoe vol staat het pand</label>
      <select id="vulling">
        <option value="0.75">Rustig gevuld, kasten grotendeels leeg</option>
        <option value="1" selected>Normaal gevuld</option>
        <option value="1.3">Vol, zolder en berging inbegrepen</option>
        <option value="1.6">Zeer vol, jarenlange opslag</option>
      </select>
    </div>
  </div>
  <div class="row">
    <div class="field">
      <label for="toegang">Bereikbaarheid</label>
      <select id="toegang">
        <option value="1" selected>Begane grond of lift, parkeren voor de deur</option>
        <option value="1.15">Eerste verdieping zonder lift</option>
        <option value="1.3">Tweede verdieping of hoger zonder lift</option>
        <option value="1.12">Parkeren op afstand of beperkte laadruimte</option>
      </select>
    </div>
    <div class="field">
      <label for="vervuiling">Staat van het pand</label>
      <select id="vervuiling">
        <option value="1" selected>Normaal</option>
        <option value="1.4">Sterk vervuild, geen ongedierte</option>
        <option value="2.2">Ernstig vervuild, ongedierte of schimmel</option>
      </select>
    </div>
  </div>
  <div class="row">
    <div class="field">
      <label for="vloer">Vloer verwijderen, aantal vierkante meter</label>
      <input type="number" id="vloer" min="0" max="400" step="5" value="0">
    </div>
    <div class="field">
      <label for="spoed">Uitvoeringstermijn</label>
      <select id="spoed">
        <option value="1" selected>Binnen twee weken</option>
        <option value="1.1">Binnen vijf werkdagen</option>
        <option value="1.25">Binnen 48 uur</option>
      </select>
    </div>
  </div>
  <div class="field">
    <label>Extra werk</label>
    <div class="opts">
      <label><input type="checkbox" id="schoon"> Eindschoonmaak</label>
      <label><input type="checkbox" id="herstel"> Gaten dichten en sausen</label>
      <label><input type="checkbox" id="tuin"> Tuin, schuur of garage</label>
    </div>
  </div>
  <div class="result" id="uitkomst" aria-live="polite"></div>
</div>
<script>
(function(){
  var ids=['type','vulling','toegang','vervuiling','vloer','spoed','schoon','herstel','tuin'];
  function euro(n){return Math.round(n/25)*25;}
  function fmt(n){return n.toLocaleString('nl-NL');}
  function reken(){
    var t=document.getElementById('type').value.split(',');
    var lo=parseFloat(t[0]), hi=parseFloat(t[1]);
    var f=parseFloat(document.getElementById('vulling').value)
        *parseFloat(document.getElementById('toegang').value)
        *parseFloat(document.getElementById('vervuiling').value)
        *parseFloat(document.getElementById('spoed').value);
    lo=lo*f; hi=hi*f;
    var extra=[];
    var m2=parseFloat(document.getElementById('vloer').value)||0;
    if(m2>0){lo+=m2*3; hi+=m2*7; extra.push('Vloer verwijderen, '+fmt(m2)+' vierkante meter');}
    if(document.getElementById('schoon').checked){lo+=150;hi+=500;extra.push('Eindschoonmaak');}
    if(document.getElementById('herstel').checked){lo+=75;hi+=300;extra.push('Gaten dichten en sausen');}
    if(document.getElementById('tuin').checked){lo+=150;hi+=600;extra.push('Tuin, schuur of garage');}
    var html='<span>Indicatie, inclusief afvoer en bezemschoon opleveren</span>'
      +'<span class="big">'+fmt(euro(lo))+' tot '+fmt(euro(hi))+' euro</span>'
      +'<p>Bandbreedte op basis van marktprijzen in 2026, exclusief btw. Een vaste prijs volgt pas uit een opname op locatie.</p>';
    if(extra.length){html+='<ul><li>'+extra.join('</li><li>')+'</li></ul>';}
    document.getElementById('uitkomst').innerHTML=html;
  }
  ids.forEach(function(id){var el=document.getElementById(id);el.addEventListener('change',reken);el.addEventListener('input',reken);});
  reken();
})();
</script>
"""

VOLUME_FORM = """
<div class="calc">
  <div class="row">
    <div class="field">
      <label for="woon">Woonkamers</label>
      <input type="number" id="woon" min="0" max="6" value="1">
    </div>
    <div class="field">
      <label for="slaap">Slaapkamers</label>
      <input type="number" id="slaap" min="0" max="8" value="2">
    </div>
  </div>
  <div class="row">
    <div class="field">
      <label for="keuken">Keukens</label>
      <input type="number" id="keuken" min="0" max="3" value="1">
    </div>
    <div class="field">
      <label for="bad">Badkamers en toiletten</label>
      <input type="number" id="bad" min="0" max="4" value="1">
    </div>
  </div>
  <div class="row">
    <div class="field">
      <label for="zolder">Zolders</label>
      <input type="number" id="zolder" min="0" max="3" value="0">
    </div>
    <div class="field">
      <label for="berging">Bergingen, schuren of garages</label>
      <input type="number" id="berging" min="0" max="4" value="0">
    </div>
  </div>
  <div class="field">
    <label for="graad">Hoe vol staan de ruimtes</label>
    <select id="graad">
      <option value="0.6">Rustig, kasten grotendeels leeg</option>
      <option value="1" selected>Normaal gevuld</option>
      <option value="1.4">Vol</option>
      <option value="1.9">Zeer vol, opslag tot aan het plafond</option>
    </select>
  </div>
  <div class="result" id="vol" aria-live="polite"></div>
</div>
<script>
(function(){
  var basis={woon:7,slaap:5,keuken:3,bad:1.5,zolder:9,berging:6};
  var ids=Object.keys(basis).concat(['graad']);
  function reken(){
    var g=parseFloat(document.getElementById('graad').value), m3=0;
    for(var k in basis){
      var v=parseFloat(document.getElementById(k).value)||0;
      m3+=v*basis[k];
    }
    m3=m3*g;
    var lo=Math.round(m3*0.8), hi=Math.round(m3*1.2);
    var ritten=Math.max(1,Math.ceil(hi/20));
    var dagen = hi<=20?'ongeveer een halve tot een hele dag':(hi<=40?'ongeveer een dag':(hi<=70?'anderhalve tot twee dagen':'twee dagen of meer'));
    document.getElementById('vol').innerHTML=
      '<span>Geschat volume</span><span class="big">'+lo+' tot '+hi+' kubieke meter</span>'
      +'<p>Dat komt neer op '+ritten+' rit'+(ritten===1?'':'ten')+' met een bakwagen van twintig kubieke meter, en '+dagen+' werk voor een ploeg van drie tot vier personen.</p>';
  }
  ids.forEach(function(id){var el=document.getElementById(id);el.addEventListener('change',reken);el.addEventListener('input',reken);});
  reken();
})();
</script>
"""


def pages():
    out = []

    out.append(_p(
        "/tools/",
        "Rekentools voor een woningontruiming | SpoedWoningOntruiming.nl",
        "Rekentools",
        "Twee rekentools: een kostenindicatie op basis van marktprijzen 2026 en een schatting van het inboedelvolume in kubieke meters.",
        "Twee hulpmiddelen om een gesprek met een ontruimingsbedrijf voor te bereiden. Beide rekenen volledig in de browser, er wordt niets verstuurd en niets opgeslagen.",
        [
            ("cards", [
                ("/tools/kostenindicatie/", "Kostenindicatie",
                 "Een bandbreedte op basis van woningtype, vulling, bereikbaarheid, staat en extra werk."),
                ("/tools/inboedelvolume/", "Inboedelvolume berekenen",
                 "Een schatting van het volume in kubieke meters, het aantal ritten en de benodigde tijd."),
            ], 2),
            ("h2", "Wat deze tools wel en niet doen"),
            ("p", "Ze geven een orde van grootte, gebaseerd op de bandbreedtes die in 2026 in de Nederlandse markt gangbaar zijn. Ze vervangen geen offerte: de werkelijke prijs volgt uit een opname op locatie, waarbij zaken meewegen die een formulier niet vangt, zoals een gelijmde vloer, een smalle trap of een kelder die pas bij de opname opengaat."),
            ("note", "Geen gegevensverwerking",
             "<p>De berekening gebeurt in de browser met een script op deze site. Er worden geen gegevens verstuurd, opgeslagen of gedeeld, en er staat geen tracking op deze pagina's.</p>"),
        ],
        [links_rail("Tools", [("/tools/kostenindicatie/", "Kostenindicatie"),
                              ("/tools/inboedelvolume/", "Inboedelvolume berekenen")]),
         ("dark", "Achtergrond", '<p>De bandbreedtes per woningtype en de losse posten staan op de <a href="/kosten/">kostenpagina</a>.</p>'),
         contactbox()],
        prio="0.8",
    ))

    out.append(_p(
        "/tools/kostenindicatie/",
        "Kostenindicatie woningontruiming 2026 | SpoedWoningOntruiming.nl",
        "Kostenindicatie woningontruiming",
        "Reken een bandbreedte uit voor een ontruiming op basis van woningtype, vulling, bereikbaarheid, staat van het pand en extra werk.",
        "Vul de zes velden in en de tool geeft een bandbreedte op basis van marktprijzen voor 2026. Alles gebeurt in de browser.",
        [
            ("raw", KOSTEN_FORM),
            ("h2", "Hoe de berekening werkt"),
            ("p", "De basis is de bandbreedte per woningtype uit de kostenpagina. Daar overheen komen vier vermenigvuldigingsfactoren en drie losse posten."),
            ("table", ["Factor", "Effect"], [
                ["Vulling", "Van 0,75 bij een rustig gevuld pand tot 1,6 bij jarenlange opslag"],
                ["Bereikbaarheid", "Tot 1,3 bij een tweede verdieping of hoger zonder lift"],
                ["Staat van het pand", "1,4 bij sterke vervuiling, 2,2 bij ongedierte of schimmel"],
                ["Uitvoeringstermijn", "1,1 binnen vijf werkdagen, 1,25 binnen 48 uur"],
                ["Vloer verwijderen", "3 tot 7 euro per vierkante meter"],
                ["Eindschoonmaak", "150 tot 500 euro"],
                ["Gaten dichten en sausen", "75 tot 300 euro"],
                ["Tuin, schuur of garage", "150 tot 600 euro"],
            ]),
            ("h2", "Wat er niet in zit"),
            ("ul", [
                "Asbestsanering, want dat is werk voor een gecertificeerd bedrijf met een eigen tarief.",
                "Bouwkundig herstel zoals het terugplaatsen van wanden of plafonds.",
                "Verrekening van een inboedel met waarde, wat het bedrag juist verlaagt.",
                "Btw, de bedragen zijn exclusief 21 procent.",
                "Zeer grote panden, vrijstaande woningen met bijgebouwen en bedrijfsruimte.",
            ]),
            ("p", "Voor de opbouw van de rekening en de posten erachter: %s. Voor het vergelijken van offertes: %s."
             % ('<a href="/kosten/kostenposten/">waar de rekening uit bestaat</a>',
                '<a href="/kosten/offertes-vergelijken/">offertes vergelijken</a>')),
            ("partner", "Van indicatie naar vaste prijs",
             "<p>%s neemt de woning ter plaatse op en legt daarna een vaste prijs vast, zonder voorrijkosten. De tarieven per woningtype staan op %s.</p>"
             % (dester("/", kind="brand"), dester("/kosten/", kind="bare"))),
        ],
        [links_rail("Tools", [("/tools/inboedelvolume/", "Inboedelvolume berekenen")]),
         ("dark", "Achtergrond", '<p>De bandbreedtes en losse posten staan uitgewerkt op de <a href="/kosten/">kostenpagina</a>.</p>'),
         links_rail("Verder", [("/kosten/offertes-vergelijken/", "Offertes vergelijken"),
                               ("/checklists/ontruiming-voorbereiden/", "Checklist voorbereiding")])],
        prio="0.7",
    ))

    out.append(_p(
        "/tools/inboedelvolume/",
        "Inboedelvolume berekenen in kubieke meters | SpoedWoningOntruiming.nl",
        "Inboedelvolume berekenen",
        "Schat het volume van een inboedel in kubieke meters, en zie hoeveel ritten en dagen daarbij horen.",
        "Volume is de belangrijkste factor achter de prijs van een ontruiming. Deze tool geeft een schatting op basis van het aantal ruimtes en de mate waarin ze gevuld zijn.",
        [
            ("raw", VOLUME_FORM),
            ("h2", "De gehanteerde kengetallen"),
            ("table", ["Ruimte", "Uitgangspunt bij normale vulling"], [
                ["Woonkamer", "7 kubieke meter"],
                ["Slaapkamer", "5 kubieke meter"],
                ["Keuken", "3 kubieke meter"],
                ["Badkamer of toilet", "1,5 kubieke meter"],
                ["Zolder", "9 kubieke meter"],
                ["Berging, schuur of garage", "6 kubieke meter"],
            ]),
            ("p", "Die aantallen worden vermenigvuldigd met de gekozen vullingsgraad, en de uitkomst krijgt een bandbreedte van plus en min twintig procent. Een bakwagen neemt ongeveer twintig kubieke meter mee, een gesloten bestelbus rond de acht."),
            ("h2", "Waar het volume mee oploopt"),
            ("ul", [
                "Kelders en kruipruimtes die bij een eerste rondgang niet zijn bekeken.",
                "Vloerbedekking en laminaat, die als los volume meegaan zodra ze eruit gehaald worden.",
                "Tuinmeubilair, tegels, plantenbakken en tuinhout.",
                "Bouwafval van een oude verbouwing dat op zolder of in de schuur is blijven staan.",
                "Boeken en papier, die in gewicht zwaarder tellen dan in volume.",
            ]),
            ("h2", "Wat het volume betekent voor de planning"),
            ("table", ["Volume", "Ritten", "Indicatie tijd"], [
                ["Tot 20 kubieke meter", "1", "Een halve tot een hele dag"],
                ["20 tot 40 kubieke meter", "2", "Ongeveer een dag"],
                ["40 tot 70 kubieke meter", "3 tot 4", "Anderhalve tot twee dagen"],
                ["Boven 70 kubieke meter", "4 of meer", "Twee dagen of meer"],
            ]),
            ("p", "Wie zelf afvoert, komt bij deze volumes snel in de knel met de limieten van gemeente en milieustraat. Zie de pagina over %s."
             % '<a href="/kennisbank/grofvuil-en-milieustraat/">grofvuil en milieustraat</a>'),
        ],
        [links_rail("Tools", [("/tools/kostenindicatie/", "Kostenindicatie")]),
         ("dark", "Zelf doen", '<p>De rekensom tussen zelf ruimen en uitbesteden staat op <a href="/kosten/zelf-doen-of-uitbesteden/">zelf doen of uitbesteden</a>.</p>'),
         contactbox()],
        prio="0.7",
    ))

    return out
