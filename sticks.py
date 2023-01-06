sticks = 10  # Можно изменять на любое кол-во
player = 1

player1 = input('Player 1 enter your name: ')
player2 = input('Player 2 enter your name: ')

while sticks > 0:
    try:
        i1 = int(input(f'{player1.capitalize() if player == 1 else player2.capitalize()} enter the number of sticks '
                       f'you want to pick up, on the table {sticks} sticks: '))
    except ValueError as x:
        print(f'You entered incorrect data: {x}. Try entering a number!')
        continue
    if 0 <= i1 and i1 >= 4:  # Также можно изменять
        print('You entered an incorrect number, try to take from 1 to 3 sticks!')
        continue
    sticks -= i1
    if sticks <= 0:
        print(f'{player1.capitalize() if player == 1 else player2.capitalize()} you lose :(, there are no more sticks '
              f'on the table')
    if player == 1:
        player = 0
    else:
        player = 1
