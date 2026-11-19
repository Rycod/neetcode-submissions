class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        ls = []
        for num in nums:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1
        for item in hm.items():
            ls.append([item[1], item[0]])
        ls.sort()
        res = []
        for i in range(k):
            res.append(ls[-i-1][1])
        return res