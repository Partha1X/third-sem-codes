# Calculate s = 1 + (1 + 2) + (1 + 2 + 3) + ... up to n

n = int(input("Enter Number of Terms: "))
s = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        s = s + j

print("Sum =", s)
