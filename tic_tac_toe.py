import random

#
# name1 = input('Введите имя первого игрока: ')
# name2 = input('Введите имя второго игрока: ')
# who_go_first = random.randint(1, 2)
# if who_go_first == 1:
#     print(f'Первым будет ходить игрок {name1}')
# else:
#     print(f'Первым будет ходить игрок {name2}')
x0 = ' '
x1 = ' '
x2 = ' '
x3 = ' '
x4 = ' '
x5 = ' '
x6 = ' '
x7 = ' '
x8 = ' '


class Game:

    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def who_go_first(self):
        who_go_first = random.randint(1, 2)
        if who_go_first == 1:
            print(f'Первым будет ходить игрок {self.name1}')
        else:
            print(f'Первым будет ходить игрок {self.name2}')

    def pole(self):
        return f'{x0}|{x1}|{x2}\n{x3}|{x4}|{x5}\n{x6}|{x7}|{x8}'

    @classmethod
    def winning_combinations(cls):
        if x0 == x4 == x8 or x0 == x3 == x6 or x1 == x4 == x7 or x2 == x5 == x8 or x0 == x1 == x2 or x3 == x4 == x5 or x6 == x7 == x8 or x2 == x4 == x6:
            return False
        else:
            return True


pole = Game("John", "Mike")
while pole.winning_combinations():
    x = input('Введите первый ход: ')
    if x ==
print(pole.pole())
print(pole.who_go_first())