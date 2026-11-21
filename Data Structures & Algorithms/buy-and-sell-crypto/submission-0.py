class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _max = 0
        _len = len(prices)
        if _len == 1:
            return 0

        l, r = 0, 1
        while r < _len:
            profit = prices[r] - prices[l]
            _max = max(_max, profit)
            if prices[l] > prices[r]:
                l = r
            r += 1    
        return _max