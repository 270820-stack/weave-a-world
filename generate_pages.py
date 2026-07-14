#!/usr/bin/env python3
"""Generate the ten dye poster pages and the collection screen for the
Weave-a-World "Living Colours" website. Run from dye-heritage-website/:

    python3 generate_pages.py
"""

import html
from pathlib import Path

ROOT = Path(__file__).parent

# Per-dye pull quotes and four-step process labels (harvest → prepare → dye → cloth)
EXTRAS = {
    "indigo-west-africa": {
        "pull": "In some West African societies, over 90% of women's ceremonial and wedding attire is dyed with indigo.",
        "process": ["Harvest the leaves", "Ferment the vat", "Dip & oxidise", "Adire cloth"],
        "art_caption": "A dyer of Abeokuta raises finished adire cloth above the indigo pits — patterns of resist-dyed white against the living blue.",
    },
    "cochineal-mexico-peru": {
        "pull": "Around 70,000 insects for a single pound of red — a dye once traded like silver.",
        "process": ["Gather the insects", "Dry & grind", "Mordant bath", "Crimson wool"],
        "art_caption": "An Oaxacan weaver works crimson threads at the backstrap loom, beside the nopal cactus that hosts the cochineal insect.",
    },
    "madder-india": {
        "pull": "Red for fertility, marriage, and the sacred — madder coloured the great block-printed cottons of the Indian Ocean trade.",
        "process": ["Dig the roots", "Dry & crush", "Simmer & dip", "Bandhani sari"],
        "art_caption": "Block printing beside a pot of madder dye — the bandhani dots of Gujarat reserved in white against alizarin red.",
    },
    "woad-celtic-europe": {
        "pull": "Roman historians wrote of Britons who went into battle painted head to toe in woad blue.",
        "process": ["Pick the leaves", "Ball & age", "Wake the vat", "Celtic plaid"],
        "art_caption": "A Celtic warrior in woad-painted spirals and a woven plaid cloak, flowering woad plants at his feet.",
    },
    "marigold-navajo": {
        "pull": "In Navajo teaching, yellow is the southern direction — warmth, renewal, and the power of the sun.",
        "process": ["Gather the blooms", "Dry the petals", "Simmer & steep", "Woven rug"],
        "art_caption": "A Diné weaver at the upright loom, marigolds at her side and the mesas of the four directions behind.",
    },
    "saffron-persia": {
        "pull": "About 75,000 blossoms, picked by hand, yield a single pound of the world's costliest colour.",
        "process": ["Pluck the stigmas", "Dry & grind", "Warm silk bath", "Golden robe"],
        "art_caption": "The autumn crocus harvest — purple flowers surrendering their three red stigmas for Persia's golden dye.",
    },
    "shibori-indigo-japan": {
        "pull": "No two shibori cloths are ever alike — the fabric remembers every fold, thread, and knot.",
        "process": ["Bind & stitch", "Compost sukumo", "Dip & repeat", "Shibori cloth"],
        "art_caption": "Arashi and kumo patterned banners drying on bamboo poles outside an Arimatsu dye house.",
    },
    "birch-bark-finland": {
        "pull": "One birch harvest could colour batch after batch of yarn — Finnish dyers wasted nothing.",
        "process": ["Collect the bark", "Soak & chop", "Gentle simmer", "Karelian wool"],
        "art_caption": "A dyer in Karelian folk dress stirs the bark pot among the birches, skeins of honey-gold wool drying nearby.",
    },
    "henna-north-africa-india": {
        "pull": "Henna has adorned human hands, hair, and cloth for more than 3,000 years.",
        "process": ["Harvest the leaves", "Mill to powder", "Mix the paste", "Mehndi & cloth"],
        "art_caption": "Hands adorned with mehndi over a bowl of fresh paste — lawsone binding to skin as it has for millennia.",
    },
    "logwood-caribbean": {
        "pull": "A dye so valuable that ships carrying it drew pirate raids across the Caribbean.",
        "process": ["Fell & chip", "Ferment the chips", "Boil the liquor", "Purple-black cloth"],
        "art_caption": "Logwood heartwood stacked on the Caribbean shore, purple cloth on the rack, a trade ship on the horizon.",
    },
}

