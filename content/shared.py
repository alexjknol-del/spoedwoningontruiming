# -*- coding: utf-8 -*-
"""Gedeelde bouwstenen voor de contentmodules."""

from build import dester, EMAIL

ONTRUIM_LINKS = [
    ("/ontruimen/spoedontruiming/", "Spoedontruiming"),
    ("/ontruimen/na-overlijden/", "Ontruiming na overlijden"),
    ("/ontruimen/seniorenwoning/", "Seniorenwoning ontruimen"),
    ("/ontruimen/vervuilde-woning/", "Vervuilde woning ontruimen"),
    ("/ontruimen/huurwoning-opleveren/", "Huurwoning opleveren"),
    ("/ontruimen/koopwoning-verkoopklaar/", "Koopwoning verkoopklaar maken"),
    ("/ontruimen/inboedel-opkoop/", "Inboedel verkopen"),
    ("/ontruimen/ontruimen-in-ruil-voor-inboedel/", "Ontruimen in ruil voor de inboedel"),
    ("/ontruimen/bedrijfspand/", "Bedrijfspand en winkel"),
]

KENNIS_LINKS = [
    ("/kennisbank/erfenis-aanvaarden/", "Erfenis aanvaarden of verwerpen"),
    ("/kennisbank/huur-opzeggen-na-overlijden/", "Huur opzeggen na overlijden"),
    ("/kennisbank/verklaring-van-erfrecht/", "Verklaring van erfrecht"),
    ("/kennisbank/oplevering-en-beschrijving/", "Oplevering en beschrijving"),
    ("/kennisbank/zelf-aangebrachte-voorzieningen/", "Zelf aangebrachte voorzieningen"),
    ("/kennisbank/grofvuil-en-milieustraat/", "Grofvuil en milieustraat"),
    ("/kennisbank/asbest-in-de-woning/", "Asbest in de woning"),
    ("/kennisbank/hergebruik-en-kringloop/", "Hergebruik en kringloop"),
    ("/kennisbank/waardevolle-spullen/", "Waardevolle spullen herkennen"),
    ("/kennisbank/begrippenlijst/", "Begrippenlijst"),
]


def hulpbox(dienst_pad, dienst_naam):
    """Donker kader in de zijkolom met een verwijzing naar het uitvoerende bedrijf."""
    return ("dark", "Uitvoering", (
        "<p>%s voert dit werk uit in een groot deel van Nederland, met een vaste prijs vooraf "
        "en oplevering volgens de eisen van corporatie of makelaar.</p>"
        "<p>Pagina over %s: %s</p>"
    ) % (dester("/", kind="brand"), dienst_naam, dester(dienst_pad, kind="bare")))


def contactbox():
    return ("plain", "Iets aanvullen", (
        '<p>Deze gids wordt bijgehouden op basis van openbare bronnen en signalen uit de praktijk. '
        'Aanvullingen en correcties zijn welkom via <a href="mailto:%s">%s</a>.</p>' % (EMAIL, EMAIL)))


def links_rail(titel, items):
    return ("links", titel, items)
