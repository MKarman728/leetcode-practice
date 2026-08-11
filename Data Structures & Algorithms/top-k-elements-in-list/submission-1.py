from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counted_dict = Counter(nums)
        list_of_count = list(counted_dict.items())
        list_of_count.sort(key=lambda x:  -x[1])
        res = []
        for n in range(k):
            res.append(list_of_count[n][0])
        return res