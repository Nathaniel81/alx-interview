#!/usr/bin/python3
"""
Doc
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    pascal = []
    if n <= 0:
        return pascal

    for i in range(n):
        inner = []
        for j in range(i + 1):
            if j == 0 or j == i:
                inner.append(1)
                continue
            top_inner = pascal[i - 1]
            value = top_inner[j - 1] + top_inner[j]
            inner.append(value)

        pascal.append(inner)

    return pascal
