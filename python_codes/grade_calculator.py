#9.
'''WAP to calculate total marks, percentage and grade of a student. Marks obtained in each of the three subjects are to be input by the user. Assign grades according to the following criteria :
a. Grade A: Percentage >=80
b. Grade B: Percentage>=70 and <80
c. Grade C: Percentage>=60 and <70
d. Grade D: Percentage>=40 and <60
e. Grade E: Percentage<40

'''

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