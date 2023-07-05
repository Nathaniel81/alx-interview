#!/usr/bin/python3
"""
Doc
"""


def canUnlockAll(boxes):
    """Checks if all boxes can be opened"""
    keys = []
    length = len(boxes)
    idx = 0

    for i in boxes:
        for j in i:
            if j not in keys and j != 0 and j != idx:
                keys.append(j)
        idx += 1
    keys = sorted(keys)
    for k in range(1, length):
        if k != keys[k - 1]:
            return False
    return True
