# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:
# My name is Michele
# Then I would see the string:
# Michele is name My
# shown back to me.

sentence = 'My name is Michele'
new_list = sentence.split()
new_list = reversed(new_list)
sentence = ' '.join(new_list)
print(sentence)
