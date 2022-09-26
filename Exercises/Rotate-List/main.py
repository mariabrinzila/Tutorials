class ListNode(object):
    def __init__(self, val=0, next=None):
        # Define a linked list element (it has a value and a pointer to the next element)
        self.val = val
        self.next = next


class Solution(object):
    def __init__(self):
        # Define an array in which the unique rotations will be stored
        self.rotation_lists = []

    def rotate_right(self, head, k):
        """
        :param head: the linked list to be rotated k times (a rotation is when the last element in the
            linked list becomes the first one and all the other ones are shifted by one position)
        :param k: the number which represents the number of times the given linked list will be
            rotated
        :return: the linked list after k rotations
        """
        # Data structure <=> Linked List
        # Algorithm <=> Dynamic Programming

        # The rotations will be repeated since a list can be uniquely rotated n times,
        # Where n is the size of the linked list
        # So we don't need to recompute these rotations, if k > n
        # We can compute all n rotations and store them in an array
        # And the given linked list after k rotations will be
        # The linked list on the k % n position in the array of rotations

        # Time complexity <=> O(n * n), where n is the size of the linked list
        # Space complexity <=> O(n * n)

        # Base cases <=> the given linked list has 0 elements or only has one element
        if head is None:
            return None

        if head.next is None:
            return head

        # Compute the size of the given linked list
        n = 0
        linked_list = head

        while linked_list is not None:
            n += 1
            linked_list = linked_list.next

        # If k <= n, we don't need to store them:
        # While we haven't done k rotations,
        # We can just do a rotation and make the given linked list equal to the resulting linked list
        # Otherwise (k > n), compute all n unique rotations and store them in an array
        # And return the one on the k % n position in the array after computing all n linked lists
        if k <= n:
            for i in range(k):
                head = self.rotation(head)

            return head

        result = head
        self.rotation_lists.append(result)

        for i in range(n):
            result = self.rotation(result)
            self.rotation_lists.append(result)

        return self.rotation_lists[k % n]

    def rotation(self, head):
        """
        :param head: the linked list to be rotated once (the last element in the linked list will become
            the first one and all the other ones are shifted by one position)
        :return: the linked list after a rotation
        """
        # Time complexity <=> O(n), where n is the size of the linked list
        # Space complexity <=> O(n)

        # For each element in the given linked list:
        # If the resulting linked list is empty, add the element and make it the first one
        # Otherwise, if the current element isn't the last one, simply add it to the resulting linked list
        # Otherwise (the current element is the last one in the given linked list):
        # Make it the first one in the resulting linked list
        result = ListNode()
        first = ListNode(-101)
        current = first

        while head is not None:
            if current.val == -101:
                current.val = head.val
            elif head.next is not None:
                current.next = ListNode(head.val)
                current = current.next
            else:
                result = ListNode(head.val)
                result.next = first

            head = head.next

        return result


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
lists1 = ListNode(1, ListNode(2, ListNode(3,  ListNode(4,  ListNode(5, None)))))
k1 = 2

solution = Solution().rotate_right(lists1, k1)

print(print_list(solution))
print("-------------------------------------")


# Example 2
lists1 = ListNode(0, ListNode(1, ListNode(2, None)))
k1 = 4

solution = Solution().rotate_right(lists1, k1)

print(print_list(solution))
print("-------------------------------------")

# Example 3
lists1 = None
k1 = 4

solution = Solution().rotate_right(lists1, k1)

print(print_list(solution))
print("-------------------------------------")

# Example 4
lists1 = ListNode(1, None)
k1 = 4

solution = Solution().rotate_right(lists1, k1)

print(print_list(solution))
print("-------------------------------------")

# Example 5
lists1 = ListNode(1, ListNode(2, ListNode(3, None)))
k1 = 2000000000

solution = Solution().rotate_right(lists1, k1)

print(print_list(solution))

