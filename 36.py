# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!

from bokeh.plotting import figure, show, output_file
from collections import Counter
import json

with open('birthdays.json', 'r') as i:
    contents = json.load(i)

months = []
for i in contents:
    j = str(int(contents[i][0] + contents[i][1]))
    months.append(j)

output_file('months.html')
categories = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
x = []
y = []
for i in months:
    if i not in x:
        x.append(i)
temp = Counter(months)
for i in x:
    y.append(temp[i])
p = figure(x_range=categories)
p.vbar(x=x, top=y, width=0.5)

show(p)
