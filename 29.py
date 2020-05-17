# Make a two-player Tic Tac Toe game!

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
player1 = True
moves = 0


def show():
    print(' --- --- ---')
    for i in range(3):
        print(f'| {board[i][0]} | {board[i][1]} | {board[i][2]} |')
        print(' --- --- ---')


def move(player1):
    while 1 == 1:
        row = int(input('row: ')) - 1
        col = int(input('col: ')) - 1
        if board[row][col] == ' ':
            board[row][col] = 'X' if player1 else 'O'
            break
        else:
            print('Already Taken!')


def check():
    win = 0
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        win = 1 if board[0][0] == 'X' else 2
        return win
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        win = 1 if board[0][2] == 'X' else 2
        return win
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            win = 1 if board[0][i] == 'X' else 2
            return win
        elif board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            win = 1 if board[i][0] == 'X' else 2
            return win


show()
while 1 == 1:
    print("Player 1's Turn!") if player1 else print("Player 2's Turn!")
    move(player1)
    show()
    player1 = False if player1 else True
    moves += 1
    if check() == 1:
        print('Player 1 wins!')
        break
    elif check() == 2:
        print('Player 2 wins!')
        break
    elif moves == 9:
        print('Draw!')
        break
