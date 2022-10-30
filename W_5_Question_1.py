# Schagne-Kenneth van der Merwe 11/10/2022
# Copywrite CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

# Create a text file with the following:
# Twinkle twinkle little star
# How I wonder what you are
# Up above the world so high
# Like a diamond in the sky
# Then write a program to read the text from the file
# and display it to the screen

Twinkle_little_star = open('twinkle_twinkle.txt', 'r')
print(Twinkle_little_star.read())

print('Twinkle twinkle little star has been read and printed.')
