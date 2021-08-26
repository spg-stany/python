import random
from tkinter import Label

class Game:

    def __init__(self, canvas, column, row):
        self.canvas = canvas
        self.column = column
        self.row = row
        self.color = None
        self.id = id
        self.coordinaty_figury_move = []

    def text_drow(self):
        self.canvas.create_text(750, 100, text="SCORE", font=("Arial", 30), fill="red")
        self.lab = Label(self.canvas, text=" ", font=("Arial", 30), bg="light blue", fg="red")
        self.lab.place(x=730, y=150)

    def max_y_figury(self, id): # самые нижние ячейки в фигуре
        s = []
        for self.one_box in id:
            s.append(self.return_cord(self.id))
        spisok_max_y_figuryy = []
        s.sort()
        for k in s:
            spisok_max_y_figuryy.append(k)
            for i in spisok_max_y_figuryy:
                if k[0] == i[0] and k[1] > i[1]:
                    i[1] = k[1]
        r = set(map(tuple, spisok_max_y_figuryy))
        spisok_max_y_figury = list(r)
        spisok_max_y_figury.sort(reverse=True)
        return spisok_max_y_figury

    def max_x_figury(self, id): #координаты крайних правых боксов, # получам координаты боксов в фигуре и выбираем те что правее по иксу
        s = []
        for self.one_box in id:
            s.append(self.return_cord(self.id))
        spisok_max_x_figuryy = []
        s.sort()
        for k in s:
            spisok_max_x_figuryy.append(k)
            for i in spisok_max_x_figuryy:
                if k[1] == i[1] and k[0] > i[0]:
                    i[0] = k[0]
        r = set(map(tuple, spisok_max_x_figuryy))
        spisok_max_x_figury = list(r)
        spisok_max_x_figury.sort(reverse=True)
        return spisok_max_x_figury

    def min_x_figury(self, id):  # координаты (колонка, столбец) крайних левых ячеек в фигуре
        s = []
        for self.one_box in id:
            s.append(self.return_cord(self.id))
        spisok_min_x_figuryy = []
        s.sort(reverse=True)
        for k in s:
            spisok_min_x_figuryy.append(k)
            for i in spisok_min_x_figuryy:
                if k[1] == i[1] and k[0] < i[0]:
                    i[0] = k[0]
        r = set(map(tuple, spisok_min_x_figuryy))
        spisok_min_x_figury = list(r)
        spisok_min_x_figury.sort()
        return spisok_min_x_figury

    @staticmethod
    def cords(column, row): #переводит колонки и ряды в координаты ипользуется в отрисовке грида
        cord1 = (column - 1) * 50, (row - 1) * 50
        cord2 = column * 50, row * 50
        cords = [cord1, cord2]
        return cords

    def box(self, column, row): #отрисовка квадратика в значениях колонка, ряд
        self.one_box = self.canvas.create_rectangle(self.cords(column, row), fill=self.color, outline="white")
        return self.one_box


    def return_cord(self, id): # переводит координаты квадратика в значения (колонки и ряды)
        f = self.canvas.coords(self.one_box)
        colum = f[0] / 50 + 1
        row = f[3] / 50
        self.coordinates = [int(colum), int(row)]
        return self.coordinates


    @staticmethod
    def matrica(slovar_L):    # список заполненных ячеек построчно [0 - 18]
        a = []
        matrica_zapolnennyh_yacheek = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        for key, value in slovar_L.items():
            if value == 1:
                a.append(key)
        for i in range(len(matrica_zapolnennyh_yacheek)):
            for j in a:
                if j[1] == i:
                    matrica_zapolnennyh_yacheek[i].append([*j])
        return matrica_zapolnennyh_yacheek


    def chek_row(self): #проверка, есть ли заполненные ряды и вывод в отдельный список
        self.w = []
        for i in self.matrica(slovar_L):
            if len(i) == 13:
                self.w.append(i)
        if len(self.w) >= 1:
            return self.w
        else:
            return False

    def bottom(self):
        global time
        for i in self.coordinaty_figury_move:
            for self.one_box in gridy:
                if self.return_cord(gridy) == i:
                    print(self.one_box)
                    self.canvas.itemconfigure(self.one_box, fill="light pink")
        return True

    def delite_row(self):
        for i in self.w:
            print("i", i)
            for self.one_box in reversed(gridy[14:(i[1][1]*13)]):
                self.canvas.itemconfigure(self.one_box, fill=self.canvas.itemcget((self.one_box - 13), "fill"))
                if self.canvas.itemcget(self.one_box, "fill") == "light blue":
                    slovar_L[tuple(self.return_cord(gridy))] = 0
                else:
                    slovar_L[tuple(self.return_cord(gridy))] = 1
        return True

    def L_matrica(self, gridy): # делаем словарь из координат грида со значением 0
        global slovar_L
        self.coordinaty_grida = []
        for self.one_box in gridy:
            self.coordinaty_grida.append(self.return_cord(self.one_box))
        print("self.coordinaty_grida", self.coordinaty_grida)
        slovar_L = dict((tuple(i), 0) for i in self.coordinaty_grida)
        return slovar_L


    @staticmethod # записываем координаты фигуры в словарь со значением 1, если  макс координаты фигуры = минимальной координате заполненного грида(включая последнюю строку грида)
    def zapys_coordynat(slovar_L, coordinaty_figury_move):
        for i in coordinaty_figury_move:
            for key, value in slovar_L.items():
                if key == tuple(i):
                    slovar_L[key] = 1

    @staticmethod # находим координаты заполненного грида со значением 1
    def coordinaty_zapolnenyh_yacheek(slovar_L):
        coordinaty_zapolnenogo_grida = []
        for key, value in slovar_L.items():
            if value == 1:
                coordinaty_zapolnenogo_grida.append(key)
        return coordinaty_zapolnenogo_grida


