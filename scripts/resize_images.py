import os
from PIL import Image

ORIGINAL_DIR = "assets/images/original"
THUMB_DIR = "assets/images/thumbs"
LARGE_DIR = "assets/images/large"

THUMB_SIZE = (600, 600)
LARGE_SIZE = (1920, 1920)

QUALITY = 85


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def resize_image(input_path, output_path, max_size):
    with Image.open(input_path) as img:
        img.thumbnail(max_size, Image.LANCZOS)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.save(output_path, "JPEG", quality=QUALITY, optimize=True)


def process():
    for root, _, files in os.walk(ORIGINAL_DIR):
        for filename in files:
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):

                input_path = os.path.join(root, filename)

                # Compute relative path
                relative_path = os.path.relpath(input_path, ORIGINAL_DIR)
                name = os.path.splitext(relative_path)[0]

                thumb_output = os.path.join(THUMB_DIR, name + ".jpg")
                large_output = os.path.join(LARGE_DIR, name + ".jpg")

                ensure_dir(os.path.dirname(thumb_output))
                ensure_dir(os.path.dirname(large_output))

                if not os.path.exists(thumb_output):
                    print(f"Creating thumb: {relative_path}")
                    resize_image(input_path, thumb_output, THUMB_SIZE)

                if not os.path.exists(large_output):
                    print(f"Creating large: {relative_path}")
                    resize_image(input_path, large_output, LARGE_SIZE)


if __name__ == "__main__":
    process()
