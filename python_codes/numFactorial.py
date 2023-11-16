#24. Write a Python Program to Find the factorial of a Number 

#a>> uing for Loop :

n = int(input("Enter a Number: "))
f = 1
# Loop through the range from n to 1 (inclusive) in descending order
for i in range(n, 0, -1):
    # Multiply the current factorial value by the loop variable
    f = f * i
print("Factorial =", f)


#b>> using while Loop :

n = int(input("Enter a Number: "))
f = 1
# Initialize a loop variable to the entered number
i = n
# Continue looping while the loop variable is greater than or equal to 1
while i >= 1:
    # Multiply the current factorial value by the loop variable
    f = f * i
    # Decrement the loop variable
    i = i - 1
    # Output: Print the factorial at each step
    print("Factorial =", f)
