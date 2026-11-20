class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        pre = pos = 1
        res = ln*[1]
        for i in range(ln):
            res[i] *= pre
            res[ln-1-i] *= pos
            pre *= nums[i]
            pos *= nums[ln-1-i]
        return res