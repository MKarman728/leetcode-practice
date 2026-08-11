class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        total = 0
        while l < r:
            if heights[l] < heights[r]:
                total = max(total, heights[l]* (r - l))
                l += 1
            else:
                total = max(total, heights[r]*(r - l))
                r -= 1
        return total