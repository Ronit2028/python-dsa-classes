import collections

class Node:
    """
    A class representing a node in a Linked List based Stack or Queue.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


# ==========================================
# Stack Implementations
# ==========================================

class ListStack:
    """
    Stack implementation using a dynamic array (Python's list).
    LIFO (Last-In, First-Out).
    """
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add an element to the top of the stack. Time Complexity: O(1) amortized."""
        self.stack.append(item)

    def pop(self):
        """Remove and return the top element. Time Complexity: O(1)."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        """Return the top element without removing it. Time Complexity: O(1)."""
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty. Time Complexity: O(1)."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of elements. Time Complexity: O(1)."""
        return len(self.stack)

    def __str__(self):
        return f"ListStack(top -> {list(reversed(self.stack))})"


class NodeStack:
    """
    Stack implementation using linked Nodes.
    LIFO (Last-In, First-Out).
    """
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        """Add an element to the top of the stack. Time Complexity: O(1)."""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Remove and return the top element. Time Complexity: O(1)."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_value = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped_value

    def peek(self):
        """Return the top element without removing it. Time Complexity: O(1)."""
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        """Check if the stack is empty. Time Complexity: O(1)."""
        return self.top is None

    def size(self):
        """Return the number of elements. Time Complexity: O(1)."""
        return self._size

    def __str__(self):
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        return "NodeStack(top -> " + " -> ".join(elements) + " -> None)"


# ==========================================
# Queue Implementations
# ==========================================

class DequeQueue:
    """
    Queue implementation using collections.deque.
    FIFO (First-In, First-Out).
    """
    def __init__(self):
        self.queue = collections.deque()

    def enqueue(self, item):
        """Add an element to the rear of the queue. Time Complexity: O(1)."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the front element. Time Complexity: O(1)."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.popleft()

    def peek(self):
        """Return the front element without removing it. Time Complexity: O(1)."""
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty. Time Complexity: O(1)."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of elements. Time Complexity: O(1)."""
        return len(self.queue)

    def __str__(self):
        return f"DequeQueue(front -> {list(self.queue)} <- rear)"


class NodeQueue:
    """
    Queue implementation using linked Nodes (with both head/front and tail/rear pointers).
    FIFO (First-In, First-Out).
    """
    def __init__(self):
        self.head = None  # Front of queue
        self.tail = None  # Rear of queue
        self._size = 0

    def enqueue(self, item):
        """Add an element to the rear of the queue. Time Complexity: O(1)."""
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        """Remove and return the front element. Time Complexity: O(1)."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        dequeued_value = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return dequeued_value

    def peek(self):
        """Return the front element without removing it. Time Complexity: O(1)."""
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        """Check if the queue is empty. Time Complexity: O(1)."""
        return self.head is None

    def size(self):
        """Return the number of elements. Time Complexity: O(1)."""
        return self._size

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "NodeQueue(front -> " + " -> ".join(elements) + " -> None)"


# ==========================================
# Self-Testing Script
# ==========================================

if __name__ == "__main__":
    print("==========================================")
    print("1. Testing ListStack")
    print("==========================================")
    lst_stack = ListStack()
    print("Is empty?", lst_stack.is_empty())
    print("Pushing 10, 20, 30...")
    lst_stack.push(10)
    lst_stack.push(20)
    lst_stack.push(30)
    print(lst_stack)
    print("Size:", lst_stack.size())
    print("Peek:", lst_stack.peek())
    print("Popped:", lst_stack.pop())
    print(lst_stack)
    print("Popped:", lst_stack.pop())
    print("Is empty?", lst_stack.is_empty())
    print("Popped:", lst_stack.pop())
    print("Is empty?", lst_stack.is_empty())

    print("\n==========================================")
    print("2. Testing NodeStack")
    print("==========================================")
    nd_stack = NodeStack()
    print("Is empty?", nd_stack.is_empty())
    print("Pushing 'A', 'B', 'C'...")
    nd_stack.push('A')
    nd_stack.push('B')
    nd_stack.push('C')
    print(nd_stack)
    print("Size:", nd_stack.size())
    print("Peek:", nd_stack.peek())
    print("Popped:", nd_stack.pop())
    print(nd_stack)
    print("Popped:", nd_stack.pop())
    print("Is empty?", nd_stack.is_empty())
    print("Popped:", nd_stack.pop())
    print("Is empty?", nd_stack.is_empty())

    print("\n==========================================")
    print("3. Testing DequeQueue")
    print("==========================================")
    dq_queue = DequeQueue()
    print("Is empty?", dq_queue.is_empty())
    print("Enqueueing 1.1, 2.2, 3.3...")
    dq_queue.enqueue(1.1)
    dq_queue.enqueue(2.2)
    dq_queue.enqueue(3.3)
    print(dq_queue)
    print("Size:", dq_queue.size())
    print("Peek front:", dq_queue.peek())
    print("Dequeued:", dq_queue.dequeue())
    print(dq_queue)
    print("Dequeued:", dq_queue.dequeue())
    print("Is empty?", dq_queue.is_empty())
    print("Dequeued:", dq_queue.dequeue())
    print("Is empty?", dq_queue.is_empty())

    print("\n==========================================")
    print("4. Testing NodeQueue")
    print("==========================================")
    nd_queue = NodeQueue()
    print("Is empty?", nd_queue.is_empty())
    print("Enqueueing 'X', 'Y', 'Z'...")
    nd_queue.enqueue('X')
    nd_queue.enqueue('Y')
    nd_queue.enqueue('Z')
    print(nd_queue)
    print("Size:", nd_queue.size())
    print("Peek front:", nd_queue.peek())
    print("Dequeued:", nd_queue.dequeue())
    print(nd_queue)
    print("Dequeued:", nd_queue.dequeue())
    print("Is empty?", nd_queue.is_empty())
    print("Dequeued:", nd_queue.dequeue())
    print("Is empty?", nd_queue.is_empty())
    print("==========================================")
    print("All basic stacks & queues tests completed successfully!")
    print("==========================================")
