#!/usr/bin/env python3
"""Generator voor spoedwoningontruiming.nl. Alleen standaardbibliotheek."""

import html
import os
import re
import shutil
import sys
from datetime import date

BASE = "https://spoedwoningontruiming.nl"
SITE = "SpoedWoningOntruiming.nl"
EMAIL = "info@spoedwoningontruiming.nl"
DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
BUILD_DATE = date(2026, 8, 28)

DESTER = "https://woningontruimingdester.nl"

NAV = [
    ("/ontruimen/", "Ontruimen"),
    ("/kosten/", "Kosten"),
    ("/kennisbank/", "Kennisbank"),
    ("/checklists/", "Checklists"),
    ("/tools/", "Tools"),
    ("/nieuws/", "Nieuws"),
    ("/over/", "Over"),
    ("/contact/", "Contact"),
]

FOOTER_COLS = [
    ("Ontruimen", [
        ("/ontruimen/spoedontruiming/", "Spoedontruiming"),
        ("/ontruimen/na-overlijden/", "Ontruiming na overlijden"),
        ("/ontruimen/seniorenwoning/", "Seniorenwoning ontruimen"),
        ("/ontruimen/vervuilde-woning/", "Vervuilde woning ontruimen"),
        ("/ontruimen/huurwoning-opleveren/", "Huurwoning opleveren"),
        ("/ontruimen/bedrijfspand/", "Bedrijfspand ontruimen"),
    ]),
    ("Uitzoeken", [
        ("/kosten/", "Wat kost een ontruiming"),
        ("/kosten/offertes-vergelijken/", "Offertes vergelijken"),
        ("/tools/kostenindicatie/", "Kostenindicatie"),
        ("/tools/inboedelvolume/", "Inboedelvolume berekenen"),
        ("/checklists/", "Checklists"),
        ("/kennisbank/begrippenlijst/", "Begrippenlijst"),
    ]),
    ("Over deze gids", [
        ("/over/", "Over SpoedWoningOntruiming.nl"),
        ("/nieuws/", "Nieuws"),
        ("/contact/", "Contact"),
        ("/privacybeleid/", "Privacybeleid"),
        ("/cookiebeleid/", "Cookiebeleid"),
    ]),
]

