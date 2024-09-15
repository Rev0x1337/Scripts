from PIL import Image
from PIL.ExifTags import TAGS

def image_meta_data(image_file):
    image = Image.open(image_file)
    info = {
        "File name": image.filename,
        "File size": image.size,
        "File height": image.height,
        "File width": image.width,
        "File format": image.format,
        "File mode": image.mode
            }

    exif = image.getexif()

    for tag_id in exif:
        tag = TAGS.get(tag_id, tag_id)
        data = exif.get(tag_id)

        if dec(data, bytes):
            data = data.decode()

        info[tag] = data
    return info
