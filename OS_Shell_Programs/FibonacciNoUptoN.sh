# WAP to Print all The Fibonacci Numbers Between 1 to n (or Upto n)

echo -n "Enter a Value of n: "
read n

a=0
b=1

echo -n "The Fibonacci Numbers are: $a $b "

while ((c < n))
do
    echo -n " $c"
    ((a=b))
    ((b=c))
    ((c=a+b))
done

echo
