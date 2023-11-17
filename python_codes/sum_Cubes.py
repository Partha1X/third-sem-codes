# Sum of Cubes of Consecutive Integers Program upto n

def sum_cubes_consecutive_integers(n):
    return ((n * (n + 1)) // 2) ** 2

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    result = sum_cubes_consecutive_integers(n)
    print("Sum of cubes of consecutive integers:", result)
