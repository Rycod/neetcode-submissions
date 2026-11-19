class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sm, tm = {}, {}
        for i in range(len(s)):
            if s[i] not in sm:
                sm[s[i]] = 0
            if t[i] not in tm:
                tm[t[i]] = 0
            sm[s[i]] += 1
            tm[t[i]] += 1
        return sm == tm