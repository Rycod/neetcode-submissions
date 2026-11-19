class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1
        l = 0
        r = len(nums) - 1
        m = (l+r)//2
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if target >= nums[m] >= nums[r]:
                l = m + 1
                continue
            if nums[r] >= target >= nums[m]:
                l = m + 1
                continue
            if nums[m] >= nums[r] >= target:
                l = m + 1
                continue
            r = m - 1
        return -1


