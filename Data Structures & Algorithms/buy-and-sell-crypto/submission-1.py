class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _max = 0
        _len = len(prices)
        if _len == 1:
            return 0

        l = 0
        for r in range(1, _len):
            profit = prices[r] - prices[l]
            _max = max(_max, profit)
            if prices[l] > prices[r]:
                l = r
        return _max