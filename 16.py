# Write a password generator in Python. Be creative with how you generate passwords
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.
# Extra:
# Ask the user how strong they want their password to be.

from random import randint

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = [i.upper() for i in lower]
numbers = [str(i) for i in range(0, 10)]
symbols = ['.', '/', '<', '>', ':', ';', '[', ']',
           '{', '}', '-', '_', '+', '=', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '~']

# Strength : Range of Chars + 1
strength = {
    'w': (2, 5),
    'm': (7, 12),
    's': (14, 21)
}

char = {
    1: lower,
    2: upper,
    3: numbers,
    4: symbols
}

while 1 == 1:
    choice = input('Weak, Medium, or Strong password? (w, m, s)\n')
    word = ''
    for i in range(0, randint((strength[choice])[0], (strength[choice])[1]) - 1):
        j = randint(1, 4)
        word = word + char[j][randint(0, len(char[j]) - 1)]
    print(word)

# Using random.sample also works
