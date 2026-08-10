class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        minPrice = 101
        for price in prices:
            minPrice = min(minPrice, price)
            maxPrice = max(maxPrice, price - minPrice)
        return maxPrice