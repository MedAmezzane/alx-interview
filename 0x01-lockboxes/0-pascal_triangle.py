#!/usr/bin/python3
"""
Lockboxes challenge
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Each box may contain keys to other boxes, and the goal
    is to figure out if it's possible to unlock all boxes
    starting from box 0.

    Args:
        boxes (list of lists): A list where each index represents a box
                               and the list at each index contains keys
                               to other boxes.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """

    total_boxes = len(boxes)  # Number of total boxes
    unlocked_boxes = set()  # Set to track unlocked boxes

    # Iterate through each box
    for index, box in enumerate(boxes):
        # Box 0 or empty boxes are considered unlocked
        if len(box) == 0 or index == 0:
            unlocked_boxes.add(index)

        # Iterate through keys in the current box
        for key in box:
            # Add to unlocked set if key is valid and not the current box
            if key < total_boxes and key != index:
                unlocked_boxes.add(key)

    # Check if all boxes have been unlocked
    return len(unlocked_boxes) == total_boxes
