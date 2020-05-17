# The next logical step is to deal with handling user input.
# When a player (say player 1, who is X) wants to place an X on the screen,
# they can’t just click on a terminal. So we are going to approximate this clicking simply by asking
# the user for a coordinate of where they want to place their piece.
# As a reminder, our tic tac toe game is really a list of lists.
# Things to note:
# For this exercise, assume that player 1 (the first player to move) will always be X and player 2 (the second player) will always be O.
# Notice how in the example I gave coordinates for where I want to move starting from (1, 1) instead of (0, 0).
# Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then a number.
# Don’t worry about checking whether someone won the game, but if a player tries to put a piece in a game position where there already is another piece, do not allow the piece to go there.
# Bonus:
# For the “standard” exercise, don’t worry about “ending” the game - no need to keep track of how many squares are full.
# In a bonus version, keep track of how many squares are full and automatically stop asking for moves when there are no more valid moves.

board = [
    ['0', '0', '0'],
    ['0', '0', '0'],
    ['0', '0', '0']
]

player1 = True
count = 0

print('P1 = X; P2 = O')

while 1 == 1:
    print(board[0])
    print(board[1])
    print(board[2])
    if count == 9:
        print('End!')
        break
    while 1 == 1:
        row = int(input('row: ')) - 1
        col = int(input('col: ')) - 1
        if board[row][col] == '0':
            board[row][col] = 'X' if player1 else 'O'
            break
        else:
            print('Already Taken!')
    player1 = False if player1 else True
    count += 1
