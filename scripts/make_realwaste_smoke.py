"""Baixa 40 imagens do RealWaste para testar o fluxo antes das fotos próprias."""

from __future__ import annotations

import csv
import hashlib
import io
import urllib.request
import zipfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / "data" / "realwaste-smoke"
ARCHIVE = ROOT / "fixtures" / "realwaste-smoke.zip"
SOURCE = "https://github.com/sam-single/realwaste"
LICENSE = "CC BY-NC-SA 4.0"
CLASSES = {
    "papel": ("Paper", 500),
    "plastico": ("Plastic", 921),
    "vidro": ("Glass", 420),
    "metal": ("Metal", 790),
}


def main() -> None:
    photos = DESTINATION / "fotos"
    photos.mkdir(parents=True, exist_ok=True)
    labels = []
    sources = []
    seen_hashes = set()
    for label, (original, maximum) in CLASSES.items():
        numbers = [1 + round(index * (maximum - 1) / 9) for index in range(10)]
        for position, number in enumerate(numbers, start=1):
            name = f"{label}-{position:02d}.jpg"
            relative = f"fotos/{name}"
            url = f"https://raw.githubusercontent.com/sam-single/realwaste/main/RealWaste/{original}/{original}_{number}.jpg"
            target = photos / name
            if not target.exists():
                request = urllib.request.Request(url, headers={"User-Agent": "triagem-reciclavel-smoke-test/1.0"})
                with urllib.request.urlopen(request, timeout=30) as response:
                    target.write_bytes(response.read())
            content = target.read_bytes()
            with Image.open(io.BytesIO(content)) as image:
                image.verify()
            digest = hashlib.sha256(content).hexdigest()
            if digest in seen_hashes:
                raise ValueError(f"Imagem duplicada: {url}")
            seen_hashes.add(digest)
            labels.append((relative, label))
            sources.append((relative, label, url, digest, LICENSE))
    with (DESTINATION / "labels.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(("path", "label"))
        writer.writerows(labels)
    with (DESTINATION / "sources.csv").open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(("path", "label", "source_url", "sha256", "license"))
        writer.writerows(sources)
    (DESTINATION / "README.md").write_text(
        "# Conjunto temporário para teste técnico\n\n"
        "Estas 40 imagens vêm do RealWaste, com 10 exemplos de cada material. "
        "Servem apenas para verificar o fluxo do notebook; não são fotos próprias "
        "e não fazem parte da avaliação local final.\n\n"
        f"Fonte: {SOURCE}\n\nLicença informada pelos autores: {LICENSE}.\n"
        "Consulte `sources.csv` para a origem de cada foto.\n",
        encoding="utf-8",
    )
    ARCHIVE.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(DESTINATION.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(DESTINATION))
    print(f"{len(labels)} imagens em {ARCHIVE}")


if __name__ == "__main__":
    main()
