# Schagne-Kenneth van der Merwe 11/10/2022
# Copywrite CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
# Write the algorithm for a program that calculates and displays the sum of the even number from 2
# to 20 inclusive. Use both pseudocode and flowchart.
# PSEUDOCODE BELOW
# DISPLAY all the numbers between 2 and 20 (inclusive).
# DECIDE if the numbers within a range of 2 and 20 are even or odd.
# ADD the even numbers to the sum of the even numbers.
# DISPLAY the sum of the even numbers with each iteration.

sum_i = 0

for i in range(2, 21):
    print('This is interation #', i)
    if i % 2 == 0:
        sum_i = sum_i + i
        print('This is an even number.')
        print('**It will be added to the sum of even numbers.**')
        print('The sum of the even numbers so far is: ', sum_i)
    else:
        print('This is an odd number.')
        print('It will not be added to the sum.')
