from turtle import *

class strelki:

    def __init__(self, x, y):
        self.x = x
        self.y = y

       # self.color = color

    def drawstrelki(self, l, r1, width, color):
        pensize(width)
        pencolor(color)
        penup()
        home()
        up()
        goto(self.x, self.y)
        setheading(90)
        down()
        rt(r1)
        forward(l*29)


if __name__ == "__main__":
    reset()
    speed()
    bgcolor('green')
    d = strelki(0, 0, "black", 30)
    d.drawstrelki(strelki, 10, 5, 3, 'blue')


    mainloop()