DYES = [
    # ----------------------------------------------------------------- 1
    {
        "slug": "indigo-west-africa",
        "num": "01",
        "living": "The Living Blue",
        "title": "Indigo Heritage of West Africa",
        "region": "Nigeria & Mali",
        "groups": "blue africa",
        "accent": "#2b3f6b", "accent_deep": "#16233f", "accent_soft": "#e4e9f2",
        "c1": "#2b3f6b", "c2": "#5a74a8",
        "palette": ["#16233f", "#2b3f6b", "#3f5b93", "#5a74a8", "#8fa3c9", "#cdd8ea"],
        "card_blurb": "A thousand-year vat tradition where fermented Indigofera leaves yield the deep blues of adire cloth, Dogon ritual, and West African identity.",
        "facts": {
            "Colour": "Deep vat blue",
            "Source": "Indigofera leaves",
            "Key molecule": "Indigotin",
            "Region": "Nigeria & Mali",
            "Heritage": "~1,000 years",
        },
        "lede": "From the Tellem caves of Mali to the dye pits of Abeokuta, indigo is West Africa's living blue — a colour of status, spiritual protection, and community identity carried in cloth for nearly a millennium.",
        "sections": [
            ("Overview",
             ["West Africa's indigo textile tradition dates back nearly 1,000 years, with Mali's Tellem caves yielding indigo-dyed textiles from the 11th century and Nigeria's royal graves containing 13th-century fragments."],
             "Indigo dye can only be extracted from leaves — not flowers — and the plant is also a legume, helping restore soil nitrogen."),
            ("Cultural Significance",
             ["In certain West African societies, over 90% of ceremonial and wedding attire for women features indigo-dyed textiles as a marker of community identity and social status. Indigo-dyed cloths symbolise status, spiritual protection, and belonging."],
             None),
            ("Chemistry Relevance",
             ["Traditional fermentation changes the vat pH from about 11.9 to 11.3 and shifts the redox potential from −404 mV to as much as −645 mV over the 20–30 day dyeing cycle, creating optimal conditions for indigotin formation. Fermentation of <em>Indigofera</em> leaves releases indigotin, the molecule behind the deep blue."],
             None),
            ("Traditional Techniques",
             ["Abeokuta, nicknamed the \u201cCapital of Adire,\u201d hosts nearly 2,000 indigo textile traders and producers, with more than 2,000 dye pits once reportedly in use across Nigeria."],
             "Some West African dyers beat additional indigo into dried cloth after dyeing, making the colour even darker and giving a distinctive sheen."),
            ("Famous Case Story: Dogon Indigo of Mali",
             ["The Dogon region's Bandiagara Escarpment, a World Heritage Site, supports thousands of households where generations of women maintain the indigo craft as a vital part of Dogon life — centuries-old vat traditions crucial to weddings and rituals."],
             None),
            ("Modern Revival & Economic Role",
             ["Despite global competition, local indigo-dyed products still account for a considerable segment of artisanal textile markets, with towns like Abeokuta (Nigeria) and Ségou (Mali) producing thousands of metres of hand-dyed cloth annually for both local sale and export."],
             None),
            ("Global Exhibition",
             ["The world's largest exhibition dedicated to the indigo heritage of West Africa is <strong>\u201cBlue Africa: Stories Woven in Indigo.\u201d</strong> Hosted at the Nike Art Gallery in Abuja, Nigeria — in partnership with the Spanish gallery MAMAH Africa, the Spanish Museum of Anthropology, and the Spanish Embassy in Nigeria — it opened on 5 July 2024 and featured indigo-dyed textiles from five West African countries."],
             None),
            ("Conservation Challenges",
             ["Chinese-manufactured synthetic adire now sells for around half the cost of local products, accelerating market decline and threatening the centuries-old natural dyeing tradition in Nigeria and Mali."],
             None),
        ],
        "youth": [
            "Start community indigo gardens to grow dye plants.",
            "Record elders' oral histories and traditional recipes.",
            "Organise dyeing workshops and craft fairs.",
            "Develop eco-conscious fashion projects linking heritage and innovation.",
            "Use digital storytelling to raise international awareness of West African indigo.",
        ],
    },
    # ----------------------------------------------------------------- 2
    {
        "slug": "cochineal-mexico-peru",
        "num": "02",
        "living": "The Living Red",
        "title": "Cochineal in Mexico & Peru",
        "region": "Mexico & Peru",
        "groups": "red americas",
        "accent": "#9b1b30", "accent_deep": "#5e0f1e", "accent_soft": "#f5e3e6",
        "c1": "#9b1b30", "c2": "#d4536a",
        "palette": ["#5e0f1e", "#9b1b30", "#c02a45", "#d4536a", "#e493a2", "#f3cfd6"],
        "card_blurb": "Carminic acid from a tiny cactus insect once traded like silver — the crimson of Mixtec, Zapotec, and Andean weaving for over a thousand years.",
        "facts": {
            "Colour": "Crimson to scarlet",
            "Source": "Dactylopius coccus insect",
            "Key molecule": "Carminic acid",
            "Region": "Oaxaca & the Andes",
            "Heritage": "~1,500 years",
        },
        "lede": "A brilliant red born from the dried bodies of an insect living on prickly pear cacti — one of the oldest and most influential dye traditions in the Americas, once as valuable as silver.",
        "sections": [
            ("Overview",
             ["Cochineal is a brilliant red dye made from the dried bodies of the cochineal insect (<em>Dactylopius coccus</em>), which lives on prickly pear cacti in the arid and highland regions of Mexico and the Andes of Peru. Archaeological and chemical analyses show cochineal use in Peru for roughly 1,500 years and in Mexico for about 1,200 years, making it one of the oldest and most influential dye traditions in the Americas."],
             "It can take around 70,000 insects to produce just one pound of cochineal dye, which helped make it as valuable as silver in colonial trade."),
            ("Cultural Significance",
             ["In Indigenous communities of Oaxaca, Puebla, and Tlaxcala in Mexico and the Andean highlands of Peru, cochineal reds have long coloured festival garments, ritual textiles, and sacred imagery linked to the sun, the gods, and blood. Cochineal became a marker of regional identity and technical mastery, with Mixtec, Zapotec, and Andean weavers using its vivid reds in community dress, bridal wear, and ceremonial cloth that signalled status, lineage, and spiritual power."],
             None),
            ("Chemistry Relevance",
             ["Cochineal's colour comes mainly from <strong>carminic acid</strong>, an anthraquinone-based molecule produced by the insect as a defence compound. Its hue can shift from orange to deep crimson depending on pH, with carminic acid showing good stability around mildly acidic conditions (roughly pH 4–5) and changing shade as solutions become more acidic or alkaline — an excellent case study in acid–base chemistry and colour."],
             None),
            ("Traditional Techniques",
             ["Traditional producers brush female insects from nopal cactus pads and then boil, steam, dry, or bake the insects before grinding them into a pigment-rich powder. In the dye houses of Oaxaca and the weaving communities of Peru, artisans simmer the powder in water and adjust pH and mordants (such as alum or lemon juice) to achieve a spectrum from soft pinks to rich scarlets and burgundies on wool and cotton."],
             "Artisans can \u201cover-dye\u201d yarns with cochineal multiple times, or layer it over other natural dyes, to deepen the red and produce complex purples and browns."),
            ("Famous Case Story: Oaxacan & Andean Cochineal",
             ["In Oaxaca, cochineal cultivation and trade were so prosperous under Spanish rule that the region's cities and churches are often described as having been \u201cbuilt on red,\u201d with Indigenous farmers and dyers at the core of the industry. In Peru's Andean textile communities, cochineal remains central to women-led weaving cooperatives, where generations pass down recipes for crimson warps and patterned ponchos vital to local identity and livelihood."],
             None),
            ("Modern Revival & Economic Role",
             ["After collapsing in the late 19th century with the rise of synthetic reds, cochineal has seen renewed demand due to concerns over artificial colourants, making Peru the world's largest producer and Mexico an important supplier once again. Today, cochineal-dyed textiles and yarns form a significant part of artisanal markets in Oaxaca and Andean towns, sold to tourists, exported through fair-trade networks, and used in high-end natural fashion and design."],
             None),
            ("Global Exhibition",
             ["A landmark exhibition highlighting cochineal's role in Mexican and Peruvian heritage is <strong>\u201cCochineal: Mexico's Red,\u201d</strong> an online and museum show by the Harvard Museums of Science &amp; Culture exploring its ritual, artistic, and global trade history from Mesoamerica to Europe. Major museums worldwide now feature cochineal-dyed textiles and paintings in galleries on colonial trade and Indigenous arts, underscoring how this tiny insect reshaped global palettes from royal robes to religious art."],
             None),
            ("Conservation Challenges",
             ["Cheap synthetic red dyes and mass-produced textiles now undercut the price of naturally dyed cochineal cloth, threatening traditional producers who face higher labour and time costs. Climate pressures on cactus-growing regions, market volatility, and the loss of younger apprentices make it harder for small-scale Indigenous farmers and dyers in Mexico and Peru to maintain cochineal-based livelihoods."],
             None),
        ],
        "youth": [
            "Start school or community cactus gardens to cultivate nopal and cochineal insects, linking biology, ecology, and traditional dyeing.",
            "Record elders' stories, myths, and recipes about cochineal and its role in clothing, rituals, and trade for digital archives and classroom use.",
            "Organise natural dye workshops, fashion circles, and local markets where cochineal-dyed textiles are demonstrated and sold alongside other sustainable crafts.",
            "Develop eco-conscious fashion and product lines — scarves, yarns, accessories — that highlight cochineal reds and share transparent stories of Indigenous makers.",
            "Use podcasts, short films, and social media campaigns to explain how a small insect on a cactus transformed global history and why protecting cochineal traditions matters today.",
        ],
    },
    # ----------------------------------------------------------------- 3
    {
        "slug": "madder-india",
        "num": "03",
        "living": "The Living Red",
        "title": "Madder Root in India",
        "region": "India",
        "groups": "red asia",
        "accent": "#a3402c", "accent_deep": "#66261a", "accent_soft": "#f6e6e1",
        "c1": "#a3402c", "c2": "#d47a5a",
        "palette": ["#66261a", "#a3402c", "#bf5a3c", "#d47a5a", "#e5a98f", "#f3d7c9"],
        "card_blurb": "Alizarin reds from Rubia cordifolia roots — the auspicious colour of bridal saris, ajrakh block prints, and centuries of Indian Ocean trade.",
        "facts": {
            "Colour": "Brick red to crimson",
            "Source": "Rubia cordifolia roots",
            "Key molecule": "Alizarin",
            "Region": "Rajasthan, Gujarat & beyond",
            "Heritage": "Many centuries",
        },
        "lede": "The roots of the manjistha plant give India its sacred reds — the colour of fertility, marriage, and blessing woven into saris, turbans, and legendary block-printed cottons.",
        "sections": [
            ("Overview",
             ["Madder is a natural red dye obtained from the roots of plants in the <em>Rubia</em> family, especially <em>Rubia cordifolia</em> (Indian madder, or manjistha) and <em>Rubia tinctorum</em>. In South Asia, archaeological and historical evidence shows madder-dyed textiles in use for many centuries, especially in northern and western India, where it became a key source of durable reds for cotton and silk."],
             "The main colouring compound in madder, alizarin, was so valued that when it was first synthesised in the 19th century it transformed global dye industries and disrupted traditional madder farming."),
            ("Cultural Significance",
             ["In many parts of India, red is associated with fertility, auspiciousness, and marital status, so madder-based reds have long appeared in bridal saris, wedding turbans, and ritual cloth. Madder reds signal protection and blessing in temple offerings, wedding canopies, and everyday garments, marking key life-cycle events such as marriage, childbirth, and major festivals."],
             None),
            ("Chemistry Relevance",
             ["Madder roots contain anthraquinone pigments such as <strong>alizarin</strong> and <strong>purpurin</strong>, which bond strongly to fibres when used with metal-salt mordants like alum or iron. These molecules show pH-sensitive colour shifts — from orange-reds to deeper crimson-browns — making madder an excellent example of how molecular structure, pH, and metal ions influence dye colour and fastness on fabric."],
             None),
            ("Traditional Techniques",
             ["Artisans harvest madder roots after several years of growth, dry and crush them, then simmer the pieces or powder in water to extract the dye. In traditional Indian dye houses, cotton yarns or fabrics are pre-mordanted, then repeatedly dipped in warm madder baths, sometimes combined with other natural dyes or metallic modifiers to produce a palette from soft peach reds to deep brick and wine tones."],
             "Some dyers age madder roots or store extracted dye cakes for months before use, believing this \u201cripening\u201d improves colour depth and evenness on high-quality saris and turbans."),
            ("Famous Case Story: Madder in Indian Textiles",
             ["Regions such as Rajasthan, Gujarat, and parts of Andhra Pradesh became known for madder-dyed block-printed cottons, including intricate ajrakh and other resist-printed textiles exported across the Indian Ocean world. These madder reds — combined with indigo and other natural dyes — formed the signature look of many village and court textiles, with particular shades reserved for bridal saris, ceremonial turbans, or cloths dedicated to local deities. The traditional Bandhani tie-dye of Gujarat, passed down through generations, is among the crafts that carried madder's reds forward."],
             None),
            ("Modern Revival & Economic Role",
             ["Although synthetic alizarin and other chemical reds largely replaced natural madder in mass production, growing interest in eco-friendly, non-toxic dyes has renewed demand for madder-dyed cloth in craft, fashion, and wellness sectors. Today, artisan clusters and social enterprises in India use madder in organic cotton, handloom saris, scarves, and ayurvedic-dyed wellness textiles, selling both domestically and through fair-trade and design-led export channels."],
             None),
            ("Global Exhibition",
             ["Madder-dyed Indian textiles regularly appear in major museum exhibitions on global trade and natural dyes, such as shows on Indian chintz and block-printed cottons in Europe and North America. These exhibitions highlight how madder reds from India influenced European fashion, furnishing fabrics, and printed-cotton industries from the 17th to 19th centuries — much as cochineal and indigo reshaped colour elsewhere."],
             None),
            ("Conservation Challenges",
             ["Low-cost synthetic dyes and industrial printing continue to undercut the price of labour-intensive madder-dyed cloth, putting pressure on small workshops and traditional dyer families. Environmental stresses on water sources, loss of local madder cultivation, and limited market visibility for genuine plant-dyed products all threaten the continuity of this heritage practice."],
             None),
        ],
        "youth": [
            "Start school herb gardens that include madder and other dye plants, documenting their growth, harvesting, and dye properties.",
            "Record elders' stories about red saris, wedding turbans, and ritual cloth, noting where natural dyes like madder once played a central role.",
            "Organise natural dye clubs and workshops where students experiment with madder on small fabric samples and create collaborative art or fashion pieces.",
            "Launch youth-led, eco-conscious fashion micro-brands that clearly label and celebrate madder-dyed items, connecting customers to farmer and dyer stories.",
            "Use zines, social media, and short videos to teach peers how madder links chemistry, ecology, and the cultural meanings of red in Indian life.",
        ],
    },
    # ----------------------------------------------------------------- 4
    {
        "slug": "woad-celtic-europe",
        "num": "04",
        "living": "The Living Blue",
        "title": "Woad in Celtic Europe",
        "region": "Britain, Ireland & Gaul",
        "groups": "blue europe",
        "accent": "#3d5a80", "accent_deep": "#22344c", "accent_soft": "#e6ecf3",
        "c1": "#3d5a80", "c2": "#7a97b8",
        "palette": ["#22344c", "#3d5a80", "#587aa0", "#7a97b8", "#a8bdd2", "#d5e0ea"],
        "card_blurb": "Europe's own indigo — the fermented blue of Pictish warriors, tribal plaids, and medieval vats, drawn from the humble leaves of Isatis tinctoria.",
        "facts": {
            "Colour": "Sky blue to blue-black",
            "Source": "Isatis tinctoria leaves",
            "Key molecule": "Indigotin & indirubin",
            "Region": "Celtic Europe",
            "Heritage": "Since prehistory",
        },
        "lede": "Before Asian indigo reached Europe, woad was the continent's living blue — the colour painted on warriors' skin, woven into tribal plaids, and fermented in vats that 'slept' overnight.",
        "sections": [
            ("Overview",
             ["Woad is a natural blue dye obtained from the leaves of <em>Isatis tinctoria</em>, a plant long cultivated across Europe and western Asia. Archaeological finds and classical sources suggest its use since prehistoric times, most notably among the Celts and Picts of northern Europe. Before indigo became widespread, woad was Europe's main source of stable blues for wool, linen, and leather — used in clothing, decoration, and body painting alike."],
             "The same indigo molecule found in tropical indigo plants occurs in woad too — just in lower concentrations, making its extraction a meticulous process prized by ancient and medieval dyers."),
            ("Cultural Significance",
             ["In Celtic and Pictish traditions, blue carried meanings of strength, otherworldly connection, and protection. Ancient accounts describe warriors painting their skin with woad before battle — a symbol of courage, spiritual defence, and tribal identity. Later, blue came to suggest nobility and steadfastness in Celtic art and textiles, used in garments, shields, and ritual banners that expressed social rank and divine favour."],
             None),
            ("Chemistry Relevance",
             ["Woad leaves yield indigoid pigments such as <strong>indigotin</strong> and <strong>indirubin</strong> through fermentation and oxidation. These compounds bond effectively with fibres, especially wool, creating colourfast blues that vary with pH and mineral content — from light sky tones to deep blue-black. Woad illustrates organic chemistry concepts such as enzymatic hydrolysis, reduction–oxidation cycles, and vat dyeing, bridging nature and molecular transformation."],
             None),
            ("Traditional Techniques",
             ["Artisans harvested woad leaves during summer, crushed them into a pulp, and formed them into \u201cballs\u201d for drying and ageing. Before dyeing, the balls were soaked and fermented to release precursor molecules that oxidise into blue on exposure to air. Celtic and later medieval dyers often controlled the vat's alkalinity using urine or lime, dipping fibres repeatedly to build rich colour and a smooth finish."],
             "Experienced dyers claimed that the strongest blues appeared only after the woad vat \u201cslept\u201d overnight — allowing the fermentation to balance naturally."),
            ("Famous Case Story: Woad in Celtic Textiles",
             ["Across Britain, Ireland, and Gaul, woad-dyed fabrics became hallmarks of tribal identity and local craft. Early woven plaids and patterned cloaks used woad blues with plant-derived yellows and reds to achieve the iconic Celtic palette. Ancient Britons painted their bodies blue for battle — referenced by Roman historians — and in Pictish and Welsh regions, woad blues adorned ceremonial clothing, shields, and banners, later influencing medieval heraldry and the blue tones of European tapestry and ecclesiastical robes."],
             None),
            ("Modern Revival & Economic Role",
             ["Although indigo from Asia and synthetic dyes displaced woad by the 19th century, renewed interest in heritage dyes has sparked a woad renaissance in Britain and France. Artisan producers now grow woad commercially for sustainable textiles, natural cosmetics, and historic re-enactment crafts. Eco-conscious designers use woad on linen, hemp, and wool, promoting it as a gentle alternative to synthetic blues with traceable local origins."],
             None),
            ("Global Exhibition",
             ["Woad-dyed European textiles appear in museum displays on Celtic art, medieval dyeing, and global colour history — often alongside indigo pieces from India, Africa, and Japan. These exhibitions spotlight how Europe's \u201cliving blue\u201d paralleled Asia's \u201cliving indigo,\u201d showing how human creativity found the same molecule through different plants and cultural paths."],
             None),
            ("Conservation Challenges",
             ["Modern textile industries favour cheap synthetic blues, and small-scale woad farming competes with limited market awareness and climate constraints. Many traditional dyeing skills — fermentation control, organic vat maintenance, and plant processing — risk being lost as industrial systems dominate rural landscapes and heritage crafts fade from public view."],
             None),
        ],
        "youth": [
            "Start community dye gardens with woad and other native plants, documenting their growth and blue-yielding processes.",
            "Record local legends and folklore about \u201cblue warriors\u201d and woad's role in ancient Celtic life.",
            "Organise workshops where students produce woad dye vats, experiment with natural fabrics, and display their results as modern art or fashion.",
            "Launch youth-led eco-craft brands that celebrate woad's revival story, connecting farmers, dyers, and young creators.",
            "Use social media and short storytelling videos to explore how woad connects chemistry, ecology, and cultural identity — bringing Europe's ancient blue back to life.",
        ],
    },
    # ----------------------------------------------------------------- 5
    {
        "slug": "marigold-navajo",
        "num": "05",
        "living": "The Living Gold",
        "title": "Marigold in Navajo Traditions",
        "region": "United States (Diné)",
        "groups": "gold americas",
        "accent": "#b07408", "accent_deep": "#6f4a04", "accent_soft": "#f8efdc",
        "c1": "#c98a10", "c2": "#eec24e",
        "palette": ["#6f4a04", "#a06a06", "#c98a10", "#e2a92c", "#eec24e", "#f7e3a4"],
        "card_blurb": "Lutein-rich petals dyed into wool for Navajo rugs and blankets — a gold that carries the sun, the southern direction, and prayers for balance.",
        "facts": {
            "Colour": "Yellow-orange gold",
            "Source": "Tagetes flower petals",
            "Key molecule": "Lutein & carotenoids",
            "Region": "Navajo Nation, USA",
            "Heritage": "Generations of weavers",
        },
        "lede": "Bright petals of Tagetes flowers give Navajo weavers their warm golds — a colour of the southern direction, the sun's life-giving strength, and the continuity of creation.",
        "sections": [
            ("Overview",
             ["Marigold, derived from the bright petals of <em>Tagetes erecta</em> and <em>Tagetes patula</em>, provides a luminous yellow-orange dye long valued by Native American weavers and artisans. Among Navajo dyers, marigold became a respected source of warm golds used in wool for rugs, blankets, and ceremonial cloths. Its sunny hue reflects the desert landscape and the sacred connection between the earth's vitality and the sky's illumination."],
             "The dye's main colouring compounds — lutein and other carotenoids — occur naturally in many flowers and vegetables, linking everyday plants to ancestral dye traditions across the Americas."),
            ("Cultural Significance",
             ["In Navajo teachings, yellow represents the southern direction, warmth, and the power of the sun. Marigold-dyed threads often symbolise harmony and renewal, appearing in woven rugs that depict sacred landscapes or the cycles of day and season. These radiant yellows echo prayers for balance within nature's four directions, honouring the sun's life-giving strength and the continuity of creation."],
             None),
            ("Chemistry Relevance",
             ["Marigold pigments are mainly <strong>carotenoids</strong> — organic molecules that dissolve in alcohol or oil and attach to fibres through natural mordants such as alum. Their colour intensity can shift with pH and light exposure, offering insights into photochemistry and molecular stability. Marigold's dye reactions illustrate how plant-based molecules form durable chromophores while remaining biodegradable and non-toxic."],
             None),
            ("Traditional Techniques",
             ["Artisans gather fresh flower heads, dry them, and then simmer the petals to release the dye. The golden bath is used for wool yarn, sometimes mixed with other native plants like rabbitbrush or chamisa to adjust hue and richness. Navajo dyers often bless the materials before immersion, transforming a dyeing act into a ceremony of renewal."],
             "Some weavers prefer to harvest marigolds at sunrise to capture \u201csun energy\u201d in the dye, believing this gives the yellow greater radiance."),
            ("Famous Case Story: Marigold in Navajo Textiles",
             ["Golden tones from marigold appear in Navajo rugs and blankets that depict sacred desert and sky motifs. These motifs emphasise harmony and directionality — the balance of light and earth — woven into the four-corner structure symbolising the Navajo cosmos. Marigold dyes also feature in community weaving projects that keep natural colour traditions alive in Diné cultural education, with ceremonial rug-weaving bringing communities together each harvest to celebrate nature."],
             None),
            ("Modern Revival & Economic Role",
             ["With growing interest in natural dyes, Navajo artists and sustainable fashion designers increasingly use marigold to highlight Indigenous ecology and craft heritage. Workshops in Arizona and New Mexico teach marigold dyeing alongside other native pigments, creating market opportunities for plant-based wool goods, organic apparel, and educational tourism centred on cultural sustainability."],
             None),
            ("Global Exhibition",
             ["Marigold-dyed Navajo textiles are featured in museum exhibitions on Indigenous fibre arts and North American natural dyes. These displays show how desert landscapes inspired a palette rooted in ecology and the philosophy of balance — connecting marigold's living gold to global narratives of plant wisdom and colour symbolism."],
             None),
            ("Conservation Challenges",
             ["Industrial textile imports, dwindling wild-plant habitats, and reduced youth engagement threaten the continuity of natural dye practice. Access to fresh marigolds, clean water, and traditional knowledge-sharing networks remains vulnerable, particularly in arid regions facing climate stress."],
             None),
        ],
        "youth": [
            "Grow marigolds in community and school gardens to learn dye extraction from local ecology.",
            "Collect elders' stories about rugs and blankets coloured with natural yellows and their meanings.",
            "Host workshops combining botany, chemistry, and traditional weaving using marigold dye.",
            "Develop youth-brand projects that label and celebrate marigold-dyed eco-textiles, connecting consumers to Navajo artistry.",
            "Use zines, short videos, and social posts to teach peers how marigold embodies the bond between sunlight, earth, and cultural identity.",
        ],
    },
    # ----------------------------------------------------------------- 6
    {
        "slug": "saffron-persia",
        "num": "06",
        "living": "The Living Gold",
        "title": "Saffron in Persia (Iran)",
        "region": "Iran",
        "groups": "gold asia",
        "accent": "#c07419", "accent_deep": "#7c480c", "accent_soft": "#f9eedd",
        "c1": "#c07419", "c2": "#e8a94b",
        "palette": ["#7c480c", "#a35f10", "#c07419", "#dd9330", "#e8a94b", "#f4d59c"],
        "card_blurb": "Crocin and crocetin from hand-picked crocus stigmas — the golden glow of Nowruz cloth, Safavid court robes, and Persian ideals of light.",
        "facts": {
            "Colour": "Sunlit gold to amber",
            "Source": "Crocus sativus stigmas",
            "Key molecule": "Crocin & crocetin",
            "Region": "Persia (Iran)",
            "Heritage": "Across dynasties",
        },
        "lede": "One of the world's most precious colours, drawn stigma by stigma from autumn crocuses — a golden hue reserved for garments of status and woven into Nowruz celebrations of rebirth.",
        "sections": [
            ("Overview",
             ["Saffron, obtained from the dried stigmas of <em>Crocus sativus</em>, yields one of the most precious golden dyes and culinary pigments known to history. In ancient and medieval Persia, saffron symbolised luxury, purity, and divine favour, used in garments, royal textiles, and festive decorations. Its luminous tone — somewhere between sunlit gold and amber — became tied to Persian identity and artistry across dynasties."],
             "It takes about 75,000 blossoms to produce a single pound of saffron, making it one of the world's most labour-intensive natural colour sources."),
            ("Cultural Significance",
             ["Golden saffron reflects the qualities of light, wisdom, and renewal — key themes in Persian spirituality. At Nowruz, the Persian New Year, saffron hues adorn celebratory cloths, garments, and table settings, symbolising rebirth and vitality. Historically, saffron-dyed robes and scarves also marked social prestige and priestly rank, signifying closeness to the sun and purity in the Zoroastrian tradition."],
             None),
            ("Chemistry Relevance",
             ["Saffron's distinctive colour comes from carotenoid compounds such as <strong>crocin</strong> and <strong>crocetin</strong>, which dissolve easily in water and yield strong yellow-orange tones. These molecules demonstrate fascinating colour chemistry: their conjugated double bonds absorb specific light wavelengths to produce the golden glow admired in both fabric and food. Saffron shows how molecular structure and natural origin affect hue and sensory perception."],
             None),
            ("Traditional Techniques",
             ["Harvesters carefully pluck saffron stigmas by hand each autumn, then dry and grind them into a fine powder for dyeing. Persian dyers traditionally infuse silk or fine wool in warm saffron baths, yielding lustrous yellows used in ceremonial attire. Because of its cost, saffron dyeing was often reserved for royal workshops or religious vestments."],
             "Some historic recipes blended saffron with pomegranate rind or walnut husk to deepen the tone and improve the fabric's longevity."),
            ("Famous Case Story: Saffron in Persian Textiles",
             ["Saffron-dyed garments appeared throughout ancient Persia — in the Achaemenid, Sassanian, and Safavid courts — where shimmering golden robes symbolised divine kingship and cosmic harmony. Persian miniature art and textiles, such as Safavid court robes, became famed for their saffron dye. Festivals like Nowruz featured saffron-coloured fabrics alongside turquoise and emerald hues, representing sunlight, sky, and vegetation — a colour language still woven into Persian decorative arts and carpet motifs today."],
             None),
            ("Modern Revival & Economic Role",
             ["Iran remains the world's largest producer of saffron, and contemporary designers draw on its symbolic power in sustainable fashion, natural cosmetics, and heritage crafts. Artisans in Mashhad and the Khorasan provinces revive saffron dyeing for eco-textile collections and cultural tourism, combining centuries-old plant knowledge with modern design markets."],
             None),
            ("Global Exhibition",
             ["Saffron-dyed Persian textiles appear in museum exhibitions on Silk Road colours and Middle Eastern craftsmanship, highlighting connections between trade, ritual, and innovation. These displays show how gold — from saffron, metal, or thread — embodied cultural ideals of illumination and nobility across Persian history."],
             None),
            ("Conservation Challenges",
             ["Climate shifts, water scarcity, and fluctuating saffron prices affect both cultivation and artisan dyeing. Traditional dyeing studios face competition from low-cost synthetics, while the rarity of pure saffron dyeing threatens artisanal transmission from elder masters to younger craftspeople."],
             None),
        ],
        "youth": [
            "Cultivate saffron in school or community gardens to learn its growth cycle and heritage value.",
            "Document stories and customs related to saffron use in Persian celebrations such as Nowruz.",
            "Host workshops combining chemistry, culture, and dye experiments with saffron.",
            "Create student-led sustainable brands that showcase saffron-dyed garments linked to Iranian craft traditions.",
            "Use short videos and digital exhibits to teach how saffron bridges science, sunlight, and cultural symbolism in Persian life.",
        ],
    },
    # ----------------------------------------------------------------- 7
    {
        "slug": "shibori-indigo-japan",
        "num": "07",
        "living": "The Living Blue",
        "title": "Shibori Indigo in Japan",
        "region": "Japan",
        "groups": "blue asia",
        "accent": "#1f3a5f", "accent_deep": "#0f2038", "accent_soft": "#e3e9f1",
        "c1": "#1f3a5f", "c2": "#4d6f9d",
        "palette": ["#0f2038", "#1f3a5f", "#33547f", "#4d6f9d", "#7f9bc0", "#c3d2e4"],
        "card_blurb": "Bound, stitched, and folded resist patterns dipped in fermented indigo vats — the 'Japan blue' of samurai, farmers, and the Arimatsu festival.",
        "facts": {
            "Colour": "'Japan blue' indigo",
            "Source": "Persicaria tinctoria leaves",
            "Key molecule": "Leuco-indigo / indigotin",
            "Region": "Japan (Arimatsu, Tokushima)",
            "Heritage": "Over 400 years in Arimatsu",
        },
        "lede": "In Japan, indigo meets pattern: cloth bound, stitched, folded, and clamped before each dip in the fermented vat, so that every shibori textile carries a memory of the hands that shaped it.",
        "sections": [
            ("Overview",
             ["Shibori is Japan's celebrated family of resist-dyeing techniques, in which cloth is bound, stitched, folded, twisted, or clamped before being dipped in indigo vats. Combined with indigo from <em>Persicaria tinctoria</em> (Japanese indigo, or <em>tade-ai</em>), shibori has flourished for centuries — the town of Arimatsu, founded in 1608 along the old Tōkaidō road, has produced shibori textiles for more than 400 years. So deep was the country's love of this colour that 19th-century visitors named it \u201cJapan blue.\u201d"],
             "Because bound and stitched areas resist the dye, no two shibori cloths are ever exactly alike — the fabric itself records the pressure of every fold, thread, and knot."),
            ("Cultural Significance",
             ["Indigo-dyed shibori cloth is linked to samurai, farmers, and seasonal festivals alike. Samurai wore indigo layers beneath armour, believing the dye protected the skin, while farmers and firefighters prized indigo garments for their strength and insect-repelling qualities. Shibori yukata, banners, and furoshiki became part of summer festivals and daily life, and the colour remains a quiet emblem of Japanese aesthetics — patience, subtlety, and harmony with natural processes."],
             None),
            ("Chemistry Relevance",
             ["Japanese indigo dyeing relies on the same core chemistry as African indigo: fermentation and reduction convert insoluble indigotin into soluble <strong>leuco-indigo</strong> in an alkaline vat. Cloth dipped in the yellowish vat turns green, then blue, as leuco-indigo oxidises back to indigotin in the air. In the traditional <em>sukumo</em> method, indigo leaves are composted for about 100 days before fermentation, and dyers read the vat's health by its smell, sheen, and the bloom of bubbles called the \u201cindigo flower.\u201d"],
             None),
            ("Traditional Techniques",
             ["Shibori encompasses dozens of named techniques: <em>kanoko</em> (bound dots), <em>kumo</em> (spider-web pleats), <em>arashi</em> (pole-wrapped \u201cstorm\u201d diagonals), <em>itajime</em> (board-clamped geometry), and <em>nui</em> (stitched resist), among others. Artisans plan patterns thread by thread, then repeat dips and oxidations — sometimes a dozen or more — to build deep, layered blues around the reserved white designs."],
             "The arashi technique is named after the Japanese word for \u201cstorm\u201d because its diagonal lines resemble driving rain — created by wrapping cloth around a long pole before dyeing."),
            ("Famous Case Story: The Arimatsu Shibori Festival",
             ["Arimatsu, near Nagoya, hosts an annual Shibori Festival each June, when the historic merchant street fills with demonstrations, competitions, and thousands of visitors celebrating four centuries of tie-dye artistry. The festival showcases intricate indigo arts passed from master to apprentice, and the townscape of Edo-period dye houses has been recognised as a Japan Heritage site."],
             None),
            ("Modern Revival & Economic Role",
             ["Tokushima Prefecture continues to produce prized <em>sukumo</em> indigo, and contemporary designers — from denim houses to haute couture — collaborate with shibori masters to bring \u201cJapan blue\u201d to global fashion. Workshops, studio tourism, and international exhibitions have made shibori one of the world's most recognised resist-dye traditions, sustaining artisan communities in Arimatsu, Tokushima, and beyond."],
             None),
            ("Global Exhibition",
             ["Shibori textiles feature prominently in international exhibitions on Japanese craft and indigo, and the World Shibori Network — founded after the first International Shibori Symposium in Nagoya in 1992 — has carried the tradition to museums and biennales worldwide. Exhibitions frequently pair Japanese shibori with African, Indian, and Central Asian resist-dye traditions, revealing a global conversation in blue."],
             None),
            ("Conservation Challenges",
             ["Synthetic indigo and machine-printed imitations dominate the market, while the number of <em>sukumo</em> producers and master shibori artisans continues to shrink as practitioners age. Hand-binding intricate patterns can take months per garment, making it difficult for authentic shibori to compete on price — and putting rare techniques at risk of disappearing with their last masters."],
             None),
        ],
        "youth": [
            "Host pattern-making workshops where students learn basic shibori binding, folding, and clamping techniques.",
            "Compare shibori with other tie-dye forms — such as Indian bandhani or West African adire — and document the similarities and differences.",
            "Visit or virtually tour indigo studios and the Arimatsu festival, recording interviews with artisans for school archives.",
            "Grow Japanese indigo in classroom gardens and experiment with fresh-leaf dyeing to observe the chemistry first-hand.",
            "Share finished shibori pieces and process videos online to introduce 'Japan blue' to international audiences.",
        ],
    },
    # ----------------------------------------------------------------- 8
    {
        "slug": "birch-bark-finland",
        "num": "08",
        "living": "The Living Amber",
        "title": "Birch Bark in Finland",
        "region": "Finland & Karelia",
        "groups": "gold europe",
        "accent": "#a37f3d", "accent_deep": "#66501f", "accent_soft": "#f5efe1",
        "c1": "#a37f3d", "c2": "#cbb075",
        "palette": ["#66501f", "#8a6b2e", "#a37f3d", "#bd9a56", "#cbb075", "#e6d8b4"],
        "card_blurb": "Simmered bark of the northern birch yields warm yellows and tans for Karelian folk costume — a forest chemistry kept alive at Finland's folk festivals.",
        "facts": {
            "Colour": "Warm yellow to tan",
            "Source": "Betula (birch) bark & leaves",
            "Key molecule": "Betulin & tannins",
            "Region": "Finland & Karelia",
            "Heritage": "Nordic folk tradition",
        },
        "lede": "In the birch forests of the north, bark and leaves simmered in iron pots give Finnish wool its warm yellows and tans — the quiet colours of Karelian folk costume and forest-borne craft.",
        "sections": [
            ("Overview",
             ["The birch (<em>Betula</em>) is the emblematic tree of Finland, and for centuries its bark and leaves have supplied Nordic households with warm yellow and tan dyes for wool. Birch dyeing belongs to a wider Finnish and Karelian tradition of forest craft, in which the same tree provided shoes, baskets, roofing, and colour. These soft, earthy hues became part of Karelian folk costumes and heritage textiles that are still worn at festivals today."],
             "Birch bark contains up to 30% betulin — the white, powdery compound that gives birch trunks their distinctive pale colour and helps protect the tree from fungi and insects."),
            ("Cultural Significance",
             ["Birch-dyed yellows and tans colour the aprons, skirts, and sashes of Karelian folk costume, part of a heritage of self-sufficient forest living in which every dye came from the surrounding landscape. The birch itself holds a cherished place in Finnish culture — from midsummer birch branches decorating doorways to the gentle birch whisks of the sauna — so wearing its colours ties dress to the rhythm of the northern forest year."],
             None),
            ("Chemistry Relevance",
             ["Birch bark contains <strong>betulin</strong>, a triterpene extracted via simmering, while bark and leaves are rich in <strong>tannins</strong> and flavonoids that bond to wool and aid colour fastness. Leaves gathered in early summer give clear yellows with an alum mordant, while bark simmered longer yields tans and warm browns; adding iron shifts the palette toward grey-greens. Birch dyeing is a fine classroom example of tannin-mordant chemistry and of how harvest time changes a dye's chemical profile."],
             None),
            ("Traditional Techniques",
             ["Dyers collect bark from felled or pruned trees — never stripping living trunks bare — then dry, chop, and soak it before a long, gentle simmer that draws out the colour. Wool yarn, pre-mordanted with alum, steeps in the strained bath until the desired depth is reached; repeated baths from the same bark give progressively softer tones. Leaves, gathered around midsummer, are treated the same way for brighter yellows."],
             "A single birch harvest can dye several successive batches of yarn — Finnish dyers traditionally used every 'after-bath' until the colour was spent, wasting nothing."),
            ("Famous Case Story: The Kaustinen Festival",
             ["Finnish textile artists keep birch-dye traditions alive at the world-renowned Kaustinen Folk Music Festival, the largest folk music and dance festival in the Nordic countries. There, performers in Karelian and Ostrobothnian folk dress — many pieces coloured with plant dyes like birch — turn heritage textiles into living performance, and craft demonstrations pass dyeing skills to new generations."],
             None),
            ("Modern Revival & Economic Role",
             ["Finland's strong design culture has embraced natural dyes, with craft schools, open-air museums, and artisan cooperatives teaching birch and other forest-plant dyeing. Betulin itself has become a subject of biochemical research and sustainable-materials innovation, while naturally dyed Finnish wool products find markets among eco-conscious consumers at home and abroad."],
             None),
            ("Global Exhibition",
             ["Karelian folk costumes and Finnish plant-dyed textiles appear in Nordic museum collections such as the National Museum of Finland and open-air museums like Seurasaari, as well as in international exhibitions on folk dress and sustainable craft. These displays connect the muted, forest-born palette of the north to the global story of natural colour."],
             None),
            ("Conservation Challenges",
             ["Industrial textiles and synthetic dyes have made hand-dyed folk costume a festival rarity rather than daily wear, and the detailed knowledge of harvest times, mordants, and bark preparation survives mainly among older craftspeople. Without active teaching, this quiet strand of Finland's forest heritage risks fading even as interest in sustainability grows."],
             None),
        ],
        "youth": [
            "Identify local dye plants — birch, alder, heather, and others — and map where they grow near school or home.",
            "Collaborate on eco-friendly dyeing projects using responsibly gathered bark and leaves, documenting each recipe and result.",
            "Interview grandparents and local craftspeople about folk costume, recording which colours and plants their families used.",
            "Create a shared swatch archive comparing birch yellows and tans across seasons, mordants, and water sources.",
            "Present findings at local festivals or online, linking Finnish forest chemistry to global natural-dye heritage.",
        ],
    },
    # ----------------------------------------------------------------- 9
    {
        "slug": "henna-north-africa-india",
        "num": "09",
        "living": "The Living Earth",
        "title": "Henna in North Africa & India",
        "region": "Morocco to Rajasthan",
        "groups": "deep africa asia",
        "accent": "#8c4a1f", "accent_deep": "#582b0f", "accent_soft": "#f6ebe0",
        "c1": "#8c4a1f", "c2": "#c07d4a",
        "palette": ["#582b0f", "#7a3d17", "#8c4a1f", "#a86234", "#c07d4a", "#e0b48c"],
        "card_blurb": "Lawsone from crushed henna leaves binds to skin and cloth alike — the red-brown of Mehndi nights, Moroccan weddings, and rites of passage.",
        "facts": {
            "Colour": "Red-brown to burnt orange",
            "Source": "Lawsonia inermis leaves",
            "Key molecule": "Lawsone",
            "Region": "North Africa & South Asia",
            "Heritage": "Millennia of ritual use",
        },
        "lede": "Few dyes live so close to the body: crushed henna leaves stain skin, hair, and cloth with the warm red-browns of weddings, festivals, and rites of passage from Morocco to Rajasthan.",
        "sections": [
            ("Overview",
             ["Henna is a red-brown dye obtained from the dried, powdered leaves of <em>Lawsonia inermis</em>, a shrub thriving in the hot, semi-arid climates of North Africa, the Middle East, and South Asia. Used for millennia on skin, hair, leather, and textiles, henna is best known for Mehndi — the intricate body art applied at weddings and festivals — but it also colours fabric printing and craft traditions across two continents."],
             "Traces of henna have been found on the hair and nails of Egyptian mummies, suggesting the dye has adorned human bodies for well over 3,000 years."),
            ("Cultural Significance",
             ["Henna marks life's great thresholds. In North Africa, the Moroccan wedding traditionally includes a henna night, when the bride's hands and feet are painted with protective motifs believed to bring baraka — blessing — and ward off misfortune. In India and Pakistan, Mehndi ceremonies gather women to sing and adorn the bride before marriage, and henna appears at Eid, Diwali, Karva Chauth, and other festivals. Beyond the body, henna-dyed and henna-printed cloth carries the same associations of joy, fertility, and protection."],
             None),
            ("Chemistry Relevance",
             ["Henna's colour comes from <strong>lawsone</strong> (2-hydroxy-1,4-naphthoquinone), a molecule that binds to the keratin proteins of skin and hair — and to the proteins in wool — through a Michael addition reaction. The bond strengthens with warmth and mildly acidic conditions, which is why pastes are mixed with lemon juice and left on warm skin for hours. On cellulose fibres like cotton, mordants help fix the dye, making henna a vivid illustration of protein versus plant-fibre dye chemistry."],
             None),
            ("Traditional Techniques",
             ["Leaves are harvested, dried, and milled into a fine green powder, then mixed with water, lemon juice, tea, or aromatic oils into a smooth paste. For body art, artists pipe the paste through rolled cones into freehand patterns — Moroccan geometric motifs, Indian paisleys and florals — that darken as the lawsone oxidises over the following days. For textiles, henna baths and block printing colour wool and cotton, especially at warmer temperatures where the dye takes best."],
             "Fresh henna stain is bright orange, then deepens to red-brown over 48 hours as lawsone oxidises within the skin's keratin — the design literally matures after the paste is removed."),
            ("Famous Case Story: The Henna Night",
             ["From Fez to Marrakech, the Moroccan henna night remains a centrepiece of wedding celebration, with a <em>hannaya</em> (henna artist) adorning the bride while family members receive smaller motifs in solidarity. In India, Rajasthan's Sojat region grows much of the world's finest henna, supplying the Mehndi traditions of millions of weddings — henna-dyed cloth and body art together weaving one continuous story of celebration across cultures."],
             None),
            ("Modern Revival & Economic Role",
             ["Henna remains a thriving cultural economy: Sojat in Rajasthan received Geographical Indication status for its henna, and artists across North Africa, South Asia, and diaspora communities worldwide sustain livelihoods through bridal art, festivals, and cosmetics. Natural henna is also reclaiming ground from chemical \u201cblack henna\u201d additives, as consumers seek the safe, plant-based original."],
             None),
            ("Global Exhibition",
             ["Henna traditions feature in museum programmes on body art and adornment worldwide, from ethnographic collections of Moroccan bridal dress to South Asian galleries displaying Mehndi-adorned wedding textiles. Community henna festivals and living-artist demonstrations — increasingly hosted by major museums — treat the art as intangible heritage performed on the body itself."],
             None),
            ("Conservation Challenges",
             ["Chemical shortcuts threaten both the craft and its reputation: \u201cblack henna\u201d adulterated with PPD causes injuries that erode trust in the tradition, while synthetic dyes displace henna in textile use. Climate stress on arid growing regions and the commercial pressure to simplify intricate regional motifs into generic patterns endanger the diversity of henna's living heritage."],
             None),
        ],
        "youth": [
            "Exchange henna designs across cultures — comparing Moroccan geometric, Indian floral, and Gulf styles — and document their meanings.",
            "Record family celebrations where henna appears, building an archive of photographs, stories, and regional recipes.",
            "Try fabric block-printing and wool dyeing with natural henna to explore its chemistry beyond body art.",
            "Learn to identify pure henna and raise awareness about the dangers of chemical 'black henna' additives.",
            "Host intercultural Mehndi evenings at school or community centres, inviting elders and artists to teach traditional motifs.",
        ],
    },
    # ----------------------------------------------------------------- 10
    {
        "slug": "logwood-caribbean",
        "num": "10",
        "living": "The Living Shadow",
        "title": "Logwood in the Caribbean",
        "region": "Jamaica, Belize & Campeche",
        "groups": "deep americas",
        "accent": "#4a2c5c", "accent_deep": "#2c1838", "accent_soft": "#ece5f1",
        "c1": "#4a2c5c", "c2": "#7c5a94",
        "palette": ["#2c1838", "#4a2c5c", "#623f78", "#7c5a94", "#a488b8", "#d3c4de"],
        "card_blurb": "Hematein purples and blacks from a thorny Caribbean tree — a dye that drove pirate raids, coloured colonial trade, and lives on in maroon festival dress.",
        "facts": {
            "Colour": "Purple to blue-black",
            "Source": "Haematoxylum campechianum heartwood",
            "Key molecule": "Hematein",
            "Region": "Caribbean & Central America",
            "Heritage": "Since the 16th century",
        },
        "lede": "From the heartwood of a thorny tree came the purples and blacks that clothed empires — a dye so valuable that ships carrying it drew pirates, and so enduring that it still stains microscope slides today.",
        "sections": [
            ("Overview",
             ["Logwood (<em>Haematoxylum campechianum</em>) is a thorny tree native to the Yucatán, Belize, and the Caribbean whose dense heartwood yields dyes ranging from violet and purple to deep blue-black. From the 16th century onward, logwood became one of the Atlantic world's most valuable commodities, shipped by the tonne to European dye houses hungry for affordable blacks and purples."],
             "Haematoxylin extracted from logwood is still the standard stain used in histology laboratories worldwide — the same tree that dyed colonial coats now colours microscope slides in nearly every hospital."),
            ("Cultural Significance",
             ["In the Caribbean, logwood's story is inseparable from the history of colonial trade and slavery: enslaved and free Black communities cut, processed, and dyed with logwood, and its purples and blacks coloured garments within those communities. In Jamaica, logwood remains woven into cultural memory — from the maroon communities whose festival costumes carry its deep tones to the logwood-honey industry that grew where dye forests once stood."],
             None),
            ("Chemistry Relevance",
             ["Logwood heartwood contains haematoxylin, which oxidises to <strong>hematein</strong> — the true colouring agent. Hematein is a remarkable chameleon: with alum mordants it gives violets and purples, with iron it yields blue-blacks, and with chrome it produces the fast blacks once standard for wool. Because its colour shifts dramatically with pH and metal ions, logwood is a classic demonstration of mordant chemistry and coordination complexes in natural dyeing."],
             None),
            ("Traditional Techniques",
             ["Dyers chip or rasp the dense heartwood, ferment or soak the chips to develop the colour, then boil them to make a strong dye liquor. Cloth or yarn mordanted with alum, iron, or copper is worked through the hot bath, with the final shade — plum, violet, grey, or black — controlled by the mordant choice and the bath's pH. Caribbean and Central American dyers historically exported both raw logs and concentrated extract cakes."],
             "By adjusting only the mordant and pH, a single logwood bath can produce purple, blue, grey, or black — early modern dyers called it one of the most 'obedient' dyes in the workshop."),
            ("Famous Case Story: The Logwood Coast & Pirate Raids",
             ["In the 17th century, logwood was so profitable that English \u201cBaymen\u201d — many of them former buccaneers — settled the Belize and Campeche coasts to cut it, and ships laden with the \u201cblue dye\u201d wood became prime targets for pirate raids in Jamaican waters. The logwood trade shaped treaties, settlements, and the founding of Belize itself, while in Jamaica the tree's legacy survives in maroon festival costumes and in place names across the island."],
             None),
            ("Modern Revival & Economic Role",
             ["Though synthetic dyes ended the great logwood trade, the tree remains economically alive: Jamaican logwood honey is a prized export, haematoxylin supports the global histology industry, and natural dyers are rediscovering logwood's purples for craft textiles and heritage fashion. Caribbean cultural projects increasingly reclaim logwood's history as part of the region's story of labour, resistance, and creativity."],
             None),
            ("Global Exhibition",
             ["Logwood-dyed textiles and trade artefacts appear in maritime and colonial-history museums across Britain, the Caribbean, and the Americas, in exhibitions tracing the Atlantic dye trade. Displays pairing logwood with indigo and cochineal show how three American dyes — black, blue, and red — coloured the wardrobes of early modern Europe."],
             None),
            ("Conservation Challenges",
             ["The living knowledge of logwood dyeing — vat management, mordant recipes, and the craft's Caribbean history — is far scarcer than the tree itself, which now grows as an invasive thicket in parts of the region. Without deliberate documentation and teaching, the human story of logwood risks being reduced to a footnote in trade history rather than a living heritage of the communities who worked it."],
             None),
        ],
        "youth": [
            "Research local dye trees and the history of the logwood trade in your parish or district, mapping old logwood stations and place names.",
            "Produce logwood swatch collections showing how mordants and pH change the colour, and share the results with other schools.",
            "Create history projects linking logwood to Caribbean stories of piracy, colonial trade, maroon resistance, and emancipation.",
            "Interview beekeepers, dyers, and elders about logwood's place in local livelihoods, past and present.",
            "Exhibit logwood-dyed craft alongside its history at school fairs and cultural festivals, reclaiming the dye's Caribbean legacy.",
        ],
    },
]

