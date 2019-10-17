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

class CardLoto:

    def __init__(self):
        self.card_loto = []

    def generator_card(self):

        for i in range(3):
            for j in range(5):
                for bar in range(1, 90):
                   self.card_loto.append(bar)
                   print(self.card_loto[i][j])

class Barrel:

    def __init__(self):
        self.keg = []

    def generator_keg(self):
        for i in range(1, 90):
            self.keg.append(i)
            print(self.keg)


loto_game = CardLoto()
loto_game.generator_card()

step = Barrel()
step.generator_keg()