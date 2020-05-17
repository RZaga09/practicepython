# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
# Extras:
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

from random import randint

while 1 == 1:
    print('Guess the Number between 1 and 9')
    guesses = 0
    num = randint(1, 10)
    while 1 == 1:
        guesses += 1
        guess = int(input())
        if guess == num:
            print(f'Win! ({guesses} guesses)')
            if input('Exit? (y/n)') == 'y':
                exit()
            else:
                break
        else:
            print('Higher!') if guess < num else print('Lower!')