BYLINE = "By Charles Huang (Hong Kong SAR) · Weave-a-World"


def nav(depth: int, active: str) -> str:
    p = "../" if depth else ""
    return f"""  <nav class="topnav">
    <a class="brand" href="{p}index.html"><span class="brand-mark"></span>Weave-a-World</a>
    <div class="topnav-links">
      <a href="{p}index.html"{' class="active"' if active == 'home' else ''}>Home</a>
      <a href="{p}collection.html"{' class="active"' if active == 'collection' else ''}>The Ten Dyes</a>
      <a href="{p}collection.html#youth">Youth Action</a>
    </div>
  </nav>"""


def footer() -> str:
    return """  <footer>
    <div class="shell footer-inner">
      <a class="brand" href="#"><span class="brand-mark"></span>Weave-a-World</a>
      <p>The Living Colours · Ten Educational Posters on Cultural Preservation · By Charles Huang (Hong Kong SAR)</p>
    </div>
  </footer>"""


def head(title: str, depth: int, accent=None, accent_deep=None, accent_soft=None) -> str:
    p = "../" if depth else ""
    override = ""
    if accent:
        override = f"""
  <style>
    :root {{ --accent: {accent}; --accent-deep: {accent_deep}; --accent-soft: {accent_soft}; }}
  </style>"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;1,500&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Jost:wght@300;400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{p}css/style.css" />{override}
</head>"""


