"""Convert and resize photos for the compliment app.

Reads all images from balder/ and lykke/, converts HEIC to JPG, resizes to
max 1200px on the long side, and saves as compressed JPG. Output goes into
the same folder with -web.jpg suffix; originals are kept (so you can rerun).

Run from project root: py scripts/convert_photos.py
"""
from pathlib import Path
from PIL import Image, ImageOps
import pillow_heif

pillow_heif.register_heif_opener()

ROOT = Path(__file__).resolve().parent.parent
FOLDERS = ['balder', 'lykke']
EXTS_INPUT = {'.heic', '.jpg', '.jpeg', '.png'}
MAX_SIZE = 1200
QUALITY = 82


def is_already_web(path: Path) -> bool:
    return path.stem.endswith('-web')


def convert_one(src: Path, dst: Path) -> None:
    img = Image.open(src)
    img = ImageOps.exif_transpose(img)  # respect rotation metadata
    img = img.convert('RGB')
    img.thumbnail((MAX_SIZE, MAX_SIZE), Image.Resampling.LANCZOS)
    img.save(dst, 'JPEG', quality=QUALITY, optimize=True, progressive=True)


def main() -> None:
    for folder in FOLDERS:
        d = ROOT / folder
        if not d.is_dir():
            print(f'skipping {folder}: not a directory')
            continue

        sources = [
            p for p in sorted(d.iterdir())
            if p.is_file()
            and p.suffix.lower() in EXTS_INPUT
            and not is_already_web(p)
        ]

        if not sources:
            print(f'{folder}: nothing to convert')
            continue

        print(f'{folder}: converting {len(sources)} files')
        for src in sources:
            dst = src.with_name(f'{src.stem}-web.jpg')
            try:
                convert_one(src, dst)
                size_kb = dst.stat().st_size // 1024
                print(f'  {src.name} -> {dst.name} ({size_kb} KB)')
            except Exception as e:
                print(f'  FAILED {src.name}: {e}')


if __name__ == '__main__':
    main()
