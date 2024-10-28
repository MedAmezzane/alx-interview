#!/usr/bin/python3
"""
Module to determine if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validates if the provided data list represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing the data set to validate.

    Returns:
        bool: True if data is a valid UTF-8 encoding, otherwise False.
    """
    remaining_bytes = 0

    for byte in data:
        if remaining_bytes == 0:
            # Check the number of leading 1 bits to determine byte length
            if (byte >> 7) == 0b0:
                # 1-byte character (ASCII), continue to next byte
                continue
            elif (byte >> 5) == 0b110:
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3
            else:
                # Invalid UTF-8 starting byte
                return False
        else:
            # Check that this byte starts with '10'
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    # Ensure there are no leftover expected continuation bytes
    return remaining_bytes == 0
