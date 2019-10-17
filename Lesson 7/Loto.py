# *Генерируем 2 карточки.  Для каждой задаем 3 строки по 5 элементов
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#	Если цифра есть на карточке - она зачеркивается и игра продолжается.
#	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#	Если цифра есть на карточке - игрок проигрывает и игра завершается.
#	Если цифры на карточке нет - игра продолжается.
# Побеждает тот, кто первый закроет все числа на своей карточке.
import random


class CardLoto:

    def __init__(self):
        self.crd_lt = []

    def generator_card(self):
        self.crd_lt = [sorted([random.randint(0, 90) for i in range(1, 6)]) for i in range(3)]
        for i in self.crd_lt:
            print(('{:>3} ' * len(i)).format(*i))

#class Barrel:

#    def __init__(self):
#        self.keg = []

#    def generator_keg(self):
#        for i in range(1, 90):
#            self.keg.append(i)
#            print(self.keg)


loto_game = CardLoto()
loto_game.generator_card()
loto_game.crd_lt_print()

#step = Barrel()
#step.generator_keg()
