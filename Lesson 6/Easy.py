# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math


class Triangles:
   # задаем атрибуты
   #координаты точек
    # a b c
    # p #полупериметр
    # h #высота
    # per #периметр
    # Sq #площадь
    # h #высота треугольника

    # задаем методы

    # Задаем координаты

    def coordinates_triangles(self):
        x1, y1 = list(map(int, input('Введите координаты точки A(x1,y1): ').split()))
        x2, y2 = list(map(int, input('Введите координаты точки B(x2,y2): ').split()))
        x3, y3 = list(map(int, input('Введите координаты точки C(x3,y3): ').split()))  # ввод координат точек
        print(x1, y1)
        print(x2, y2)
        print(x3, y3)
        return x1, x2, x3, y1, y2, y3

    # вычисление сторон через векторы
    def tr_length(self):
        a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        c = math.sqrt((x3 - xx) ** 2 + (y3 - y1) ** 2)
        print('Длины сторон треугольника', a, b, c)

    # Вычисление периметра
    def tr_perimeter(self):
        per = a + b + c
        print('Периметр треугольника', per)

    # Вычисление высоты
    def tr_height(self):
        p = (1 / 2) * per
        h = (2 / a) * (math.sqrt(p * (p - a) * (p - b) * (p - c)))
        print('Высота треугольника: ', p, h)
        # Вычисление площади

    def tr_square(self):
        Sq = (1 / 2) * a * h
        print('Площадь треугольника: ', Sq)


class Trapezes:

    def coordinates_trapeze():
        x1, y1 = list(map(int, input('Введите координаты точки A(x1,y1): ').split()))
        x2, y2 = list(map(int, input('Введите координаты точки B(x2,y2): ').split()))
        x3, y3 = list(map(int, input('Введите координаты точки C(x3,y3): ').split()))
        x4, y4 = list(map(int, input('Введите координаты точки D(x3,y3): ').split()))# ввод координат точек
        print(x1, y1)
        print(x2, y2)
        print(x3, y3)
        print(x4, y4)
        return x1, x2, x3, x4, y1, y2, y3, y4



trtr = Triangles()
trtr.coordinates_triangles()
trtr.tr_length()
trtr.tr_perimeter()
trtr.tr_square()

trtr2 = Trapezes()
trtr2.coordinates_trapeze()