CSS = """
:root{
  --ink:#15272e;--ink-soft:#41565e;--line:#dfe4e2;--paper:#ffffff;
  --wash:#f5f3ee;--deep:#12333c;--deep-2:#0c242b;--accent:#b45a2b;
  --accent-soft:#f4e7dd;--good:#2f6b4f;--radius:10px;
  --sans:"Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:var(--sans);font-size:17px;line-height:1.65;color:var(--ink);background:var(--paper)}
img{max-width:100%;height:auto}
a{color:var(--deep)}
a:hover{color:var(--accent)}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
.skip{position:absolute;left:-9999px}
.skip:focus{left:8px;top:8px;background:#fff;padding:8px 12px;z-index:99;border:2px solid var(--deep)}

/* topbar */
.topbar{background:var(--deep-2);color:#cfdcdf;font-size:13.5px}
.topbar .wrap{display:flex;flex-wrap:wrap;gap:6px 22px;padding-top:8px;padding-bottom:8px}
.topbar span::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--accent);margin-right:8px;vertical-align:2px}

/* header */
header.site{background:var(--deep);color:#fff;position:sticky;top:0;z-index:40}
header.site .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:14px;padding-bottom:14px}
.brand{font-family:var(--serif);font-size:21px;font-weight:600;color:#fff;text-decoration:none;letter-spacing:.2px;line-height:1.2}
.brand small{display:block;font-family:var(--sans);font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;color:#8fb3ba;font-weight:500;margin-top:3px}
nav.main ul{list-style:none;display:flex;flex-wrap:wrap;gap:2px;margin:0;padding:0}
nav.main a{display:block;padding:7px 11px;color:#dbe9ec;text-decoration:none;font-size:15px;border-radius:6px}
nav.main a:hover,nav.main a[aria-current="true"]{background:rgba(255,255,255,.12);color:#fff}

/* hero */
.hero{background:linear-gradient(180deg,var(--deep) 0%,#17414c 100%);color:#fff;padding:56px 0 60px}
.hero h1{font-family:var(--serif);font-size:clamp(30px,4.4vw,46px);line-height:1.12;margin:0 0 16px;font-weight:600}
.hero p.lead{font-size:19px;color:#d6e6e9;max-width:64ch;margin:0 0 26px}
.hero .cta{display:flex;flex-wrap:wrap;gap:12px}
.btn{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;padding:12px 20px;border-radius:var(--radius);font-weight:600;font-size:16px;border:1px solid var(--accent)}
.btn:hover{background:#9c4c23;color:#fff}
.btn.ghost{background:transparent;border:1px solid rgba(255,255,255,.45);color:#fff}
.btn.ghost:hover{background:rgba(255,255,255,.12)}

main{padding:0 0 10px}
section.band{padding:46px 0}
section.band.wash{background:var(--wash)}
h2{font-family:var(--serif);font-size:clamp(23px,2.7vw,30px);line-height:1.22;margin:0 0 14px;font-weight:600}
h3{font-size:19px;margin:26px 0 8px;font-weight:650}
h4{font-size:17px;margin:20px 0 6px;font-weight:650}
p{margin:0 0 15px}
ul,ol{margin:0 0 16px;padding-left:22px}
li{margin-bottom:7px}
.muted{color:var(--ink-soft)}

/* page head */
.pagehead{background:var(--wash);border-bottom:1px solid var(--line);padding:34px 0 30px}
.pagehead h1{font-family:var(--serif);font-size:clamp(27px,3.6vw,38px);line-height:1.16;margin:0 0 12px;font-weight:600}
.pagehead p{font-size:18px;color:var(--ink-soft);max-width:70ch;margin:0}
.crumbs{font-size:13.5px;color:var(--ink-soft);margin:0 0 12px}
.crumbs a{color:var(--ink-soft)}

.layout{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:44px;padding:40px 0 8px;align-items:start}
article{max-width:73ch}
article h2{margin-top:34px}
article h2:first-child{margin-top:0}
aside.rail{position:sticky;top:86px}
.railbox{border:1px solid var(--line);border-radius:var(--radius);padding:18px;margin-bottom:18px;background:var(--paper)}
.railbox h3{margin:0 0 10px;font-size:16px;text-transform:uppercase;letter-spacing:.07em;color:var(--ink-soft)}
.railbox ul{list-style:none;padding:0;margin:0;font-size:15px}
.railbox li{margin-bottom:8px}
.railbox.dark{background:var(--deep);border-color:var(--deep);color:#e7f1f3}
.railbox.dark h3{color:#8fb3ba}
.railbox.dark a{color:#fff}

/* cards */
.grid{display:grid;gap:18px}
.grid>*{min-width:0}
.layout>*{min-width:0}
.g2{grid-template-columns:repeat(2,minmax(0,1fr))}
.g3{grid-template-columns:repeat(3,minmax(0,1fr))}
.g4{grid-template-columns:repeat(4,minmax(0,1fr))}
.card{border:1px solid var(--line);border-radius:var(--radius);padding:20px;background:var(--paper);display:flex;flex-direction:column}
.card h3{margin:0 0 8px;font-size:18px}
.card h3 a{text-decoration:none}
.card p{font-size:15.5px;color:var(--ink-soft);margin:0 0 12px}
.card .more{margin-top:auto;font-size:15px;font-weight:600;text-decoration:none}
.card .more::after{content:" \\2192"}

.usp{display:grid;gap:16px;grid-template-columns:repeat(4,minmax(0,1fr))}
.usp div{background:var(--paper);border:1px solid var(--line);border-radius:var(--radius);padding:16px}
.usp strong{display:block;font-size:16px;margin-bottom:4px}
.usp p{font-size:14.5px;color:var(--ink-soft);margin:0}

/* news highlight box */
.newsbox{border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:var(--radius);background:var(--paper);padding:24px}
.newsbox h2{margin-top:0}
.newslist{list-style:none;padding:0;margin:0 0 16px}
.newslist li{display:flex;flex-direction:column;padding:12px 0;border-bottom:1px solid var(--line)}
.newslist li:last-child{border-bottom:0}
.newslist time{font-size:13px;color:var(--ink-soft);letter-spacing:.04em;text-transform:uppercase}
.newslist a{font-weight:600;text-decoration:none}

.meta{font-size:13.5px;color:var(--ink-soft);margin:0 0 18px;letter-spacing:.03em;text-transform:uppercase}

/* callouts */
.note{border:1px solid var(--line);border-left:4px solid var(--deep);background:var(--wash);border-radius:var(--radius);padding:16px 18px;margin:22px 0}
.note h4{margin:0 0 6px;font-size:16px}
.note p:last-child,.note ul:last-child{margin-bottom:0}
.note.warn{border-left-color:var(--accent);background:var(--accent-soft)}

/* tables */
.tablewrap{overflow-x:auto;margin:0 0 20px}
table{border-collapse:collapse;width:100%;font-size:15.5px;min-width:460px}
th,td{border:1px solid var(--line);padding:9px 12px;text-align:left;vertical-align:top}
th{background:var(--wash);font-weight:650}

/* faq */
details{border:1px solid var(--line);border-radius:var(--radius);padding:0;margin-bottom:10px;background:var(--paper)}
details summary{cursor:pointer;padding:14px 16px;font-weight:650;list-style:none}
details summary::-webkit-details-marker{display:none}
details summary::after{content:"+";float:right;color:var(--accent);font-weight:700}
details[open] summary::after{content:"\\2212"}
details .answer{padding:0 16px 4px}

/* steps */
ol.steps{list-style:none;counter-reset:s;padding:0}
ol.steps>li{counter-increment:s;position:relative;padding-left:46px;margin-bottom:18px}
ol.steps>li::before{content:counter(s);position:absolute;left:0;top:0;width:32px;height:32px;border-radius:50%;background:var(--deep);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:650;font-size:15px}
ol.steps h3{margin:2px 0 6px}

/* checklist */
ul.check{list-style:none;padding:0}
ul.check li{position:relative;padding-left:30px;margin-bottom:9px}
ul.check li::before{content:"";position:absolute;left:0;top:6px;width:16px;height:16px;border:2px solid var(--deep);border-radius:4px}

/* calculator */
.calc{border:1px solid var(--line);border-radius:var(--radius);padding:22px;background:var(--wash);margin:0 0 24px}
.calc label{display:block;font-weight:650;font-size:15px;margin:0 0 6px}
.calc .field{margin-bottom:16px}
.calc select,.calc input[type=number]{width:100%;padding:10px;border:1px solid var(--line);border-radius:8px;font:inherit;background:#fff;color:var(--ink)}
.calc .row{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.calc .opts{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:15px}
.calc .opts label{font-weight:500;display:flex;gap:7px;align-items:center;margin:0}
.result{background:var(--deep);color:#fff;border-radius:var(--radius);padding:20px;margin-top:6px}
.result .big{font-family:var(--serif);font-size:30px;font-weight:600;display:block;margin:4px 0 6px}
.result p{margin:0;font-size:14.5px;color:#cfe0e3}
.result ul{margin:10px 0 0;font-size:14.5px;color:#cfe0e3}

/* partner block */
.partner{border:1px solid var(--line);border-radius:var(--radius);padding:22px;background:var(--wash);margin:26px 0}
.partner h3{margin:0 0 8px;font-size:19px}
.partner p:last-child{margin-bottom:0}

/* footer */
footer.site{background:var(--deep-2);color:#b9cbd0;margin-top:50px;padding:44px 0 26px;font-size:15px}
footer.site .cols{display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:30px}
footer.site h4{color:#fff;font-size:15px;margin:0 0 12px;letter-spacing:.03em}
footer.site ul{list-style:none;padding:0;margin:0}
footer.site li{margin-bottom:8px}
footer.site a{color:#b9cbd0;text-decoration:none}
footer.site a:hover{color:#fff;text-decoration:underline}
footer.site .brandline{font-family:var(--serif);color:#fff;font-size:20px;margin:0 0 10px}
.legal{border-top:1px solid rgba(255,255,255,.14);margin-top:30px;padding-top:18px;font-size:13.5px;display:flex;flex-wrap:wrap;gap:8px 20px;justify-content:space-between}

@media (max-width:960px){
  .layout{grid-template-columns:1fr;gap:26px}
  aside.rail{position:static}
  .g4,.usp{grid-template-columns:repeat(2,minmax(0,1fr))}
  footer.site .cols{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (max-width:640px){
  body{font-size:16.5px}
  header.site{position:static}
  header.site .wrap{flex-direction:column;align-items:flex-start}
  nav.main ul{gap:1px}
  nav.main a{padding:6px 9px;font-size:14.5px}
  .g2,.g3,.g4,.usp,.calc .row{grid-template-columns:1fr}
  footer.site .cols{grid-template-columns:1fr}
  .hero{padding:38px 0 42px}
}
"""


