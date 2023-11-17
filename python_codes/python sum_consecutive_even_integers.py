#Sum of Consecutive Even Integers Using Python(2+4+6=12)

def sum_consecutive_even_integers(n):
    return n * (n + 1)

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    result = sum_consecutive_even_integers(n)
    print("Sum of consecutive even integers:", result)


