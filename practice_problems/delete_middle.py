class Node:
    """
    Singly Linked List Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_middle(head: Node) -> Node:
    """
    Delete the middle node of the singly linked list.
    If the list has 1 node, it becomes empty, return None.
    If there are even number of nodes, delete the second middle node.
    Returns the head of the updated list.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    # TODO: Implement this function.
    # 1. Base cases: empty or single node list.
    # 2. Use two pointers slow and fast, keeping track of the predecessor of slow.
    # 3. Unlink the slow node.
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
    print("--- Testing Delete Middle ---")
    
    # Test Case 1: (1 -> 2 -> 3 -> 4 -> 5) -> Expected: (1 -> 2 -> 4 -> 5)
    list1 = create_linked_list([1, 2, 3, 4, 5])
    print("Original list:")
    print_list(list1)
    updated_head = delete_middle(list1)
    print("After deleting middle (Expected: 1 -> 2 -> 4 -> 5 -> None):")
    print_list(updated_head)
    
    # Test Case 2: (1 -> 2 -> 3 -> 4) -> Expected: (1 -> 2 -> 4)
    list2 = create_linked_list([1, 2, 3, 4])
    print("\nOriginal list:")
    print_list(list2)
    updated_head2 = delete_middle(list2)
    print("After deleting middle (Expected: 1 -> 2 -> 4 -> None):")
    print_list(updated_head2)
