class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowestPrice = 0
        highestProfit = 0

        for i, price in enumerate(prices):
            if price < prices[lowestPrice]:
                lowestPrice = i
            currentProfit = price - prices[lowestPrice]

            if currentProfit > highestProfit:
                highestProfit = currentProfit

        return highestProfit