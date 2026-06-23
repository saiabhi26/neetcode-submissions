class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        maxprofit = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit > maxprofit:
                maxprofit = profit
            if profit < 0:
                buy = sell
            sell+=1
        return maxprofit
                