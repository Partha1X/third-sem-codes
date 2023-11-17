# Calculate 1^2+2^2+3^2 if n>0; otherwise, it prints an error(PyQ2019)

n = int(input("Enter a positive integer: "))

if n > 0:
  s = 1**2 + 2**2 + 3**2
  print("Sum=",s)
else:
  print("Error: Please enter a positive integer.")
