class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        lowday = 0
        maxprofit = 0
        for i in range(len(prices)):
            price = prices[i]
            maxprofit = max(maxprofit, price - low)
            if price < low:
                low = price
                lowday = i
        return maxprofit
            