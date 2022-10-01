class Solution(object):
    def find_median_sorted_arrays(self, nums1, nums2):
        """
        :param nums1: the first sorted array to be merged with the second array
        :param nums2: the second array
        :return: the median of the sorted merged array (if the merged array has an odd size, the median
            is the number in the middle and the sum of the 2 numbers in the middle divided by 2, otherwise)
        """
        # Data structure <=> Array
        # Algorithm <=> Merge Sort

        # We need to merge 2 sorted arrays <=> the merge part in merge sort
        # After having the sorted merged array, we can compute the median using the merged array's size

        # Time complexity <=> O(max), where max is the maximum between the size of the first array (m)
        # And the size of the second array (n)
        # Space complexity <=> O(m + n)

        # While none of the arrays are empty:
        # Pick the smallest element of the 2 current elements in the 2 arrays
        # Put the element in the merged array
        # Go further in the array the element belongs to
        # If one of the arrays is finished before the other one:
        # Add the remaining elements of the non-empty array to the merged array
        # Since we know both given arrays are sorted
        # At the end, if the size of the merged array is odd:
        # We have one number in the middle (on position size // 2)
        # So the median is this number divided by 1
        # Otherwise, we have 2 numbers in the middle (on positions size // 2 - 1 and size // 2)
        # So the median is the sum of the 2 numbers divided by 2
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        merged = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            elif nums2[j] < nums1[i]:
                merged.append(nums2[j])
                j += 1
            else:
                # Add the first element
                merged.append(nums1[i])
                i += 1

                # Add the second element
                merged.append(nums2[j])
                j += 1

        while i < m:
            merged.append(nums1[i])
            i += 1

        while j < n:
            merged.append(nums2[j])
            j += 1

        merged_size = len(merged)

        if merged_size % 2 == 1:
            return merged[merged_size // 2] / 1

        return (merged[merged_size // 2 - 1] + merged[merged_size // 2]) / 2


# Example 1
numbers1 = [1, 3]
numbers2 = [2]

print(Solution().find_median_sorted_arrays(numbers1, numbers2))
print("-------------------------------------")

# Example 2
numbers1 = [1, 2]
numbers2 = [3, 4]

print(Solution().find_median_sorted_arrays(numbers1, numbers2))
