import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

i1 = input('Player 1 enter your name: ')
i2 = input('Player 2 enter your name: ')

first = random.randint(1, 2)


def print_state(state):
    for i, c in enumerate(state):
        if (i + 1) % 3 == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')


win_comb = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def get_winner(state, combinations):
    for x, y, z in combinations:
        if state[x] == state[y] == state[z] and (state[x] == 'X' or state[x] == 'O'):
            return state[x]
    return ''


def play_game(board):
    global first
    sign = 'X'
    while get_winner(board, win_comb) == '':
        try:
            index = int(input(f'{i1.capitalize() if first == 1 else i2.capitalize()} where do u want to draw {sign}? '))
        except ValueError as x:
            print(f'You entered incorrect data: {x}. Try entering a number!')
            continue
        if 8 < index < 0:
            print('You entered an incorrect number, try 0 to 8!')
            continue
        board[index] = sign
        print(print_state(board))
        win_sign = get_winner(board, win_comb)
        if win_sign != '':
            print(f'We have a winner: {win_sign}')
        sign = 'X' if sign == 'O' else 'O'

        if first == 1:
            first = 0
        else:
            first = 1


play_game(board)
