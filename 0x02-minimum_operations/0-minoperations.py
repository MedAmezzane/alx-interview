#!/usr/bin/python3
"""
Minimum operations Python challenge
"""


def minOperations(n):
    """
    Determines the minimum number of operations required to reach
    exactly n characters in a file, starting with a single character 'H'.
    The only operations allowed are 'Copy All' and 'Paste'.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed to achieve n 'H'
             characters, or 0 if n cannot be achieved.
    """

    if n <= 1:
        return 0

    current_chars = 1  # Current number of 'H' characters
    clipboard = 0      # Tracks the last copied number of characters
    operations_count = 0  # Total number of operations performed

    # Repeat operations until we reach exactly n characters
    while current_chars < n:
        # If current number of characters is a factor of n
        if n % current_chars == 0:
            clipboard = current_chars  # Copy current number of 'H's
            current_chars += clipboard  # Paste copied characters
            operations_count += 2  # Two operations: Copy and Paste
        else:
            # Only Paste the previously copied characters
            current_chars += clipboard
            operations_count += 1

    return operations_count
