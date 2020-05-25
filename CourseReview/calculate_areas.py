"""***************************************************************************

                                  calculate_areas.py

Calculate areas of geometric shapes

***************************************************************************"""

# To run this program, start python and then type:
# calculate_areas

import math

rect_length = 10
rect_height = 20

circle_radius = 10

a = 30
b = 24
c = 18

p = (a + b + c) / 2

print('The area of a rectangle of length ', rect_length,' and height', rect_height, ' is ', rect_length*rect_height)

print('The area of a circle of radius', circle_radius, ' is ', math.pi*circle_radius*circle_radius)

print("The area of a triangle of dimensions a=", a, ",b=", b, ",c=", c,
      " using Heron's Formula is", math.sqrt(p*(p-a)*(p-b)*(p-c)))

