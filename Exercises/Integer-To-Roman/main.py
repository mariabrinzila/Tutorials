class Solution(object):
    def __init__(self):
        # Define an array of tuples (integer, roman number) to map the transformation between the 2 types
        self.int_roman_list = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
                               (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

    def int_to_roman(self, num):
        """
        :param num: the number that will be converted to a roman number
        :return: the computed roman number from the given number
        """
        # Data structures <=> String and Array

        # Time complexity <=> O(13)
        # Space complexity <=> O(13)

        # While there are still tuples in the integer - roman array that haven't been considered:
        # If the given number is 0, return the solution
        # If the result of the given number - the current number value >= 0:
        # Subtract it from the given number
        # Append the corresponding roman value to the roman number solution
        # Otherwise, move on to the next tuple in the array
        roman_number = ""
        i = 0

        while i < 13:
            integer = self.int_roman_list[i][0]
            roman_value = self.int_roman_list[i][1]

            if num == 0:
                return roman_number

            if num - integer >= 0:
                num -= integer
                roman_number += roman_value
            else:
                i += 1


# Example 1
nr = 3

print(Solution().int_to_roman(nr))
print("-------------------------------------")

# Example 2
nr = 58

print(Solution().int_to_roman(nr))
print("-------------------------------------")

# Example 3
nr = 1994

print(Solution().int_to_roman(nr))
