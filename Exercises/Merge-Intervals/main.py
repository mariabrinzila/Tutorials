class Solution(object):
    def __init__(self):
        # Define an array which will hold all the non-overlapping intervals
        self.solutions = []

    def merge(self, intervals):
        """
        :param intervals: the array of intervals that will be merged, if they overlap (each interval
            is an array containing 2 elements, the starting point and the end point of the interval)
        :return: the array of all non-overlapping intervals in the given array of intervals
        """
        # Data structure <=> Array

        # Time complexity <=> O(n), where n is the size of the array
        # Space complexity <=> O(n)

        # Sort the intervals by the starting point (O(n * log n) at best time complexity
        # And O(log n) at best space complexity)
        sorted_intervals = sorted(intervals, key=lambda item: item[0])

        # For each interval in the array of sorted intervals:
        # If the array of solutions is empty, simply add the interval in the array of solutions
        # And make the current interval in the solution equal to this interval
        # Otherwise:
        # If there's an overlap between the current interval
        # And the current interval in the solution:
        # Merge the 2 intervals
        # Otherwise, add the current interval in the array of solutions
        # And make the current interval in the solution equal to this interval
        for interval in sorted_intervals:
            if len(self.solutions) == 0:
                self.solutions.append(interval[:])
            else:
                if interval[0] == self.solutions[len(self.solutions) - 1][0] \
                        and interval[1] >= self.solutions[len(self.solutions) - 1][1]:
                    self.solutions[len(self.solutions) - 1][1] = interval[1]
                elif interval[0] > self.solutions[len(self.solutions) - 1][0] \
                        and interval[0] > self.solutions[len(self.solutions) - 1][1]:
                    self.solutions.append(interval[:])
                elif interval[0] > self.solutions[len(self.solutions) - 1][0] \
                        and interval[1] > self.solutions[len(self.solutions) - 1][1]:
                    self.solutions[len(self.solutions) - 1][1] = interval[1]

        return self.solutions


# Example 1
intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]

print(Solution().merge(intervals1))
print("-------------------------------------")

# Example 2
intervals1 = [[1, 4], [4, 5]]

print(Solution().merge(intervals1))
