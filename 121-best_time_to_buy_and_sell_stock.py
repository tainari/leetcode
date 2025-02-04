"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Beats 99.76%
Difficulty: Easy
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < buy:
                max_profit = max(max_profit, sell - buy)
                buy = sell = price
            if price > sell:
                sell = price
        max_profit = max(max_profit, sell - buy)
        return max_profit