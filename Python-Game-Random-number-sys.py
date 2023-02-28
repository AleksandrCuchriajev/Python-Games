import sys
from random import randint

# Generate number from 1 to 10
random_number = randint(int(sys.argv[1]), int(sys.argv[2]))

while True:
    # Get input from user
    try:
        user_guess = int(input('Type the number between 1 and 10: '))
        # Check if the user guess is the random number

        if 1 < user_guess < 10:
            if user_guess > random_number:
                print('Try again. Your number is higher')
            elif user_guess < random_number:
                print('Try again. Your number is lower')
            else:
                print(f'The lucky number is {user_guess}. End of game..')
                break
        else:
            print('You have typed the wrong number. It must be between 1 and 10')
    except ValueError:
        print('Please enter the number')
