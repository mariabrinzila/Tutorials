class Solution(object):
    def find_ladders(self, begin_word, end_word, word_list):
        """
        :param begin_word: the string with which the shortest sequence starts (the beginning point)
        :param end_word: the string with which the shortest sequence ends (the end point)
        :param word_list: the array of strings representing the dictionary (the words that we can
            use in the sequence between the beginning and end word)
        :return: all the shortest sequences between the beginning and end word where each word
            in the sequence is different from the previous and next word by just one character, if one
            exists and an empty array, otherwise
        """
        # Data structure <=> String, Array, Hash Map, Queue
        # Algorithm <=> BFS

        # The process of constructing the graph is time-consuming
        # As the process of checking which words only differ by one letter is time-consuming
        # But this can be done more efficiently
        # Since each word has m intermediate words, where m is the size of the word
        # An intermediate word being a word that differs by one character from the original one
        # And that letter is marked with a *
        # For example, for dog, the intermediate words are *og, d*g and do*
        # So we can store all the words that have the same intermediate word in an array <=> hash map
        # After doing this processing of the words in the given array
        # We go from the beginning point, compute all its intermediate words
        # And find the words that have intermediate words in common with it
        # Which simulates the process of a graph (each word is a vertex and the ones that have
        # Intermediate words in common with it are connected by an edge)
        # Then go from each of these words in order and repeat the process
        # Until we find the end point or until we can't go to any other word anymore <=> BFS
        # In order to compute all the solution, each element in the queue will also have a path
        # When we find an unvisited word and we add it to the queue, its path will be the previous one
        # + the current word
        # And when we find the end word, it means we have a complete solution in the path (+ the end word)

        # Key <=> the intermediate word (the * is the letter that will be substituted)
        # Value <=> the array of words that have that intermediate word in their list of intermediate words
        # Hash function <=> H(intermediate) = [w1, w2, ...]

        # Time complexity <=> O(n * m * m), where n is the size of the array
        # And m is the size of each string
        # Space complexity <=> O(n * m * m)
        # BFS takes just as much time as the word processing (in the worst case)

        # Base case <=> the end word doesn't exist in the dictionary, so we can't get to it
        if end_word not in word_list:
            return []

        # Compute the hash map with all the intermediate words and the words that share them
        hash_map = self.process_words(word_list)

        # While the queue isn't empty:
        # For each element in the queue at this point (all the words on this level):
        # Pop the first element of the queue
        # Compute all the intermediate words of the current word
        # Compute all the other words that have intermediate words in common with the current word
        # These words will be the vertices in the graph that are adjacent with the current word
        # If the current adjacent word is the end word
        # Add to the array of solutions the path + the end word
        # Add the unvisited adjacent words to the queue (tuples of (word, path + word))
        visited = [begin_word]
        queue = [(begin_word, [begin_word])]
        all_solutions = []
        m = len(begin_word)

        while queue and not all_solutions:
            queue_size = len(queue)

            for _ in range(queue_size):
                current_tuple = queue.pop(0)
                current_word = current_tuple[0]
                path = current_tuple[1]

                for i in range(m):
                    intermediate_word = current_word[:i] + "*" + current_word[(i + 1):]

                    if hash_map.get(intermediate_word) is not None:
                        for word in hash_map[intermediate_word]:
                            if word == end_word:
                                all_solutions.append(path + [end_word])

                            if word not in visited:
                                queue.append((word, path + [word]))
                                visited.append(word)

        if len(all_solutions) == 0:
            return []

        return all_solutions

    def process_words(self, word_list):
        """
        :param word_list: the array of strings representing the dictionary (the words that we can
            use in the sequence between the beginning and end word)
        :return: the hash map containing all the intermediate words of each word as the keys and
            all the words that share the intermediate word key as the values
        """
        # Time complexity <=> O(n * m * m), where n is the size of the array
        # And m is the size of each string (each word has m substrings)
        # Space complexity <=> O(n * m * m) (each word of size m will be put as a value in all m substrings)

        # For each word in the array of words (the dictionary of words):
        # Compute all intermediate words by putting a * instead of each letter of the current word
        # Add the current word in the array of values for each intermediate word (the key)
        hash_map = dict()

        for word in word_list:
            m = len(word)

            for i in range(m):
                intermediate_word = word[:i] + "*" + word[(i + 1):]

                if hash_map.get(intermediate_word) is not None:
                    hash_map[intermediate_word].append(word)
                else:
                    hash_map[intermediate_word] = [word]

        return hash_map


# Example 1
begin = "hit"
end = "cog"
dictionary = ["hot", "dot", "dog", "lot", "log", "cog"]

print(Solution().find_ladders(begin, end, dictionary))
print("-------------------------------------")

# Example 2
begin = "hit"
end = "cog"
dictionary = ["hot", "dot", "dog", "lot", "log"]

print(Solution().find_ladders(begin, end, dictionary))
print("-------------------------------------")
