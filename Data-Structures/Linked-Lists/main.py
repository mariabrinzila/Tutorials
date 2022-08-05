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
        :param nodes: the array of data fields to be put in the linked list
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
        :return: the array of data fields in the linked list
        """
        # While the end of the linked list hasn't been reached:
        # Put the current data field in an array
        # Go to the next node
        data = []
        current = self.head

        while current is not None:
            data.append(current.data)
            current = current.next

        return data

    def search(self, data):
        """
        :param data: the data field to be sought
        :return: the node with that data, if the node exists in the linked list and -1, otherwise
        """
        # While the end of the linked list hasn't been reached:
        # If the sought node is found, return it
        # Otherwise, return -1
        current = self.head

        while current is not None:
            if current.data == data:
                return current

            current = current.next

        return -1

    def get_last(self):
        """
        :return: the last element in the linked list
        """
        # While the end of the linked list hasn't been reached:
        # Traverse the nodes and return the last one
        current = self.head

        while current is not None:
            if current.next is None:
                return current

            current = current.next

    def previous(self, node):
        """
        :param node: the node to be searched for in the linked list
        :return: the node before the given node, if the given node exists and -1, otherwise
        """
        # While the end of the linked list hasn't been reached:
        # If the sought node is found, return the one before it
        # Otherwise, return -1
        current = self.head
        previous_node = None

        while current is not None:
            if current == node:
                return previous_node

            previous_node = current
            current = current.next

        return -1

    def insertion_first(self, new_data):
        """
        :param new_data: the data field to be inserted in the linked list
        :return: void
        """
        # The new node will be inserted at the beginning of the linked list
        new_node = LinkedListNode(new_data)

        # Head must point to the new node
        previously_first = self.head
        self.head = new_node

        # The new node must point to the previously first node
        new_node.next = previously_first

    def insertion_after(self, new_data, given_data):
        """
        :param new_data: the data field to be inserted in the linked list
        :param given_data: the data field after which the new data field should be inserted
        :return: void
        """
        # The new node will be inserted after the given element
        new_node = LinkedListNode(new_data)

        # Search for the given node
        given_node = self.search(given_data)

        if given_node != -1:
            # Element found
            # The new node must point to the one that was previously after the given one
            new_node.next = given_node.next

            # The given node must point to the new one
            given_node.next = new_node
        else:
            # Element not found
            print("Could not insert element " + str(new_data) + " as the given element "
                  + str(given_data) + " doesn't exist in the linked list")

    def insertion_end(self, new_data):
        """
        :param new_data: the data field to be inserted in the linked list
        :return: void
        """
        # The new node will be inserted at the end of the linked list
        new_node = LinkedListNode(new_data)

        # Traverse the linked list and get the last node
        last = self.get_last()

        # The new node will be after the previously last one
        last.next = new_node

    def deletion(self, data):
        """
        :param data: the data field of the element to be deleted
        :return: void
        """
        # Search for the node with the given data field
        given_node = self.search(data)

        if given_node != -1:
            # Element found

            if given_node == self.head:
                # Element is at the beginning of the linked list
                # Head must point to the node that is after the given one
                self.head = given_node.next
            elif given_node == self.get_last():
                # Element is at the end of the linked list
                # The node before it must point to None
                previous_node = self.previous(given_node)
                previous_node.next = None
            else:
                # The element is somewhere in the middle of the linked list
                # The node before it must point to the one after it
                previous_node = self.previous(given_node)
                previous_node.next = given_node.next
        else:
            # Element not found
            print("The element " + str(data) + " isn't in the linked list so it can't be deleted")


nodes_data = [1, 2, 3, 9, 10, 11, 12, 4, 5, 6]

# Creation
linked_list_created = LinkedList()
linked_list_created.creation(nodes_data)

# Traversal
print("The list creation result after traversal is: " + str(linked_list_created.traversal()))
print("-------------------------------------")

# Search
print("The search result for 9 is: " + str(linked_list_created.search(9)))
print("The search result for 456 is: " + str(linked_list_created.search(456)))
print("-------------------------------------")

# The last element
print("The last element in the list is: " + str(linked_list_created.get_last().data))
print("-------------------------------------")

# Insertion (at the beginning)
linked_list_created.insertion_first(20)
print("After the insertion of 20 at the beginning of the list, the result is: "
      + str(linked_list_created.traversal()))
print("-------------------------------------")

# Insertion (after a given node)
linked_list_created.insertion_after(45, 456)
print("-------------------------------------")

linked_list_created.insertion_after(45, 9)
print("After the insertion of 45 after 9, the result is: "
      + str(linked_list_created.traversal()))
print("-------------------------------------")

# Insertion (at the end)
linked_list_created.insertion_end(205)
print("After the insertion of 205 at the end of the list, the result is: "
      + str(linked_list_created.traversal()))
print("-------------------------------------")

# Deletion
linked_list_created.deletion(33)
print("-------------------------------------")

linked_list_created.deletion(20)
print("After deleting 20, the result is: "
      + str(linked_list_created.traversal()))
print("-------------------------------------")

linked_list_created.deletion(11)
print("After deleting 11, the result is: "
      + str(linked_list_created.traversal()))
print("-------------------------------------")

linked_list_created.deletion(205)
print("After deleting 205, the result is: "
      + str(linked_list_created.traversal()))
print("-------------------------------------")
