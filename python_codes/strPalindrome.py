# 3. Write a Python Program to Check Whether a Given 'String is Palindrome' or Not

# Take input from the user
s = input("Enter the Value: ")

# Reverse the string using slicing
reverse = s[::-1]

# Check if the original string is equal to its reverse
if s == reverse:
    print("Yes, it is a Palindrome")
else:
    print("It is not a palindrome")