# ---------------------------------------------------------------- helpers

def esc(t):
    return html.escape(t, quote=False)


def dester(path, anchor=None, kind="brand"):
    """Uitgaande link naar de klantsite. Ankertekst: merknaam, kale URL of volledige URL."""
    url = DESTER + path
    if anchor is None:
        if kind == "brand":
            anchor = "Woningontruiming De Ster"
        elif kind == "bare":
            anchor = "woningontruimingdester.nl" + ("" if path == "/" else path)
        else:
            anchor = url
    return ('<a href="%s" rel="nofollow noopener" target="_blank">%s</a>' % (url, esc(anchor)))


def nl_date(d):
    maanden = ["januari", "februari", "maart", "april", "mei", "juni", "juli",
               "augustus", "september", "oktober", "november", "december"]
    return "%d %s %d" % (d.day, maanden[d.month - 1], d.year)


# ---------------------------------------------------------------- blocks

def render_blocks(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "h2":
            out.append("<h2 id=\"%s\">%s</h2>" % (slugify(b[1]), b[1]))
        elif kind == "h3":
            out.append("<h3>%s</h3>" % b[1])
        elif kind == "h4":
            out.append("<h4>%s</h4>" % b[1])
        elif kind == "p":
            out.append("<p>%s</p>" % b[1])
        elif kind == "ul":
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in b[1]))
        elif kind == "ol":
            out.append("<ol>%s</ol>" % "".join("<li>%s</li>" % i for i in b[1]))
        elif kind == "check":
            out.append('<ul class="check">%s</ul>' % "".join("<li>%s</li>" % i for i in b[1]))
        elif kind == "steps":
            items = []
            for title, text in b[1]:
                items.append("<li><h3>%s</h3><p>%s</p></li>" % (title, text))
            out.append('<ol class="steps">%s</ol>' % "".join(items))
        elif kind == "table":
            head = "".join("<th>%s</th>" % h for h in b[1])
            rows = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in b[2])
            out.append('<div class="tablewrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (head, rows))
        elif kind == "note":
            out.append('<div class="note"><h4>%s</h4>%s</div>' % (b[1], b[2]))
        elif kind == "warn":
            out.append('<div class="note warn"><h4>%s</h4>%s</div>' % (b[1], b[2]))
        elif kind == "partner":
            out.append('<div class="partner"><h3>%s</h3>%s</div>' % (b[1], b[2]))
        elif kind == "faq":
            items = []
            for q, a in b[1]:
                items.append('<details><summary>%s</summary><div class="answer">%s</div></details>' % (q, a))
            out.append("".join(items))
        elif kind == "cards":
            cards = []
            for href, title, text in b[1]:
                cards.append('<div class="card"><h3><a href="%s">%s</a></h3><p>%s</p>'
                             '<a class="more" href="%s">Lezen</a></div>' % (href, title, text, href))
            cols = b[2] if len(b) > 2 else 3
            out.append('<div class="grid g%d">%s</div>' % (cols, "".join(cards)))
        elif kind == "raw":
            out.append(b[1])
        else:
            raise ValueError("onbekend blok: %r" % (kind,))
    return "\n".join(out)


def slugify(t):
    t = re.sub(r"<[^>]+>", "", t).lower()
    t = t.replace("ë", "e").replace("é", "e").replace("ï", "i").replace("ö", "o").replace("ü", "u")
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t or "sectie"


# ---------------------------------------------------------------- shell

TITLE_SUFFIX = " | " + SITE


def fit_title(t):
    """Houd de title kort genoeg voor de zoekresultaten door het merkachtervoegsel te laten vallen."""
    if len(t) > 62 and t.endswith(TITLE_SUFFIX):
        return t[:-len(TITLE_SUFFIX)]
    return t


def head_html(page):
    canonical = BASE + page["url"]
    extra = page.get("head", "")
    return """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta name="robots" content="index, follow">
<meta property="og:type" content="%s">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:site_name" content="%s">
<meta property="og:locale" content="nl_NL">
<link rel="alternate" type="application/rss+xml" title="%s nieuws" href="%s/rss.xml">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>%s</style>
%s</head>
<body>
<a class="skip" href="#inhoud">Ga naar inhoud</a>
""" % (esc(fit_title(page["title"])), esc(page["description"]), canonical,
       "article" if page.get("is_article") else "website",
       esc(page.get("og_title", page["h1"])), esc(page["description"]), canonical, SITE,
       SITE, BASE, CSS, extra)


def topbar():
    items = ["Landelijk overzicht", "Onafhankelijke uitleg", "Geen ontruimingsbedrijf", "Bijgewerkt in 2026"]
    return '<div class="topbar"><div class="wrap">%s</div></div>' % "".join(
        "<span>%s</span>" % i for i in items)


def header(page):
    links = []
    for href, label in NAV:
        cur = ' aria-current="true"' if page["url"].startswith(href) else ""
        links.append('<li><a href="%s"%s>%s</a></li>' % (href, cur, label))
    return """<header class="site"><div class="wrap">
<a class="brand" href="/">SpoedWoningOntruiming.nl<small>Gids bij woningontruiming</small></a>
<nav class="main" aria-label="Hoofdmenu"><ul>%s</ul></nav>
</div></header>""" % "".join(links)


def footer():
    cols = []
    for title, links in FOOTER_COLS:
        items = "".join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in links)
        cols.append("<div><h4>%s</h4><ul>%s</ul></div>" % (title, items))
    return """<footer class="site"><div class="wrap">
<div class="cols">
<div>
<p class="brandline">SpoedWoningOntruiming.nl</p>
<p>Onafhankelijke gids over het ontruimen van woningen en bedrijfspanden in Nederland. Uitleg over kosten, regels en werkwijze, zonder verkoop en zonder bemiddeling.</p>
<p>Vragen of een correctie doorgeven: <a href="mailto:%s">%s</a></p>
</div>
%s
</div>
<div class="legal">
<span>%d SpoedWoningOntruiming.nl</span>
<span><a href="/privacybeleid/">Privacybeleid</a> &middot; <a href="/cookiebeleid/">Cookiebeleid</a> &middot; <a href="/contact/">Contact</a> &middot; <a href="/sitemap.xml">Sitemap</a></span>
</div>
</div></footer>
</body>
</html>
""" % (EMAIL, EMAIL, "".join(cols), BUILD_DATE.year)


