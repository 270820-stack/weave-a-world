#!/usr/bin/env python3
"""Export the dye poster content as plain-text files ready to paste into
Canva's website editor. Run from dye-heritage-website/:

    python3 canva_export.py

Creates canva-export/ with one file per poster plus home/collection copy.
"""

import re
from pathlib import Path

from generate_pages import BYLINE, DYES, EXTRAS

ROOT = Path(__file__).parent
OUT = ROOT / "canva-export"

TAG_RE = re.compile(r"<[^>]+>")


def strip_tags(text: str) -> str:
    return TAG_RE.sub("", text).replace("&amp;", "&")


def poster_text(dye: dict) -> str:
    extras = EXTRAS[dye["slug"]]
    lines = [
        f"{dye['living']}: {dye['title']}",
        f"Poster {dye['num']} of 10 · {dye['region']}",
        BYLINE,
        "",
        strip_tags(dye["lede"]),
        "",
        "QUICK FACTS",
    ]
    for k, v in dye["facts"].items():
        lines.append(f"  {k}: {v}")
    lines += ["", f"PULL QUOTE (use as a large callout): \u201c{extras['pull']}\u201d", ""]

    for idx, (heading, paras, dyk) in enumerate(dye["sections"], start=1):
        lines.append(f"{idx}. {heading.upper()}")
        for p in paras:
            lines.append(strip_tags(p))
        if dyk:
            lines.append(f"Did you know? {strip_tags(dyk)}")
        lines.append("")

    lines.append("9. HOW YOUTH CAN PRESERVE")
    for n, item in enumerate(dye["youth"], start=1):
        lines.append(f"  {n}. {strip_tags(item)}")
    lines += [
        "",
        "FROM SOURCE TO CLOTH (4-step graphic):",
        "  " + "  →  ".join(extras["process"]),
        "",
        f"ILLUSTRATION: images/{dye['slug']}.png",
        f"Caption: {extras['art_caption']}",
    ]
    return "\n".join(lines) + "\n"


def main():
    OUT.mkdir(exist_ok=True)
    for dye in DYES:
        (OUT / f"{dye['num']}-{dye['slug']}.txt").write_text(poster_text(dye), encoding="utf-8")
        print(f"  wrote canva-export/{dye['num']}-{dye['slug']}.txt")

    home = [
        "WEAVE-A-WORLD · THE LIVING COLOURS",
        "Ten Educational Posters on Cultural Preservation",
        BYLINE,
        "",
        "HERO HEADLINE: The Living Colours of the World's Dye Traditions",
        "",
        "HERO TEXT: Before synthetic chemistry, every colour worn by humanity was coaxed "
        "from leaves, roots, bark, flowers, and even insects. This collection travels through "
        "ten natural dye traditions — from the indigo vats of West Africa to the logwood "
        "forests of the Caribbean — tracing the culture, chemistry, and stories behind each "
        "hue, and asking how the next generation can keep them alive.",
        "",
        "HERO IMAGE: images/home-hero.png",
        "",
        "STATS: 10 Dye Traditions · 6 Continents Touched · 3,000+ Years of Heritage · "
        "9 Lenses per Poster · 1 Shared Future",
        "",
        "SECTION: Colour is Culture — and Chemistry",
        "A vat of fermenting indigo is at once a chemistry experiment, a family inheritance, "
        "and a community ritual. When a natural dye tradition disappears, we lose more than a "
        "colour: we lose recipes refined over centuries, the ecological knowledge of dye plants "
        "and insects, and the ceremonies that bound people to their landscapes.",
        "",
        "THE TEN PAGES (one Canva page per dye):",
    ]
    for dye in DYES:
        home.append(f"  {dye['num']}. {dye['living']}: {dye['title']} ({dye['region']})")
    (OUT / "00-home-page.txt").write_text("\n".join(home) + "\n", encoding="utf-8")
    print("  wrote canva-export/00-home-page.txt")
    print("Done.")


if __name__ == "__main__":
    main()
