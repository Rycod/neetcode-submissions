class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        _max = 0
        _cur = 0
        while l < r:
            l_h, r_h = heights[l], heights[r]
            _cur = min(l_h, r_h)*(r-l)
            _max = max(_max, _cur)
            if l_h < r_h:
                l += 1
            else:
                r -= 1
        return _max