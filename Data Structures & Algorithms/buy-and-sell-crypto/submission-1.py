class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' QUESTION
            1. what's the difference between sliding window and two pointer
        '''
        # sliding window  

        # To earn the best profit buy at the lowest price ; 
        profit, L = 0, 0

        # if L is smaller than the previous one, 
        for R in range(len(prices)) :
            if prices[L] > prices[R]:
                L = R
            profit = max(profit, prices[R]-prices[L])
        return profit


