# 5. Check Whether a Number is Armstrong or Not 

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
