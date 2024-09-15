import sys
import pikepdf
from PIL import Image
from PIL.ExifTags import TAGS
from sympy import pprint


def meta_pdf(pdf_file):
    pdf = pikepdf.Pdf.open(pdf_file)
    return dict(pdf.docinfo)

def image_meta(image):
    img = Image.open(image)

    info = {
        "Image name": image.filename,
        "Image size": image.size,
        "Image height": image.height,
        "Image width": image.width,
        "Image format": image.format,
        "Image mode": image.mode
    }
    exif = image.getexif()
    for id_tag in exif:
        tag = TAGS.get(id_tag, id_tag)
        data = exif.get(id_tag)

        if dec(data, bytes):
            data = data.decode()

        info[tag] = data

    return info

if __name__ == "__main__":
    file = sys.argv[1]

    if file.endswith(".pdf"):
        print(meta_pdf(file))
    elif file.endswith(".jpg"):
        print(image_meta(file))
    else:
        print("ERROR")
