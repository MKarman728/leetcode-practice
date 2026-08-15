class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini, maxi = 1, max(piles)
        while mini < maxi:
            m = (maxi + mini) // 2
            speed_eaten = 0
            for num in piles:
                speed_eaten += math.ceil(num / m)
            if speed_eaten > h:
                mini = m + 1
            else:
                maxi = m
        return mini
            
