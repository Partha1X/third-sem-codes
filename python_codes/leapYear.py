#1.b) Check Whether a given Year is a Leap Year or not(16.11.2023)

yr = int (input("Enter a Year :"))
if yr%100==0:
    if yr%400==0:
        print("The Year %d is a Leap Year"%yr)
    else:
        print("The Year %d is Not a Leap Year"%yr)
else:
    if yr%4==0:
        print("The Year %d is a Leap Year"%yr)
    else:
        print("The Year %d is not a Leap Year"%yr)