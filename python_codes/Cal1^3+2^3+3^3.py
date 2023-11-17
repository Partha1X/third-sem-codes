# Calculate the sum of cubes 1^3 + 2^3 + 3^3 + ... up to n

n = int(input("Enter the value of n: "))

sum_of_cubes = sum(i**3 for i in range(1, n + 1))

print("Sum of cubes:", sum_of_cubes)
