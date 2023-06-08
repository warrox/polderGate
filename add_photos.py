import import_image

picture_choosed = []


def add_path_pictures():
    while True:
        user_choice = input("Choose picture(s) to downsize, add the repository adress")
        picture_choosed.append(user_choice)
        a = input("Would you like to add more pictures ? (y) or (n)")

        if a == "n":
            return picture_choosed

        if a == "y":
            add_path_pictures()
        else:
            break

p = add_path_pictures()
import_image.downsize_images(p)
#quand choix y joue la boucle  add_path_pictures() 2 fois meme si on dit non par la suite.
