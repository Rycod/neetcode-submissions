class Solution:

    def encode(self, strs: List[str]) -> str:
        delims = []
        pre = ''
        for i, word in enumerate(strs):
            delims.append(str(len(word)) + ',')
        pre = "".join(delims) + '@'
        # print(delims)
        return(pre + "".join(strs))

    def decode(self, s: str) -> List[str]:
        delims = []
        res = []
        cutout = 0
        csum = 0
        for i, c in enumerate(s):
            if c == '@':
                cutout = i+1
                break
            if c <= '9' and c >= '0':
                csum = csum*10 + int(c)
            if c == ',':
                delims.append(csum)
                csum = 0
        
        s = s[cutout:]
        cutout = 0
        for delim in delims:
            word = s[cutout:cutout+delim]
            cutout += delim
            res.append(word)
        # print(res)
        return res