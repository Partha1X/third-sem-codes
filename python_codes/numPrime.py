#4. WAP to Check whether a No is Prime or not (16.11.2023)

n = int(input("Enter a Number: "))
c = 0

# Loop should start from 1 instead of 'i'
for i in range(1, n + 1):
    if n % i == 0:
        c = c + 1

# Changed the condition to check if 'c' is equal to 2
if c == 2:
    print("The Number %d is a prime Number" % n)
else:
    print("The Number %d is Not a prime Number" % n)
