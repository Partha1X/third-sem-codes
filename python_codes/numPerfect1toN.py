# Print all the Perfect Numbers between 1 to n

n = int(input("Enter value of n: "))
print("The Perfect Numbers Are: ")

for i in range(1, n + 1):
    s = 0
    for j in range(1, i):
        if i % j == 0:
            s = s + j

    if s == i:
        print(i, end=' ')
