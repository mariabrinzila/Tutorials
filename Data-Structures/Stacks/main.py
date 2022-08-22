class Stack:
    def __init__(self, capacity):
        # The stack's capacity (maximum number of elements)
        self.capacity = capacity

        # The elements of the stack are stored in an array
        self.stack = []

    def push(self, element_value):
        """
        :param element_value: the element to be inserted in the stack
        :return: False, if the stack is already at capacity and True, otherwise
        """
        if self.is_at_capacity():
            return False

        self.stack.append(element_value)

        return True

    def pop(self):
        """
        :return: the element that was deleted (the last element added), if the stack isn't empty
            and False, otherwise
        """
        if self.is_empty():
            return False

        element = self.stack[self.size() - 1]
        self.stack.remove(element)

        return element

    def search(self, element_value):
        """
        :param element_value: the element to be searched in the stack
        :return: True, if the element is in the stack and False, otherwise
        """
        if element_value in self.stack:
            return True

        return False

    def top(self):
        """
        :return: the top of the stack (the last element that was added), if the stack isn't empty
            and False, otherwise
        """
        if self.is_empty():
            return False

        return self.stack[self.size() - 1]

    def size(self):
        """
        :return: the size of the stack (the number of elements in it)
        """
        return len(self.stack)

    def is_empty(self):
        """
        :return: True, if the stack is empty and False, otherwise
        """
        if self.size() == 0:
            return True

        return False

    def is_at_capacity(self):
        """
        :return: True, if the stack is at capacity (we have the maximum number of elements in it)
            and False, otherwise
        """
        if self.size() == self.capacity:
            return True

        return False


# Creation
stack = Stack(5)

# Is empty
if stack.is_empty():
    print("The stack is currently empty")
else:
    print("The stack is currently not empty")

print("-------------------------------------")

# Insertion and size
stack.push(1)
stack.push(45)
stack.push(23)
stack.push(3)
stack.push(9)

print("After inserting 1, 45, 23, 3 and 9, the stack has " + str(stack.size())
      + " elements and it's currently: " + str(stack.stack))

result = stack.push(34)

if not result:
    print("Couldn't insert another element since the stack is at capacity")
else:
    print("Inserted the element and the stack is now: " + str(stack.stack))

print("-------------------------------------")

# Is at capacity
if stack.is_at_capacity():
    print("The stack is currently at capacity")
else:
    print("The stack is not currently at capacity")

print("-------------------------------------")

# Search
if stack.search(3):
    print("The element 3 exists in the stack")
else:
    print("The element 3 doesn't exist in the stack")

if stack.search(55):
    print("The element 55 exists in the stack")
else:
    print("The element 55 doesn't exist in the stack")

print("-------------------------------------")

# Deletion
deleted = stack.pop()

if not deleted:
    print("The stack is empty so no element can be deleted")
else:
    print("After the pop operation, the stack is: " + str(stack.stack)
          + " and the deleted element is " + str(deleted))

deleted = stack.pop()

if not deleted:
    print("The stack is empty so no element can be deleted")
else:
    print("After the pop operation, the stack is: " + str(stack.stack)
          + " and the deleted element is " + str(deleted))

print("-------------------------------------")

# Top
print("The stack's top element is currently: " + str(stack.top()))
