class DoublyNode:
    """
    Doubly Linked List Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def reverse_doubly_list(head: DoublyNode) -> DoublyNode:
    """
    Reverse a Doubly Linked List in-place.
    Returns the new head of the reversed list.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    # TODO: Implement this function by swapping 'prev' and 'next' pointers for all nodes
    pass


# ==================================================
# Helper Functions for Testing
# ==================================================

def create_doubly_linked_list(arr):
    if not arr:
        return None
    head = DoublyNode(arr[0])
    current = head
    for val in arr[1:]:
        new_node = DoublyNode(val)
        current.next = new_node
        new_node.prev = current
        current = new_node
    return head

def print_list_forward(head):
    elements = []
    current = head
    while current:
        elements.append(str(current.data))
        current = current.next
    print("None <-> " + " <-> ".join(elements) + " <-> None")


if __name__ == "__main__":
    print("--- Testing Reverse Doubly Linked List ---")
    
    # Test Case 1: (10 <-> 20 <-> 30 <-> 40) -> Expected: (40 <-> 30 <-> 20 <-> 10)
    list1 = create_doubly_linked_list([10, 20, 30, 40])
    print("Original list:")
    print_list_forward(list1)
    
    reversed_head = reverse_doubly_list(list1)
    print("Reversed list (Expected: None <-> 40 <-> 30 <-> 20 <-> 10 <-> None):")
    print_list_forward(reversed_head)
