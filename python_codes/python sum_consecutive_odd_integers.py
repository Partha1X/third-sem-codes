#Sum of Consecutive Odd Integers using Python(1+3+5=9)

def sum_consecutive_odd_integers(n):
    return n**2

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    result = sum_consecutive_odd_integers(n)
    print("Sum of consecutive odd integers:", result)
