# Let’s say the word the player has to guess is “EVAPORATE”.
# For this exercise, write the logic that asks a player to guess a letter and
# displays letters in the clue word that were guessed correctly.
# For now, let the player guess an infinite number of times until they get the entire word.
# As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again.
# Remember to stop the game when all the letters have been guessed correctly!

word = 'EVAPORATE'
blanks = ['_' for _ in range(0, len(word))]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while 1 == 1:
    guess = input('Guess a letter! ')
    if guess.upper() not in letters:
        print('Already chosen!')

    elif guess.upper() in word:
        letters.remove(guess.upper())
        indeces = [i for i, j in enumerate(word) if j == guess.upper()]
        for i in indeces:
            blanks[i] = guess.upper()

    else:
        letters.remove(guess.upper())
        print('Not correct!')

    hangman = (''.join(blanks))
    print(hangman)
    if hangman == word:
        print('YOU WIN')
        break
