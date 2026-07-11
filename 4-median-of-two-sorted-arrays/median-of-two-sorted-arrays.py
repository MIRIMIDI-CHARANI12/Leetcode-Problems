class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        i = j = 0
        merged = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        while i < m:
            merged.append(nums1[i])
            i += 1
        while j < n:
            merged.append(nums2[j])
            j += 1

        total = m + n
        mid = total // 2
        if total % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2.0
        else:
            return float(merged[mid])
        