def poster_page(i: int, dye: dict) -> str:
    prev_dye = DYES[(i - 1) % len(DYES)]
    next_dye = DYES[(i + 1) % len(DYES)]

    facts = "\n".join(
        f'      <div class="fact"><b>{html.escape(k)}</b><span>{html.escape(v)}</span></div>'
        for k, v in dye["facts"].items()
    )

    extras = EXTRAS[dye["slug"]]

    pull_quote = f"""      <blockquote class="pull-quote reveal">
        <span class="pull-quote-mark" aria-hidden="true">&ldquo;</span>
        <p>{extras['pull']}</p>
      </blockquote>"""

    process_steps = "\n".join(
        f"""          <div class="process-step">
            <span class="process-dot">{n}</span>
            <span class="process-label">{html.escape(label)}</span>
          </div>"""
        for n, label in enumerate(extras["process"], start=1)
    )
    process_strip = f"""      <div class="process-strip reveal" aria-label="From plant to cloth">
        <span class="process-title">From Source to Cloth</span>
        <div class="process-steps">
{process_steps}
        </div>
      </div>"""

    toc_items = []
    sections_html = []
    for idx, (heading, paras, dyk) in enumerate(dye["sections"], start=1):
        sec_id = f"s{idx}"
        toc_items.append(f'        <a href="#{sec_id}">{idx}. {html.escape(heading)}</a>')
        para_tags = []
        for p_i, p in enumerate(paras):
            cls = ' class="dropcap"' if idx == 1 and p_i == 0 else ""
            para_tags.append(f"        <p{cls}>{p}</p>")
        paras_html = "\n".join(para_tags)
        dyk_html = ""
        if dyk:
            dyk_html = f"""
        <div class="didyouknow">
          <b>Did you know?</b>
          <p>{dyk}</p>
        </div>"""
        sections_html.append(f"""      <section class="poster-section reveal" id="{sec_id}">
        <div class="poster-section-head">
          <span class="poster-section-num">{idx:02d}</span>
          <h2>{html.escape(heading)}</h2>
        </div>
{paras_html}{dyk_html}
      </section>""")
        # Interleave feature elements between the prose sections
        if idx == 2:
            sections_html.append(pull_quote)
        elif idx == 4:
            sections_html.append(process_strip)

    # Section 9: youth preservation
    youth_id = "s9"
    toc_items.append(f'        <a href="#{youth_id}">9. How Youth Can Preserve</a>')
    youth_items = "\n".join(f"          <li>{item}</li>" for item in dye["youth"])
    sections_html.append(f"""      <section class="poster-section reveal" id="{youth_id}">
        <div class="poster-section-head">
          <span class="poster-section-num">09</span>
          <h2>How Youth Can Preserve</h2>
        </div>
        <ol class="youth-list">
{youth_items}
        </ol>
      </section>""")

    palette = "".join(f'<span style="background:{c}"></span>' for c in dye["palette"])

    return f"""{head(f"{dye['living']}: {dye['title']} · Weave-a-World", 1, dye['accent'], dye['accent_deep'], dye['accent_soft'])}
<body>
{nav(1, 'collection')}

  <header class="poster-hero">
    <div class="shell poster-hero-grid">
      <div class="poster-hero-text">
        <div class="poster-kicker">Poster {dye['num']} of 10 · {html.escape(dye['region'])}</div>
        <h1><em>{html.escape(dye['living'])}:</em><br />{html.escape(dye['title'])}</h1>
        <p class="poster-byline">{html.escape(BYLINE)}</p>
        <p class="poster-lede">{dye['lede']}</p>
      </div>
      <figure class="poster-hero-art">
        <img src="../images/{dye['slug']}.png" alt="Textile-art illustration: {html.escape(dye['title'])}" />
        <figcaption>{html.escape(extras['art_caption'])}</figcaption>
      </figure>
    </div>
  </header>

  <div class="factbar">
    <div class="shell factbar-inner">
{facts}
    </div>
  </div>

  <main class="poster-body">
    <div class="shell poster-layout">
      <aside class="poster-toc">
{chr(10).join(toc_items)}
      </aside>
      <article>
        <div class="palette-strip" aria-hidden="true">{palette}</div>
{chr(10).join(sections_html)}
      </article>
    </div>
  </main>

  <nav class="pager">
    <div class="pager-inner">
      <a href="{prev_dye['slug']}.html" class="prev">
        <small>&larr; Previous poster</small>
        <b>{html.escape(prev_dye['title'])}</b>
      </a>
      <a href="{next_dye['slug']}.html" class="next">
        <small>Next poster &rarr;</small>
        <b>{html.escape(next_dye['title'])}</b>
      </a>
    </div>
  </nav>

{footer()}
  <script src="../js/main.js"></script>
</body>
</html>
"""


