class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 1
        for num in nums:
            if num - 1 in nums_set:
                continue
            current_value = num
            count = 1
            while current_value + 1 in nums_set:
                count+=1
                longest = max(longest, count)
                current_value += 1
        return longest

