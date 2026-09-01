class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap =[]
        for point in points:
            x, y = point
            d = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (d, [x,y]))
        res = []
        for i in range(k):
            _, c = heapq.heappop(heap)
            res.append(c)
        return res