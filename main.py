"""One-sentence pitch for a bizarre startup, for make.fun's Ridiculous at First Glance, Real by the Second."""
import os

OUTPUT_PATH = "/output/entry.txt"

PITCH = (
    "We sell naming rights to potholes, so the café on the corner sponsors the crater "
    "outside its door and every driver slows down to read the ad."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
