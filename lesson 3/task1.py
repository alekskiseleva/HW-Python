# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m, fib1, fib2):

    if n < 2:
        quit()

    print(fib1, end=' ')
    print(fib2, end=' ')

    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

    print('\n')

    for i in range(2, m):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

    return

fib1 = fib2 = 1

n = int(input("Номер n элемента ряда Фибоначчи: "))
m = int(input("Номер m элемента ряда Фибоначчи: "))

fibonacci(n, m, fib1, fib2)


n = int(input("Номер n элемента ряда Фибоначчи: "))

f1 = 1
f2 = 1

print(f1, f2, end=" ")
for i in range(3, n+1):
    print(f1+f2, end=" ")
    b = f1
    f1 = f2
    f2 = b + f1

print()
