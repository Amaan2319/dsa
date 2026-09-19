class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        profit = 0
        for d in range(0, len(prices)):
            if prices[d] < buy:
                buy = prices[d]
            curr_profit = prices[d] - buy
            if curr_profit > profit:
                profit = curr_profit
        return profit