# Weave-a-World · The Living Colours

A static educational website presenting **ten posters on natural dye traditions and cultural preservation**, by Charles Huang (Hong Kong SAR).

## Structure

- `index.html` — home page (project introduction, stats, featured posters)
- `collection.html` — tab selection screen; filter the ten dyes by colour family or region
- `dyes/*.html` — one poster page per dye, each with nine sections: Overview, Cultural Significance, Chemistry Relevance, Traditional Techniques, Famous Case Story, Modern Revival & Economic Role, Global Exhibition, Conservation Challenges, and How Youth Can Preserve
- `css/style.css` — shared stylesheet (per-page accent colours are set inline in each poster's `<head>`)
- `js/main.js` — tab filtering, reveal-on-scroll animation, and table-of-contents scrollspy

## The ten dyes

1. Indigo — West Africa (Nigeria & Mali)
2. Cochineal — Mexico & Peru
3. Madder Root — India
4. Woad — Celtic Europe
5. Marigold — Navajo Traditions (USA)
6. Saffron — Persia (Iran)
7. Shibori Indigo — Japan
8. Birch Bark — Finland
9. Henna — North Africa & India
10. Logwood — the Caribbean

## Viewing the site

No build step is required — open `index.html` in a browser, or serve locally:

```bash
python3 -m http.server 8642
# then visit http://localhost:8642
```

## Editing content

All poster text lives in `generate_pages.py` (the `DYES` list). After editing, regenerate the HTML:

```bash
python3 generate_pages.py
```
