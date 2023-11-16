#Find the sum of all even Numbers upto n terms

n=int(input("Enter no of terms :"))
count=0
s=0
num=1
while count<n:
    if num%2==0:
        print(num,end=' ')
        s=s+num
        count=count+1
    num=num+1
print("\nSum=",s)