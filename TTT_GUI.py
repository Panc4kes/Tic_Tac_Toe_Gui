import os
import platform
from tkinter import *

global pos


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


__license__ = open("LICENSE", "r").read()

pos = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def menu():
    clear()
    print("=" * 30)
    print("= " + "Welcome to Tic Tac Toe!".center(26) + " =")
    print("=" * 30 + "\n")
    print("select an option below")
    print("1 = Player vs Player")
    print("2 = License")
    print("3 = Exit")
    inp = input("> ")

    if inp == "1":
        clear()
        p1()
    elif inp == "2":
        clear()
        print(__license__)
        print("\nPress 'enter' to return to menu")
        input()
        menu()
    elif inp == "3":
        sys.exit()
    else:
        print("Invalid keyword, press 'enter' to return to menu\n")
        input()
        menu()


def board():
    root = Tk()
    B1 = Button(root, text=pos[0], width=8, height=4)
    B1.grid(row=1, column=0)
    B2 = Button(root, text=pos[1], width=8, height=4)
    B2.grid(row=1, column=1)
    B3 = Button(root, text=pos[2], width=8, height=4)
    B3.grid(row=1, column=2)
    B4 = Button(root, text=pos[3], width=8, height=4)
    B4.grid(row=2, column=0)
    B5 = Button(root, text=pos[4], width=8, height=4)
    B5.grid(row=2, column=1)
    B6 = Button(root, text=pos[5], width=8, height=4)
    B6.grid(row=2, column=2)
    B7 = Button(root, text=pos[6], width=8, height=4)
    B7.grid(row=3, column=0)
    B8 = Button(root, text=pos[7], width=8, height=4)
    B8.grid(row=3, column=1)
    B9 = Button(root, text=pos[8], width=8, height=4)
    B9.grid(row=3, column=2)
    root.mainloop()


def ask():
    while True:
        print("\nplay again? (Y/N)")
        inp = input("> ")
        if inp.lower() == "n":
            raise SystemExit

        elif inp.lower() == "y":

            clear()
            p1()
        else:
            print("Undefined keyword")


if __name__ == "__main__":
    board()
