# 5. Check Whether a Number is Armstrong or Not(PyQ2021)
#Example: 1 ^3+5 ^3+3 ^3  = 1+125+27 = 153

import math 
# Take input from the user
n = int(input("Enter a Number: "))
tmp = n
s = 0
# Loop through each digit of the number
while tmp != 0:
    # Extract the last digit
    r = tmp % 10    
    # Add the cube of the digit to the sum
    s = s + int(math.pow(r, 3))    
    # Remove the last digit from the number
    tmp = tmp // 10
# Check if the original number is equal to the sum of cubes of its digits
if n == s:
    print("The Number %d is Armstrong" % n)
else:
    print("The Number %d is Not Armstrong" % n)

'''
#WAP to Find Armstrong Number Upto limit 'N'

import math

def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    if num_digits == 1:
        return False
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num

def find_armstrong_numbers_up_to_n(N):
    armstrong_numbers = [num for num in range(N + 1) if is_armstrong_number(num)]
    return armstrong_numbers

try:
    # Get user input for the limit 'N'
    N = int(input("Enter the limit (N) to find Armstrong numbers up to: "))

    # Find and print Armstrong numbers up to N
    armstrong_numbers = find_armstrong_numbers_up_to_n(N)
    
    if armstrong_numbers:
        print(f"Armstrong numbers up to {N}: {armstrong_numbers}")
    else:
        print(f"There are no Armstrong numbers between 0 and {N}.")

except ValueError:
    print("Error: Please enter a valid integer for the limit.")

'''