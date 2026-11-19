class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        curr = [0]*26
        total = defaultdict(list)
        for word in strs:
            curr = [0]*26
            for letter in word:
                curr[ord(letter) - ord('a')] += 1
            currT = tuple(curr)
            if currT in total:
                res[total[currT]].append(word)
            else:
                total[currT] = len(res)
                res.append([word])
        return res