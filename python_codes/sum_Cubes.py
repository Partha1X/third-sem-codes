# Sum of Cubes of Consecutive Integers Program upto n(1^3+2^3+3^3...+n^3)

def sum_cubes_consecutive_integers(n):
    return ((n * (n + 1)) // 2) ** 2

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    result = sum_cubes_consecutive_integers(n)
    print("Sum of cubes of consecutive integers:", result)