class Grid(Game):
    global score
    global time
    global speed

    def __init__(self, canvas, column, row, color):
        super().__init__(canvas, column, row)
        self.color = color


    def grid_drow(self): # рисуем грид из боксов
        global gridy
        self.coordinaty_grida = []
        gridy = [self.box(self.row, self.column) for self.column in range(1, 19) for self.row in range(1, 14)]
        for self.one_box in gridy:
            self.coordinaty_grida.append(self.return_cord(self.one_box))
        print(self.L_matrica(gridy))
        return gridy


    def compare_last_drow(self): # занята ли хотя бы одна ячейка в первом ряду
        for key, value in slovar_L.items():
            if key[1] == 1 and value == 1:
                return False
        else:
            return True

    def drow_figury(self, slovar_L, speed): #запускаем отрисовку и движение фигуры рандомно
        d = [Line, Square, L, T]
        colors = ["IndianRed", "steelBlue", "fireBrick", "khaki", "olive", "tomato", "BlueViolet", "deep pink"]
        color = random.choice(colors)
        clas = random.choice(d)
        self.t = clas(self.canvas, 7, -1, color)
        if self.compare_last_drow() == True:
            self.t.drow_figura()
            self.t.move_figura(speed)
        else:
            self.canvas.create_text(750, 300, text="GAME OVER", font=("Arial", 20), fill="deep pink")


    def game_again(self, slovar_L, score, time, speed): # запускаем цикл новой фигуры по времени
        self.drow_figury(slovar_L, speed)
        self.canvas.update()
        if self.chek_row() != False:
            score += (13 * len(self.w))
            speed -= 10
            time -= 200
            print("score", score)
            print("speed", speed)
            print("time", time)
        self.delite_row()
        self.lab["text"] = "%s" % score
        self.canvas.after(time, self.game_again, slovar_L, score, time, speed)


