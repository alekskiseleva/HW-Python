__author__ = 'Киселева Александра'


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib1 = fib2 = 1

    if (n < 2) or (m < 2):
        quit()

    else:
        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2

        for j in range(m - n + 1):
            fib1, fib2 = fib2, fib1 + fib2
            print(fib2, end=' ')


n = int(input("Номер n элемента ряда Фибоначчи: "))
m = int(input("Номер m элемента ряда Фибоначчи: "))

print('\nРяд чисел Фибоначчи с n =', n, 'по m =', m, '\n')
fibonacci(n, m)
