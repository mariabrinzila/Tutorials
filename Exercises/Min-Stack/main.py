class MinStack(object):
    def __init__(self):
        # Data structure <=> Stack

        # Each stack element will be a tuple (value, minimum)
        # The value is the value of the element
        # And the minimum is the minimum value in the stack up until the current element
        # This way, the top of the stack will always contain the stack's minimum value

        # Time complexity <=> O(1)
        # Space complexity <=> O(n), where n is the current number of elements in the stack

        # Define a number which represents the stack's current capacity (the current number of elements in it)
        self.capacity = 0

        # Define a stack that will hold the (value, minimum) tuple elements
        self.stack = []

    def push(self, val):
        """
        :param val: the number that will be added at the end of the stack
        :return: void
        """
        # Time complexity <=> O(1)
        # Space complexity <=> O(n), where n is the current number of elements in the stack

        # If the stack is empty, the current element's minimum will be its value
        # Otherwise, if the value to be added to the stack is smaller than the top's minimum:
        # The minimum of the current element will be the value
        # Otherwise (the stack isn't empty and the value to be added to the stack is >= the top's minimum):
        # The minimum of the current element will be the top's minimum
        # Append the (value, minimum) tuple to the stack and increment the stack's current capacity
        if self.capacity == 0:
            element = (val, val)
        elif val < self.stack[self.capacity - 1][1]:
            element = (val, val)
        else:
            element = (val, self.stack[self.capacity - 1][1])

        self.stack.append(element)
        self.capacity += 1

    def pop(self):
        """
        :return: void (but it removes the stack's current top)
        """
        # Time complexity <=> O(1)
        # Space complexity <=> O(n), where n is the current number of elements in the stack

        # Remove the last element added in the stack and decrement the stack's current capacity
        self.stack.pop(self.capacity - 1)
        self.capacity -= 1

    def top(self):
        """
        :return: the number that is the top of the stack's value (the last element added to the stack's
            value)
        """
        # Time complexity <=> O(1)
        # Space complexity <=> O(n), where n is the current number of elements in the stack

        # The top of the stack is on position capacity - 1
        return self.stack[self.capacity - 1][0]

    def get_min(self):
        """
        :return: the number that is the minimum value in the stack
        """
        # Time complexity <=> O(1)
        # Space complexity <=> O(n), where n is the current number of elements in the stack

        # Since each element in the stack has a minimum up until it
        # The top of the stack's minimum will correspond to the overall minimum value in the stack
        return self.stack[self.capacity - 1][1]


# Example 1
commands = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
elements = [[], [-2], [0], [-3], [], [], [], []]
results = []
size = len(commands)
stack = MinStack()

for i in range(1, size):
    command = commands[i]
    element1 = elements[i]

    if command == "push":
        stack.push(element1[0])
        results.append(None)
    elif command == "getMin":
        results.append(stack.get_min())
    elif command == "pop":
        stack.pop()
        results.append(None)
    else:
        results.append(stack.top())

print(results)
