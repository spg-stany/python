import os
from tkinter import *
from tetrisBox.grid import Grid

from tetrisBox.grid import Game

root = Tk()

root.title("TETRIS")
canvas = Canvas(root,
                width=851,
                height=901, highlightthickness=0, bg="light blue")
canvas.focus_set()
canvas.pack()
speed = 300
w = Game(canvas, 16, 20)

def refresh():
    root.destroy()
    os.startfile("main.pyw")


a = Grid(canvas, 1, 1, "light blue")
a.text_drow()
btn = Button(canvas, text="START AGAIN", bg="light blue", fg="red", padx='10', pady='10', font="40",
             command=refresh)
btn.place(x=680, y=20)
gridy = a.grid_drow()
slovar_L = {}
score = 0
time = 5500

a.game_again(slovar_L, score, time, speed)


canvas.focus_set()
root.mainloop()


