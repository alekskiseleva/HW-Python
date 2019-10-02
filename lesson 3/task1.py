# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(fib_ext):

    fib1 = fib2 = 1

    if n < 2:
        quit()

    fib_ext.extend([1, 1])

    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        fib_ext.append(fib2)
    return

fib_ext = []

n = int(input("Номер n элемента ряда Фибоначчи: "))

fibonacci(fib_ext)
myMurr2 = fib_ext

print("массив ", myMurr2)



