class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            minPrice = min(price,minPrice)

            profit = price - minPrice

            maxProfit = max(maxProfit, profit)
        
        return maxProfit
  

        
