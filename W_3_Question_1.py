# Schagne-Kenneth van der Merwe 11/10/2022
# Copywrite CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
# At the Chisholm Carnival there is a ride that only allows children
# on if they are 10 or older and 130cm or taller. Write a program,
# using a logical operator, which decides whether a child is allowed
# on or is rejected for the ride.

# Declare the acceptable height to ride is 130cm or more
go_height = 130
# Declare the acceptable age to ride is 10 years or older
go_age = 10

age = int(input('Enter the rider age in full years:  '))
height = int(input('Enter the rider height in full centimetres:  '))
if (age >= go_age) and (height >= go_height):
    print('They may ride.')
elif (age < go_age) and (height < go_height):
    print('They may not ride.')
