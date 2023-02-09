"""
Exercise: Coin Change
Difficulty: Medium
Time: 25 min
LeetCode: https://leetcode.com/problems/coin-change/
"""


# Time: O(n*m), Space: O(m), where n is the numer of amount of coins, and m the amount
def solution(coins, amount):
    min_coins = [0] + [float("inf")] * amount

    for val in range(1, amount + 1):
        for coin in coins:
            if coin <= val:
                min_coins[val] = min(min_coins[val], min_coins[val - coin] + 1)

    # No solution was found
    if min_coins[amount] == float("inf"):
        return -1

    return min_coins[amount]