class Figura(Game):
    global speed
    def __init__(self, canvas, column, row, color):
        super().__init__(canvas, column, row)
        self.color = color

    def left(self, event): #движение влево
        if self.compare_y(slovar_L, 1) == True and self.compare_y_left(slovar_L, 1) == True and self.compare_x_left(slovar_L, 1) == True:
            for self.one_box in self.id:
                self.canvas.move(self.one_box, -50, 0)
        else:
            pass
        print(event)

    def right(self, event): #движение вправо
        if self.compare_y(slovar_L, 1) == True and self.compare_y_right(slovar_L, 1) == True and self.compare_x_right(slovar_L, 1) == True:
            for self.one_box in self.id:
                self.canvas.move(self.one_box, 50, 0)
        else:
            pass
        print(event)

    def drow_figura(self): #метод отрисовки фигуры
            self.id = []
            return self.id

    def rotate(self, event): #поворот против часовой стрелки
        pass

    def coord_figura(self):
        self.coordinaty_figury = []
        for self.one_box in self.id:
            self.coordinaty_figury.append(self.return_cord(self.one_box))
        return self.coordinaty_figury


    def compare_y(self, slovar_L, h):#сранение максимальной координаты фигуры по ряду с минимальной координатой заполненного грида
        t = self.max_y_figury(self.id)
        d = 0
        for d in range(len(t)):
            if t[d][1] >= 19 - h:
                return False
            else:
                for key, value in slovar_L.items():
                    if t[d][0] == key[0] and t[d][1] + h == key[1]:
                        if value == 0:
                            break
                        else:
                            return False
                d += 1
        else:
            return True

    def compare_y_right(self, slovar_L, hr):#сравнение для ограничения движения вправо если справа внизу есть фигура
        t = self.max_y_figury(self.id)
        for i in t:
            for key, value in slovar_L.items():
                if i[0] + 1 == key[0] and i[1] + hr == key[1]:
                    if value == 1:
                        return False
        else:
            return True

    def compare_y_left(self, slovar_L, hl):#сравнение для ограничения движения влево если слева внизу есть фигура
        t = self.max_y_figury(self.id)
        for i in t:
            for key, value in slovar_L.items():
                if i[0] - 1 == key[0] and i[1] + hl == key[1]:
                    if value == 1:
                        return False
        else:
            return True

    def compare_x_right(self, slovar_L, wr):#сранение максимальной координаты фигуры по колонке с минимальной координатой колонки заполненного грида
        t = self.max_x_figury(self.id)
        d = 0
        for d in range(len(t)):
            if t[d][0] >= 14 - wr:
                return False
            else:
                for key, value in slovar_L.items():
                    if t[d][1] == key[1] and t[d][0] + wr == key[0]:
                        if value == 0:
                            break
                        else:
                            return False
                d += 1
        else:
            return True

    def compare_x_left(self, slovar_L, wl): #сранение максимальной координаты фигуры по колонке с минимальной координатой колонки заполненного грида
        t = self.min_x_figury(self.id)
        d = 0
        for d in range(len(t)):
            if t[d][0] <= 0 + wl:
                return False
            else:
                for key, value in slovar_L.items():
                    if t[d][1] == key[1] and t[d][0] - wl == key[0]:
                        if value == 0:
                            break
                        else:
                            return False
                d += 1
        else:
            return True

    def move_figura(self, speed):
        global slovar_L

        self.coordinaty_figury_move = []
        for self.one_box in self.id:
            self.canvas.bind('<Left>', lambda event: self.left(event))
            self.canvas.bind('<Right>', lambda event: self.right(event))
            self.canvas.bind('<Up>', lambda event: self.rotate(event))
            self.canvas.move(self.one_box, 0, 50)
            self.coordinaty_figury_move.append(self.return_cord(self.one_box))
        if self.compare_y(slovar_L, 1) == True:
            self.canvas.after(speed, self.move_figura, speed)
        else:
            print("coordinaty_figury_move", self.coordinaty_figury_move)
            self.zapys_coordynat(slovar_L, self.coordinaty_figury_move)
            self.matrica(slovar_L)
            print("self.matrica(slovar_L)", self.matrica(slovar_L))
            print("gridy", gridy)
            self.bottom()
            print("slovar_L", slovar_L)
            for self.one_box in self.id:
                self.canvas.delete(self.one_box)


class Line(Figura):

    def __init__(self, canvas, column, row, color):
        super().__init__(canvas, column, row, color)

    def drow_figura(self):
        self.id = [self.box(self.column, self.row), self.box(self.column + 1, self.row), self.box(self.column + 2, self.row),
                   self.box(self.column + 3, self.row)]
        print(self.id)
        return self.id



    def rotate(self, event):
        self.coordinaty_figury = self.coord_figura()
        print(event)
        print("self.coordinaty_figury, self.id", self.coordinaty_figury, self.id)
        if self.coordinaty_figury[0][1] == self.coordinaty_figury[2][1] == self.coordinaty_figury[3][1]:
            if self.compare_y(slovar_L, 2) == True:
                self.canvas.move(self.id[0], 50,  50)
                self.canvas.move(self.id[2], -50, -50)
                self.canvas.move(self.id[3], -100, -100)
            else:
                pass
        elif self.coordinaty_figury[0][0] == self.coordinaty_figury[1][0] == self.coordinaty_figury[3][0]:
            if self.compare_x_right(slovar_L, 2) == True and self.compare_x_left(slovar_L, 1) == True \
                    and self.compare_y_left(slovar_L, 1) == True and self.compare_y_right(slovar_L, 2) == True:
                self.canvas.move(self.id[0], -50, -50)
                self.canvas.move(self.id[2], 50, 50)
                self.canvas.move(self.id[3], 100, 100)
            else:
                pass


