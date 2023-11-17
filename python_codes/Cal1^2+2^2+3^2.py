# Calculate s = 1^2 + 2^2 + 3^2 + ... up to n using math function

import math 
n = int(input("Enter the value of n:"))
s = 0
for i in range(1, n+1):
    s = s + math.pow(i, 2)  # in floating point
    # s = s + int(math.pow(i, 2))  # in integer

print("Sum =", s)
