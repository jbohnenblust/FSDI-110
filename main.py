#imports
from display import print_menu, print_header, clear
from album import Album
import os
clear = lambda: os.system('cls')
clear()


#globals

    #declare a catalog variable (list)

#functions


def register_album():
    print_header("Register an album: ")

    # title, genre, artist, release year, price, album_art, related_artist, record_label
    title = input("Please provide album title: ")
    genre = input("Please provide album genre: ")
    artist = input("Please provide album artist: ")
    release_year = int(input("Please provide album release year: "))
    price = float(input("Please provide album price: $"))
    album_art = input("Please provide album art URL: ")
    related_artist = input("Please provide related artist: ")
    record_label = input("Please provide record label: ")

    album = Album(title, genre, artist, release_year, price, album_art, related_artist, record_label)

    print(album)

    # push the album into the list (.push)



    input("Press enter to continue...")


#instructions

opc = ''
while(opc != 'q' and opc != 'x'):
    clear()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == '1'):
        register_album()