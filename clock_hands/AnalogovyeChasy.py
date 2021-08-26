from turtle import *

from ArabskieCifry import arabskiecifry




class ciferblat(arabskiecifry):

    def __init__(self, x, y, l):
        self.x = x
        self.y = y
        arabskiecifry.__init__(self)


    def cicle(self):
        up()
        setpos(self.x, self.y)
        for i in range(13):
            setheading(90)
            rt((i) * 30)
            forward(self.l * 30)
            dot(self.l, 'lime')
            forward(3 * self.l)
            setheading(0)
            arabskiecifry.draw(self, i, color)
            up()
            goto(self.x, self.y)


        for i in range(60):
            setheading(90)
            rt((i) * 6)
            forward((self.l * 30))
            down()
            dot(self.l / 2, 'lime')
            up()
            goto(self.x, self.y)





if __name__ == "__main__":
    reset()
    speed(0)
    c = ciferblat(0, 0, 5)
    c.cicle()



    mainloop()