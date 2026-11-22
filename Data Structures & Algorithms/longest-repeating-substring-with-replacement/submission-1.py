class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k or len(s) == 1:
            return len(s)
        freq = defaultdict(int)
        mf = 0
        longest = 0

        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            mf = max(mf, freq[s[r]])
            while r - l + 1 - mf > k:
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest
        
