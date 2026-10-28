class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        m = -1
        while t <= b:
            m = (t + b) // 2
            if matrix[m][0] <= target <= matrix[m][len(matrix[0])-1]:
                break
            elif target < matrix[m][0]:
                b = m - 1
            else:
                t = m + 1
        if m == -1:
            return False
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mr = (l + r) // 2
            if matrix[m][mr] == target:
                return True
            elif matrix[m][mr] < target:
                l = mr + 1
            else:
                r = mr - 1
        return False
