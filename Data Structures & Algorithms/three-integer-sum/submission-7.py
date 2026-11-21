class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if -num > 2*nums[-1]:
                continue
            # print('inside for')
            l, r = i+1, len(nums)-1
            target = -num
            while i < l < r and nums[r] >= 0:
                if nums[l]+nums[r] == target:
                    curr = [num, nums[l], nums[r]]
                    if curr not in res:
                        res.append(curr)
                    l += 1
                    r -= 1
                elif nums[l]+nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res
        