def crumbs(page):
    parts = [p for p in page["url"].strip("/").split("/") if p]
    if not parts:
        return ""
    trail = ['<a href="/">Home</a>']
    path = ""
    for i, p in enumerate(parts):
        path += "/" + p
        label = page.get("crumb_labels", {}).get(path + "/", p.replace("-", " ").capitalize())
        if i == len(parts) - 1:
            trail.append(esc(label))
        else:
            trail.append('<a href="%s/">%s</a>' % (path, esc(label)))
    return '<p class="crumbs">%s</p>' % " / ".join(trail)


def rail(page):
    boxes = page.get("rail", [])
    if not boxes:
        return ""
    out = []
    for box in boxes:
        if box[0] == "links":
            items = "".join('<li><a href="%s">%s</a></li>' % (h, t) for h, t in box[2])
            out.append('<div class="railbox"><h3>%s</h3><ul>%s</ul></div>' % (box[1], items))
        elif box[0] == "dark":
            out.append('<div class="railbox dark"><h3>%s</h3>%s</div>' % (box[1], box[2]))
        elif box[0] == "plain":
            out.append('<div class="railbox"><h3>%s</h3>%s</div>' % (box[1], box[2]))
    return '<aside class="rail">%s</aside>' % "".join(out)


def render_page(page):
    if page.get("full"):
        body = page["body"]
    else:
        r = rail(page)
        inner = render_blocks(page["blocks"])
        meta = ('<p class="meta">%s</p>' % page["meta"]) if page.get("meta") else ""
        layout = ('<div class="wrap"><div class="layout"><article id="inhoud">%s%s</article>%s</div></div>'
                  % (meta, inner, r))
        body = """<div class="pagehead"><div class="wrap">%s<h1>%s</h1><p>%s</p></div></div>
<main>%s</main>""" % (crumbs(page), esc(page["h1"]), page["intro"], layout)
    return head_html(page) + topbar() + header(page) + body + footer()


