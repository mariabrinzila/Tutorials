class ListNode(object):
    def __init__(self, val=0, next_elem=None):
        self.val = val
        self.next = next_elem


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    l1_numbers = []
    l2_numbers = []

    # Iterate through the first list
    get_through_list(l1, l1_numbers)

    # Iterate through the second list
    get_through_list(l2, l2_numbers)

    # Compute number for the first list
    number1 = compute_number(l1_numbers)

    # Compute number for the second list
    number2 = compute_number(l2_numbers)

    # Compute sum of numbers
    numbers_sum = number1 + number2

    # Turn the sum of numbers to a list
    return compute_result_list(numbers_sum)


def get_through_list(elem1, digits_list):
    digits_list.append(elem1.val)

    if elem1.next is None:
        return 0

    return get_through_list(elem1.next, digits_list)


def compute_number(digits_list):
    number = 0
    i = len(digits_list) - 1

    while i >= 0:
        digit = digits_list[i]
        number = number * 10 + digit
        i -= 1

    return number


def compute_result_list(number):
    result = []

    if number // 10 == 0:
        return ListNode(number, None)

    while number > 0:
        result.append(number % 10)
        number //= 10

    # Convert to ListNodes
    list_node = compute_result_list_node(result, 0)

    return list_node


def compute_result_list_node(result_list, index):
    if index == len(result_list) - 1:
        return ListNode(result_list[index], None)

    return ListNode(result_list[index], compute_result_list_node(result_list, index + 1))


# Example 1
L1 = ListNode(2, ListNode(4, ListNode(3, None)))
L2 = ListNode(5, ListNode(6, ListNode(4, None)))

list_node1 = add_two_numbers(L1, L2)

digits = []
get_through_list(list_node1, digits)
print(digits)

# Example 2
L1 = ListNode(0, None)
L2 = ListNode(0, None)

list_node1 = add_two_numbers(L1, L2)

digits = []
get_through_list(list_node1, digits)
print(digits)
