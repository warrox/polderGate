from PIL import Image, ImageOps

def downsize_images(pic):
    l = 0
    for picture in range(0,len(pic)):
        t = Image.open((pic[picture]))  # My image is a 200x374 jpeg that is 102kb large
        fixed_image = ImageOps.exif_transpose(t)
        # downsize the image with an ANTIALIAS filter (gives the highest quality)
        fixed_image.thumbnail((300,300),Image.LANCZOS)
        fixed_image.save(f'/Users/warren/Downloads/image_scaled{str(l)}.jpeg', quality=95)
        l += 1
        #picture += 1
        if picture == len(pic):
            break

    #foo.save('/Users/warren/Downloads/image_scaled.jpeg', quality=95)  # The saved downsized image size is 24.8kb

    #foo.save('/Users/warren/Downloads/image_scaled1.jpeg', optimize=True, quality=95)  # The saved downsized image size is 22.

