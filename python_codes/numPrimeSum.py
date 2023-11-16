#Find the sum of first 'n' prime numbers .Also find the numbers

n = int(input("Enter value of n:"))
count = 0  # to count the number of prime numbers
s = 0  # to store the sum of prime numbers
num = 2  # starting from the first prime number

while count < n:
    c = 0
    for i in range(1, num + 1):
        if num % i == 0:
            c += 1
    if c == 2:
        print(num, end=' ')
        s += num
        count += 1
    num += 1

print("\nSum =", s)
