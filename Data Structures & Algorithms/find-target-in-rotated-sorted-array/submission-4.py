class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif (nums[l] <= target and target < nums[m]) or (nums[l] > nums[m] and nums[m] < target and nums[l] > target):
                r = m - 1
            else:
                l = m + 1
        return -1