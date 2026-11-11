class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        maxMap = {}
        maxV = prices[-1]

        for i, price in enumerate(prices[::-1]):
            maxV = max(maxV, price)
            maxMap[len(prices) - (i+1)] = maxV

        maxP = 0

        for i, price in enumerate(prices):
            maxP = max(maxP, maxMap[i] - price)

        return maxP