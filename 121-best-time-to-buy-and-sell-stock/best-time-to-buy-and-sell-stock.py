class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for curr_price in prices:
            if curr_price < min_price :
                min_price = curr_price
            profit = curr_price - min_price
            max_profit = max(max_profit,profit)
        return max_profit
            