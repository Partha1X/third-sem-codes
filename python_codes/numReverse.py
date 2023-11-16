#28.b) WAP to reverse a Number

num = int(input("Enter a Number: "))
reversed_num = 0# Initialize variables
while num > 0:# Reverse the number
    digit = num % 10  # Extract the last digit
    reversed_num = reversed_num * 10 + digit  # Append the digit to the reversed number
    num = num // 10  # Remove the last digit
print("Reversed Number:", reversed_num)
