import random

should_cont = True

while should_cont:
    player = input('Select R - rock, S - scissors, P - paper: ')

    if player not in ['R', 'S', 'P']:
        print('Try again, your input incorrect!')
        continue

    computer = random.randint(1, 3)

    if computer == 1:
        comp_choice = 'R'
    elif computer == 2:
        comp_choice = 'S'
    else:
        comp_choice = 'P'

    winning_comb = [('P', 'R'), ('R', 'S'), ('S', 'P')]

    if player == comp_choice:
        print('Draw')
    elif (player, comp_choice) in winning_comb:
        print('You win!!!')
    else:
        print('Computer win :(')

    should_cont = input('Want play again? y/n : ').lower() == 'y'
