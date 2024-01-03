# WAP to Check Whether a Given year is LeapYear or Not

echo -n "Enter a Year: "
read yr

if ((yr % 100 == 0)); then
    if ((yr % 400 == 0)); then
        echo "The Year $yr is a Leap Year."
    else
        echo "The Year $yr is Not a Leap Year."
    fi
else
    if ((yr % 4 == 0)); then
        echo "The Year $yr is a Leap Year."
    else
        echo "The Year $yr is Not a Leap Year."
    fi
fi
