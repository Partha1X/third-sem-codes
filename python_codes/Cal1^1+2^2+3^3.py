# Calculate s = 1^1 + 2^2 + 3^3 + 4^4 + ... up to n

n = int(input("Enter Number of Terms: "))
s = 0

for i in range(1, n + 1):
    s = s + i**i

print("Sum =", s)
