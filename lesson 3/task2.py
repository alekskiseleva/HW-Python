__author__ = 'Киселева Александра'

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

from random import randint


def sort_to_max(lst_dz3):

    n = len(lst_dz3)
    for i in range(n):

        for j in range(n - i - 1):
            a, b = lst_dz3[j], lst_dz3[j + 1]

            if a > b:
                lst_dz3[j], lst_dz3[j + 1] = b, a


m = int(input("Введите количество элементов для списка: "))

lst_dz3 = [randint(-100, 100) for i in range(m)]

print('Исходный список:')
for i in lst_dz3:
    print(i, end=' ')

print()

print('Отсортированный список:')
sort_to_max(lst_dz3)
for i in lst_dz3:
    print(i, end=' ')
