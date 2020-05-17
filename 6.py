# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

print('Type a word')
word = input()

c = ([i for i in word])
d = list(reversed(c))
print('Palindrome') if d == c else print('Not')
