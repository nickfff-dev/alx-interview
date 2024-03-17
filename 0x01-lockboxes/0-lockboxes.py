#!/usr/bin/python3
""" module defines the lockboxes challenge """


def canUnlockAll(boxes):
    """
    function that Determines if all the boxes can be opened.
    """
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for box in range(1, len(boxes) - 1):
        checked_boxes = False
        for idx in range(len(boxes)):
            checked_boxes = box in boxes[idx] and box != idx
            if checked_boxes:
                break
        if checked_boxes is False:
            return checked_boxes
    return True
