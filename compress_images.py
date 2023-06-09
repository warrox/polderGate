from PIL import Image, ImageOps
from pillow_heif import register_heif_opener
import os.path

def downsize_images(file_path):
    l = 0
    #loop for to convert all the images path stock in the list
    for picture in range(0, len(file_path)):
        register_heif_opener()  # .Heic reader function
        t = Image.open((file_path[picture]))  # My image is a 200x374 jpeg that is 102kb large
        fixed_image = ImageOps.exif_transpose(t)
        fixed_image.thumbnail((300,300),Image.LANCZOS)  # downsize the image with an Lanczos filter
        fixed_image.save(f'{os.path.expanduser("~")}/PolderGate/image_scaled{str(l)}.jpeg', quality=95)
        l += 1
        #picture += 1
        if picture == len(file_path):
            break

    #foo.save('/Users/warren/Downloads/image_scaled.jpeg', quality=95)  # The saved downsized image size is 24.8kb

    #foo.save('/Users/warren/Downloads/image_scaled1.jpeg', optimize=True, quality=95)  # The saved downsized image size is 22.

