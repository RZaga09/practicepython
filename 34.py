# In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk,
# rather than having the dictionary defined in the program.
# Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary,
# and update the JSON file you have on disk with the scientist’s name.

import json
birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706'
}

# CREATE JSON FROM birthdays


def get_json():
    with open("birthdays.json", "w") as json_file:
        json.dump(birthdays, json_file)


def search_bday(name):
    if name in contents:
        print(contents[name])
    else:
        print('Not in Dict')


def add_bday(name, bday):
    contents[name] = bday
    print(contents)
    with open('birthdays.json', 'w') as json_file:
        json.dump(contents, json_file)


# get_json()
with open('birthdays.json', 'r') as json_file:
    contents = json.load(json_file)
search_bday('Albert Einstein')  # prints bday
search_bday('Trump')  # prints 'Not in Dict'
add_bday('USA', '07/04/1776')  # adds parameters to json
