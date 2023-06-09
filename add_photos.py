import compress_images
import os

all_directory_files = []


def add_path_pictures():
    while True:
        user_choice = input("Choose picture(s) to downsize, add the repository adress")
        f = get_immediate_subdirectories(user_choice)
        re_add = input("Would you like to add more pictures ? (y) or (n)")
        for i in f:
            file = os.listdir(user_choice + "/" + i) #sort by .JPEG,HEIC,PNG & remove video format
            all_directory_files.append(file)
        if re_add == "n":
            return all_directory_files
        if re_add == "y":
            return add_path_pictures()
        else:
            break



def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]