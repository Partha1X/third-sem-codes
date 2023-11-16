#WAP to print all the Numbers between 1 and 300 which are 'divisible by 5 and 7'

print("The Numbers divisible by 5 and 7 are:")
for i in range(1, 301):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=' ')