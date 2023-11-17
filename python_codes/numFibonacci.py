#Write a program to find the first ‘n’ terms of Fibonacci series(PyQ2020)
n_terms = int(input ("How many terms the user wants to print? "))  
  
# First two terms  
n_1 = 0  
n_2 = 1  
count = 0  
  
# Now, we will check if the number of terms is valid or not  
if n_terms <= 0:  
    print ("Please enter a positive integer, the given number is not valid")  
# if there is only one term, it will return n_1  
elif n_terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")  
    print(n_1)  
# Then we will generate Fibonacci sequence of number  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < n_terms:  
        print(n_1)  
        nth = n_1 + n_2  
       # At last, we will update values  
        n_1 = n_2  
        n_2 = nth  
        count += 1  

'''
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
'''