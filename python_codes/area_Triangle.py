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


''''
This code first defines a function "triangle_area()" that takes the side lengths of a triangle as arguments.
The function checks if any side length is negative, in which case it raises a "ValueError".
It also checks if the sides satisfy the triangle inequality, in which case it raises another "ValueError".

If no errors are raised, the function calculates
the semiperimeter 's' of the triangle and then uses Heron's formula to calculate the area.
Finally, the function returns the area.

The main part of the code prompts the user to enter the side lengths of the triangle,
converts them to floats,and calls the "triangle_area()" function with the user-entered values.
If the function raises an error, the error message is printed to the console.
Otherwise, the area of the triangle is printed.
'''