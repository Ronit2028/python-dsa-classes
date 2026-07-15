class Node:
    """
    Singly Linked List Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def find_nth_from_end(head: Node, n: int) -> Node:
    """
    Find the N-th node from the end of the singly linked list (1-indexed).
    If N is greater than the length of the list, return None.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    # TODO: Implement this function using two pointers.
    # 1. Move 'ref_ptr' by N nodes.
    # 2. If 'ref_ptr' becomes None before N nodes, return None.
    # 3. Move both 'ref_ptr' and 'main_ptr' until 'ref_ptr' reaches the end.
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
    print("--- Testing N-th Node from End ---")
    
    # Test Case 1: (1 -> 2 -> 3 -> 4 -> 5), n = 2 -> Expected: Node(4)
    list1 = create_linked_list([1, 2, 3, 4, 5])
    print("List:")
    print_list(list1)
    
    node = find_nth_from_end(list1, 2)
    print(f"2nd node from end (Expected 4): {node.data if node else 'None'}\n")

    # Test Case 2: (1 -> 2 -> 3 -> 4 -> 5), n = 5 -> Expected: Node(1)
    node = find_nth_from_end(list1, 5)
    print(f"5th node from end (Expected 1): {node.data if node else 'None'}\n")

    # Test Case 3: Out of bounds (1 -> 2 -> 3), n = 5 -> Expected: None
    list2 = create_linked_list([1, 2, 3])
    node = find_nth_from_end(list2, 5)
    print(f"5th node from end on length 3 (Expected None): {node}")
