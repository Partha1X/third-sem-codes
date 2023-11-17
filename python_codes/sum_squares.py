# Sum of Squares of Consecutive Integers upto n(1^2+2^2+3^2+...n^2)

def sum_squares_consecutive_integers(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    result = sum_squares_consecutive_integers(n)
    print("Sum of squares of consecutive integers:", result)
