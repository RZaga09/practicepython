# Implement a function that takes as input three variables, and returns the largest of the three.
# Do this without using the Python max() function!


def largest():
    x = int(input())
    y = int(input())
    z = int(input())
    ans = x if x > y and x > z else y if y > z else z
    return ans


print(largest())
