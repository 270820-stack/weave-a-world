#!/usr/bin/env python3
"""One-off: strip the black background from the Weave-a-World logo by
flood-filling transparency inward from the image edges, then crop."""

from collections import deque

from PIL import Image

SRC = "/Users/huangzetao/.cursor/projects/Users-huangzetao-Documents-chaewon-minecraft-schematic/assets/Weave_A_World_Logo_Draft_01_Option_01-307c0a49-4df4-4532-ba03-4272cafdcc72.png"
DST = "images/logo.png"
THRESHOLD = 45  # r, g, b all below this counts as background black


def main():
    im = Image.open(SRC).convert("RGBA")
    w, h = im.size
    px = im.load()

    def is_black(x, y):
        r, g, b, a = px[x, y]
        return a > 0 and r < THRESHOLD and g < THRESHOLD and b < THRESHOLD

    seen = [[False] * h for _ in range(w)]
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if is_black(x, y) and not seen[x][y]:
                seen[x][y] = True
                q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            if is_black(x, y) and not seen[x][y]:
                seen[x][y] = True
                q.append((x, y))

    cleared = 0
    while q:
        x, y = q.popleft()
        px[x, y] = (0, 0, 0, 0)
        cleared += 1
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < w and 0 <= ny < h and not seen[nx][ny] and is_black(nx, ny):
                seen[nx][ny] = True
                q.append((nx, ny))

    # Second pass: black counters enclosed inside the letters (A, O, etc.)
    # are not connected to the border, so the flood fill misses them.
    # The lettering sits in the top band of the image; the textile
    # continents (which legitimately contain dark pixels) sit lower, so
    # only sweep the band above the globes.
    text_band = int(h * 0.30)
    swept = 0
    for y in range(text_band):
        for x in range(w):
            if is_black(x, y):
                px[x, y] = (0, 0, 0, 0)
                swept += 1

    bbox = im.getbbox()
    im = im.crop(bbox)
    im.save(DST)
    print(f"cleared {cleared} px + {swept} in letter counters, cropped to {im.size}, saved {DST}")

    # Square favicon from the full logo, centred on a transparent canvas
    side = max(im.size)
    fav = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    fav.paste(im, ((side - im.width) // 2, (side - im.height) // 2))
    fav = fav.resize((128, 128), Image.LANCZOS)
    fav.save("images/favicon.png")
    print("saved images/favicon.png")


if __name__ == "__main__":
    main()
