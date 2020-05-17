#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# |   |   |   |
#  --- --- ---
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes
# (8x8 for chess, 19x19 for Go, and many more).
# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

size = int(input('Size of board? \n'))


def horizontal_lines(size):
    hori = ''
    for _ in range(size):
        hori = hori + ' ---'
    return hori


def vertical_lines(size):
    verti = ''
    for _ in range(size + 1):
        verti = verti + '|   '
    return verti


def print_board():
    print(horizontal_lines(size))
    for _ in range(size):
        print(vertical_lines(size))
        print(horizontal_lines(size))


print_board()
