import random

random_number = random.randint(1, 50)
attempt = 6

while attempt != 0:
    a = int(input('Please enter a guess number between 1 and 50: '))
    if a < 1 or a > 50:
        continue
    if random_number > a:
        print('The guessed number is greater than the entered one!')
    elif random_number < a:
        print('The guessed number is less than the entered one!')
    else:
        print('You guessed the number!')
        break
    attempt -= 1
