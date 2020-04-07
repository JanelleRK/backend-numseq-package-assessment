__author__ = "Janelle Kuhns w/help from demo"

def primes(n):
    """
    Prime numbers
    """
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def is_prime(m):
    """
    Is prime number
    """
    if m == 2 or m == 3:
        return True
    if m % 2 == 0 or m < 2:
        return False
    for i in range(3, int(m ** 0.5) + 1, 2):
        if m % i == 0:
            return False
    return True

