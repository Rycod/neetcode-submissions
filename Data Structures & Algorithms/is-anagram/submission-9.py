class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss, st = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            ss[s[i]] += 1
            st[t[i]] += 1
        return ss == st 

            