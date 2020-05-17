# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
# At the end of this exchange, your program should print out how many guesses it took to get your number.

nums = [i for i in range(1, 101)]
guesses = 0
print('Answer with 1 (too high), 2 (too low), 3 (correct)')

while 1 == 1:
    guess = nums[int(len(nums)/2) - 1]
    guesses += 1
    print(guess)
    ans = input()
    if ans == '1':
        for i in nums:
            if i >= guess:
                nums.remove(i)
    elif ans == '2':
        for i in nums:
            if i <= guess:
                nums.remove(i)
    else:
        print(f'Took me {guesses} guesses!')
        break
