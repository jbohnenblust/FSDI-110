#imports
from display import print_menu, print_header, clear
from album import Album
from songs import Songs
import os
clear = lambda: os.system('cls')
clear()


#globals

catalog = [] # [] is NOT an array in python, but a list

album_count = 0


#functions


def register_album():
    global album_count
    print_header("Register an album: ")

    # id, title, genre, artist, release year, price, album_art, related_artist, record_label
    title = input("Please provide album title: ")
    genre = input("Please provide album genre: ")
    artist = input("Please provide album artist: ")
    release_year = int(input("Please provide album release year: "))
    price = float(input("Please provide album price: $"))
    album_art = input("Please provide album art URL: ")
    related_artist = input("Please provide related artist: ")
    record_label = input("Please provide record label: ")

    album = Album(album_count, title, genre, artist, release_year, price, album_art, related_artist, record_label)

    album_count += 1

    # push the album into the list (.push)

    catalog.append(album)

    print("** Album created!")


def print_albums():
    print_header("Your current albums:")

    for album in catalog: # for loop: for <variable> in <list>
        print(f"{album.id} | {album.title} | {album.release_year}")



def register_songs():
    print_header("Register your songs:")

    # let the user choose an album for the song

    print_albums()
    album_id = int(input("Please choose the album Id: "))

    # find the album with that Id
    found = False
    for album in catalog:
        if (album.id == album_id):
            found = True
            the_album = album
    if (not found):
        print("*Error: Incorrect Id type. Please try again.")
        return


    # create the song
    title = input("Please enter track name:")
    featured_artist = input("Please enter featured artist:")
    length_of_track = input("Please enter length of track:")
    written_by = input("Please enter artist's name:")

    songs = Songs(1, title, featured_artist, length_of_track, written_by)

    # push the song to the album list
    the_album.add_song(songs)

    print("** Song registered!")

#instructions

opc = ''
while(opc != 'q' and opc != 'x'):
    clear()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == '1'):
        register_album()

    elif (opc == '2'):
        register_songs()

    elif (opc == '3'): # else if / python does NOT support switch cases
        print_albums()

    input("Press enter to continue...")
