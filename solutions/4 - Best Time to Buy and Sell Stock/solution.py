"""
Exercise: Best Time to Buy and Sell Stock
Difficulty: Easy
Time: 20 min
LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


# Time: O(n), Space: O(1), where n is the length of the prices array
def solution(prices):
    min_price, profit = float("inf"), 0
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit
