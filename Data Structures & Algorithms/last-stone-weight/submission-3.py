class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [-x for x in stones]
        heapq.heapify(stones_heap)
        while len(stones_heap) > 1:
            x, y = -heapq.heappop(stones_heap), -heapq.heappop(stones_heap)
            if x != y:
                print(abs(x-y))
                heapq.heappush(stones_heap, -abs(x - y))
        if len(stones_heap) == 1:
            return -stones_heap[0]
        else:
            return 0


