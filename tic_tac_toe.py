import random

x0 = ' '
x1 = ' '
x2 = ' '
x3 = ' '
x4 = ' '
x5 = ' '
x6 = ' '
x7 = ' '
x8 = ' '

i1 = input('Введите имя игрок 1: ')
i2 = input('Введите имя игрок 2: ')


class Game:

    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    @staticmethod
    def who_go_first(self):
        who_go_first = random.randint(1, 2)
        if who_go_first == 1:
            print(f'Первым будет ходить игрок {self.name1}')
        else:
            print(f'Первым будет ходить игрок {self.name2}')

    @staticmethod
    def winning_combinations():
        if x0 == x4 == x8 or x0 == x3 == x6 or x1 == x4 == x7 or x2 == x5 == x8 or x0 == x1 == x2 or x3 == x4 == x5 or x6 == x7 == x8 or x2 == x4 == x6:
            return False
        else:
            return True

    @staticmethod
    def pole():
        return f'{x0}|{x1}|{x2}\n{x3}|{x4}|{x5}\n{x6}|{x7}|{x8}'


pole1 = Game(i1, i2)
pole2 = Game.pole()


def game(pole2):
    sign = 'X'
    should_cont = True
    while Game.winning_combinations() or should_cont:
        try:
            i = int(input(f'{i1 if Game.who_go_first() else i2} куда Вы хотите поставить '
                          f'крестик? Выберите число от 0 до 8:'))
        except ValueError as x:
            print(f'You entered incorrect data: {x}. Try entering a number!')
            continue
        if 0 < i and i > 8:
            print('You entered an incorrect number, try to take from 0 to 8 sticks!')
            continue
        if i == 0:
            pass
        should_cont = input('Want play again? y/n : ').lower() == 'y'
