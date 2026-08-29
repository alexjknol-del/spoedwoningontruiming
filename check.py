#!/usr/bin/env python3
"""Controle op de gebouwde site in dist/."""

import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, "dist")
BASE = "https://spoedwoningontruiming.nl"

TOEGESTANE_HOSTS = {"woningontruimingdester.nl"}
TOEGESTANE_ANKERS = [
    re.compile(r"^Woningontruiming De Ster$"),
    re.compile(r"^woningontruimingdester\.nl(/[a-z0-9\-/]*)?$"),
    re.compile(r"^https://woningontruimingdester\.nl(/[a-z0-9\-/]*)?$"),
]

AANSPREEK = re.compile(
    r"(?<![a-zA-ZÀ-ſ])(je|jij|jou|jouw|jullie|uw|u|we|wij|ons|onze|onszelf)"
    r"(?![a-zA-ZÀ-ſ])")

DUMMY = re.compile(r"(lorem ipsum|todo|tbd|xxx|placeholder|dummy|hier komt|vul aan|"
                   r"\[invullen\]|nog aan te vullen|voorbeeldtekst)", re.I)

fouten = []
waarschuwingen = []


def html_files():
    for dirpath, _dirs, files in os.walk(DIST):
        for f in files:
            if f.endswith(".html"):
                yield os.path.join(dirpath, f)


def url_of(path):
    rel = os.path.relpath(path, DIST)
    if rel == "index.html":
        return "/"
    if rel == "404.html":
        return "/404.html"
    return "/" + os.path.dirname(rel).replace(os.sep, "/") + "/"


def strip_html(s):
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S)
    s = re.sub(r"<style.*?</style>", " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    s = s.replace("&middot;", " ").replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"\s+", " ", s)


def main():
    if not os.path.isdir(DIST):
        print("dist/ ontbreekt, draai eerst build.py")
        return 1

    docs = {}
    for p in html_files():
        with open(p, encoding="utf-8") as f:
            docs[url_of(p)] = f.read()

    titles = defaultdict(list)
    descs = defaultdict(list)
    inkomend = defaultdict(int)

    for url, doc in sorted(docs.items()):
        tekst = strip_html(doc)

        # title
        m = re.search(r"<title>(.*?)</title>", doc, re.S)
        if not m:
            fouten.append("%s: geen title" % url)
        else:
            t = m.group(1).strip()
            titles[t].append(url)
            if len(t) > 68:
                waarschuwingen.append("%s: title %d tekens" % (url, len(t)))
            if len(t) < 25:
                waarschuwingen.append("%s: title kort, %d tekens" % (url, len(t)))

        # description
        m = re.search(r'<meta name="description" content="(.*?)">', doc, re.S)
        if not m:
            fouten.append("%s: geen meta description" % url)
        else:
            d = m.group(1).strip()
            descs[d].append(url)
            if not (70 <= len(d) <= 185):
                waarschuwingen.append("%s: description %d tekens" % (url, len(d)))

        # canonical
        if url != "/404.html" and 'rel="canonical"' not in doc:
            fouten.append("%s: geen canonical" % url)

        # h1
        h1 = re.findall(r"<h1[^>]*>", doc)
        if len(h1) != 1:
            fouten.append("%s: %d h1-elementen" % (url, len(h1)))

        # dubbele id's
        ids = re.findall(r' id="([^"]+)"', doc)
        if len(ids) != len(set(ids)):
            dubbel = [i for i in set(ids) if ids.count(i) > 1]
            fouten.append("%s: dubbele id's %s" % (url, dubbel))

        # afbeeldingen
        for img in re.findall(r"<img[^>]*>", doc):
            if "alt=" not in img:
                fouten.append("%s: img zonder alt" % url)

        # streepjes
        for teken, naam in ((u"—", "em-dash"), (u"–", "en-dash")):
            if teken in tekst:
                fouten.append("%s: %s in de tekst" % (url, naam))

        # dummytekst
        m = DUMMY.search(tekst)
        if m:
            fouten.append("%s: dummytekst %r" % (url, m.group(0)))

        # aanspreekvormen in zichtbare tekst
        for m in AANSPREEK.finditer(tekst):
            fouten.append("%s: aanspreekvorm %r rond %r"
                          % (url, m.group(0), tekst[max(0, m.start() - 45):m.end() + 45]))

        # interne links
        for href in re.findall(r'href="(/[^"#]*)"', doc):
            if href.startswith("//"):
                continue
            if href in ("/sitemap.xml", "/rss.xml", "/robots.txt", "/favicon.svg"):
                continue
            if href not in docs:
                fouten.append("%s: kapotte interne link naar %s" % (url, href))
            elif href != url:
                inkomend[href] += 1

        # uitgaande links
        for m in re.finditer(r'<a href="(https?://[^"]+)"([^>]*)>(.*?)</a>', doc, re.S):
            doel, attrs, anker = m.group(1), m.group(2), strip_html(m.group(3)).strip()
            host = re.sub(r"^https?://", "", doel).split("/")[0]
            if host not in TOEGESTANE_HOSTS:
                fouten.append("%s: externe link naar niet-toegestane host %s" % (url, host))
                continue
            if "nofollow" not in attrs or "noopener" not in attrs:
                fouten.append("%s: uitgaande link zonder nofollow noopener: %s" % (url, doel))
            if 'target="_blank"' not in attrs:
                fouten.append("%s: uitgaande link zonder target blank: %s" % (url, doel))
            if not any(p.match(anker) for p in TOEGESTANE_ANKERS):
                fouten.append("%s: ankertekst niet toegestaan: %r" % (url, anker))

        # lege links
        for m in re.finditer(r'<a [^>]*>\s*</a>', doc):
            fouten.append("%s: lege link" % url)

    for t, urls in titles.items():
        if len(urls) > 1:
            fouten.append("dubbele title %r op %s" % (t, urls))
    for d, urls in descs.items():
        if len(urls) > 1:
            fouten.append("dubbele description op %s" % urls)

    for url in docs:
        if url in ("/", "/404.html"):
            continue
        if inkomend.get(url, 0) == 0:
            fouten.append("%s: verweesde pagina, geen inkomende links" % url)

    # sitemap
    sm = os.path.join(DIST, "sitemap.xml")
    with open(sm, encoding="utf-8") as f:
        smtxt = f.read()
    in_sitemap = set(re.findall(r"<loc>%s([^<]*)</loc>" % re.escape(BASE), smtxt))
    for url in docs:
        if url == "/404.html":
            continue
        if url not in in_sitemap:
            fouten.append("%s ontbreekt in de sitemap" % url)
    for url in in_sitemap:
        if url not in docs:
            fouten.append("sitemap verwijst naar onbekende pagina %s" % url)

    woorden = sum(len(strip_html(d).split()) for d in docs.values())

    print("pagina's: %d" % len(docs))
    print("woorden in de html: ongeveer %d" % woorden)
    print("uitgaande links: %d" % sum(
        len(re.findall(r'href="https://woningontruimingdester\.nl', d)) for d in docs.values()))
    print("")
    for w in waarschuwingen:
        print("let op: %s" % w)
    if waarschuwingen:
        print("")
    if fouten:
        for f in fouten:
            print("FOUT: %s" % f)
        print("\n%d fouten" % len(fouten))
        return 1
    print("geen fouten")
    return 0


if __name__ == "__main__":
    sys.exit(main())
