# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math


class Triangles:
   # задаем атрибуты
   x1, x2, x3, y1, y2, y3 = 0, 0, 0, 0, 0, 0
   a, b, c, p, h, per = 0, 0, 0, 0, 0, 0

   # координаты точек
   def __init__(self):
       self.x1, self.y1 = list(map(int, input('Введите координаты точки A(x1,y1): ').split()))
       self.x2, self.y2 = list(map(int, input('Введите координаты точки B(x2,y2): ').split()))
       self.x3, self.y3 = list(map(int, input('Введите координаты точки C(x3,y3): ').split()))

    # вычисление сторон через векторы
   def tr_length(self):
       self.a = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
       self.b = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
       self.c = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
       print('\nДлины сторон треугольника: ', '\n  a = ', self.a, '\n  b = ', self.b, '\n  c = ', self.c)

    # Вычисление периметра
   def tr_perimeter(self):
       self.per = self.a + self.b + self.c
       print('Периметр треугольника: ', self.per)

    # Вычисление высоты
   def tr_height(self):
       self.p = (1 / 2) * self.per
       self.h = (2 / self.a) * (math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c)))
       print('Высота треугольника: ', self.p, self.h)

    # Вычисление площади
   def tr_square(self):
       self.Sq = (1 / 2) * self.a * self.h
       print('Площадь треугольника: ', self.Sq)


trtr = Triangles()
trtr.tr_length()
trtr.tr_perimeter()
trtr.tr_height()
trtr.tr_square()


