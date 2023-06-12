import compress_images
import os

all_directory_files = []
adf = [] #retirer puis commit


def add_path_pictures():
    while True:
        root = input("Choose picture(s) to downsize, add the repository adress")
        subdirectories = get_immediate_subdirectories(root)
        re_add = input("Would you like to add more pictures ? (y) or (n)")

        if re_add == "n":
            return subdirectories, root
        if re_add == "y":
            return add_path_pictures()
        else:
            break


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def sort_files(sub_list, uc):

    for i in sub_list:
        file = os.listdir(uc + "/" + i)  # orginal/9

        for e in file:  # element in file
            if e.endswith(".png") or e.endswith(".heic") or e.endswith(".jpg"):
                all_directory_files.append(str(uc) + "/" + i + "/" + str(e))
            elif e.endswith(".mov"):
                continue
    return all_directory_files
