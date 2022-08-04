class LinkedListNode:
    def __init__(self, data):
        # Data field
        self.data = data

        # Reference to the next element (initially None)
        self.next = None


class LinkedList:
    def __init__(self):
        # Head points to the first element in the list (initially None)
        self.head = None

    def creation(self, nodes):
        """
        :param nodes: array of data fields to be put in the linked list
        :return: the linked list created with the data fields given
        """
        # Head points to the first element in nodes
        first = LinkedListNode(nodes[0])
        self.head = first

        # For every element left in nodes:
        # Create the node with that data field
        # Link the previous node to the current one
        previous = self.head
        length = len(nodes)

        for i in range(1, length):
            current = LinkedListNode(nodes[i])
            previous.next = current
            previous = current

    def traversal(self):
        """
        :return: the array of the data fields in linked_list
        """
        # While the end of the list hasn't been reached:
        # Put the current data field in an array
        # Go to the next element
        data = []
        current = self.head

        while current is not None:
            data.append(current.data)
            current = current.next

        print(data)


nodes_data = [1, 2, 3, 6, 47, 3, 12, 100, 4, 5, 2]

# Creation
linked_list_created = LinkedList()
linked_list_created.creation(nodes_data)

# Traversal
linked_list_created.traversal()
