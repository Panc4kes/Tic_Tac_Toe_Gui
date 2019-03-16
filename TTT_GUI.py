import os
import platform
from tkinter import *
from tkinter.messagebox import showinfo

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


turn = "X"

__license__ = open("LICENSE", "r").read()

position = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


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
        board()
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


def update():
    global B1, B2, B3, B4, B5, B6, B7, B8, B9, position, root
    B1.config(text=position[0])
    B2.config(text=position[1])
    B3.config(text=position[2])
    B4.config(text=position[3])
    B5.config(text=position[4])
    B6.config(text=position[5])
    B7.config(text=position[6])
    B8.config(text=position[7])
    B9.config(text=position[8])

    combo = [position[0] + position[1] + position[2],
             position[3] + position[4] + position[5],
             position[6] + position[7] + position[8],
             position[0] + position[3] + position[6],
             position[1] + position[4] + position[7],
             position[2] + position[5] + position[8],
             position[0] + position[4] + position[8],
             position[2] + position[4] + position[6]]
    combo = [position[0]+position[1]+position[2],
             position[3]+position[4]+position[5],
             position[6]+position[7]+position[8],
             position[0]+position[3]+position[6],
             position[1]+position[4]+position[7],
             position[2]+position[5]+position[8],
             position[0]+position[4]+position[8],
             position[2]+position[4]+position[6]]

    if "XXX" in combo:
        showinfo("Result", "Player 1 Won!")
        root.destroy()
        ask()
    elif "OOO" in combo:
        showinfo("Result!", "Player 2 Won!")
        root.destroy()
        ask()
    elif " " not in position:
        showinfo("Result", "Tie!")
        root.destroy()
        ask()


def resolve(pos):
    global position
    global turn

    if position[pos] == " ":

        if turn == "X":
            position[pos] = "X"
            turn = "O"
        elif turn == "O":
            position[pos] = "O"
            turn = "X"
    else:
        showinfo("ERROR!", "There's already a marker there!")
    update()


def board():
    global B1, B2, B3, B4, B5, B6, B7, B8, B9, root
    root = Tk()

    root.iconbitmap("icon.ico")
    root.title("Tik Tok Toe")

    B1 = Button(root, text=position[0], width=6, height=3, font=("Helvetica", 25, "bold"), command=lambda: resolve(0), )
    B1.grid(row=1, column=0)
    B2 = Button(root, text=position[1], width=6, height=3, font=("Helvetica", 25, "bold"), command=lambda: resolve(1))
    B2.grid(row=1, column=1)
    B3 = Button(root, text=position[2], width=6, height=3, font=("Helvetica", 25, "bold"), command=lambda: resolve(2))
    B3.grid(row=1, column=2)
    B4 = Button(root, text=position[3], width=6, height=3, font=("Helvetica", 25, "bold"), command=lambda: resolve(3))
    B4.grid(row=2, column=0)
    B5 = Button(root, text=position[4], width=6, height=3, font=("Helvetica", 25, "bold"), command=lambda: resolve(4))
    B5.grid(row=2, column=1)
    B6 = Button(root, text=position[5], width=6, height=3, font=("Helvetica", 25, "bold"), command=lambda: resolve(5))
    B6.grid(row=2, column=2)
    B7 = Button(root, text=position[6], width=6, height=3, font=("Helvetica", 25, "bold"), command=lambda: resolve(6))
    B7.grid(row=3, column=0)
    B8 = Button(root, text=position[7], width=6, height=3, font=("Helvetica", 25, "bold"), command=lambda: resolve(7))
    B8.grid(row=3, column=1)
    B9 = Button(root, text=position[8], width=6, height=3, font=("Helvetica", 25, "bold"), command=lambda: resolve(8))
    root.mainloop()


def ask():
    global position
    while True:
        print("Play again? (Y/N)")
        inp = input("> ")
        if inp.lower() == "n":
            raise SystemExit

        elif inp.lower() == "y":
            clear()
            position = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            board()

        else:
            print("Undefined keyword")


if __name__ == "__main__":
    menu()
