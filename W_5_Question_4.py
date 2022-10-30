# Schagne-Kenneth van der Merwe 11/10/2022
# Copywrite CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

# Write a program that stores the word “debugging” in a variable
# and then takes the first letter of the word,“d”, and places
# it at the end of the word.

first_w = 'debugging'
cropped_fw = first_w[1:]
first_l = first_w[0]
print('The first word is: ')
print('"', first_w, '"')
print('The first letter in the first word is: ')
print('"', first_l, '"')
print('If you crop the first letter from the first word: ')
print('"', cropped_fw, '"')
print('If you add the first letter to the end of the cropped first word: ')
print('"', cropped_fw + first_l, '"')