class Square(Figura):

    def __init__(self, canvas, column, row, color):
        super().__init__(canvas, column, row, color)

    def drow_figura(self):
        self.id = [self.box(self.column, self.row), self.box(self.column + 1, self.row),
                   self.box(self.column, self.row + 1), self.box(self.column + 1, self.row + 1)]
        print(self.id)
        return self.id


    def rotate(self, event):
        pass

class L(Figura):

    def __init__(self, canvas, column, row, color):
        super().__init__(canvas, column, row, color)

    def drow_figura(self):
        self.id = [self.box(self.column, self.row), self.box(self.column, self.row + 1),
                   self.box(self.column, self.row + 2), self.box(self.column + 1, self.row + 2)]
        print(self.id)
        return self.id

    def rotate(self, event):
        self.coordinaty_figury = self.coord_figura()
        print(event)
        print("self.coordinaty_figury, self.id", self.coordinaty_figury, self.id)
        if self.coordinaty_figury[0][0] == self.coordinaty_figury[1][0] == self.coordinaty_figury[2][0]:
            if self.coordinaty_figury[0][1] < self.coordinaty_figury[2][1]:
                if self.compare_x_left(slovar_L, 1) == True and self.compare_y_left(slovar_L, 1) == True:
                    self.canvas.move(self.id[0], -50, 50)
                    self.canvas.move(self.id[2], 50, -50)
                    self.canvas.move(self.id[3], 0, -100)
                else:
                    pass
            elif  self.coordinaty_figury[0][1] > self.coordinaty_figury[2][1]:
                if self.compare_x_right(slovar_L, 1) == True and self.compare_y_right(slovar_L, 1) == True:
                    self.canvas.move(self.id[0], 50, -50)
                    self.canvas.move(self.id[2], -50, 50)
                    self.canvas.move(self.id[3], 0, 100)
                else:
                    pass
        if self.coordinaty_figury[0][1] == self.coordinaty_figury[1][1] == self.coordinaty_figury[2][1]:
            if self.coordinaty_figury[0][0] < self.coordinaty_figury[2][0]:
                if self.compare_y(slovar_L, 2) == True:  # сранение максимальной координаты фигуры по ряду с минимальной координатой заполненного грида
                    self.canvas.move(self.id[0], 50, 50)
                    self.canvas.move(self.id[2], -50, -50)
                    self.canvas.move(self.id[3], -100, 0)
                else:
                    pass
            elif self.coordinaty_figury[0][0] > self.coordinaty_figury[2][0]:
                self.canvas.move(self.id[0], -50, -50)
                self.canvas.move(self.id[2], 50, 50)
                self.canvas.move(self.id[3], 100, 0)

class T(Figura):

    def __init__(self, canvas, column, row, color):
        super().__init__(canvas, column, row, color)

    def drow_figura(self):
        self.id = [self.box(self.column, self.row), self.box(self.column + 1, self.row),
                   self.box(self.column + 2, self.row), self.box(self.column + 1, self.row + 1)]
        print(self.id)
        return self.id

    def rotate(self, event):
        self.coordinaty_figury = self.coord_figura()
        print(event)
        print("self.coordinaty_figury, self.id", self.coordinaty_figury, self.id)
        if self.coordinaty_figury[0][1] == self.coordinaty_figury[1][1] == self.coordinaty_figury[2][1]:
            if self.compare_y(slovar_L, 2) == True:
                self.canvas.move(self.id[0], 50, -50)
            else:
                pass
        if self.coordinaty_figury[0][0] == self.coordinaty_figury[1][0] == self.coordinaty_figury[3][0]:
            if self.compare_x_left(slovar_L, 1) == True:
                self.canvas.move(self.id[3], -50, -50)
            else:
                pass
        if self.coordinaty_figury[3][1] == self.coordinaty_figury[1][1] == self.coordinaty_figury[2][1]:
            if self.compare_y(slovar_L, 2) == True:
                self.canvas.move(self.id[2], -50, 50)
            else:
                pass
        if self.coordinaty_figury[0][0] == self.coordinaty_figury[1][0] == self.coordinaty_figury[2][0]:
            if self.compare_x_right(slovar_L, 1) == True:
                self.canvas.move(self.id[0], -50, 50)
                self.canvas.move(self.id[2], 50, -50)
                self.canvas.move(self.id[3], 50, 50)
            else:
                pass

