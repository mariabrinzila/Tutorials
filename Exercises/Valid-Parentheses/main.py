class Solution(object):
    def is_valid(self, s):
        """
        :param s: the string only containing (, ), [, ], {, }
        :return: True, if the string is valid (all opened parentheses close by the same type of
            parenthesis, in the correct order) and False, otherwise
        """
        # Data structures <=> String and Stack

        # Time complexity <=> O(n), where n is the size of the string
        # Space complexity <=> O(n)

        # Base case <=> s only has one character
        if len(s) == 1:
            return False

        # For every character in the given string:
        # If the current character is an open parenthesis, append it to the stack
        # Otherwise:
        # If the stack is empty, the string is invalid, so return False
        # If the top of the stack is the corresponding open parenthesis:
        # Pop it
        # Otherwise, the string is invalid, so return False
        stack = []
        open_parentheses = "([{"

        for character in s:
            if character in open_parentheses:
                stack.append(character)
            else:
                if len(stack) == 0:
                    return False

                if (character == ')' and stack[len(stack) - 1] == '(') or \
                        (character == ']' and stack[len(stack) - 1] == '[') or \
                        (character == '}' and stack[len(stack) - 1] == '{'):
                    stack.pop(len(stack) - 1)
                else:
                    return False

        # If at the end the stack isn't empty, the string is invalid, so return False
        if len(stack) > 0:
            return False

        return True


# Example 1
s1 = "()"

print(Solution().is_valid(s1))
print("-------------------------------------")

# Example 2
s1 = "()[]{}"

print(Solution().is_valid(s1))
print("-------------------------------------")

# Example 3
s1 = "(]"

print(Solution().is_valid(s1))
print("-------------------------------------")

# Example 4
s1 = "("

print(Solution().is_valid(s1))
print("-------------------------------------")

# Example 5
s1 = "){"

print(Solution().is_valid(s1))
