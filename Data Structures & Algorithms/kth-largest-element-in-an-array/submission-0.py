class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_negative = [-num for num in nums]
        heapq.heapify(nums_negative)
        for _ in range(k - 1):
            num = heapq.heappop(nums_negative)
        return -nums_negative[0]