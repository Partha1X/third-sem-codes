# Print all the Prime Numbers Between 1 and Number

echo -n "Enter a Value of n: "
read n
echo -n "The Prime Numbers are: "

for ((i=2; i<=n; i++)); do
    c=0

    for ((j=1; j<=i; j++)); do
        if ((i % j == 0)); then
            ((c=c+1))
        fi
    done

    if ((c==2)); then
        echo -n "$i "
    fi
done

echo ""  # Adding a new line for better formatting
