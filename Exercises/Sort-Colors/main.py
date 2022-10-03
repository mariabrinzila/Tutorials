class Solution(object):
    def sort_colors(self, nums):
        """
        :param nums: the array of colors represented as numbers (0 for red, 1 for white and 2 for blue)
            that will be sorted so that objects of the same color are adjacent, with the colors in the
            order red, white, and blue (0, 1 and 2)
        :return: void (the array is sorted in-place)
        """
        # Data structure <=> Array and Hash Map
        # Algorithm <=> Counting Sort

        # Key <=> the number associated to the color (0, 1 or 2)
        # Value <=> the corresponding frequency of that color in the given array
        # Hash function <=> H(color) = frequency

        # Since the values that we will sort are 0, 1 and 2,
        # An efficient way of sorting the array is through counting sort
        # So basically traversing the given array and counting how many times each color appears

        # Time complexity <=> O(n + 3), where n is the size of the array
        # Space complexity <=> O(3)

        # Base case <=> the array only has one color in it
        if len(nums) == 1:
            return nums

        # For each element in the given array of colors:
        # If there already is a key in the hash map with that color's associated number:
        # Increment the frequency
        # Otherwise, add a key - value pair in the hash map, where the key is the color
        # And the value is frequency = 1
        hash_map = dict()
        n = len(nums)

        for i in range(n):
            if hash_map.get(nums[i]) is not None:
                hash_map[nums[i]] = hash_map[nums[i]] + 1
            else:
                hash_map[nums[i]] = 1

        # The sorted array will have each color as many times as its frequency in the hash map
        # For each possible color:
        # If it exists as a key in the hash map:
        # Change the part between start and end in the initial array
        # With the current color for the frequency in the hash map times
        start = 0
        end = 0

        for i in range(3):
            if hash_map.get(i) is not None:
                end += hash_map[i]
                nums[start:end] = [i] * hash_map[i]
                start += hash_map[i]


# Example 1
nums1 = [2, 0, 2, 1, 1, 0]
Solution().sort_colors(nums1)

print(nums1)
print("-------------------------------------")

# Example 2
nums1 = [2, 0, 1]
Solution().sort_colors(nums1)

print(nums1)
