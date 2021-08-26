import time
from turtle import*
from Strelki import strelki
from AnalogovyeChasy import ciferblat
from time import localtime
from time import sleep

ciferblat.x = 0
ciferblat.y = 0
ciferblat.l = 13


def strelki_clock(ciferblat, color, outline=False):
    speed(0)
    tracer(100)
    if outline:
        pencolor(color)
    else:
        pencolor(color)

    second_strelka = mytime.tm_sec * 6
    minute_strelka = mytime.tm_min * 6 + second_strelka / 60
    hour_strelka = mytime.tm_hour % 12 * 30 + minute_strelka / 12

    strelki.drawstrelki(ciferblat, 12, second_strelka, 1, color)
    strelki.drawstrelki(ciferblat, 11, minute_strelka, 5, color)
    strelki.drawstrelki(ciferblat, 9, hour_strelka, 10, color)

def strelki_clock1(ciferblat, color, outline = False):
    if outline:
        pencolor(color)
    else:
        pencolor()



    second_strelka = mytime1.tm_sec * 6
    minute_strelka = mytime1.tm_min * 6 + second_strelka / 60
    hour_strelka = mytime1.tm_hour % 12 * 30 + minute_strelka / 12


    strelki.drawstrelki(ciferblat, 12, second_strelka, 1, "magenta")
    strelki.drawstrelki(ciferblat, 11, minute_strelka, 5, "lime")
    strelki.drawstrelki(ciferblat, 9, hour_strelka, 8, "lime")



hideturtle()
speed(0)
bgcolor('midnight blue')


ciferblat.cicle(ciferblat)

mytime = localtime()
print(mytime)
print(mytime.tm_year)
while True:
    mytime1 = localtime()
    if mytime1 is not mytime:

        strelki_clock(ciferblat, bgcolor())
        strelki_clock1(ciferblat, color())

   # time.sleep(5)
    mytime = mytime1




