# Tehtävä 2.3

import math

# Given values
d = 6.4  # length of the diagonal in meters
ratio_a = 3
ratio_b = 2

# Solve for x using the Pythagorean theorem: (3x)^2 + (2x)^2 = d^2
# Expanding: 9x^2 + 4x^2 = d^2 simplifies to: 13x^2 = d^2
x = math.sqrt(d**2 / (ratio_a**2 + ratio_b**2))

# Calculate side lengths a and b
a = ratio_a * x
b = ratio_b * x

print("The length of side a is:", a, "meters")
print("The length of side b is:", b, "meters")
# vastaus
#The length of side a is: 5.3251218837622005 meters
#The length of side b is: 3.5500812558414667 meters