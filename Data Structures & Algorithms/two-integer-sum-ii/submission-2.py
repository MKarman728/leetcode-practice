class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(numbers):
            m = target - num
            if m in d:
                return [d[m], i + 1]
            else:
                d[num] = i + 1
        return [0, 0]
