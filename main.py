# Created by Warren Hamdi
#         06/09/23
#        PolderGate
import os

import add_photos
import compress_images


def start_program():
    subdirectory, root = add_photos.add_path_pictures()
    sorted_list = add_photos.sort_files(subdirectory, root)
    compress_images.downsize_images(sorted_list)


# Create a new folder if first launch or start directly the program
parent_dir = os.path.expanduser('~')
directory = "PolderGate"
path = os.path.join(parent_dir, directory)

if os.path.exists(path):
    start_program()

else:
    os.mkdir(path)
    print("Directory '% s' created" % directory)
    start_program()
