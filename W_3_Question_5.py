# Schagne-Kenneth van der Merwe 11/10/2022
# Copywrite CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
# Write the algorithm for a program that sets the weight of a parcel to 12g. If the weight is 8 g or
# less, there is delivery charge of a flat fee of $1.50. If the weight is more than 8 g then $1.50 plus
# $0.50 for each gram over 8g is charged for delivery. The program displays the weight and the
# delivery fee. Use both pseudocode and a flowchart.
# PSEUDOCODE BELOW
# SET p_weight = 12 (grams)
# DECIDE if p_weight <= 8
# THEN delivery_c = $1.50
# OTHERWISE delivery_c = 1.5 + (0.5*(p_weight - 8))
# DISPLAY p_weight
# DISPLAY delivery_c

p_weight = 12
# for input use: p_weight = int(input('What is the weight of the package, in grams?'))
if p_weight >= 8:
    delivery_c = 1.5 + (0.5 * (p_weight - 8))
else:
    delivery_c = 1.5
print('The package weight is ', p_weight)
print('The delivery fee is ', delivery_c)
