# Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:
# Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# Optional additions:
# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman.

from random import randint

stickman = ['( )', '( )\n |\n |', '( )\n\|\n |', '( )\n\|/\n |',
            '( )\n\|/\n |\n/', '( )\n\|/\n |\n/ \\']


def get_words():
    with open('words.txt', 'r') as dictionary:
        words = [i for i in dictionary.readlines()]
        word = words[randint(0, len(words) - 1)]
        return word


word = get_words().strip('\n')
blanks = ['_' for _ in range(0, len(word))]
done = []
wrong_guesses = 0
print('HANGMAN GAME\n')

while 1 == 1:
    guess = input('Guess a Letter: ').upper()
    if guess not in done:
        done.append(guess)
        if guess in word:
            indeces = [i for i, j in enumerate(word) if j == guess]
            for i in indeces:
                blanks[i] = guess
        else:
            wrong_guesses += 1
            print(stickman[wrong_guesses - 1])
            if wrong_guesses == 6:
                print('You Lose')
                print(word)
                break
    else:
        print('Already Guessed')

    hangman = ''.join(blanks)
    print(hangman)
    if hangman == word:
        print('Win!')
        break
