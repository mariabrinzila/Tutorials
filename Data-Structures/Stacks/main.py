class Stack:
    def __init__(self):
        # The elements of the stack are stored in an array
        self.stack = []

    def push(self, element_value):
        """
        :param element_value: the element to be inserted in the stack
        :return: void
        """
        self.stack.append(element_value)

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


# Creation
stack = Stack()

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
      + " elements and the is currently: " + str(stack.stack))
print("-------------------------------------")

# Top
print("The stack's top element is currently: " + str(stack.top()))
print("-------------------------------------")

# Search
if stack.search(3):
    print("The element 3 is in the stack")
else:
    print("The element 3 isn't in the stack")

if stack.search(55):
    print("The element 55 is in the stack")
else:
    print("The element 55 isn't in the stack")

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
