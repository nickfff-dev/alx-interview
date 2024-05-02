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
    if total <= 0:
        return 0

    # Initialize dp list with a large number for all values up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins are needed to make change for 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
