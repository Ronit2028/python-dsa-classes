# Linked Lists

This directory contains the theory and implementations for one of the most fundamental data structures in computer science: **Linked Lists**.

---

## 1. Singly Linked List

A **Singly Linked List** is a linear data structure where elements (called **Nodes**) are stored in sequence. Unlike arrays, nodes are not stored in contiguous memory locations. Instead, each node points to the next node in the sequence via a reference pointer. The final node points to `None`, indicating the end of the list.

### Node Structure
Each node contains:
1. **Data**: The value stored in the node.
2. **Next**: A pointer or reference to the next node in the list.

```mermaid
graph LR
    Head((Head)) --> Node1
    subgraph Node 1
        Node1[Data: 10 | Next]
    end
    subgraph Node 2
        Node2[Data: 20 | Next]
    end
    subgraph Node 3
        Node3[Data: 30 | Next]
    end
    Node1 --> Node2
    Node2 --> Node3
    Node3 --> Null[None / Null]
```

### Core Operations and Time Complexities

- **Insertion at Beginning**: $O(1)$ - Simply point the new node's next reference to the current head, and set it as the new head.
- **Insertion at End**: $O(N)$ (or $O(1)$ if a tail reference is maintained) - Traverse to the end of the list and update the last node's next reference.
- **Deletion by Value**: $O(N)$ - Traverse to locate the node, keeping track of the previous node to bridge the gap.
- **Search**: $O(N)$ - Linearly traverse from the head until the key is found or the end is reached.
- **Traversal**: $O(N)$ - Visit every node from the head to the end.

---

## 2. Doubly Linked List

A **Doubly Linked List** extends the singly linked list by adding an extra pointer to each node that points to the **previous** node. This allows bidirectional traversal (forward and backward).

### Node Structure
Each node contains:
1. **Prev**: Reference to the previous node.
2. **Data**: The value stored in the node.
3. **Next**: Reference to the next node.

```mermaid
graph LR
    None1[None] <--> Node1[Prev | Data: 100 | Next] <--> Node2[Prev | Data: 200 | Next] <--> None2[None]
```

### Advantages & Disadvantages
- **Advantages**:
  - Can be traversed in both directions.
  - Deletion operation is more efficient if the node to be deleted is already given (since we have access to the previous node in $O(1)$ time).
- **Disadvantages**:
  - Extra memory required for the `prev` pointer.
  - Slightly more overhead during insertion/deletion to maintain extra pointers.

---

## 3. Complexity Comparison Table

| Operation | Array / Dynamic Array | Singly Linked List | Doubly Linked List |
| :--- | :--- | :--- | :--- |
| **Access / Search** | $O(1)$ (using index) | $O(N)$ | $O(N)$ |
| **Insert / Delete at Start** | $O(N)$ (shifting required) | $O(1)$ | $O(1)$ |
| **Insert / Delete at End** | $O(1)$ (amortized) | $O(N)$ (without tail) / $O(1)$ (with tail) | $O(1)$ (with tail) |
| **Insert / Delete in Middle** | $O(N)$ (shifting required) | $O(N)$ (search time) | $O(N)$ (search time) |
| **Memory Overhead** | Low (contiguous block) | Medium (one pointer per node) | High (two pointers per node) |

---

## 4. Classic Algorithms & Techniques

### Reversing a Linked List
Reversing a singly linked list in-place is done by traversing the list and swapping the next pointer of each node to point to its predecessor.
- **Iterative Approach**: Maintain three pointers: `prev`, `curr`, and `nxt`. Update pointers in a loop. Time Complexity: $O(N)$, Space Complexity: $O(1)$.

### Cycle Detection (Floyd's Cycle-Finding Algorithm)
Determines if a linked list contains a loop (cycle).
- **Floyd's Tortoise and Hare**: Maintain two pointers: a slow pointer moving one step at a time, and a fast pointer moving two steps at a time. If they meet, a cycle exists. If the fast pointer hits `None`, no cycle exists. Time Complexity: $O(N)$, Space Complexity: $O(1)$.

---

## 5. Implementations Overview

In [linked_list.py](file:///Users/ronitjaiprakash/Desktop/Classes/linked_list/linked_list.py), we provide:
1. **SinglyLinkedList**: Standard singly linked list with insertion, deletion, searching, reversing, and cycle detection.
2. **DoublyLinkedList**: Standard doubly linked list with bidirectional insertion and traversal.

### How to Run:
```bash
python3 linked_list/linked_list.py
```
