class Node:
    """
    Singly Linked List Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head: Node) -> Node:
    """
    Find the middle of the linked list.
    If the list has an even number of nodes, return the second middle node.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    # TODO: Implement this function using the two-pointer approach (slow & fast)
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
    print("--- Testing Middle of Linked List ---")
    
    # Test Case 1: Odd length (1 -> 2 -> 3 -> 4 -> 5) -> Expected: 3
    list1 = create_linked_list([1, 2, 3, 4, 5])
    print("List 1:")
    print_list(list1)
    mid1 = find_middle(list1)
    print(f"Middle node value (Expected 3): {mid1.data if mid1 else 'None'}\n")
    
    # Test Case 2: Even length (1 -> 2 -> 3 -> 4 -> 5 -> 6) -> Expected: 4
    list2 = create_linked_list([1, 2, 3, 4, 5, 6])
    print("List 2:")
    print_list(list2)
    mid2 = find_middle(list2)
    print(f"Middle node value (Expected 4): {mid2.data if mid2 else 'None'}\n")

    # Test Case 3: Empty List -> Expected: None
    mid3 = find_middle(None)
    print(f"Middle node of empty list (Expected None): {mid3}")
