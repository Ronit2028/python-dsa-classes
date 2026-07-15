class Node:
    """
    Singly Linked List Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def traverse_circular_list(head: Node) -> list:
    """
    Traverse a circular linked list and return a list of its elements.
    If the list is empty, return an empty list.
    
    Time Complexity: O(N)
    Space Complexity: O(N) (to store returned list)
    """
    # TODO: Implement this function.
    # Note: Keep in mind the last node points back to the head node.
    pass


# ==================================================
# Helper Functions for Testing
# ==================================================

def create_circular_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    current.next = head  # Link back to head to make it circular
    return head


if __name__ == "__main__":
    print("--- Testing Circular Linked List Traversal ---")
    
    # Create circular list: 10 -> 20 -> 30 -> 40 -> (back to 10)
    circular_head = create_circular_list([10, 20, 30, 40])
    
    elements = traverse_circular_list(circular_head)
    print("Traversed Elements (Expected: [10, 20, 30, 40]):")
    print(elements)
    
    # Asserting correctness once the user implements it:
    # assert elements == [10, 20, 30, 40]
