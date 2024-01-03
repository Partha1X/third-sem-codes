# Write a Shell Program of the Factorial of a Number 
echo -n "Enter a No: "
read n
f=1
for ((i=n; i>=1; i--))
do
    ((f=f*i))
done
echo "Factorial = $f"
