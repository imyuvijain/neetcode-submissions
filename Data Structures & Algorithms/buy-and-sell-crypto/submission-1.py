class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        minV = prices[0]

        maxP = 0

        for i, price in enumerate(prices):
            minV = min(minV, price)
            
            maxP = max(price-minV, maxP)

        return maxP