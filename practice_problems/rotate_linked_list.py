class Node:
    """
    Singly Linked List Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def rotate_list(head: Node, k: int) -> Node:
    """
    Rotate the singly linked list counter-clockwise by k nodes.
    For example: 
    Input:  10 -> 20 -> 30 -> 40 -> 50 -> 60 -> None, k = 4
    Output: 50 -> 60 -> 10 -> 20 -> 30 -> 40 -> None
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    # TODO: Implement this function.
    # 1. Handle base cases: empty list, single node, or k = 0.
    # 2. Find the length and make the list circular.
    # 3. Find the new tail (k % length) node and break the circle at the new head.
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
    print("--- Testing Rotate Linked List ---")
    
    # Test Case 1: List (10->20->30->40->50->60), k=4 -> Expected: (50->60->10->20->30->40)
    list1 = create_linked_list([10, 20, 30, 40, 50, 60])
    print("Original list:")
    print_list(list1)
    
    rotated_head = rotate_list(list1, 4)
    print("Rotated list by k=4 (Expected: 50 -> 60 -> 10 -> 20 -> 30 -> 40 -> None):")
    print_list(rotated_head)
