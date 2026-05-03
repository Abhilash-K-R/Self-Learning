# 121. Best Time to Buy and Sell Stock

def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        sell = 0
        res = 0

        for i in range(1,len(prices)) :
            buy = min(buy , prices[i])
            res = max(res , prices[i] - buy)
        return res

''' Input: prices = [7,1,5,3,6,4]
Output: 5 '''
