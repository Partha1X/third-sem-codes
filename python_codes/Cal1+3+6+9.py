# Calculate s = 1 + 3 + 6 + 9 + ... up to n

n = int(input("Enter Number of Terms: "))
p = 1
c = 1
s = 0

while c <= n:
    s = s + p
    c = c + 1
    p = p + c

print("Sum =", s)
