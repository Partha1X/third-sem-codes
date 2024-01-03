: <<COMMENT
Write a Shell Program to Check Whether a Given No is Even or Odd.
COMMENT

echo -n "Enter a No: "
read n

if ((n % 2 == 0)); then #if [ $((n % 2)) -eq 0 ];
    echo "The number is even."
else
    echo "The number is odd."
fi
