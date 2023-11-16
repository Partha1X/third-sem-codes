# 7. WAP to Print Fibonacci Series up to n number

# Take input from the user for the upper limit
n = int(input("Enter the Upper Limit: "))

# Initialize the first two terms of the Fibonacci series
a = 0
b = 1

# Print the initial terms
print("The Fibonacci Series is:")

# Print the first two terms without newline
print("%d %d" % (a, b), end=' ')

# Initialize the next term in the series
c = a + b

# Continue the Fibonacci series until reaching the upper limit
while c <= n:
    # Print the current term
    print(c, end=' ')
    
    # Update the values for the next iteration
    a = b
    b = c
    c = a + b
