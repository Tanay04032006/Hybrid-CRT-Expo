import math

def mod_expo(a, b, m):
    """Computes (a^b) % m using Exponentiation by Squaring."""
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:  # If b is odd
            result = (result * a) % m
        a = (a * a) % m
        b //= 2  # Integer division
    return result

def extended_gcd(a, b):
    """Computes the Greatest Common Divisor (GCD) and modular coefficients."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    """Finds the modular inverse of a modulo m using Extended Euclidean Algorithm."""
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist for {a} mod {m}")
    return x % m

def find_two_prime_factors(n):
    """Finds two distinct prime factors of n (assuming n is a product of two primes)."""
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and is_prime(i):
            q = n // i
            if is_prime(q):
                return i, q
    raise ValueError("The given modulus m is not a product of two primes.")

def is_prime(num):
    """Checks if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def chinese_remainder(x_p, x_q, p, q):
    """Combines results using the Chinese Remainder Theorem (CRT)."""
    m1, m2 = q, p
    inv1 = mod_inverse(m1, p)
    inv2 = mod_inverse(m2, q)
    
    x = (x_p * m1 * inv1 + x_q * m2 * inv2) % (p * q)
    return x

def hybrid_crt_expo(a, b, m):
    """Computes (a^b) % m using the Hybrid Chinese Remainder Theorem method."""
    # Step 1: Factorize m into two coprimes (assumes m is a product of two primes)
    p, q = find_two_prime_factors(m)

    # Step 2: Compute x_p = a^b mod p
    x_p = mod_expo(a, b, p)

    # Step 3: Compute x_q = a^b mod q
    x_q = mod_expo(a, b, q)

    # Step 4: Combine using CRT
    return chinese_remainder(x_p, x_q, p, q)

# Example usage:
a, b, m = 3, 200, 55  # Example values
result = hybrid_crt_expo(a, b, m)
print(f"Result: {result}")  # Output: (3^200) % 55
