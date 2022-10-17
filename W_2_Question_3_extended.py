# Schagne-Kenneth van der Merwe 11/10/2022
# Copywrite CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
# Write a program that uses a nested if to calculate the shipping cost
# for Chisholm Gadgets. They only
# ship their headphones within Australia (AU) or the USA (US).
# For US if the order is $100 or less then the shipping cost is $50
# but if it is over $100 then it is $25.
# Within AU if the order is $100 or less then the shipping cost is $10
# and if it is over $100 then it is free shipping

hphone_cost1 = 20
std_ship_us = 50
dis_ship_us = 25
std_ship_au = 10
dis_ship_au = 0
delivery_fee = None
total_cost = None
num_ord = int(input('How many pairs of headphones would you like to order?  '))
goods_cost = num_ord * hphone_cost1
discounted_amount = goods_cost * 0.1
discounted_cost = goods_cost - discounted_amount

if num_ord > 500:
    print('the total cost of 600 headphones with a 10% discount is: ', '$', discounted_cost)
else:
    print('the total cost of ', num_ord, 'headphones without a discount is: ', '$', goods_cost)

if goods_cost > 100:
    ship_where = input('Do you want delivery to the "USA" (United States of America) or to "AUS" (Australia)?')
    if ship_where == 'USA':
        print('The discounted USA delivery will be: ', '$', dis_ship_us)
        total_cost = dis_ship_us + goods_cost
        print('The total cost will be: ', '$', total_cost)
    elif ship_where != 'USA':
        print('The USA delivery fee will be: ', '$', std_ship_us)
        total_cost = std_ship_us + goods_cost
        print('The total cost will be: ', '$', total_cost)
elif goods_cost <= 100:
    ship_where = input('Do you want delivery to the "USA" (United States of America) or to "AUS" (Australia)?')
    if ship_where == 'AUS':
        print('The discounted Australian delivery fee will be: ', '$', dis_ship_au)
        total_cost = dis_ship_au + goods_cost
        print('The total cost will be: ', '$', total_cost)
    elif ship_where != 'AUS':
        print('The Australian delivery fee will be: ', '$', std_ship_au)
        total_cost = std_ship_au + goods_cost
        print('The total cost will be: ', '$', total_cost)

# Need to figure out how to make the location not case sensitive

