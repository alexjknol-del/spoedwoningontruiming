# spoedwoningontruiming.nl

Statische site over woningontruiming in Nederland. Gegenereerd met Python zonder dependencies en gehost op Cloudflare Pages.

## Bouwen

```
python3 build.py   # bouwt dist/
python3 check.py   # controleert de gebouwde site
```

`dist/` is meegecommit, zodat Cloudflare Pages niets hoeft te bouwen.
Instelling in Cloudflare Pages: framework preset None, build command leeg, output directory `dist`, production branch `main`.

## Opbouw

- `build.py` bevat sjablonen, CSS, navigatie en de renderlogica
- `content/` bevat de pagina's per rubriek
- `check.py` controleert kapotte links, dubbele meta, ankerteksten, aanspreekvormen, streepjes en dummytekst
