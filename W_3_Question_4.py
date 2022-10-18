# Schagne-Kenneth van der Merwe 11/10/2022
# Copywrite CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
# Write the algorithm for a program that sets the radius of a circle at 10cm and then calculate and
# displays the area and circumference of the circle (A=πr^2 and C=2πr ) using pseudocode and a
# flowchart
# PSEUDOCODE BELOW
# SET r = 10
# DECLARE A = Pi x (r x r)
# DECLARE C = 2 x (Pi x r)
# DISPLAY A
import math

r = 10
A = math.pi * (r * r)
C = 2 * (math.pi * r)
print('The area of a circle with the radius of', r, 'cm is', A)
print('The circumference of a circle with the radius of', r, 'cm is', C)
