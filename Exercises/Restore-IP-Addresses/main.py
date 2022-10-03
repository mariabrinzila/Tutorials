class Solution(object):
    def __init__(self):
        self.IP_addresses = []

    def restore_IP_addresses(self, s):
        """
        :param s: the string containing only digits that will be split in all possible IP addresses
            (an IP address is consists of exactly four integers separated by single dots, each integer
            is between 0 and 255 (inclusive) and cannot have leading zeros)
        :return: the array containing all possible IP addresses with the digits in the given string
            (their order can't be changed)
        """
        # Data structure <=> String, Array
        # Algorithm <=> Backtracking

        # We need to generate all possible IP addresses <=> backtracking
        # We need to pick 4 maximum 3 character long strings that are separated by .

        # Time complexity <=> O(n), where n is the size of the array
        # Space complexity <=> O(1)

        # Base case <=> s contains too many or too few digits (an IP address can have at most 12 digits
        # And at least 4 digits)
        # Or only contains 4 digits
        if len(s) == 4:
            solution = s[0] + '.' + s[1] + '.' + s[2] + '.' + s[3]
            return [solution]
        elif 4 > len(s) > 12:
            return []

        self.backtracking(s, 0, "")

        return self.IP_addresses

    def backtracking(self, s, position, solution):
        """
        :param s: the string containing only digits that will be split in all possible IP addresses
            (an IP address is consists of exactly four integers separated by single dots, each integer
            is between 0 and 255 (inclusive) and cannot have leading zeros)
        :param position: the current position we've reached in s
        :param solution: the current IP address solution
        :return: void
        """
        # Time complexity <=> O(n), where n is the size of the array
        # Space complexity <=> O(1)

        # Base case <=> we finished the given array
        n = len(s)

        if position == n:
            print(s[:(n - 1)])
            self.IP_addresses.append(s[:(n - 1)])

        # For each element in the given string, from current position on:
        # Pick one character, then 2, then 3 and see if it leads to a valid solution
        for i in range(position, n):
            if s[i] == "0":
                copy = s
                s = s[:(i + 1)] + '.' + s[(i + 1):]

                self.backtracking(s, position + 2, solution)
                s = copy
            elif int(s[i]) > 2 and s[i] != '.':
                if i + 1 < n:
                    copy = s
                    s = s[:(i + 2)] + '.' + s[(i + 2):]

                    self.backtracking(s, position + 3, solution)
                    s = copy

                copy = s
                s = s[:(i + 1)] + '.' + s[(i + 1):]

                self.backtracking(s, position + 2, solution)
                s = copy
            else:
                if i + 2 < n:
                    copy = s
                    s = s[:(i + 3)] + '.' + s[(i + 3):]

                    self.backtracking(s, position + 4, solution)
                    s = copy

                if i + 1 < n:
                    copy = s
                    s = s[:(i + 2)] + '.' + s[(i + 2):]

                    self.backtracking(s, position + 3, solution)
                    s = copy

                copy = s
                s = s[:(i + 1)] + '.' + s[(i + 1):]

                self.backtracking(s, position + 2, solution)
                s = copy

    def backtracking1(self, s, position, solution):
        """
        :param s: the string containing only digits that will be split in all possible IP addresses
            (an IP address is consists of exactly four integers separated by single dots, each integer
            is between 0 and 255 (inclusive) and cannot have leading zeros)
        :param position: the current position we've reached in s
        :param solution: the current IP address solution
        :return: void
        """
        # Time complexity <=> O(n), where n is the size of the array
        # Space complexity <=> O(1)

        # Base case <=> we finished the given array
        n = len(s)

        if position == n and self.valid_IP_address(solution, s):
            self.IP_addresses.append(solution[:(len(solution) - 1)])

        # For each element in the given string, from current position on:
        # Pick one character, then 2, then 3 and see if it leads to a valid solution
        for i in range(position, n):
            if s[i] == "0":
                solution_copy = solution
                solution += s[i] + "."

                self.backtracking(s, position + 1, solution)
                solution = solution_copy
            else:
                if i + 2 < n and int(s[i] + s[i + 1] + s[i + 2]) <= 255:
                    solution_copy = solution
                    solution += s[i] + s[i + 1] + s[i + 2] + "."

                    self.backtracking(s, position + 3, solution)

                    solution = solution_copy

                if i + 1 < n:
                    solution_copy = solution
                    solution += s[i] + s[i + 1] + "."

                    self.backtracking(s, position + 2, solution)

                    solution = solution_copy

                solution_copy = solution
                solution += s[i] + "."

                self.backtracking(s, position + 1, solution)

                solution = solution_copy

    def valid_IP_address(self, IP, s):
        """
        :param s: the string containing only digits that will be split in all possible IP addresses
            (an IP address is consists of exactly four integers separated by single dots, each integer
            is between 0 and 255 (inclusive) and cannot have leading zeros)
        :param IP: the IP address computed that may or may not be valid
        :return: True, if the IP address is valid and False, otherwise
        """
        # Time complexity <=> O(n), where n is the size of the string
        # Space complexity <=> O(4)

        # Split the IP by .
        numbers = IP.split(".")

        # Valid IP address <=> contains all digits in the given string, in the correct order
        # Base case <=> the size of all numbers doesn't add up to the size of the given string
        if len(numbers[0]) + len(numbers[1]) + len(numbers[2]) + len(numbers[3]) != len(s):
            return False

        # For each number:
        # For each digit in the current number:
        # If it doesn't match with the respective digit in the given string, the IP isn't valid
        index_s = 0

        for number in numbers:
            size = len(number)

            for i in range(size):
                if number[i] != s[index_s]:
                    return False

                index_s += 1

        return True


# Example 1
s1 = "25525511135"

print(Solution().restore_IP_addresses(s1))
print("-------------------------------------")
