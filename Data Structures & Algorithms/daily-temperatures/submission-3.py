class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        # Each item will be the idx and temp in the stack
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                idx, _ =stack.pop()
                res[idx] = i - idx
            stack.append((i, temp))
        return res