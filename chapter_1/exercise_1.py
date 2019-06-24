from math import sqrt

def fib(n: int) -> float:
    """
    http://mathworld.wolfram.com/images/equations/FibonacciNumber/NumberedEquation6.gif
    """
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
