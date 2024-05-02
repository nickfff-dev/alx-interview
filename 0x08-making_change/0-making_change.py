#!/usr/bin/python3
"""This module provides a function to determine the fewest number of coins
needed to meet a given amount total."""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given amount
    total.

    Args:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount for which we need to find
    the fewest number of coins.

    Returns:
    int: The fewest number of coins needed to meet total.
    Returns -1 if total cannot be met by any number of coins.
    """
    coins.sort(reverse=True)  # Sort coins in descending order
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    return count if total == 0 else -1
