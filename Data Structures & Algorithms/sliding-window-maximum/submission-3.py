import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        heap = []
        res = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        maxi, i = heap[0]
        res.append(-maxi)
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            left = r - k + 1
            while heap[0][1] < left:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res