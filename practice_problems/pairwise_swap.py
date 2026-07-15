class Node:
    """
    Singly Linked List Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def pairwise_swap(head: Node) -> Node:
    """
    Pairwise swap nodes of a singly linked list in-place by changing links.
    Returns the head of the updated list.
    
    Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5 -> None
    Output: 2 -> 1 -> 4 -> 3 -> 5 -> None
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    # TODO: Implement this function by changing the links between nodes.
    # 1. Base case: If list is empty or has only one node, return head.
    # 2. Swap first two nodes and recursively or iteratively swap the rest.
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
    print("--- Testing Pairwise Swap ---")
    
    # Test Case 1: Odd length list (1 -> 2 -> 3 -> 4 -> 5) -> Expected: (2 -> 1 -> 4 -> 3 -> 5)
    list1 = create_linked_list([1, 2, 3, 4, 5])
    print("Original list:")
    print_list(list1)
    
    swapped_head = pairwise_swap(list1)
    print("After pairwise swap (Expected: 2 -> 1 -> 4 -> 3 -> 5 -> None):")
    print_list(swapped_head)
    
    # Test Case 2: Even length list (10 -> 20 -> 30 -> 40) -> Expected: (20 -> 10 -> 40 -> 30)
    list2 = create_linked_list([10, 20, 30, 40])
    print("\nOriginal list:")
    print_list(list2)
    
    swapped_head2 = pairwise_swap(list2)
    print("After pairwise swap (Expected: 20 -> 10 -> 40 -> 30 -> None):")
    print_list(swapped_head2)
