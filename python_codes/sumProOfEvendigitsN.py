# Find the Sum and product of Even Digits of a Number
#Hint= if r%2==0:

n = int(input("Enter a Number: "))
sum_even = 0
product_even = 1

while n != 0:
    r = n % 10

    # Check if the digit is even
    if r % 2 == 0:
        print(r, end=' ')
        sum_even += r
        product_even *= r

    n = n // 10

print("\nSum of Even Digits =", sum_even)
print("Product of Even Digits =", product_even)
