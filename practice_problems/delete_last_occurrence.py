class Node:
    """
    Singly Linked List Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_last_occurrence(head: Node, key) -> Node:
    """
    Delete the last occurrence of the given key in the singly linked list.
    Returns the head of the updated list.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    # TODO: Implement this function.
    # Traverse the list and remember:
    # 1. The last node that matched the key.
    # 2. The node preceding that last node.
    pass


# ==================================================
# Helper Functions for Testing
# ==================================================

def create_linked_list(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_list(head):
    elements = []
    current = head
    while current:
        elements.append(str(current.data))
        current = current.next
    print(" -> ".join(elements) + " -> None")


if __name__ == "__main__":
    print("--- Testing Delete Last Occurrence ---")
    
    # Test Case 1: (1 -> 2 -> 3 -> 2 -> 4 -> 2 -> 5), delete last occurrence of 2 -> Expected: (1 -> 2 -> 3 -> 2 -> 4 -> 5)
    list1 = create_linked_list([1, 2, 3, 2, 4, 2, 5])
    print("Original list:")
    print_list(list1)
    
    updated_head = delete_last_occurrence(list1, 2)
    print("After deleting last occurrence of 2 (Expected: 1 -> 2 -> 3 -> 2 -> 4 -> 5 -> None):")
    print_list(updated_head)
    
    # Test Case 2: (2 -> 2 -> 2), delete last occurrence of 2 -> Expected: (2 -> 2)
    list2 = create_linked_list([2, 2, 2])
    print("\nOriginal list:")
    print_list(list2)
    updated_head2 = delete_last_occurrence(list2, 2)
    print("After deleting last occurrence of 2 (Expected: 2 -> 2 -> None):")
    print_list(updated_head2)
