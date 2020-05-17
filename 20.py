# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.
# Extras:
# Use binary search.

from random import randint
from math import floor

nums = sorted([randint(0, 99) for i in range(0, 51)])
guess = randint(0, 99)
print(guess)


def check():
    while len(nums) != 1:
        print(nums)
        index = floor((len(nums) - 1)/2)
        if guess == nums[index]:
            return True
        elif guess > nums[index]:
            for _ in range(index + 1):
                nums.pop(0)
        else:
            for _ in range(len(nums) - (index + 1)):
                nums.pop()

    if guess not in nums:
        return False


print(check())
