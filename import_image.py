from PIL import Image, ImageOps


t = Image.open('/Users/warren/Downloads/GIBE.jpeg')  # My image is a 200x374 jpeg that is 102kb large
fixed_image = ImageOps.exif_transpose(t)
# downsize the image with an ANTIALIAS filter (gives the highest quality)
fixed_image.thumbnail((300,300),Image.LANCZOS)
fixed_image.save('/Users/warren/Downloads/image_scaled1.jpeg', quality=95)

#foo.save('/Users/warren/Downloads/image_scaled.jpeg', quality=95)  # The saved downsized image size is 24.8kb

#foo.save('/Users/warren/Downloads/image_scaled1.jpeg', optimize=True, quality=95)  # The saved downsized image size is 22.