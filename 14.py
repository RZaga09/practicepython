# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Extras:
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.

sample_list = [1, 1, 3, 5, 7, 7, 9, 9, 9]

new_list = list(set(sample_list))
print(new_list)

# USING LOOPS
for i in sample_list:
    if sample_list.count(i) > 1:
        sample_list.remove(i)
print(sample_list)
