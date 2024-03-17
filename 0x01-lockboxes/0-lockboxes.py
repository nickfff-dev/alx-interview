#!/usr/bin/python3
""" module defines the lockboxes challenge """


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Parameters:
    boxes (list of lists): A list of lists
    where each list represents the keys in a box.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    # Create a set of unlocked boxes
    unlocked_boxes = set()
    # Start with the first box unlocked
    unlocked_boxes.add(0)

    def dfs(box):
        """
        Depth-first search to unlock all boxes.

        Parameters:
        box (int): The current box to unlock.

        Returns:
        bool: True if all boxes can be unlocked, else False.
        """
        for key in boxes[box]:
            if key not in unlocked_boxes:
                unlocked_boxes.add(key)
                if not dfs(key):
                    return False
        return True

    # Start DFS from the first box
    return dfs(0)
