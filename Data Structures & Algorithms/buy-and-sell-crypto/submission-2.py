class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        minBuy = prices[0]

        for price in prices[1:]:
            if price-minBuy > maxProf:
                maxProf = price-minBuy
            if price < minBuy:
                minBuy = price
        return maxProf