"""Resize and compress BAU photos for web use."""
from pathlib import Path
from PIL import Image, ImageOps

RAW = Path("bau-raw")
OUT = Path("images")
OUT.mkdir(exist_ok=True)

# (source, dest, max_long_edge, quality)
HERO_JOBS = [
    ("04FJ1717.jpg",                         "hero-stage.jpg",          2200, 82),
    ("IMG_20251004_175627.jpg",              "hero-editorial.jpg",      2200, 82),
    ("IMG_20260318_120041.jpg",              "founder-portrait.jpg",    1800, 82),
    ("IMG_20260228_110717.jpg",              "community-lifestyle.jpg", 2000, 82),
    ("IMG-20260303-WA0019.jpg",              "fashion-flatlay.jpg",     1600, 82),
    ("IMG-20260303-WA0024.jpg",              "fashion-detail.jpg",      1600, 82),
    ("IMG-20260301-WA0019_edit_61698866594751.jpg", "founder-lifestyle.jpg", 1800, 82),
]

# Event gallery tiles for Carol's Pick
TILE_JOBS = [
    ("IMG-20260205-WA0003(1).jpg",  "event-erre-duo.jpg",     1200, 80),
    ("IMG-20260205-WA0004(1).jpg",  "event-signature-style.jpg", 1200, 80),
    ("IMG-20260205-WA0005.jpg",     "event-power-dressing.jpg", 1200, 80),
    ("IMG_20260228_125323.jpg",     "community-masterclass.jpg", 1600, 82),
    ("IMG-20260303-WA0016.jpg",     "event-grazing.jpg",       1400, 82),
]

def resize(src: Path, dst: Path, max_edge: int, quality: int) -> None:
    img = Image.open(src)
    img = ImageOps.exif_transpose(img)
    if img.mode != "RGB":
        img = img.convert("RGB")
    w, h = img.size
    if max(w, h) > max_edge:
        if w >= h:
            new_w = max_edge
            new_h = round(h * max_edge / w)
        else:
            new_h = max_edge
            new_w = round(w * max_edge / h)
        img = img.resize((new_w, new_h), Image.LANCZOS)
    img.save(dst, "JPEG", quality=quality, optimize=True, progressive=True)
    size_kb = dst.stat().st_size / 1024
    print(f"  {dst.name:30s} {img.size[0]}x{img.size[1]}  {size_kb:7.1f} KB")

print("Hero / section backgrounds:")
for src, dst, edge, q in HERO_JOBS:
    resize(RAW / src, OUT / dst, edge, q)

print("\nGallery tiles:")
for src, dst, edge, q in TILE_JOBS:
    resize(RAW / src, OUT / dst, edge, q)

print("\nDone.")
