class Node:
    """
    Singly Linked List Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head: Node) -> Node:
    """
    Reverse the singly linked list in-place.
    Returns the new head of the reversed list.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    # TODO: Implement this function by updating the pointers in-place
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
    print("--- Testing Reverse Linked List ---")
    
    # Test Case 1: Standard List (1 -> 2 -> 3 -> 4 -> 5) -> Expected: 5 -> 4 -> 3 -> 2 -> 1 -> None
    list1 = create_linked_list([1, 2, 3, 4, 5])
    print("Original list:")
    print_list(list1)
    
    reversed_head = reverse_list(list1)
    print("Reversed list (Expected: 5 -> 4 -> 3 -> 2 -> 1 -> None):")
    print_list(reversed_head)
    
    # Test Case 2: Single node
    list2 = create_linked_list([10])
    print("\nOriginal single node list:")
    print_list(list2)
    print_list(reverse_list(list2))
