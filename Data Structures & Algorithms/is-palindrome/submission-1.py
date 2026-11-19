class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        half = 0
        even = 0
        for l in s:
            if l.isalnum():
                s2 += l.lower()
        print(len(s2))
        if len(s2) % 2 == 0:
            half = int(len(s2)/2)
            print(s2[-1:half-1:-1])
            print(s2[0:half:1])
            even = 0
            return s2[-1:half-1:-1] == s2[0:half:1]
        else:
            half = int(len(s2)/2)
            print(s2[-1:half+1:-1])
            print(s2[0:half-1:1])
            return s2[-1:half:-1] == s2[0:half:1]
        return s2[-1:half+even:-1] == s2[0:half+even:1]