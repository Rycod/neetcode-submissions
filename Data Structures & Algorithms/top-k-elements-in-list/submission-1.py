class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        counts = []
        res = []
        for num in nums:
            seen[num] += 1
        for item in seen.items():
            counts.append((item[1], item[0]))
        counts.sort(reverse = True)
        for i in range(k):
            res.append(counts[i][1])
        return res