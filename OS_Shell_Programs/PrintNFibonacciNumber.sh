# WAP to Print First n Fibonacci Numbers or Upto n Terms

echo -n "Enter Value for n: "
read n

a=0
b=1
echo -n "The Fibonacci Numbers are: $a $b"

for ((i=1; i<=n-2; i++))
do
    ((c=a+b))
    echo -n " $c"
    a=$b
    b=$c
done

echo
