class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        #Handling No Negatives/Positives Cases
        if nums[0] >= 0:
            if nums[2] == 0:
                return [[0,0,0]]
            else:
                return []
        if nums[-1] <= 0:
            if nums[-3] == 0:
                return [[0,0,0]]
            else:
                return []
        
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if -num > 2*nums[-1] or i > 0 and nums[i] == nums[i-1]:
                continue
            # print('inside for')
            l, r = i+1, len(nums)-1
            target = -num
            while l < r and nums[r] >= 0:
                if nums[l]+nums[r] == target:
                    curr = [num, nums[l], nums[r]]
                    res.append(curr)
                    left = target - nums[r]
                    right = target - nums[l]
                    while nums[l] == left and l < r:
                        l += 1
                    while nums[r] == right and l < r:
                        r -= 1
                while nums[l]+nums[r] < target and l < r:
                    l += 1
                while nums[l]+nums[r] > target and l < r and nums[r] >= 0:
                    r -= 1
        return res
        
