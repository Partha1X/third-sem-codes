# Geometric Series (Sum):

def geometric_series_sum(a, r, n):
    return a * (1 - r**n) / (1 - r)

if __name__ == "__main__":
    a = float(input("Enter the first term (a): "))
    r = float(input("Enter the common ratio (r): "))
    n = int(input("Enter the number of terms (n): "))
    
    result = geometric_series_sum(a, r, n)
    
    print("Sum of the geometric series:", result)
