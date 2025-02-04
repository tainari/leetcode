"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
Beats 100%
Difficulty: Medium
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = sell = prices[0]
        for price in prices[1:]:
            if price < sell:
                profit += sell - buy
                buy = sell = price
            if price > sell:
                sell = price
        profit += sell - buy
        return profit