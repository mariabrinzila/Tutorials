class Solution(object):
    def __init__(self):
        # Define the map (dictionary) of key - value pairs
        # Key <=> the roman number
        # Value <=> the corresponding integer value
        self.int_roman_map = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
                              "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}

    def roman_to_int(self, s):
        """
        :param s: the string representing the roman number to be converted to an integer
        :return: the computed integer from the given roman number
        """
        # Data structures <=> string and map (dictionary)

        # Time complexity <=> O(n), where n is the size of the given string
        # Space complexity <=> O(1)

        # While there are still characters in the given string that haven't been considered:
        # If the current character isn't I, X or C:
        # Add the corresponding value to the integer solution and move up 1 position in the given string
        # Otherwise, look ahead at the next position
        # If it's one that could make a valid roman number (it exists in the map):
        # Add the corresponding value to the integer solution
        # Move up 2 positions in the given string
        integer_solution = 0
        size = len(s)
        i = 0

        while i < size:
            search = ""

            if (s[i] == 'I' or s[i] == 'X' or s[i] == 'C') and i + 1 < size:
                if self.int_roman_map.get(s[i] + s[i + 1]) is not None:
                    search = s[i] + s[i + 1]

            if search == "":
                integer_solution += self.int_roman_map[s[i]]
                i += 1
            else:
                integer_solution += self.int_roman_map[search]
                i += 2

        return integer_solution


# Example 1
s1 = "III"

print(Solution().roman_to_int(s1))
print("-------------------------------------")

# Example 2
s1 = "LVIII"

print(Solution().roman_to_int(s1))
print("-------------------------------------")

# Example 3
s1 = "MCMXCIV"

print(Solution().roman_to_int(s1))
print("-------------------------------------")

# Example 4
s1 = "MCDLXXVI"

print(Solution().roman_to_int(s1))
