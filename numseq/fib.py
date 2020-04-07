__author__ = "Janelle Kuhns w/help from demo"



def fib(n):
    """
    Fibonacci numbers
    """
    fibs = [0, 1]
    for _ in range(2, n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs