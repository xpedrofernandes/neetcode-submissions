class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maximum profit
        maxP = 0

        # initialize pointers left (buy), right (sell)
        buy, sell = 0, 1

        while sell < len(prices):
            # if profitable, determine the profit made and the max so far
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]     
                maxP = max(maxP, profit)
            # if not profitable, move the buy pointer to the sell position. if we only move it once, it will be higher the current buy price
            else:
                buy = sell
            sell += 1
        
        return maxP
            

        