from PIL import Image, ImageOps
from pillow_heif import register_heif_opener
import os.path


def downsize_images(file_path):
    saved_image_int = 0
    # loop for to convert all the images path stock in the list
    for picture in range(0, len(file_path)):
        register_heif_opener()  # .Heic reader function
        t = Image.open((file_path[picture]))  # My image is a 200x374 jpeg that is 102kb large
        fixed_image = ImageOps.exif_transpose(t)
        fixed_image.thumbnail((400, 600), Image.LANCZOS)  # downsize the image with an Lanczos filter
        fixed_image.save(f'{os.path.expanduser("~")}/PolderGate/image_scaled{str(saved_image_int)}.png', quality=150)
        saved_image_int += 1
        # picture += 1
        if picture == len(file_path):
            break
