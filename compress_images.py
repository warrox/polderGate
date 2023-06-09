from PIL import Image, ImageOps
from pillow_heif import register_heif_opener
import os.path

def downsize_images(file_path):
    l = 0
    for picture in range(0, len(file_path)):
        register_heif_opener()
        t = Image.open((file_path[picture]))  # My image is a 200x374 jpeg that is 102kb large
        fixed_image = ImageOps.exif_transpose(t)
        # downsize the image with an ANTIALIAS filter (gives the highest quality)
        fixed_image.thumbnail((300,300),Image.LANCZOS)
        fixed_image.save(f'/Users/warren/PolderGate/image_scaled{str(l)}.jpeg', quality=95)
        l += 1
        #picture += 1
        if picture == len(file_path):
            break

    #foo.save('/Users/warren/Downloads/image_scaled.jpeg', quality=95)  # The saved downsized image size is 24.8kb

    #foo.save('/Users/warren/Downloads/image_scaled1.jpeg', optimize=True, quality=95)  # The saved downsized image size is 22.

