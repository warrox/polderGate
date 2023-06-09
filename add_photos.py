import compress_images


picture_choosed = []

def add_path_pictures():
    while True:
        user_choice = input("Choose picture(s) to downsize, add the repository adress")
        picture_choosed.append(user_choice)
        a = input("Would you like to add more pictures ? (y) or (n)")

        if a == "n":
            return picture_choosed

        if a == "y":
            return add_path_pictures()
        else:
            break


