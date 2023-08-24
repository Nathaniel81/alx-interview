#!/usr/bin/python3
"""
Test 0x08 Coin Change Problem
"""


def makeChange(coins, total):
    """
    makeChange implementation with greedy algorithm
    """
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total = total % coin

    if total != 0:
        return -1

    return num_coins
