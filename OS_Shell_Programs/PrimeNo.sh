# WAP to Check Whether a Given Number is Prime or Not

echo -n "Enter a No: "
read number
count=0

for ((i=1; i<=$number; i++))
do
    if ((number % i == 0)); then
        ((count=count+1))
    fi
done

if ((count == 2)); then
    echo "The Number $number is Prime."
else
    echo "The Number $number is Not Prime."
fi
