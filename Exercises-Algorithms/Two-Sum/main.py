def two_sum(nums, target):
    # For each number, compute a pair (number, target - number)
    # If that pair is duplicated, it's a candidate for the numbers we're looking for
    # If both numbers are in nums, we found the pair we were looking for
    if len(nums) == 2:
        return [0, 1]

    pairs = []

    for number in nums:
        needed_value = target - number

        min_value = min(number, needed_value)
        max_value = max(number, needed_value)

        pair = [min_value, max_value]
        pairs.append(pair)

    new_pairs = []

    for pair in pairs:
        if pair not in new_pairs:
            new_pairs.append(pair)
        else:
            # The current pair is duplicated
            number1 = pair[0]
            number2 = pair[1]

            # Check if both numbers are in nums
            if number1 in nums and number2 in nums:
                i = nums.index(number1)
                j = nums.index(number2)

                if i == j:
                    # The number is duplicated
                    # Compute the other index (the last index of that number in nums)
                    j = len(nums) - nums[::-1].index(number2) - 1

                return [i, j]


numbers = [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1]
target_sum = 11
print(two_sum(numbers, target_sum))
