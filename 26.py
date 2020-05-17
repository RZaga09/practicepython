# If a game of Tic Tac Toe is represented as a list of lists, like so:
# game = [[1, 2, 0],
#	[2, 1, 0],
#	[2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space,
# and a 2 means that player 2 put their token in that space.
# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.
# Here are some more examples to work with:
winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]


def check(board):
    win = 0
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        win = 1 if board[0][0] == 1 else 2
        return win
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        win = 1 if board[0][2] == 1 else 2
        return win
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != 0:
            win = 1 if board[0][i] == 1 else 2
            return win
        elif board[i][0] == board[i][1] == board[i][2] and board[i][0] != 0:
            win = 1 if board[i][0] == 1 else 2
            return win


print(check(winner_is_2))
print(check(winner_is_1))
print(check(winner_is_also_1))
print(check(no_winner))
print(check(also_no_winner))
