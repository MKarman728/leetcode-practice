class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            x2, y2 = points[i]
            d = math.sqrt((x2-0)**2 + (y2- 0)**2)
            heapq.heappush(heap, (d, [x2,y2]))
        res = []
        for _ in range(k):
            d, points = heapq.heappop(heap)
            res.append(points)
        return res