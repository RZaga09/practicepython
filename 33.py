# For this exercise, we will keep track of when our friend’s birthdays are,
# and be able to find that information based on their name.
# Create a dictionary (in your file) of names and birthdays.
# When you run your program it should ask the user to enter a name,
# and return the birthday of that person back to them.

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706'
}


def get_bday(name):
    print('Enter a Name')
    bday = birthdays.get(name, 'Not in the Dict')
    print(f'{name} was born on {bday}')


get_bday('Albert Einstein')
get_bday('Benjamin Franklin')
get_bday('Leonardo da Vinci')
