# Schagne-Kenneth van der Merwe 11/10/2022
# Copywrite CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
# The company Chisholm Gadgets sell headphones for $20. '''
# If you order over 500 of the headphones you get a 10% discount '''
# Write a program using an if statement that calculates the cost '''
# of an order of 600 headphones and  displays the cost.   '''
# use if else function.

headphones_cost1 = 20
number_ordered = 600
total_cost = number_ordered * headphones_cost1
discounted_amount = total_cost * 0.1
discounted_cost = total_cost - discounted_amount
if number_ordered > 500:
    print('the total cost of 600 headphones with a 10% discount is: ', '$', discounted_cost)
