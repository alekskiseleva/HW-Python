# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math


class Trapezes:
    # задаем атрибуты
    x1, x2, x3, x4, y1, y2, y3, y4 = 0, 0, 0, 0, 0, 0, 0, 0
    a, b, c, d, p, per, Sq = 0, 0, 0, 0, 0, 0, 0

    # координаты точек
    def __init__(self):
        self.x1, self.y1 = list(map(int, input('Введите координаты точки A(x1,y1): ').split()))
        self.x2, self.y2 = list(map(int, input('Введите координаты точки B(x2,y2): ').split()))
        self.x3, self.y3 = list(map(int, input('Введите координаты точки C(x3,y3): ').split()))
        self.x4, self.y4 = list(map(int, input('Введите координаты точки C(x3,y3): ').split()))

    # вычисление сторон через векторы
    def trpz_length(self):
        self.a = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.b = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        self.c = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
        self.d = math.sqrt((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2)
        print('\nДлины сторон трапеции: ', '\n  a = ', self.a, '\n  b = ', self.b, '\n  c = ', self.c, '\n  c = ', self.d)

    #определяем является ли фигура равнобедренной трапецией
    #def trpz_isosceles:       pass

    # Вычисление периметра
    def trpz_perimeter(self):
        self.per = self.a + self.b + self.c +  self.d
        print('Периметр трапеции: ', self.per)

    # Вычисление площади
    def trpz_square(self):
        self.Sq = (self.a + self.b)/2 * (math.sqrt(self.c**2 - (((self.a - self.b)**2)/4)))
        print('Площадь трапеции: ', self.Sq)



trpz = Trapezes()
#trpz.trpz_isosceles()
trpz.trpz_length()
trpz.trpz_perimeter()
trpz.trpz_square()
