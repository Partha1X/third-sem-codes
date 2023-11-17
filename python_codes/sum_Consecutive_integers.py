# Sum of Consecutive Integers upto n(1+2+3..n)

def sum_consecutive_integers(n):
    return (n * (n + 1)) // 2

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    result = sum_consecutive_integers(n)
    print("Sum of consecutive integers:", result)

