__author__ = 'Киселева Александра'

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

from random import randint


def sort_to_max(lst_dz3):
    for i in range(n):

        for j in range(n - i - 1):

            if lst_dz3[j] > lst_dz3[j + 1]:
                lst_dz3[j + 1], lst_dz3[j] = lst_dz3[j], lst_dz3[j + 1]


n = int(input("Введите количество элементов для списка: "))

lst_dz3 = [randint(-100, 100) for i in range(n)]

print(lst_dz3, end=' ')

sort_to_max(lst_dz3)

print('\nОтсортированный список:\n', lst_dz3, end=' ')
