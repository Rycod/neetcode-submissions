class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsCompliment = nums[:]
        for i in range(len(nums)):
            nums[i] = target - nums[i]
        indexes = []
        for i in range(len(nums)):
            if nums[i] in (numsCompliment[:i] + numsCompliment[i+1:]):
                    indexes.append(i)
        return indexes
