#8. Loop Example in Python 

#1. While Loop:
i=1
while(i<=5):
    print(i,end=" ")
    i=i+1

#2. For Loop:
for i in range(1,6):
    print(i,end=" ")

#3. Nested Loops
even_list = []

for item in range(1, 11):
    if item % 2 == 0:
        even_list.append(item)

print("Even Numbers:", even_list)

