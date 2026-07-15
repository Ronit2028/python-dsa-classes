from typing import Tuple, Optional

class Node:
    """
    Singly Linked List Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_alternate(first: Optional[Node], second: Optional[Node]) -> Tuple[Optional[Node], Optional[Node]]:
    """
    Merge the nodes of the second list into the first list at alternate positions.
    Returns a tuple of (head_of_merged_first_list, head_of_remaining_second_list).
    
    Example:
    first:  1 -> 3 -> 5 -> None
    second: 2 -> 4 -> 6 -> 8 -> 10 -> None
    Merged first:  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
    Remaining second: 8 -> 10 -> None
    
    Time Complexity: O(min(N1, N2))
    Space Complexity: O(1)
    """
    # TODO: Implement this function.
    # Traverse both lists, save next pointers, and stitch them in alternate fashion.
    return first, second


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
    if not head:
        print("None")
        return
    elements = []
    current = head
    while current:
        elements.append(str(current.data))
        current = current.next
    print(" -> ".join(elements) + " -> None")


if __name__ == "__main__":
    print("--- Testing Merge Alternate Positions ---")
    
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6, 8, 10])
    
    print("First list:")
    print_list(list1)
    print("Second list:")
    print_list(list2)
    
    merged, remaining = merge_alternate(list1, list2)
    
    print("\nAfter Merging:")
    print("Merged first list (Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None):")
    print_list(merged)
    print("Remaining second list (Expected: 8 -> 10 -> None):")
    print_list(remaining)
