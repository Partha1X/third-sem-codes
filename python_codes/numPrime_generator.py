#29. WAP to generate 'first n Prime Numbers' in Python

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Example usage:
n = int(input("Enter the value of n: "))
result = generate_primes(n)
print(f"The first {n} prime numbers are: {result}")
