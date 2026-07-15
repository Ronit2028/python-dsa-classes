class Node:
    """
    A class representing a node in a Singly Linked List.
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    A class representing a Singly Linked List.
    """
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """
        Insert a new node with 'data' at the start of the list.
        Time Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node with 'data' at the end of the list.
        Time Complexity: O(N) where N is the number of nodes.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_by_value(self, key):
        """
        Deletes the first node that contains the value 'key'.
        Time Complexity: O(N)
        """
        current = self.head

        # Case 1: The head node itself holds the value to be deleted
        if current and current.data == key:
            self.head = current.next
            return True

        # Case 2: Search for the key, keeping track of the previous node
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # Case 3: Key was not present in the list
        if not current:
            return False

        # Unlink the node from the linked list
        prev.next = current.next
        return True

    def search(self, key):
        """
        Search for a value in the list. Returns True if found, False otherwise.
        Time Complexity: O(N)
        """
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def reverse(self):
        """
        Reverses the linked list in-place.
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        prev = None
        current = self.head
        while current:
            nxt = current.next  # Temporarily store the next node
            current.next = prev  # Reverse the pointer
            prev = current       # Move prev and current one step forward
            current = nxt
        self.head = prev

    def has_cycle(self):
        """
        Detects if the linked list has a cycle using Floyd's Tortoise and Hare algorithm.
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            if slow == fast:
                return True           # Cycle detected
        return False                  # No cycle detected

    def traverse(self):
        """
        Prints the elements of the linked list in order.
        Time Complexity: O(N)
        """
        elements = []
        current = self.head
        
        # Guard against cycle to avoid infinite loop during printing
        visited = set()
        while current:
            if id(current) in visited:
                elements.append(f"Cycle to Node(Val: {current.data})")
                break
            visited.add(id(current))
            elements.append(str(current.data))
            current = current.next
            
        if current is None:
            print(" -> ".join(elements) + " -> None")
        else:
            print(" -> ".join(elements))


# ==========================================
# Doubly Linked List Implementation
# ==========================================

class DoublyNode:
    """
    A class representing a node in a Doubly Linked List.
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to next node
        self.prev = None  # Pointer to previous node


class DoublyLinkedList:
    """
    A class representing a Doubly Linked List.
    """
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """
        Insert a node at the start.
        Time Complexity: O(1)
        """
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a node at the end.
        Time Complexity: O(N)
        """
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def delete_by_value(self, key):
        """
        Deletes the first node that contains the value 'key'.
        Time Complexity: O(N)
        """
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next  # Deleting the head node

                if current.next:
                    current.next.prev = current.prev

                return True
            current = current.next
        return False

    def traverse_forward(self):
        """
        Traverse the list from Head to End.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print("None <-> " + " <-> ".join(elements) + " <-> None")

    def traverse_backward(self):
        """
        Traverse the list from End to Head.
        """
        if not self.head:
            print("List is empty")
            return

        # Go to the end node
        current = self.head
        while current.next:
            current = current.next

        # Traverse backward
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        print("None <-> " + " <-> ".join(elements) + " <-> None (Backward)")


# ==========================================
# Self-Testing Script
# ==========================================

if __name__ == "__main__":
    print("==========================================")
    print("1. Testing Singly Linked List")
    print("==========================================")
    sll = SinglyLinkedList()
    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.insert_at_beginning(5)
    print("Initial SLL:")
    sll.traverse()  # Expected: 5 -> 10 -> 20 -> None
    
    print("Searching for 10:", sll.search(10))  # Expected: True
    print("Searching for 100:", sll.search(100))  # Expected: False
    
    print("Deleting 10...")
    sll.delete_by_value(10)
    sll.traverse()  # Expected: 5 -> 20 -> None

    print("Reversing the list...")
    sll.reverse()
    sll.traverse()  # Expected: 20 -> 5 -> None

    print("Checking for cycle:", sll.has_cycle())  # Expected: False

    print("\nCreating a cycle in the list for testing...")
    # Link the last node back to head to make a cycle
    # Currently sll is: 20 -> 5 -> None. Make it 20 -> 5 -> 20 -> ...
    curr = sll.head
    while curr.next:
        curr = curr.next
    curr.next = sll.head  # 5 points to 20
    
    print("Checking for cycle:", sll.has_cycle())  # Expected: True
    print("Traversing cycle (guarded):")
    sll.traverse()

    print("\n==========================================")
    print("2. Testing Doubly Linked List")
    print("==========================================")
    dll = DoublyLinkedList()
    dll.insert_at_end(100)
    dll.insert_at_end(200)
    dll.insert_at_beginning(50)
    
    print("DLL Forward traversal:")
    dll.traverse_forward()  # Expected: None <-> 50 <-> 100 <-> 200 <-> None
    
    print("DLL Backward traversal:")
    dll.traverse_backward()  # Expected: None <-> 200 <-> 100 <-> 50 <-> None (Backward)

    print("Deleting 100...")
    dll.delete_by_value(100)
    
    print("After deleting 100 (Forward):")
    dll.traverse_forward()  # Expected: None <-> 50 <-> 200 <-> None
    print("After deleting 100 (Backward):")
    dll.traverse_backward()  # Expected: None <-> 200 <-> 50 <-> None (Backward)
    print("==========================================")
    print("All basic linked list tests completed successfully!")
    print("==========================================")
