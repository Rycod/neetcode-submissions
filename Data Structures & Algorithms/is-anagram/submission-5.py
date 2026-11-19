class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm = {}
        for l in s:
            if not l in hm:
                hm[l] = 1
            else:
                hm[l] += 1
        for l in t:
            if not l in hm:
                return False
            else:
                hm[l] -= 1
                if (hm[l]<0):
                    return False
        return True