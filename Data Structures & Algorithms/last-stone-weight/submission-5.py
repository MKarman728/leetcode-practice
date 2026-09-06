class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        queue= [-stone for stone in stones]
        heapq.heapify(queue)
        while len(queue) > 1:
            x, y = -1*heapq.heappop(queue), -1*heapq.heappop(queue)
            if x > y:
                heapq.heappush(queue, -(x - y))
            elif x < y:
                heapq.heappush(queue, -(y - x))
        return -queue[0] if len(queue) == 1 else 0