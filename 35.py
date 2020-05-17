# In this exercise, load that JSON file from disk, extract the months of all the birthdays,
# and count how many scientists have a birthday in each month.

from collections import Counter
import json

months = []

with open('birthdays.json', 'r') as i:
    contents = json.load(i)

for i in contents:
    j = int(contents[i][0] + contents[i][1])
    months.append(j)

print(Counter(months))
