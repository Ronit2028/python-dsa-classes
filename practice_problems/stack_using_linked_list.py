class Node:
    """
    Singly Linked List Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """
    LIFO Stack implemented using a Singly Linked List.
    All operations must have O(1) time complexity.
    """
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        """Add an element to the top of the stack. Time Complexity: O(1)"""
        # TODO: Implement this method
        pass

    def pop(self):
        """Remove and return the top element of the stack. Time Complexity: O(1)"""
        # TODO: Implement this method
        pass

    def peek(self):
        """Return the top element of the stack without removing it. Time Complexity: O(1)"""
        # TODO: Implement this method
        pass

    def is_empty(self) -> bool:
        """Check if the stack is empty. Time Complexity: O(1)"""
        # TODO: Implement this method
        pass

    def size(self) -> int:
        """Return the current size of the stack. Time Complexity: O(1)"""
        return self._size


if __name__ == "__main__":
    print("--- Testing Stack Using Linked List ---")
    s = Stack()
    
    print("Pushing 100, 200, 300...")
    s.push(100)
    s.push(200)
    s.push(300)
    
    print(f"Stack Size (Expected 3): {s.size()}")
    print(f"Top element (Expected 300): {s.peek()}")
    
    print(f"Popped (Expected 300): {s.pop()}")
    print(f"Popped (Expected 200): {s.pop()}")
    print(f"Top element now (Expected 100): {s.peek()}")
    print(f"Is stack empty? (Expected False): {s.is_empty()}")
    
    print(f"Popped (Expected 100): {s.pop()}")
    print(f"Is stack empty? (Expected True): {s.is_empty()}")
