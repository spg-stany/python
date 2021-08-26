from turtle import *

class arabskiecifry:


    def __init__(self, l):
        self.l = l


    def draw_1(self):

        up()
        rt(90), fd(self.l), lt(135), down(), fd((2 * self.l ** 2) ** (1 / 2)), rt(135), fd(self.l + self.l)
        up()

    def draw_2(self):

        up()
        down(), fd(self.l), rt(90), fd(self.l), rt(45), fd((2* self.l**2)**(1/2)), lt(135), fd(self.l)
        up()

    def draw_3(self):

        up()
        down(), fd(self.l), rt(90), fd(self.l), rt(90), fd(self.l), lt(180), up(), fd(self.l), rt(90), down(), fd(self.l), rt(90), fd(self.l)
        up()


    def draw_4(self):

        up()
        down(), rt(90), fd(self.l), lt(90), fd(self.l), lt(90), fd(self.l), lt(180), up(), fd(self.l), down(), fd(self.l)
        up()

    def draw_5(self):

        up()
        down(), fd(self.l), up(), bk(self.l), down(), rt(90), fd(self.l), lt(90), fd(self.l), rt(90), fd(self.l), rt(90), fd(self.l)
        up()

    def draw_6(self):

        up()
        down(), fd(self.l), up(), bk(self.l), down(), rt(90), fd(self.l), lt(90), fd(self.l), rt(90), fd(self.l), rt(90), fd(self.l), rt(90), fd(self.l)
        up()

    def draw_7(self):

        up()
        down(), fd(self.l),rt(90),fd(self.l+self.l)
        up()

    def draw_8(self):

        up()
        down(), fd(self.l), rt(90), fd(self.l+self.l), rt(90), fd(self.l), rt(90), fd(self.l+self.l), up(), bk(self.l), rt(90), down(), fd(self.l)
        up()

    def draw_9(self):

        up()
        down(), fd(self.l), rt(90), fd(self.l+self.l), rt(90), fd(self.l), up(), rt(90), fd(self.l+self.l), down(), bk(self.l), rt(90), fd(self.l)
        up()

    def draw_10(self):

        up()
        down(), fd(self.l), rt(90), fd(self.l + self.l), rt(90), fd(self.l), rt(90), fd(self.l + self.l), rt(180)
        up(), fd(self.l), rt(90), fd(self.l+self.l), rt(135), down()
        fd((2 * self.l ** 2) ** (1 / 2)), rt(135), fd(self.l + self.l)
        up()


    def draw_11(self):

        up()
        up(), rt(90), fd(self.l), lt(135), down()
        fd((2 * self.l ** 2) ** (1 / 2)), rt(135), fd(self.l + self.l)
        up(), rt(90), fd(self.l + self.l), rt(90), down()
        fd(self.l + self.l), lt(135), fd((2 * self.l ** 2) ** (1 / 2))
        up()


    def draw_12(self):
        up()
        down(), fd(self.l), rt(90), fd(self.l), rt(45), fd((2 * self.l ** 2) ** (1 / 2)), lt(135), fd(self.l)
        up(), bk(self.l + self.l), lt(90), down()
        fd(self.l + self.l), lt(135), fd((2 * self.l ** 2) ** (1 / 2))


    def draw(self, i, color):
        pencolor('lime')

        if i == 1:
            arabskiecifry.draw_1(self)
        elif i == 2:
            arabskiecifry.draw_2(self)
        elif i == 3:
            arabskiecifry.draw_3(self)
        elif i == 4:
            arabskiecifry.draw_4(self)
        elif i == 5:
            arabskiecifry.draw_5(self)
        elif i == 6:
            arabskiecifry.draw_6(self)
        elif i == 7:
            arabskiecifry.draw_7(self)
        elif i == 8:
            arabskiecifry.draw_8(self)
        elif i == 9:
            arabskiecifry.draw_9(self)
        elif i == 10:
            arabskiecifry.draw_10(self)
        elif i == 11:
            arabskiecifry.draw_11(self)
        elif i == 12:
            arabskiecifry.draw_12(self)
