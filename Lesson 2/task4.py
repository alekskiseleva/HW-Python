__author__ = 'Киселева Александра'

# Задача-4: Дан список, заполненный произвольными целыми числами
# Получите новый список, элементами которого будут только уникальные элементы исходного
# Например, lst = [1,2,4,5,6,2,5,2], нужно получить lst2 = [1,4,6]

from random import randint

# my_list = [randint(0, 100) for i in range(30)]
#my_list = [1, 2, 4, 6, 8, 5, 6, 2, 5, 2, 9, 11, 0, 7]

my_list = [10, 1, 2, 3, 3]

print('Список, заполненный произвольными целыми числами:')
for i in my_list:
    print(i, end=' ')

mdict = dict()

for x in my_list:
    if x not in mdict:
        mdict[x] = 1
    else:
        mdict[x] = mdict[x] + 1

print(mdict)
lst = []

for k, v in mdict.items():

    if v == 1:
        lst.append(k)

if lst == '':

    print('Список пуст')

else:
    print('Cписок уникальных элементов исходного:')
    print(lst)
