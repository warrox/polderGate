p = add_photos.add_path_pictures()
x = 0
y = 0
for file in p[x]:
    print(str(file))
    if str(file).find(".mov"):
        p.remove(file)
    # add_photos.all_directory_files.remove(file)
# if y >= len(p[y]):
# x += 1
# compress_images.downsize_images(p)