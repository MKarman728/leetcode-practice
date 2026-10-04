class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            d = ((x - 0)**2 + (y - 0)**2)**(1/2)
            heapq.heappush(heap, (d, (x, y)))
        res = []
        for _ in range(k):
            d, coords = heapq.heappop(heap)
            res.append(coords)
        return res
