class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix) - 1, len(matrix[0]) - 1
        # find the correct row
        t, b = 0, ROW
        row = 0
        while t < b:
            m = (t + b) // 2
            if matrix[m][0] <= target <= matrix[m][COL]:
                row = m
                break
            elif target >= matrix[m][COL]:
                t = m + 1
            else:
                b = m - 1
        l, r = 0, COL
        while l < r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                l = m + 1
            elif matrix[row][m] < target:
                r = m - 1
            else:
                return True
        return False