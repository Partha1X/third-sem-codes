# Break Statement
for i in range(1, 10):
    print(i)
    if i == 5:  # Use '==' for comparison, not '=' which is for assignment
        break  # Terminate the loop when i equals 5

# continue Statement
for i in range(1, 10):
    if i == 5 or i == 7:
        continue  # Skips the rest of the loop body when i is 5 or 7
    print(i)

# Pass Statement
for i in range(1, 10):
    if i % 2 == 0:
        pass  # Do nothing and continue to the next iteration
    else:
        print(i)
