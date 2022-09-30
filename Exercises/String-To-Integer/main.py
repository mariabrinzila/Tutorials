class Solution(object):
    def __init__(self):
        # Define an upper and lower limit for a 32-bit signed integer
        self.upper_limit = 2 ** 31 - 1
        self.lower_limit = 2 ** 31 * (-1)

    def my_atoi(self, s):
        """
        :param s: the string to be turned into a signed integer containing English letters (upper and
            lower case), space, +, -, . and digits
        :return: the signed integer which the string was converted to
        """
        # Data structure <=> String

        # Time complexity <=> O(n), where n is the size of the string
        # Space complexity <=> O(1)

        # For each character in the string:
        # If the current character is a space and there haven't been any other characters, ignore it
        # If the current character is a + / -, the integer will have the sign + / -
        # If the string doesn't contain + / -, the integer will have the sign + by default
        # If the string is already signed (there has already been a + / - sign),
        # The following + / - is considered a letter, so return 0
        # If the current character is a digit, compute the integer
        # If the current character is a letter:
        # If there hasn't been a digit so far, return 0, otherwise, return the computed integer
        # If the computed integer isn't between -2 ^ 31 and 2 ^ 31 - 1:
        # It'll either be -2 ^ 31 (if the integer's sign is -), or 2 ^ 31 - 1
        digits = "0123456789"
        integer = 0
        sign = 1
        signed = False
        n = len(s)

        for i in range(n):
            character = s[i]

            if character == ' ' and not signed and integer == 0:
                continue
            elif character == '+' and not signed:
                signed = True
            elif character == '-' and not signed:
                sign = -1
                signed = True
            elif character not in digits and integer == 0:
                return 0
            elif character in digits:
                for j in range(i, n):
                    if s[j] not in digits:
                        return integer

                    if integer == 0:
                        integer = (integer * 10 + int(s[j])) * sign
                    else:
                        if sign == 1:
                            integer = integer * 10 + int(s[j])
                        else:
                            integer = integer * 10 - int(s[j])

                    if integer < self.lower_limit:
                        return self.lower_limit
                    elif integer > self.upper_limit:
                        return self.upper_limit

                # If after the digits, s is done, return the integer
                return integer

        # If the integer doesn't contain any digits, return 0
        return integer


# Example 1
s1 = "-42"

print(Solution().my_atoi(s1))
print("-------------------------------------")

# Example 2
s1 = "words and 987"

print(Solution().my_atoi(s1))
print("-------------------------------------")

# Example 3
s1 = "4193 with words"

print(Solution().my_atoi(s1))
print("-------------------------------------")

# Example 4
s1 = "   -2147483648  dfs"

print(Solution().my_atoi(s1))
print("-------------------------------------")

# Example 5
s1 = "2147483647123"

print(Solution().my_atoi(s1))
print("-------------------------------------")

# Example 6
s1 = "  +  413"

print(Solution().my_atoi(s1))
