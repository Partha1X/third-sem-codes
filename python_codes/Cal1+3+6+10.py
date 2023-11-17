'''Compute the sum of first n terms of the following series:
s=1+3+6+10+15+...
'''

n = int(input("Enter No of terms: "))
# Initialize variables
count = 0  # Counter for the number of terms
s = 0      # Variable to store the sum
num = 1    # Initial term of the series
step = 2   # Difference between consecutive terms in the series

# Loop to generate terms and calculate the sum
while count < n:
    print(num, end=' ')  # Print the current term
    s = s + num          # Add the current term to the sum
    num = num + step     # Update the current term for the next iteration
    step = step + 1      # Increase the step for the next iteration
    count = count + 1    # Increment the counter

# Print the final sum after the loop
print("\nSum =", s)


#Another Method :👇
'''s = 0
p = 0
n = int(input("Enter a value for n: "))

for i in range(1, n + 1):  # Corrected the range to start from 1
    p = p + i
    s = s + p

print(s)'''
