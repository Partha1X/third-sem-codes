# Find the Sum and product of Odd Digits of a Number

n = int(input("Enter a Number: "))
s = 0
m = 1

while n != 0:
    r = n % 10

    # Corrected the syntax for the if statement
    if r % 2 == 1:
        print(r, end=' ')
        s = s + r
        m = m * r

    n = n // 10

print("\nSum =", s)
print("Product =", m)
