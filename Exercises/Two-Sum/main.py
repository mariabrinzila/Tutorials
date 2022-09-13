class Solution(object):
    def two_sum(self, nums, target):
        """
        :param nums: the array of integers
        :param target: the target sum
        :return: the list of 2 indices of 2 numbers in the array that add up to target
        """
        # Data structure <=> hash map

        # Hash function <=> H(i) = target - i (the rest needed so that i + H(i) = target)

        # Time complexity <=> O(n), where n is the number of elements in the array
        # Space complexity <=> O(n)

        # For each number in the array:
        # Compute the remainder (the number that added with the current number equals the target sum)
        # Put the key - value pair in the hash map (key = remainder, value = current number)
        hash_map = dict()

        for number in nums:
            remainder = target - number
            hash_map[remainder] = number

        # For each number in the array:
        # If the remainder for it exists as a key in the hash map,
        # We've found the 2 numbers that add up to the target sum
        # Compute the remainder's index in the array
        # If its index in not the index of the current number,
        # Put the indices in an array and return it
        size = len(nums)

        for i in range(size):
            rest = hash_map.get(nums[i])

            if hash_map.get(rest) is not None:
                j = nums.index(rest)

                if j != i:
                    return [i, j]

    def two_sum_better(self, nums, target):
        """
        :param nums: the array of integers
        :param target: the target sum
        :return: the list of 2 indices of 2 numbers in the array that add up to target
        """
        # Data structure <=> Hash Map

        # H(x) = index(x) (key = x, value = H(x))

        # Time complexity <=> O(n), where n is the number of elements in the array
        # Space complexity <=> O(n)

        # For each element in the array:
        # If the complement already exists in the hash map, return the indices
        # Otherwise, put the current element in the array accordingly
        size = len(nums)
        hash_map = dict()

        for i in range(size):
            complement = target - nums[i]

            if hash_map.get(complement) is not None:
                j = hash_map[complement]

                if j != i:
                    return [i, j]

            hash_map[nums[i]] = i


# Example 1
numbers = [2, 7, 11, 15]
target_sum = 9
solution = Solution()

print(solution.two_sum(numbers, target_sum))
print(solution.two_sum_better(numbers, target_sum))
print("-------------------------------------")

# Example 2
numbers = [3, 2, 4]
target_sum = 6
solution = Solution()

print(solution.two_sum(numbers, target_sum))
print(solution.two_sum_better(numbers, target_sum))
print("-------------------------------------")

# Example 3
numbers = [3, 3]
target_sum = 6
solution = Solution()

print(solution.two_sum(numbers, target_sum))
print(solution.two_sum_better(numbers, target_sum))
print("-------------------------------------")
