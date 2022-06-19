
from queue import Empty


class LinkedStack:
    """ Stack ADT using Singly Linked List

    :raises Empty: if the stack is empty
    :return: the top element of the stack
    :rtype: object or None if the stack is empty
    """

    class _Node:
        # save memory by not creating a new object for each node
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self, head=0, size=0):
        self._head = head
        self._size = size

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def print_stack(self):
        if self.is_empty():
            print('Stack is empty')
        else:
            current = self._head
            while current:
                print(current._element, end='->')
                current = current._next
            print()

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


def test_LinkedStack():
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.print_stack()
    print(stack.top())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    stack.print_stack()


class LinkedQueue:
    """ Queue ADT using Singly Linked List

    :raises Empty: if the queue is empty
    :return: the first element of the queue (FIFO)
    :rtype: object or None if the queue is empty
    """

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self, head=None, tail=None):
        self._head = head
        self._tail = head
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def print_queue(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            current = self._head
            while current:
                print(current._element, end='->')
                current = current._next
            print()
    # return but not remove the head

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():  # if queue is empty then head and tail point to the same node
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue_all(self):
        while not self.is_empty():
            self.dequeue()


def test_LinkedQueue():
    queue = LinkedQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print_queue()
    print(queue.first())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    queue.print_queue()


if __name__ == '__main__':
    test_LinkedStack()
    test_LinkedQueue()
