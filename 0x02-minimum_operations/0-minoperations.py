#!/usr/bin/python3
""" Module defines a function that
 Calculates the fewest number of operations needed
 to result in exactly n H characters in the file"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed,
    or 0 if n is impossible to achieve.
    """
    if n <= 0:
        return 0

    operations = 0
    while n > 1:
        n //= 2
        operations += 1

    return operations
