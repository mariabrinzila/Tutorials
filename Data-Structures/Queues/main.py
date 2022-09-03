class Queue:
    def __init__(self, capacity):
        # The queue's capacity (maximum number of elements)
        self.capacity = capacity

        # The elements of the queue are stored in an array
        self.queue = [None] * self.capacity

        # The front and rear indices and the queue's size
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, element_value):
        """
        :param element_value: the element to be inserted in the queue
        :return: False, if the queue is already at capacity and True, otherwise
        """
        if self.is_at_capacity():
            return False

        self.rear += 1
        self.size += 1
        self.queue[self.rear] = element_value

        return True

    def dequeue(self):
        """
        :return: False, if the queue is empty and the element at the front before deleting it
        """
        if self.is_empty():
            return False

        element = self.queue[self.front]
        self.queue.remove(self.get_front())
        self.rear -= 1
        self.size -= 1

        return element

    def search(self, element_value):
        """
        :param element_value: the element to be searched in the queue
        :return: True, if the element is in the queue and False, otherwise
        """
        if element_value in self.queue:
            return True

        return False

    def get_front(self):
        """
        :return: the element at the front (at the beginning) of the queue, if the queue isn't empty
            and None, otherwise
        """
        if not self.is_empty():
            return self.queue[self.front]

        return None

    def get_rear(self):
        """
        :return: the element at the rear (at the end) of the queue, if the queue isn't empty
            and None, otherwise
        """
        if not self.is_empty():
            return self.queue[self.rear]

        return None

    def is_empty(self):
        """
        :return: True, if the queue is empty and False, otherwise
        """
        if self.size == 0:
            return True

        return False

    def is_at_capacity(self):
        """
        :return: True, if the queue is at capacity (we have the maximum number of elements in the queue)
            and False, otherwise
        """
        if self.size == self.capacity:
            return True

        return False


# Creation
queue = Queue(6)

# Is empty
if queue.is_empty():
    print("The queue is currently empty")
else:
    print("The queue is currently not empty")

print("-------------------------------------")

# Insertion
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(30)
queue.enqueue(5)
queue.enqueue(67)
queue.enqueue(3)

print("After inserting 1, 2, 30, 5, 67, 3, the queue has " + str(queue.size)
      + " elements and it's currently: " + str(queue.queue))

result = queue.enqueue(45)

if not result:
    print("Couldn't insert another element since the queue is at capacity")
else:
    print("Inserted the element and the queue is now: " + str(queue.queue))

print("-------------------------------------")

# Is at capacity
if queue.is_at_capacity():
    print("The queue is currently at capacity")
else:
    print("The queue is not currently at capacity")

print("-------------------------------------")

# Search
if queue.search(3):
    print("The element 3 exists in the queue")
else:
    print("The element 3 doesn't exist in the queue")

if queue.search(300):
    print("The element 300 exists in the queue")
else:
    print("The element 300 doesn't exist in the queue")
print("-------------------------------------")

# Deletion
result = queue.dequeue()

print("The element " + str(result) + " was deleted and now the queue is: " + str(queue.queue))

result = queue.dequeue()

print("The element " + str(result) + " was deleted and now the queue is: " + str(queue.queue))
print("-------------------------------------")

# Rear and front
print("The element at the rear of the queue is currently " + str(queue.get_rear())
      + " and the one at the front of the queue is currently " + str(queue.get_front()))
