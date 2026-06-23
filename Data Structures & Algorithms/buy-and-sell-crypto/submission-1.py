class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = 0
        prevlowest = prices[cur]
        maxprofit = 0
        while cur < len(prices):
            profit = prices[cur] - prevlowest
            maxprofit = max(maxprofit,profit)
            prevlowest = min(prevlowest,prices[cur])
            cur+=1
        return maxprofit
        
                