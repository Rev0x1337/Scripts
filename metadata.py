import sys
import pikepdf
from PIL import Image
from PIL.ExifTags import TAGS

def meta_pdf(pdf_file):
    pdf = pikepdf.Pdf.open(pdf_file)
    return dict(pdf.docinfo)

def image_meta(image):
    img = Image.open(image)

    info = {
        "Image name": img.filename,
        "Image size": img.size,
        "Image height": img.height,
        "Image width": img.width,
        "Image format": img.format,
        "Image mode": img.mode
    }
    exif = img.getexif()
    for id_tag in exif:
        tag = TAGS.get(id_tag, id_tag)
        data = exif.get(id_tag)

        if isinstance(data, bytes):
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
