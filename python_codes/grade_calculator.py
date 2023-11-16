#Input Marks From the Subjects
s1=float(input("Enter mark for Mathematics :"))
s2=float(input("Enter mark for Physics :"))
s3=float(input("Enter mark for Chemistry"))
#Calculate total marks
total=s1+s2+s3
#Calculate Percentage
percentage= (total/300)*100
#Assign grades based on Percentage
if percentage>=80:
    grade='A'
elif 70 <= percentage<80:
    grade='B'
elif 60 <= percentage <70:
    grade='C'
elif 40 <=percentage <60:
    grade='D'
else:
    grade='E'
#Display Results
print("Total Marks:",total)
print("Percentage:",percentage,"%")
print("Grade:",grade)