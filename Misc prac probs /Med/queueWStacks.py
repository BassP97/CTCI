"""
Implement a queue with 2 stacks. Your queue should have an enqueue 
and a dequeue method and it should be "first in first out" (FIFO).

Optimize for the time cost of m calls on your queue. These can 
be any mix of enqueue and dequeue calls.

Assume you already have a stack implementation and it gives 
O(1) time push and pop.
"""

class Stack(object):
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class queue(object):
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()
    def enqueue(self, item):
        self.inStack.push(item)
    def dequeue(self):
        if self.outStack.peek() is None:
            if self.inStack.peek() is None:
                raise ValueError("Can't dequeue empty queue")
            while self.inStack.peek() is not None:
                self.outStack.push(self.inStack.pop())
        return self.outStack.pop()