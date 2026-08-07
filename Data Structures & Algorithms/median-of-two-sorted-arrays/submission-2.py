class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        if len(a) > len(b): 
            a, b = b, a
        total = len(a) + len(b)
        mid = total // 2
        lo, hi = 0, len(a)
        while lo <= hi:
            m = (lo + hi) // 2
            j = mid - m
            left1 = float("-inf") if m == 0 else a[m - 1]
            right1 = float("inf") if m == len(a) else a[m]
            left2 = float("-inf") if j == 0 else b[j - 1]
            right2 = float("inf") if j == len(b) else b[j]
            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                m = hi - 1
            else:
                m = lo + 1
        return -1