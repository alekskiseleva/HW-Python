__author__ = 'Киселева Александра'


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib1 = fib2 = 1
    fib_list = []

    if (n < 2) or (m < 2):
        print('При заданных числах нельзя вывести ряд')
        quit()

    else:

        for i in range(2, n):
            fib1, fib2 = fib2, fib1 + fib2

        for j in range(m - n + 1):
            fib1, fib2 = fib2, fib1 + fib2
            fib_list.append(fib2)

    return fib_list


n = int(input("Номер n элемента ряда Фибоначчи: "))
m = int(input("Номер m элемента ряда Фибоначчи: "))

fibonacci(n, m)
for i in fib_list:
    print(i, end=' ')
