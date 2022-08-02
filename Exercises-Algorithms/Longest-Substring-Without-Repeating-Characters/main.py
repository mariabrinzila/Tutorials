def all_numbers_of_length(k):
    if len(sol) == lg:
        print(sol)
        return 0

    for i in options:
        sol.append(i)
        all_numbers_of_length(k + 1)
        sol.remove(i)


class Solution(object):
    def length_of_longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1

        length = len(s)
        maximum_length = 0
        solution = ""

        for i in range(length):
            for j in range(i, length + 1):
                substring = s[i:j]

                if not self.check_duplicates(substring) and len(substring) > maximum_length:
                    maximum_length = len(substring)
                    solution = substring

        print(solution)
        return maximum_length

    def check_duplicates(self, string):
        length = len(string)

        for i in range(length):
            copy_string = string[(i + 1):]

            if string[i] in copy_string:
                return True

        return False


s1 = "auba"
solution1 = Solution()
print(solution1.length_of_longest_substring(s1))


sol = []
options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
lg = 2
