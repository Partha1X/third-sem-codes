#19. Write a Program to Implemant a Simple Calculator(+,-,*,/)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

while True:
    print("\n***** Simple Calculator *****")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("1. Add: ", add(num1, num2))
    print("2. Subtract: ", subtract(num1, num2))
    print("3. Multiply: ", multiply(num1, num2))
    print("4. Divide: ", divide(num1, num2))


 #Python program that implements a Proper basic calculator:👇

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y != 0:
#         return x / y
#     else:
#         return "Cannot divide by zero."

# while True:
#     print("\n***** Simple Calculator *****")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")

#     choice = input("Enter your choice (1/2/3/4/5): ")

#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             print("Result:", add(num1, num2))
#         elif choice == '2':
#             print("Result:", subtract(num1, num2))
#         elif choice == '3':
#             print("Result:", multiply(num1, num2))
#         elif choice == '4':
#             print("Result:", divide(num1, num2))
#     elif choice == '5':
#         print("Exiting the calculator. Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please enter a valid option (1/2/3/4/5).")
