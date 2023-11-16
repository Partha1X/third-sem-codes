#16. WAP to print all Prime Numbers between 1 and n
#(numbers having only two factors,1 & itsself)

n = int(input("Enter The Upper Limit: "))
print("The Prime Numbers are:")
for i in range(1, n + 1): # Loop through numbers from 1 to n (inclusive)
    c = 0 # Initialize a counter for factors of the current number i
    for j in range(1, i + 1): # Check for factors of i by looping through numbers from 1 to i (inclusive)
        if i % j == 0: # If j is a factor of i, increment the counter c
            c = c + 1
    if c == 2: # If the counter c is 2, the number i is prime (it has only two factors: 1 and itself)
        print(i, end=' ') # Print the prime number i, end with a space

