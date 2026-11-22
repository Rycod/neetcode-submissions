class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= k or len(s) == 1:
            return len(s)
        freq = 26*[0]
        mf = 0
        # longest = 0

        l = 0
        for r, c in enumerate(s):
            i = ord(c)-65
            freq[i] += 1
            mf = max(mf, freq[i])
            if r - l - mf > k-1:
                freq[ord(s[l])-65] -= 1
                l += 1
            # longest = max(longest, r-l+1)
        return len(s) - l
        
