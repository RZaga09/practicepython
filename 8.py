# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner
# and ask if the players want to start a new game)

# DICT (ITEM: WHAT ITEM WINS AGAINST)
game_dict = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}

while 1 == 1:
    print('Rock, Paper, Scissors!')
    print('Player 1 choose play')
    p1 = input()
    print('Player 2 choose play')
    p2 = input()

    if p1 == p2:
        print('Draw\n')
    else:
        print('P1 Wins!\n') if game_dict[p1] == p2 else print('P2 wins!\n')

    if input('Continue? (y/n)') == 'n':
        break
