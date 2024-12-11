#!/usr/bin/python3
"""
Module for the Prime Game
"""


def is_prime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a prime number, else False.
    """
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_numbers(start, end):
    """
    Returns a list of prime numbers within a range.

    Args:
        start (int): Start of the range.
        end (int): End of the range (inclusive).

    Returns:
        list: List of prime numbers in the range.
    """
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes


def isWinner(rounds, nums):
    """
    Determines the winner of the Prime Game.

    Args:
        rounds (int): Number of game rounds.
        nums (list): List of numbers for each round.

    Returns:
        str: Name of the player who won the most rounds.
             "Maria" or "Ben".
             None if there is no winner.
    """
    # Initialize the counts for Maria and Ben
    maria_count = 0
    ben_count = 0

    # Validate inputs
    if not nums or rounds < 1:
        return None

    for num in nums:
        # Generate the range and find primes within it
        range_numbers = list(range(1, num + 1))
        primes = prime_numbers(1, num)

        # If no primes, Ben wins the round
        if not primes:
            ben_count += 1
            continue

        maria_turn = True  # Flag to track whose turn it is

        # Continue the game until no primes remain
        while True:
            if not primes:
                # Update the winner based on the last turn
                if maria_turn:
                    ben_count += 1
                else:
                    maria_count += 1
                break

            # Remove the least prime number and its multiples
            least_prime = primes.pop(0)
            range_numbers.remove(least_prime)
            range_numbers = [
                x for x in range_numbers if x % least_prime != 0
            ]

            # Switch turns
            maria_turn = not maria_turn

    # Determine the overall winner
    if maria_count > ben_count:
        return "Maria"
    if ben_count > maria_count:
        return "Ben"
    return None
