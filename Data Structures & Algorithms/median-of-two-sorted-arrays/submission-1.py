class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(A) > len(B):
            A, B = B, A
        l1 = len(A)
        l2 = len(B)
        half = (l1 + l2) // 2
        l, r = 0, len(A)
        while l <= r:
            m = (l + r) // 2
            j = half - m
            left1 = float("-inf") if m == 0 else A[m - 1]
            right1 = float("inf") if m == l1 else A[m]
            left2 = float("-inf") if j == 0 else B[j - 1]
            right2 = float("inf") if j == l2 else B[j]
            if left1 <= right2 and left2 <= right1:
                if (l1 + l2) % 2 == 1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif right1 < left2:
                l = m + 1
            else:
                r = m - 1
        return -1

