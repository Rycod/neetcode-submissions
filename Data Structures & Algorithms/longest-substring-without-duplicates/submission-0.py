class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        l = longest = curr = 0
        s_l = len(s)
        if s_l <= 1:
            return s_l
        for r in range(s_l):
            count[s[r]] += 1
            curr += 1
            while count[s[r]] > 1:
                count[s[l]] -= 1
                curr -= 1
                l += 1
            longest = max(longest, curr)
        return longest
        
        