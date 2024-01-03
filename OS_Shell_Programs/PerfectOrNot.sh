: <<COMMENT
 WAP to Check Whether a Number is Perfect or Not
 [ The sum of all positive divisors of a number,
   excluding the number itself,
   equals the original number(eg-1 + 2 + 4 + 7 + 14 = 28) ]
COMMENT


echo -n "Enter a Number: "
read n
s=0

for ((i=1; i<=n/2; i++))
do
    if ((n % i == 0)); then
        ((s = s + i))
    fi
done

if ((s == n)); then
    echo "The Number $n is Perfect"
else
    echo "The Number $n is not Perfect"
fi
