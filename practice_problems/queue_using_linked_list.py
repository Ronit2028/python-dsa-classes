class Node:
    """
    Singly Linked List Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """
    FIFO Queue implemented using a Singly Linked List.
    All operations must have O(1) time complexity.
    """
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, item):
        """Add an element to the rear of the queue. Time Complexity: O(1)"""
        # TODO: Implement this method
        pass

    def dequeue(self):
        """Remove and return the front element of the queue. Time Complexity: O(1)"""
        # TODO: Implement this method
        pass

    def peek(self):
        """Return the front element without removing it. Time Complexity: O(1)"""
        # TODO: Implement this method
        pass

    def is_empty(self) -> bool:
        """Check if the queue is empty. Time Complexity: O(1)"""
        # TODO: Implement this method
        pass

    def size(self) -> int:
        """Return the current size of the queue. Time Complexity: O(1)"""
        return self._size


if __name__ == "__main__":
    print("--- Testing Queue Using Linked List ---")
    q = Queue()
    
    print("Enqueuing 10, 20, 30...")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    print(f"Queue Size (Expected 3): {q.size()}")
    print(f"Front element (Expected 10): {q.peek()}")
    
    print(f"Dequeued (Expected 10): {q.dequeue()}")
    print(f"Dequeued (Expected 20): {q.dequeue()}")
    print(f"Front element now (Expected 30): {q.peek()}")
    print(f"Is queue empty? (Expected False): {q.is_empty()}")
    
    print(f"Dequeued (Expected 30): {q.dequeue()}")
    print(f"Is queue empty? (Expected True): {q.is_empty()}")
