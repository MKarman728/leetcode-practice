class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        l = sorted(d.items(), key = lambda x: -x[1])
        res = [l[i][0] for i in range(k)]
        return res