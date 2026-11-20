class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_st = set(nums)
        seen = set()
        longest = 1

        for num in num_st:
            # print(count)
            if num-1 in num_st:
                continue
            else:
                count = 1
                while num+count in num_st:
                    count += 1
                longest = max(longest, count)

        # print(longest)
        return longest
