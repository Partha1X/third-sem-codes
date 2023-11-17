'''
Write a program to recive inputs as three side of a triangle ,
and output the area of triangle .
Show Error if the values entered cannot make triangle (PyQ2019)

Triangle using Heron's formula:
Area = sqrt(s * (s - a) * (s - b) * (s - c))

where:
- a, b, and c are the lengths of the sides of the triangle.
- s is the semi-perimeter of the triangle, calculated as s = (a + b + c) / 2.

'''

import math

def triangle_area(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Side lengths cannot be negative")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Sides do not form a triangle")

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

try:
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))

    area = triangle_area(a, b, c)
    print("Area of triangle:", area)
except ValueError as e:
    print(e)