# ---------------------------------------------------------------- write

def write(page):
    url = page["url"]
    if url == "/404.html":
        path = os.path.join(DIST, "404.html")
    else:
        path = os.path.join(DIST, url.strip("/"), "index.html") if url != "/" else os.path.join(DIST, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(render_page(page))


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="12" fill="#12333c"/>
<path d="M14 34 32 18l18 16v14a2 2 0 0 1-2 2H16a2 2 0 0 1-2-2z" fill="none" stroke="#f2ece3" stroke-width="4" stroke-linejoin="round"/>
<path d="M25 50V38h14v12" fill="none" stroke="#b45a2b" stroke-width="4" stroke-linejoin="round"/>
</svg>
"""


def build_sitemap(pages):
    rows = []
    for p in pages:
        if p["url"] == "/404.html":
            continue
        pr = p.get("priority", "0.6")
        lm = p.get("date", BUILD_DATE).isoformat()
        rows.append("  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>"
                    % (BASE, p["url"], lm, pr))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(rows) + "\n</urlset>\n")


def build_rss(articles):
    items = []
    for a in articles:
        pub = a["date"].strftime("%a, %d %b %Y") + " 09:00:00 +0200"
        items.append("""  <item>
    <title>%s</title>
    <link>%s%s</link>
    <guid isPermaLink="true">%s%s</guid>
    <pubDate>%s</pubDate>
    <description>%s</description>
  </item>""" % (esc(a["h1"]), BASE, a["url"], BASE, a["url"], pub, esc(a["description"])))
    return """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
<title>%s nieuws</title>
<link>%s/nieuws/</link>
<description>Nieuws en achtergrond over woningontruiming, nalatenschappen en het opleveren van huurwoningen.</description>
<language>nl-nl</language>
%s
</channel></rss>
""" % (SITE, BASE, "\n".join(items))


def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from content import core, ontruimen, kosten, kennisbank, checklists, tools, nieuws

    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    articles = nieuws.ARTICLES
    pages = []
    pages += core.pages(articles)
    pages += ontruimen.pages()
    pages += kosten.pages()
    pages += kennisbank.pages()
    pages += checklists.pages()
    pages += tools.pages()
    pages += nieuws.pages()

    seen = {}
    for p in pages:
        if p["url"] in seen:
            raise SystemExit("dubbele url: %s" % p["url"])
        seen[p["url"]] = p
        write(p)

    with open(os.path.join(DIST, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(build_sitemap(pages))
    with open(os.path.join(DIST, "rss.xml"), "w", encoding="utf-8") as f:
        f.write(build_rss(articles))
    with open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE)
    with open(os.path.join(DIST, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(FAVICON)
    with open(os.path.join(DIST, "_headers"), "w", encoding="utf-8") as f:
        f.write("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n"
                "  X-Frame-Options: SAMEORIGIN\n  Permissions-Policy: geolocation=(), microphone=(), camera=()\n")

    print("gebouwd: %d pagina's" % len(pages))


if __name__ == "__main__":
    main()
