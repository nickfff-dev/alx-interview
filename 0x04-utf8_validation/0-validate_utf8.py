#!/usr/bin/python3
"""
Module for validating UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Parameters:
    data (list): A list of integers, where each integer
    represents 1 byte of data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    n = len(data)
    i = 0
    while i < n:
        # Check the number of bytes in the current character
        if (data[i] >> 7) == 0:
            # 1-byte character
            i += 1
        elif (data[i] >> 5) == 0b110:
            # 2-byte character
            if i + 1 >= n or (data[i + 1] >> 6) != 0b10:
                return False
            i += 2
        elif (data[i] >> 4) == 0b1110:
            # 3-byte character
            if i + 2 >= n or (data[i + 1] >> 6) != 0b10 or \
                    (data[i + 2] >> 6) != 0b10:
                return False
            i += 3
        elif (data[i] >> 3) == 0b11110:
            # 4-byte character
            if i + 3 >= n or (data[i + 1] >> 6) != 0b10 or \
                    (data[i + 2] >> 6) != 0b10 or (data[i + 3] >> 6) != 0b10:
                return False
            i += 4
        else:
            # Invalid UTF-8 character
            return False
    return True
