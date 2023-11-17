''' Geometric Series (Sum):
geometric series a+ar+ar^2+ar^3...
Here , 
'S' is the sum of the series
'a' is the first term
'r' is the common ratio
We have ,  infinite geometric series also
'''
'''
#The key difference is how the terms in the series are generated:

~In an arithmetic series, each term is obtained by adding a fixed number to the previous term.
~In a geometric series, each term is obtained by multiplying the previous term by a fixed number.
'''

def geometric_series_sum(a, r, n):
    return a * (1 - r**n) / (1 - r)

if __name__ == "__main__":
    a = float(input("Enter the first term (a): "))
    r = float(input("Enter the common ratio (r): "))
    n = int(input("Enter the number of terms (n): "))
    
    result = geometric_series_sum(a, r, n)
    
    print("Sum of the geometric series:", result)
