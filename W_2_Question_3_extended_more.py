# Schagne-Kenneth van der Merwe 11/10/2022
# Copywrite CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
# Original task (str): Write a program that uses a nested if to calculate the shipping cost
# for Chisholm Gadgets. They only ship their headphones within Australia (AU) or the USA (US).
# For US if the order is $100 or less than the shipping cost is $50 but if it is over $100
# then it is $25. Within AU if the order is $100 or less than the shipping cost is $10
# and if it is over $100 then it is free shipping.
# Additional capabilities added (ul):
# Added greeting with user's name input
# Added time delays to the outputs
# Added bulk order discount of 10% for orders of over 600 units
# Capabilities to add (ul):
# Add variable bulk order quantity
# Add variable bulk order discount percentile
# Add auto capitalization to the user's name input
# Add animation for '...' between outputs
# Add loop back to append order (change/update)
# Add payment method inquiry
# Add CC information collection
# Add receipt
# Add goodbye

# importing the time library
import time

# greet user
user_name = input('Hello, what is your name?   ')


def greeting():

    # Add delay between sentences.

    print(f'Welcome to the Chisholm gadget store, {user_name}!')
    print('...')
    time.sleep(2)
    print('We have excellent headphones for sale today.')
    print('...')
    time.sleep(2)
    print('And we have a 10% discount for orders of over 500 pairs!')
    print('...')
    time.sleep(2)
    print('You could also get discounted delivery if you order is over $100!')
    print('...')
    time.sleep(2)


greeting()


# user enters quantity to order
def ordering_hphones():
    num_ord = int(input('How many pairs of headphones would you like to order?  '))
    time.sleep(1)

    # variables
    hphone_cost1 = 20
    goods_cost = num_ord * hphone_cost1
    # apply 10% discount
    discounted_amount = goods_cost * 0.1
    discounted_cost = goods_cost - discounted_amount
    # define valid answers for country
    usa_country_ul = ['usa', 'united states', 'united states of america']
    aus_country_ul = ['aus', 'australia']
    # define shipping fee
    std_ship_us = 50
    dis_ship_us = 25
    std_ship_au = 10
    dis_ship_au = 0

    # determination of discounted unit cost
    if num_ord > 500:
        print('The total cost of 600 headphones with a 10% discount is: ', '$', discounted_cost)
        time.sleep(2)
    else:
        print('The cost of ', num_ord, 'headphones is: ', '$', goods_cost)
        time.sleep(2)

    # Determination of discounted delivery fee
    if goods_cost > 100:

        # Application of discounted delivery fee
        def discount_rate():

            # Determination of which country to apply discounted delivery fee
            ship_where = input('Do you want delivery to the "USA" (United States of America) or to "AUS" (Australia)? ')
            # Check if shipping country code is accepted and ask for new entry if not in the list
            while (ship_where.lower() not in usa_country_ul) and (ship_where.lower() not in aus_country_ul):
                time.sleep(2)
                ship_where = str(input('Invalid country code. Retry with "USA" or "AUS":  '))

            # Application of discounted delivery fee for USA
            if ship_where.lower() in usa_country_ul:
                time.sleep(2)
                print('The discounted USA delivery will be: ', '$', dis_ship_us)
                if dis_ship_us == 0:
                    time.sleep(2)
                    print("That's zip, nada, totally free delivery to your door!")
                total_cost = dis_ship_us + goods_cost
                time.sleep(2)
                print('The total cost will be: ', '$', total_cost)

            # Application of discounted delivery fee for AUS
            elif ship_where.lower() in aus_country_ul:
                time.sleep(2)
                print('The discounted Australian delivery fee will be: ', '$', dis_ship_au)
                if dis_ship_au == 0:
                    time.sleep(2)
                    print("That's zip, nada, totally free delivery to your door!")
                total_cost = dis_ship_au + goods_cost
                time.sleep(2)
                print('The total cost will be: ', '$', total_cost)

        discount_rate()

    # Determination of full delivery fee
    elif goods_cost <= 100:

        # Application of full delivery fee
        def full_rate():

            # Determination of which country to apply discounted delivery fee
            ship_where = input('Do you want delivery to the "USA" (United States of America) or to "AUS" (Australia)? ')
            # Check if shipping country code is accepted and ask for new entry if not in the list
            while (ship_where.lower() not in usa_country_ul) and (ship_where.lower() not in aus_country_ul):
                time.sleep(2)
                ship_where = str(input('Invalid country code. Retry with "USA" or "AUS":  '))

            # Application of full delivery fee for USA
            if ship_where.lower() in usa_country_ul:
                time.sleep(2)
                print('The USA delivery fee will be: ', '$', std_ship_us)
                total_cost = std_ship_us + goods_cost
                time.sleep(2)
                print('The total cost will be: ', '$', total_cost)

            # Application of full delivery fee for AUS
            elif ship_where.lower() in aus_country_ul:
                time.sleep(2)
                print('The Australian delivery fee will be: ', '$', std_ship_au)
                total_cost = std_ship_au + goods_cost
                time.sleep(2)
                print('The total cost will be: ', '$', total_cost)

        full_rate()


ordering_hphones()
