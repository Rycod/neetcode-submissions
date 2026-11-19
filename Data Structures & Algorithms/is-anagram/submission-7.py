class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = defaultdict(int)
        for l in s:
            seen[l] += 1
        for l in t:
            if l not in seen:
                return False
            seen[l] -= 1
            if seen[l] < 0:
                return False
        for elem in seen:
            if seen[elem] != 0:
                return False
        return True