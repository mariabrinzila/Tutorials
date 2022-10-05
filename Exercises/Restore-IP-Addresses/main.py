class Solution(object):
    def __init__(self):
        # Define an array of all the valid IP addresses from the given string
        self.IP_addresses = []

    def restore_IP_addresses(self, s):
        """
        :param s: the string containing only digits that will be split in all possible IP addresses
            (an IP address consists of exactly four integers separated by single dots, each integer
            is between 0 and 255 (inclusive) and cannot have leading zeros)
        :return: the array containing all possible IP addresses with the digits in the given string
            (their order can't be changed)
        """
        # Data structure <=> String, Array
        # Algorithm <=> Backtracking

        # We need to generate all possible IP addresses <=> backtracking
        # We need to pick 4 maximum 3 character long strings that will be separated by .

        # Time complexity <=> O(n * (n / 2) * (n / 3) ^ 4), where n is the size of the array
        # Space complexity <=> O(size * (n + 3)), where size is the number of valid IP addresses created

        # Base case <=> the given string contains too many or too few digits
        # An IP address can have at most 12 digits and at least 4 digits
        # Or the given string only contains 4 digits
        if len(s) == 4:
            solution = s[0] + '.' + s[1] + '.' + s[2] + '.' + s[3]
            return [solution]
        elif len(s) < 4 or len(s) > 12:
            return []

        self.backtracking(s, 0, "")

        return self.IP_addresses

    def backtracking(self, s, segment_number, solution):
        """
        :param s: the current string containing only digits that will be split in all possible IP addresses
            (an IP address is consists of exactly four integers separated by single dots, each integer
            is between 0 and 255 (inclusive) and cannot have leading zeros)
        :param segment_number: the current number of segments in the current solution (a segment is
            a number before a dot)
        :param solution: the current IP address solution
        :return: void
        """
        # Time complexity <=> O(n * (n / 2) * (n / 3) ^ 4), where n is the size of the array
        # Space complexity <=> O(size * (n + 3)), where size is the number of valid IP addresses created

        # If the segment number is > 4, backtrack
        # If the segment number is equal to 4 and the whole given string has been traversed:
        # We've found a new IP address solution, so add it to the array of solutions
        # Otherwise (the segment number is < 4):
        # For each character in the current string s:
        # If we've found a 0 or a character / group of characters between 1 and 255:
        # We've found a valid number for the current segment
        # So go from that point and look for a number for the next segment in the current solution
        # If the current character / group of characters doesn't lead to a valid IP address:
        # Backtrack and try to find another number for that segment
        if segment_number > 4:
            return

        if segment_number == 4 and not s:
            self.IP_addresses.append(solution[:-1])
            return

        n = len(s)

        for i in range(1, n + 1):
            if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) <= 255):
                self.backtracking(s[i:], segment_number + 1, solution + s[:i] + '.')


# Example 1
s1 = "25525511135"

print(Solution().restore_IP_addresses(s1))
print("-------------------------------------")

# Example 2
s1 = "101023"

print(Solution().restore_IP_addresses(s1))
print("-------------------------------------")

# Example 3
s1 = "0000"

print(Solution().restore_IP_addresses(s1))
