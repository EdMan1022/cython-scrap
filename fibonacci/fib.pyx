from __future__ import print_function

def fib(n: int):
    """
    Prints the Fibonacci series up to n

    :param n: (int) Stopping point for printing the series
    :return: None
    """
    a = 0
    b = 1

    while b < n:
        print(b, end=' ')
        a = b
        b = a + b

    print()