def collection_page() -> str:
    cards = []
    for dye in DYES:
        cards.append(f"""      <a class="dye-card reveal" href="dyes/{dye['slug']}.html" data-groups="{dye['groups']}" style="--c1:{dye['c1']}; --c2:{dye['c2']}">
        <div class="dye-card-swatch">
          <img src="images/{dye['slug']}.png" alt="Textile-art illustration: {html.escape(dye['title'])}" loading="lazy" />
          <span class="dye-card-num">No. {dye['num']}</span>
          <span class="dye-card-region-tag">{html.escape(dye['region'])}</span>
        </div>
        <div class="dye-card-body">
          <span class="sub">{html.escape(dye['living'])}</span>
          <h3>{html.escape(dye['title'])}</h3>
          <p>{html.escape(dye['card_blurb'])}</p>
          <span class="dye-card-cta">Read the poster &rarr;</span>
        </div>
      </a>""")

    tabs = [
        ("all", "All Ten Dyes"),
        ("blue", "Blues"),
        ("red", "Reds"),
        ("gold", "Golds"),
        ("deep", "Deep Hues"),
        ("africa", "Africa"),
        ("asia", "Asia"),
        ("americas", "The Americas"),
        ("europe", "Europe"),
    ]
    tabs_html = "\n".join(
        f'      <button class="tab{" active" if key == "all" else ""}" data-filter="{key}">{label}</button>'
        for key, label in tabs
    )

    return f"""{head("The Ten Dyes · Weave-a-World", 0)}
<body>
{nav(0, 'collection')}

  <header class="collection-hero">
    <div class="shell">
      <p class="eyebrow">The Collection</p>
      <h1>Ten Dyes, Ten Living Traditions</h1>
      <p>Each poster below explores one natural dye through nine lenses — its overview, cultural significance, chemistry, traditional techniques, a famous case story, modern revival, global exhibitions, conservation challenges, and the ways young people can keep the tradition alive. Choose a tab to explore by colour family or by region.</p>
    </div>
  </header>

  <div class="shell" id="youth">
    <div class="tabs" role="tablist" aria-label="Filter the dye collection">
{tabs_html}
    </div>

    <div class="dye-grid">
{chr(10).join(cards)}
    </div>
  </div>

{footer()}
  <script src="js/main.js"></script>
</body>
</html>
"""


