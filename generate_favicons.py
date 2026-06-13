#!/usr/bin/env python3
"""Generate favicons for 1w1.ch — SBB red background, '1w1' in Inter Black."""

import io
import os
import sys
import zipfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(SCRIPT_DIR, "docs")
FONT_CACHE = os.path.join(SCRIPT_DIR, ".font_cache", "Inter-Black.ttf")
FONT_ZIP_URL = "https://github.com/rsms/inter/releases/download/v4.0/Inter-4.0.zip"
FONT_IN_ZIP = "extras/ttf/Inter-Black.ttf"

RED = (235, 0, 0)   # #EB0000
TEXT = "1w1"
PADDING = 0.85       # text fills this fraction of the icon size


def ensure_font() -> str:
    if os.path.exists(FONT_CACHE):
        return FONT_CACHE
    import requests
    os.makedirs(os.path.dirname(FONT_CACHE), exist_ok=True)
    print(f"Downloading Inter from GitHub…")
    r = requests.get(FONT_ZIP_URL, stream=True, timeout=30)
    r.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(r.content)) as z:
        with z.open(FONT_IN_ZIP) as src, open(FONT_CACHE, "wb") as dst:
            dst.write(src.read())
    print(f"Font cached → {FONT_CACHE}")
    return FONT_CACHE


def make_icon(size: int, font_path: str):
    from PIL import Image, ImageDraw, ImageFont

    img = Image.new("RGBA", (size, size), (*RED, 255))
    draw = ImageDraw.Draw(img)

    # Binary-search for the largest font size that fits within PADDING * size
    max_px = int(size * PADDING)
    lo, hi = 1, size * 3
    while lo < hi:
        mid = (lo + hi + 1) // 2
        font = ImageFont.truetype(font_path, mid)
        bb = draw.textbbox((0, 0), TEXT, font=font)
        if (bb[2] - bb[0]) <= max_px and (bb[3] - bb[1]) <= max_px:
            lo = mid
        else:
            hi = mid - 1

    font = ImageFont.truetype(font_path, lo)
    bb = draw.textbbox((0, 0), TEXT, font=font)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    x = (size - w) // 2 - bb[0]
    y = (size - h) // 2 - bb[1]
    draw.text((x, y), TEXT, fill=(255, 255, 255, 255), font=font)
    return img


def main():
    font_path = ensure_font()

    from PIL import Image

    png_sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "apple-touch-icon.png": 180,
        "android-chrome-192x192.png": 192,
        "android-chrome-512x512.png": 512,
    }

    # favicon.ico — embed 16, 32, 48
    ico_imgs = [make_icon(s, font_path) for s in [48, 32, 16]]
    ico_path = os.path.join(DOCS_DIR, "favicon.ico")
    ico_imgs[0].save(
        ico_path,
        format="ICO",
        sizes=[(48, 48), (32, 32), (16, 16)],
        append_images=ico_imgs[1:],
    )
    print(f"  favicon.ico")

    for name, size in png_sizes.items():
        img = make_icon(size, font_path).convert("RGB")
        img.save(os.path.join(DOCS_DIR, name), format="PNG")
        print(f"  {name}")

    print("Done.")


if __name__ == "__main__":
    main()
