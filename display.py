import os

def print_menu():
    print("*" * 20)
    print("**Audio Manager Over 9000**")
    print("*" * 20)

    print("[1] Register a new album")
    print("[2] Register a new song")
    print("[3] Display album(s)")

    print("[q] Quit")

def clear():
    if(os.name == 'nt'):
        return os.system("cls")
    else:
        return os.system("clear")

def print_header(text):
    clear()
    print("-" * 20)
    print(text)
    print("-" * 20)