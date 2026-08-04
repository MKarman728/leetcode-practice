class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left_1 = 0
        left_2 = 0
        end_1 = len(nums1) - 1
        end_2 = len(nums2) - 1
        merged_array = []
        while left_1 <= end_1 and left_2 <= end_2:
            if nums1[left_1] <= nums2[left_2]:
                merged_array.append(nums1[left_1])
                left_1 += 1
            else:
                merged_array.append(nums2[left_2])
                left_2 += 1
        if left_1 > end_1:
            merged_array = merged_array + nums2[left_2:]
        else:
            merged_array = merged_array + nums1[left_1:]
        l, r = 0, len(merged_array) - 1
        m = (l + r) // 2
        if len(merged_array) % 2 != 0:
            return merged_array[m]
        else:
            return (merged_array[m] + merged_array[m + 1]) / 2

