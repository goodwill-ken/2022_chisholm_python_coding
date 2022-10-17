# Schagne-Kenneth van der Merwe 11/10/2022
# Copywrite CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
# Write a program that sets a number to 14
# The program then displays whether the number is odd or even.
# c = a % b
# print('Line 5 - Value of c is ', c)


num1 = int(input('Choose a whole number:'))
if num1 % 2 == 0:
    print('This value is even')
elif num1 % 2 != 0:
    print('This value is odd')

