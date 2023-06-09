import compress_images
import os

all_directory_files = []
adf = []


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
    e = 0
    for i in sub_list:
        file = os.listdir(uc + "/" + i)  # sort by .JPEG,HEIC,PNG & remove video format
        lenght_sub += 1

        check = file[e]
        if check.endswith(".png") or check.endswith(".heic") or check.endswith(".jpg"):
            all_directory_files.append(check)
        elif check.endswith(".mov"):
            continue
        if lenght_sub == len(sub_list):
            e += 1
    return all_directory_files
