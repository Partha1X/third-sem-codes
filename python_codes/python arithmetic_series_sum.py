''' Arithmetic Series (Sum):
s = n/2.(2a + (n - 1)d) '''
# Example = 1+3+5+7=16
'''Here , First term = 1 #User input
  Common Difference  = 2 #User input
    Number of Terms  = 4 #User input
sum of The Arithmatic Series= 16 #Result
'''

def arithmetic_series_sum(a, d, n):
    return (n / 2) * (2 * a + (n - 1) * d)

if __name__ == "__main__":
    a = float(input("Enter the first term (a): "))
    d = float(input("Enter the common difference (d): "))
    n = int(input("Enter the number of terms (n): "))
    
    result = arithmetic_series_sum(a, d, n)
    
    print("Sum of the arithmetic series:", result)
