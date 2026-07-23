from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini, maxi = 1, max(piles)
        result = maxi
        while mini <= maxi:
            speed = (mini + maxi) // 2
            hours = 0
            for num in piles:
                hours += ceil(num/speed)
            if hours <= h:
                result = speed
                maxi = speed - 1
            else:
                mini = speed + 1
        return result