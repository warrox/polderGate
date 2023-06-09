# Created by Warren Hamdi
#         06/09/23
#        PolderGate
import os

import add_photos
import compress_images


def start_program():
    p = add_photos.add_path_pictures()
    compress_images.downsize_images(p)


parent_dir = os.path.expanduser('~')
directory = "PolderGate"
path = os.path.join(parent_dir, directory)

if os.path.exists(path):
    start_program()
else:
    os.mkdir(path)
    print("Directory '% s' created" % directory)
    start_program()
