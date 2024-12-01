#!/usr/bin/python3
"""
Module containing the make_change function.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to achieve a given total.

    Args:
        coins (list): A list of the denominations of coins available.
        total (int): The target amount to achieve.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be met using the available coins.
    """
    if not coins:
        return -1
    if total <= 0:
        return 0

    coin_count = 0
    coins = sorted(coins, reverse=True)  # Sort coins in descending order

    for coin in coins:
        while coin <= total:
            total -= coin
            coin_count += 1

        if total == 0:
            return coin_count

    return -1
