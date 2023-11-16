#1.a) Function to calculate HCF/GCD

def calculate_hcf(x, y):
    while y != 0:
        x, y = y, x % y
    return x

# Calculate LCM
def calculate_lcm(x, y):
    lcm = (x * y) // calculate_hcf(x, y)
    return lcm

# User Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and display HCF/GCD
hcf = calculate_hcf(num1, num2)
print("HCF/GCD of", num1, "and", num2, "is", hcf)

# Display LCM
lcm = calculate_lcm(num1, num2)
print("LCM of", num1, "and", num2, "is", lcm)
