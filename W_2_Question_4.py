# Schagne-Kenneth van der Merwe 11/10/2022
# Copywrite CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
# Write a program that will prompt the user to enter an integer.
# If the number is greater than 10 the program will display “The
# number entered is larger than 10”
# otherwise the program will display “The number entered in not larger than 10”

user_input = int(input('Please enter a whole number:'))
if user_input > 10:
    print('The number entered is larger than 10')
elif user_input < 10:
    print('The number entered is not larger than 10')
if user_input == 10:
    print('The number entered is equal to 10')
