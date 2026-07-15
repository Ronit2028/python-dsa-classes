class Node:
    """
    Singly Linked List Node
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def count_occurrences(head: Node, key) -> int:
    """
    Count the number of times the given key appears in the singly linked list.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    # TODO: Implement this function by traversing the list and counting matches.
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
    print("--- Testing Count Occurrences ---")
    
    # Test Case 1: List (1 -> 2 -> 1 -> 2 -> 1 -> 3 -> 1), key = 1 -> Expected: 4
    list1 = create_linked_list([1, 2, 1, 2, 1, 3, 1])
    print("List:")
    print_list(list1)
    
    count = count_occurrences(list1, 1)
    print(f"Occurrences of 1 (Expected 4): {count}")
    
    # Test Case 2: key = 5 (not in list) -> Expected: 0
    count2 = count_occurrences(list1, 5)
    print(f"Occurrences of 5 (Expected 0): {count2}")
