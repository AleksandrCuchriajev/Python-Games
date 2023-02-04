import random

# Choosing random number between 1 and 100
random_selection = random.choice(range(1, 101))
# random_number=random.randint(1, 100)
is_game_over = False
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
logo = """

   _____                       _   _                                  _               
  / ____|                     | | | |                                | |              
 | |  __ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   

"""


def choose_difficulty():
    """Function to choose difficulty"""
    option = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if option == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif option == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        print("You typed wrong word. We set an easy difficulty.")
        return EASY_LEVEL_ATTEMPTS


def guess_check(guess_number, attempts_number, random_number):
    """Function to check the user guess against actual number"""
    if random_number == guess_number:
        print(f"You win. The number was {random_number}. \nYou had {attempts_number} attempts remaining to guess the "
              f"number.")
    elif random_number > guess_number:
        attempts_number -= 1
        print(f'Too low.')
    elif random_number < guess_number:
        attempts_number -= 1
        print(f'Too high.')
    else:
        pass
    return attempts_number


print(logo)
print("Welcome to the Guessing the Number Game!")
print("A guessing number is between 1 and 100.")

attempts = choose_difficulty()


while not is_game_over:
    # User guess a number
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess : "))
    if guess > 100 or guess < 1:
        print(f'You typed wrong number.\nYou have {attempts} remaining to guess the number.')
        continue
    # Repeating the guessing functionality
    attempts = guess_check(guess_number=guess, attempts_number=attempts, random_number=random_selection)
    if attempts == 0 or random_selection == guess:
        print(f"You lost the game. No attempts left")
        is_game_over = True
