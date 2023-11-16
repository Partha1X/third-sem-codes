#28.a) WAP to find of the sum of all digits of a Number 

n = int(input("Enter a Number:"))
s = 0

while n != 0:# Iterate through each digit of the number until it becomes 0
    r = n % 10# Extract the last digit of the number
    s = s + r# Add the current digit to the sum
    n = n // 10# Remove the last digit from the number
print("Sum =", s)