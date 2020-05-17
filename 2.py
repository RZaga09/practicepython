# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

print('Number?')
num = int(input())
if num % 4 == 0:
    print('Div by 4')
else:
    print('Even') if num % 2 == 0 else print('Odd')

print('Type Two More Numbers')
num = int(input())
check = int(input())
print(f'{num} divides equally by {check}') if num % check == 0 else print(
    f'{num} does not divide equally by {check}')
