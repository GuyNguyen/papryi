import cv2
import pathlib

from isbntools.app import meta
from pathlib import Path


def isbn_formatter(num: str) -> str:
    num = "-".join([num[:3], num[3:4], num[4:9], num[9:12], num[12:13]])

    return num


def barcode_reader(image: str) -> None:
    image = cv2.imread(image)
    bd = cv2.barcode.BarcodeDetector()

    decoded_info = bd.detectAndDecode(image)

    isbn = isbn_formatter(decoded_info[1][0])

    print(isbn)
    print(meta(isbn))


def isbn_grab(images: list[Path]) -> None:
    for image in images:
        print(image)
        barcode_reader(str(image))


def list_of_files() -> list[Path]:
    path = pathlib.Path("papryi\\barcodes").glob("*.jpg")
    result: list[Path] = [file for file in path if file.is_file()]

    return result


if __name__ == "__main__":
    images: list[Path] = list_of_files()
    isbn_grab(images)
