class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        lmax, rmax = heights[l], heights[r]
        maxi = 0
        while l < r:
            height = min(lmax, rmax)
            maxi = max(maxi, height*(r - l))
            if heights[l] < heights[r]:
                l += 1
                lmax = max(lmax, heights[l])
            else:
                r -= 1
                rmax = max(rmax, heights[r])
        return maxi
            