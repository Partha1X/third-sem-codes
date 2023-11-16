#18. Write a menu Driven Program to Find the Area of a Square ,rectangle and Circle , after receving appropriate input from the user

import math
def square_area(side):
    return side * side

def rectangle_area(length, width):
    return length * width

def circle_area(radius):
    return math.pi * radius * radius

while True:
    print("\n***** Area Calculator *****")
    print("1. Calculate the Area of a Square")
    print("2. Calculate the Area of a Rectangle")
    print("3. Calculate the Area of a Circle")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        side = float(input("Enter the side length of the square: "))
        print("Area of the square:", square_area(side))

    elif choice == '2':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print("Area of the rectangle:", rectangle_area(length, width))

    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        print("Area of the circle:", circle_area(radius))

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4).")
