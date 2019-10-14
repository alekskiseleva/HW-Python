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