#Check whether a Number is a perfect or Not 
'''
The divisors of 28 (excluding 28 itself) are 1, 2, 4, 7, and 14.
1+2+4+7+14=28
'''
n = int(input("Enter Number: "))
s = 0
for i in range(1, n):
    if n % i == 0:
        s = s + i
# The check for perfection should be outside the loop
if s == n:
    print("The Number %d is Perfect" % n)
else:
    print("The Number %d is Not Perfect" % n)
