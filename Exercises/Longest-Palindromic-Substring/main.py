class Solution(object):
    def longest_palindrome(self, s):
        """
        :param s: the string from which the longest palindromic substring will be computed
            (it only contains digits and English letters)
        :return: the longest palindromic substring of the given string
        """
        # Data structure <=> String
        # Algorithm <=> Dynamic Programming

        # P(i, j) = true, if s[i:j] is a palindrome and false, otherwise
        # P(i, j) = (P(i - 1, j + 1) and s[i] = s[j]) so the substring s[(i - 1):(j + 1)] is a palindrome
        # And the first and last characters coincide (for example ababa)
        # A palindrome mirrors around its center
        # There are 2 * n - 1 centers in a string of size n
        # As the center of a palindrome is between at least 2 letters

        # Time complexity <=> O(n * n), where n is the size of the string
        # Space complexity <=> O(1)

        # Base cases <=> s only has 1 character, s is in itself a palindrome or s is None
        n = len(s)

        if n < 1 or s is None:
            return ""

        if n == 1:
            return s

        if self.is_palindrome(s):
            return s

        # For every character in the string:
        # Take the current character as a substring and expand it as much as possible (if it's a palindrome)
        # Do the same for the substring containing the current character and the one after it
        # If the maximum of the 2 computed lengths for the 2 substrings is greater
        # Than the length of the current palindrome substring (it starts at start and ends at end + 1):
        # We've found a longer palindrome substring so
        # Compute its start and end indices
        start = end = 0

        for i in range(n - 1):
            size1 = self.expand_around_center(s, i, i)
            size2 = self.expand_around_center(s, i, i + 1)

            maximum_size = max(size1, size2)

            if maximum_size > end - start:
                start = i - (maximum_size - 1) // 2
                end = i + maximum_size // 2

        return s[start:(end + 1)]

    def expand_around_center(self, s, left, right):
        """
        :param s: the given string
        :param left: the index of the beginning of the substring we're trying to expand
        :param right: the index of the end of the substring we're trying to expand
        :return: the length of the computed expanded substring
        """
        # Time complexity <=> O(n), where n is the size of the string
        # Space complexity <=> O(1)

        # While the same character exists on both sides of the substring:
        # Expand the substring (add an element to the left and the right)
        n = len(s)

        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1

    def is_palindrome(self, substring):
        """
        :param substring: the substring of the string
        :return: True, if the substring is a palindrome and False, otherwise
        """
        # Time complexity <=> O(1)
        # Space complexity <=> O(1)

        # If the reversed substring is equal to the substring, the substring is a palindrome
        if substring[::-1] == substring:
            return True

        return False


# Example 1
initial_string = "babad"
solution = Solution()

print(solution.longest_palindrome(initial_string))
print("-------------------------------------")

# Example 2
initial_string = "cbbd"
solution = Solution()

print(solution.longest_palindrome(initial_string))
print("-------------------------------------")

# Example 3
initial_string = "bananas"
solution = Solution()

print(solution.longest_palindrome(initial_string))
