class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for num in nums:
            duplicates[num] = duplicates.get(num, 0) + 1
            if duplicates[num] > 1:
                return True
        return False