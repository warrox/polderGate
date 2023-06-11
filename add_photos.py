import compress_images
import os

all_directory_files = []
adf = [] #retirer puis commit


def add_path_pictures():
    while True:
        user_choice = input("Choose picture(s) to downsize, add the repository adress")
        subdirectories = get_immediate_subdirectories(user_choice)
        re_add = input("Would you like to add more pictures ? (y) or (n)")

        if re_add == "n":
            return subdirectories, user_choice
        if re_add == "y":
            return add_path_pictures()
        else:
            break


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def sort_files(sub_list, uc):
    lenght_sub = 0
    max_occurence = 0
    e = 0

    for i in sub_list:
        file = os.listdir(uc + "/" + i)  # orginal/9
        for x in file:
            if x.endswith(".png") or x.endswith(".heic") or x.endswith(".jpg"):
                all_directory_files.append(x)
            elif x.endswith(".mov"):
                continue
    return all_directory_files
