class ListNode(object):
    def __init__(self, val=0, next=None):
        # Define a linked list element (it has a value and a pointer to the next element)
        self.val = val
        self.next = next


class Solution(object):
    def merge_k_lists(self, lists):
        """
        :param lists: the array of sorted linked lists (in ascending order)
        :return: the sorted merged linked list of all the linked lists in the given array
        """
        # Data structure <=> Linked List
        # Algorithm <=> Merge Sort and Divide and Conquer

        # Traversing a variable number of linked lists (or any data structure) at the same time is hard
        # But traversing 2 linked lists at the same time is easy
        # So split the problem into subproblems:
        # We can traverse and merge 2 linked lists, which will give us a new linked list
        # For every current k linked lists, keep merging each 2 and putting each result in an array
        # This will result in k / 2 linked lists
        # And the new k will be k / 2
        # Keep merging the linked lists and splitting k in half until only one linked list remains

        # To merge 2 linked lists, we'll use the merge part in the sorting algorithm
        # Since the 2 parts we need to sort are already sorted:
        # Simultaneously traverse both linked lists
        # At each step, pick the smallest element
        # Go further in the linked list the element belongs to

        # Time complexity <=> O(log k * n), where n is the maximum size of a linked list in the array
        # Space complexity <=> O(m), where m is the sum of the sizes of all the given linked lists

        # Base cases <=> the given array has 0 linked lists or 1 linked list
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        # While k > 1:
        # Split the current k linked lists in 2 resulting in k / 2 linked lists
        # New k = k / 2
        k = len(lists)
        output = lists

        while k > 1:
            output = self.merge_lists(output)
            k = len(output)

        return output[0]

    def merge_lists(self, lists):
        """
        :param lists: the current array of sorted linked lists (in ascending order)
        :return: the array of sorted merged linked lists (after merging each 2)
        """
        # Time complexity <=> O(k / 2), where k is the size of the array
        # Space complexity <=> O(m), where m is the sum of the sizes of all the linked lists given

        # For every 2 linked lists in the given array:
        # Merge them and append the result in the output array
        # This will in the end half k
        output = []
        k = len(lists)
        i = 0

        while i < k:
            if i == k - 1:
                merged_list = lists[i]
                i += 1
            else:
                merged_list = self.merge_2_lists(lists[i], lists[i + 1])
                i += 2

            output.append(merged_list)

        return output

    def merge_2_lists(self, list1, list2):
        """
        :param list1: the linked list to merge with the second one
        :param list2: the linked list the first one will be merged with
        :return: the sorted merged linked list
        """
        # Time complexity <=> O(n), where n is the maximum size of the 2 linked lists
        # Space complexity <=> O(n1 + n2), where n1 is the size of the first linked list
        # And n2 is the size of the second linked list

        # Base case <=> both linked lists are empty or one of them is empty
        if list1 is None and list2 is None:
            return None

        if list1 is None and list2 is not None:
            return list2

        if list1 is not None and list2 is None:
            return list1

        # For each element in the first linked list (el1) and for each element in the second one (el2):
        # If el1 = el2, put both of them in the sorted merged linked list and go on in both given lists
        # If el1 < el2, put el1 in the sorted merged linked list and go on in the first list
        # Otherwise, put el2 in the sorted merged linked list and go on in the second list
        sorted_merged_list = ListNode()
        head = sorted_merged_list

        if list1 is not None and list2 is not None:
            if list1.val == list2.val:
                # Add both values in the sorted merged linked list
                sorted_merged_list = ListNode(list1.val)
                second_element = ListNode(list2.val)
                sorted_merged_list.next = second_element
                head = sorted_merged_list.next

                # Go on in both linked lists
                list1 = list1.next
                list2 = list2.next
            elif list1.val < list2.val:
                # Add the first values in the sorted merged linked list
                sorted_merged_list = ListNode(list1.val)
                head = sorted_merged_list

                # Go on in the first linked list
                list1 = list1.next
            elif list1.val > list2.val:
                # Add the second values in the sorted merged linked list
                sorted_merged_list = ListNode(list2.val)
                head = sorted_merged_list

                # Go on in the second linked list
                list2 = list2.next

        while list1 is not None and list2 is not None:
            if list1.val == list2.val:
                # Add both values in the sorted merged linked list
                first_element = ListNode(list1.val)
                second_element = ListNode(list2.val)
                first_element.next = second_element
                head.next = first_element
                head = second_element

                # Go on in both linked lists
                list1 = list1.next
                list2 = list2.next
            elif list1.val < list2.val:
                # Add the first values in the sorted merged linked list
                element = ListNode(list1.val)
                head.next = element
                head = element

                # Go on in the first linked list
                list1 = list1.next
            else:
                # Add the second values in the sorted merged linked list
                element = ListNode(list2.val)
                head.next = element
                head = element

                # Go on in the second linked list
                list2 = list2.next

        # If one of the lists finishes before the other one:
        # Copy the remaining elements in the sorted merged linked list
        # Since they're already sorted
        while list1 is not None:
            element = ListNode(list1.val)
            head.next = element
            head = element
            list1 = list1.next

        while list2 is not None:
            element = ListNode(list2.val)
            head.next = element
            head = element
            list2 = list2.next

        return sorted_merged_list


def print_list(linked_list):
    """
    :param linked_list: the linked list to be printed
    :return: the array of elements (values) in the given linked list
    """
    # Time complexity <=> O(n), where n is the size of the linked list
    # Space complexity <=> O(n)
    elements = []

    while linked_list is not None:
        elements.append(linked_list.val)
        linked_list = linked_list.next

    return elements


# Example 1
lists1 = [ListNode(1, ListNode(4, ListNode(5, None))),
          ListNode(1, ListNode(3, ListNode(4, None))),
          ListNode(2, ListNode(6, None))]

merged = Solution().merge_k_lists(lists1)

print(print_list(merged))
print("-------------------------------------")

# Example 2
lists1 = []

merged = Solution().merge_k_lists(lists1)

print(print_list(merged))
print("-------------------------------------")

# Example 3
lists1 = [None]

merged = Solution().merge_k_lists(lists1)

print(print_list(merged))
print("-------------------------------------")

# Example 4
lists1 = [None, None]

merged = Solution().merge_k_lists(lists1)

print(print_list(merged))
print("-------------------------------------")

# Example 5
lists1 = [None, ListNode(1, None)]

merged = Solution().merge_k_lists(lists1)

print(print_list(merged))
print("-------------------------------------")

# Example 6
lists1 = [ListNode(1, ListNode(2, ListNode(3, None))),
          ListNode(4, ListNode(5, ListNode(6, ListNode(7, None))))]

merged = Solution().merge_k_lists(lists1)

print(print_list(merged))
