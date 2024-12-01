#!/usr/bin/python3
"""
Change comes from within
"""


def make_change(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of the denominations of coins available.
        total (int): The target amount to achieve.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be met using the available coins.
    """
    current_sum = 0
    coin_count = 0

    if total < 1:
        return 0

    # Iterate through coins sorted in descending order
    for coin in sorted(coins, reverse=True):
        while current_sum + coin <= total:
            current_sum += coin
            coin_count += 1

    # If the total cannot be achieved, return -1
    if current_sum != total:
        return -1

    return coin_count
