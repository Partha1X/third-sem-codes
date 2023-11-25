# Sequential Control Structure:
a = 10
b = 20
print("Sum:", a + b)


# Conditional Control Structure:
# 1. if Statement:
a = 10
if a > 5:
    print("a is Big")
    print("Outside if block")

# 2. if-else Statement:
a = 10
if a < 5:
    print("a is less than 5")
else:
    print("a is greater than 5")

# 3. if-elif Statement:
x = 0
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")


# Loop Control Structure:
# 1. While Loop:
#while loops are often used when you need to repeatedly execute code until a specific condition is met.
i = 1
while i < 5:
    print(i, end=" ")
    i = i + 1

# 2. For Loop:
#for loops are generally used when you have a known iterable to iterate over.
for i in range(1, 6):
    print(i, end=" ")
