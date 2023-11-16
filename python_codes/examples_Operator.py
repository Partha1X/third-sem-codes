#1. Arithmetic Operators
a = 5
b = 2
result_addition = a + b
result_subtraction = a - b
result_multiplication = a * b
result_division = a / b
result_modulus = a % b
result_exponentiation = a ** b

#2. Comparison (Relational) Operators
x = 5
y = 10
result_equal = x == y
result_not_equal = x != y
result_greater_than = x > y
result_less_than = x < y
result_greater_equal = x >= y
result_less_equal = x <= y

#3. Logical Operators
p = True
q = False
result_and = p and q
result_or = p or q
result_not = not p

#4. Assignment Operators
c = 5
c += 2  # Equivalent to c = c + 2
c -= 1  # Equivalent to c = c - 1
c *= 3  # Equivalent to c = c * 3
c /= 2  # Equivalent to c = c / 2

#5. Bitwise Operators
x = 5
y = 3
result_and_bitwise = x & y
result_or_bitwise = x | y
result_xor_bitwise = x ^ y
result_not_bitwise = ~x
result_left_shift = x << 1
result_right_shift = x >> 1

#6. Membership Operators
fruits = ['apple', 'banana', 'orange']
fruit_to_check = 'banana'
result_membership = fruit_to_check in fruits  # True if fruit_to_check is in fruits

#7. Identity Operators
x = 5
y = 5
result_identity_equal = x is y  # True if x is the same object as y
result_identity_not_equal = x is not y  # True if x is not the same object as y

# Displaying results
print("Arithmetic Operators:")
print("Addition:", result_addition)
print("Subtraction:", result_subtraction)
print("Multiplication:", result_multiplication)
print("Division:", result_division)
print("Modulus:", result_modulus)
print("Exponentiation:", result_exponentiation)

print("\nComparison (Relational) Operators:")
print("Equal to:", result_equal)
print("Not equal to:", result_not_equal)
print("Greater than:", result_greater_than)
print("Less than:", result_less_than)
print("Greater than or equal to:", result_greater_equal)
print("Less than or equal to:", result_less_equal)

print("\nLogical Operators:")
print("Logical AND:", result_and)
print("Logical OR:", result_or)
print("Logical NOT:", result_not)

print("\nAssignment Operators:")
print("Add and Assign:", c)

print("\nBitwise Operators:")
print("Bitwise AND:", result_and_bitwise)
print("Bitwise OR:", result_or_bitwise)
print("Bitwise XOR:", result_xor_bitwise)
print("Bitwise NOT:", result_not_bitwise)
print("Left Shift:", result_left_shift)
print("Right Shift:", result_right_shift)

print("\nMembership Operators:")
print(f"{fruit_to_check} is in fruits:", result_membership)

print("\nIdentity Operators:")
print("Identity Equal:", result_identity_equal)
print("Identity Not Equal:", result_identity_not_equal)
