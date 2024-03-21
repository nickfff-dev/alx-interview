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
    if n < 0:
        return 0

    currentSequence = 'H'
    nextSequence = 'H'
    operationCount = 0
    while (len(currentSequence) < n):
        if n % len(currentSequence) == 0:
            operationCount += 2
            nextSequence = currentSequence
            currentSequence += currentSequence
        else:
            operationCount += 1
            currentSequence += nextSequence

    if len(currentSequence) != n:
        return 0

    return operationCount
