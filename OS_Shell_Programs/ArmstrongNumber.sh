# WAP to Check Whether a Given Number is Armstrong or Not

echo -n "Enter a Number: "
read n
s=0
temp=$n

while ((n!=0)); do
    r=$((n%10))
    s=$((s+r*r*r))
    n=$((n/10))
done

if ((s==temp)); then
    echo "The Number $temp is Armstrong"
else
    echo "The Number $temp is Not Armstrong"
fi
