# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
#   Add on to the previous program by asking the user for another number and printing out
#       that many copies of the previous message. (Hint: order of operations exists in Python)
#   Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

print('Name?')
name = input()
print('Age?')
year = str(100 - int(input()) + 2020)

print('One More Number?')
num = int(input())

for i in range(0, num):
    print(f'{i + 1}: Hi {name}! You will turn 100 in the year {year}')
