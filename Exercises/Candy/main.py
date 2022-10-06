class Solution(object):
    def candy(self, ratings):
        """
        :param ratings: the array of children's ratings (children get at least one candy and children with
            a higher rating get more candies than their neighbors)
        :return: the minimum number of candies to be distributed to all children
        """
        # Data structure <=> Array
        # Algorithm <=> Greedy

        # We must have a minimum amount of candy
        # So we can at first consider we give each child one candy
        # And then increment the number of candy for the children with higher ratings than
        # Their neighbours <=> Greedy

        # Time complexity <=> O(n * 3), where n is the size of the array
        # Space complexity <=> O(n * 2)

        # Base case <=> there's only one rating in the array
        n = len(ratings)

        if n == 1:
            return 1

        # Compute the array containing the amount of candy for each child when going from left to right
        # And the array containing the amount of candy for each child when going from right to left
        # In the left to right traversal, we only consider the left neighbour of each child
        # In the right to left traversal, we only consider the right neighbour of each child
        # Initially all children receive one candy in both traversals
        left = [1 for _ in range(n)]
        right = [1 for _ in range(n)]

        # For each child's rating starting from the beginning of the array (the left to right traversal):
        # If the current child's rating is > its left neighbour:
        # Make its candy amount in the left to right traversal the candy amount of its left neighbour + 1
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # For each child's rating starting from the end of the array (the right to left traversal):
        # If the current child's rating is > its right neighbour:
        # Make its candy amount in the right to left traversal the candy amount of its right neighbour + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        # For each child:
        # The candy amount will be the maximum of the left to right traversal candy amount
        # And the right to left traversal candy amount
        minimum_amount = 0

        for i in range(n):
            minimum_amount += max(left[i], right[i])

        return minimum_amount

    def candy1(self, ratings):
        """
        :param ratings: the array of children ratings (children get at least one candy and children with
            a higher rating get more candies than their neighbors)
        :return: the minimum number of candies to be distributed to the children
        """
        # Data structure <=> Array
        # Algorithm <=> Greedy

        # We must have a minimum amount of candy
        # So we can at first consider we give each child one candy
        # And then increment the number of candy for the children with higher ratings than
        # Their neighbours <=> Greedy

        # Time complexity <=> O(n * n * n), where n is the size of the array
        # Space complexity <=> O(n)

        # Base case <=> there's only one rating in the array
        if len(ratings) == 1:
            return 1

        # Compute the array of predecessors where it's -1, if the candy for that child is 1
        # -2, if the candy for the child is the maximum of both its neighbours
        # And the element from which the amount of candy will be computed, otherwise
        n = len(ratings)
        pre = [1 for _ in range(n)]

        # For each rating:
        # If the current rating is > the previous rating, make the current child's predecessor the previous
        # One, since the amount of candy for the current child will be the amount of candy for the
        # Previous child + 1
        # If the current rating is > the next rating, make the current child's predecessor the next one
        # If the current rating is > both the previous and next onex:
        # Make the current child's predecessor -2
        for i in range(n):
            if i == 0:
                if ratings[i] > ratings[i + 1]:
                    pre[i] = i + 1
            elif i == n - 1:
                if ratings[i] > ratings[i - 1]:
                    pre[i] = i - 1
            else:
                if ratings[i] > ratings[i - 1] and ratings[i] > ratings[i + 1]:
                    pre[i] = -2
                else:
                    if ratings[i] > ratings[i - 1]:
                        pre[i] = i - 1
                    elif ratings[i] > ratings[i + 1]:
                        pre[i] = i + 1

        # For each element in the predecessor array:
        # If the current predecessor is -1, increment the minimum amount of candy by 1
        # Since the current child will receive one candy
        # If the current predecessor is -2:
        # Compute the amount of candy for both the predecessor of the current element
        # And the successor of the current element
        # And the amount of candy for the current element will be the maximum of these values + 1
        # Otherwise, go from one predecessor to the other until finding an element with -1
        # And keep incrementing the minimum amount of candy by 1 at each step
        minimum_amount = 0

        for i in range(n):
            if pre[i] == -1:
                minimum_amount += 1
            elif pre[i] == -2:
                previous = 1
                element = pre[i - 1]

                while element != -1:
                    element = pre[element]
                    previous += 1

                next = 1
                element = pre[i + 1]

                while element != -1:
                    element = pre[element]
                    next += 1

                minimum_amount += max(previous, next) + 1
            else:
                element = pre[i]

                while element != -1:
                    element = pre[element]
                    minimum_amount += 1

                minimum_amount += 1

        return minimum_amount


# Example 1
ratings1 = [1, 0, 2]

print(Solution().candy(ratings1))
print("-------------------------------------")

# Example 2
ratings1 = [1, 2, 2]

print(Solution().candy(ratings1))
print("-------------------------------------")

# Example 3
ratings1 = [1, 3, 4, 5, 2]

print(Solution().candy(ratings1))
