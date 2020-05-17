from random import randint


def get_words():
    with open('words.txt', 'r') as dictionary:
        words = [i for i in dictionary.readlines()]
        for i in words:
            i.strip('')
        word = words[randint(0, len(words) - 1)]
        return word


print(get_words())
