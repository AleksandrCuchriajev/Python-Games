from random import shuffle


def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Pick a number 0,1 or 2 : ')
    return int(guess)


def check_guess(my_list, guess):
    if my_list[guess] == 'O':
        print(my_list)
        return 'You have won!'
    print(my_list)
    return 'You lose!'


# Initial list with data
my_list = [' ', 'O', ' ']
# Mixed list
mixed_list = shuffle_list(my_list)
# User guess
guess = player_guess()
# Result
print(check_guess(mixed_list, guess))