def index_page() -> str:
    spectrum = "".join(f'<span style="background:{d["c1"]}"></span>' for d in DYES)
    featured = []
    for dye in DYES[:3]:
        featured.append(f"""      <a class="dye-card reveal" href="dyes/{dye['slug']}.html" style="--c1:{dye['c1']}; --c2:{dye['c2']}">
        <div class="dye-card-swatch">
          <img src="images/{dye['slug']}.png" alt="Textile-art illustration: {html.escape(dye['title'])}" loading="lazy" />
          <span class="dye-card-num">No. {dye['num']}</span>
          <span class="dye-card-region-tag">{html.escape(dye['region'])}</span>
        </div>
        <div class="dye-card-body">
          <span class="sub">{html.escape(dye['living'])}</span>
          <h3>{html.escape(dye['title'])}</h3>
          <p>{html.escape(dye['card_blurb'])}</p>
          <span class="dye-card-cta">Read the poster &rarr;</span>
        </div>
      </a>""")

    return f"""{head("Weave-a-World · The Living Colours", 0)}
<body>
{nav(0, 'home')}

  <header class="hero-home">
    <div class="shell hero-home-grid">
      <div>
        <p class="eyebrow">Ten Educational Posters on Cultural Preservation</p>
        <h1>The <em>Living Colours</em> of the World's Dye Traditions</h1>
        <p class="hero-lede">Before synthetic chemistry, every colour worn by humanity was coaxed from leaves, roots, bark, flowers, and even insects. This collection travels through ten natural dye traditions — from the indigo vats of West Africa to the logwood forests of the Caribbean — tracing the culture, chemistry, and stories behind each hue, and asking how the next generation can keep them alive.</p>
        <p class="hero-byline">{html.escape(BYLINE)}</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="collection.html">Explore the Ten Dyes</a>
          <a class="btn btn-ghost" href="dyes/indigo-west-africa.html">Begin with Indigo</a>
        </div>
      </div>
      <figure class="hero-home-art reveal visible">
        <img src="images/home-hero.png" alt="Textile-art illustration of naturally dyed fabrics from ten traditions hanging on lines" />
        <figcaption>Ten traditions on one line — indigo, cochineal, madder, woad, marigold, saffron, shibori, birch, henna, and logwood.</figcaption>
      </figure>
    </div>
  </header>

  <div class="spectrum" aria-hidden="true">{spectrum}</div>

  <div class="ticker" aria-hidden="true">
    <div class="ticker-track">
      <span>Indigotin</span><i>◆</i><span>Carminic Acid</span><i>◆</i><span>Alizarin</span><i>◆</i><span>Indirubin</span><i>◆</i><span>Lutein</span><i>◆</i><span>Crocetin</span><i>◆</i><span>Leuco-indigo</span><i>◆</i><span>Betulin</span><i>◆</i><span>Lawsone</span><i>◆</i><span>Hematein</span><i>◆</i>
      <span>Indigotin</span><i>◆</i><span>Carminic Acid</span><i>◆</i><span>Alizarin</span><i>◆</i><span>Indirubin</span><i>◆</i><span>Lutein</span><i>◆</i><span>Crocetin</span><i>◆</i><span>Leuco-indigo</span><i>◆</i><span>Betulin</span><i>◆</i><span>Lawsone</span><i>◆</i><span>Hematein</span><i>◆</i>
    </div>
  </div>

  <main>
    <div class="shell">
      <div class="stats reveal">
        <div class="stat"><b>10</b><span>Dye Traditions</span></div>
        <div class="stat"><b>6</b><span>Continents Touched</span></div>
        <div class="stat"><b>3,000+</b><span>Years of Heritage</span></div>
        <div class="stat"><b>9</b><span>Lenses per Poster</span></div>
        <div class="stat"><b>1</b><span>Shared Future</span></div>
      </div>

      <section class="mission">
        <div class="reveal">
          <p class="eyebrow">Why This Project</p>
          <h2>Colour is Culture — and Chemistry</h2>
          <p>A vat of fermenting indigo is at once a chemistry experiment, a family inheritance, and a community ritual. When a natural dye tradition disappears, we lose more than a colour: we lose recipes refined over centuries, the ecological knowledge of dye plants and insects, and the ceremonies that bound people to their landscapes.</p>
          <p>These ten posters were created for the Weave-a-World cultural preservation initiative. Each pairs the <strong>cultural significance</strong> of a dye with its <strong>molecular story</strong> — indigotin, carminic acid, alizarin, lawsone, hematein and more — alongside famous case studies and concrete actions young people can take today.</p>
        </div>
        <div class="mission-panel reveal">
          <h3>Every Poster Explores</h3>
          <ul>
            <li>Overview &amp; historical roots</li>
            <li>Cultural significance</li>
            <li>Chemistry relevance</li>
            <li>Traditional techniques</li>
            <li>A famous case story</li>
            <li>Modern revival &amp; economic role</li>
            <li>Global exhibitions</li>
            <li>Conservation challenges</li>
            <li>How youth can preserve</li>
          </ul>
        </div>
      </section>

      <section class="home-preview">
        <div class="home-preview-head reveal">
          <div>
            <p class="eyebrow">Begin the Journey</p>
            <h2 class="section-title">Featured Posters</h2>
          </div>
          <p>Three traditions to start with — then browse the full collection of ten by colour family or region.</p>
        </div>
        <div class="dye-grid">
{chr(10).join(featured)}
        </div>
        <div class="hero-actions" style="justify-content:center">
          <a class="btn btn-primary" href="collection.html">View All Ten Posters</a>
        </div>
      </section>
    </div>
  </main>

{footer()}
  <script src="js/main.js"></script>
</body>
</html>
"""


def main():
    dyes_dir = ROOT / "dyes"
    dyes_dir.mkdir(exist_ok=True)
    for i, dye in enumerate(DYES):
        (dyes_dir / f"{dye['slug']}.html").write_text(poster_page(i, dye), encoding="utf-8")
        print(f"  wrote dyes/{dye['slug']}.html")
    (ROOT / "collection.html").write_text(collection_page(), encoding="utf-8")
    print("  wrote collection.html")
    (ROOT / "index.html").write_text(index_page(), encoding="utf-8")
    print("  wrote index.html")
    print("Done.")


if __name__ == "__main__":
    main()
