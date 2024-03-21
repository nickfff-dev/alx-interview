#!/usr/bin/python3
""" Module defines a function that
 Calculates the fewest number of operations needed
 to result in exactly n H characters in the file"""


def minOperations(n: int) -> int:
    """
    Determines the minimum number of operations required to achieve exactly n
    'H' characters in the file.

    Parameters:
    n (int): The desired number of 'H' characters.

    Returns:
    int: The minimum number of operations needed, or 0 if n is
    impossible to achieve.
    """
    if n < 2:
        return 0
    ops = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                ops.append(i)
    return sum(ops)
