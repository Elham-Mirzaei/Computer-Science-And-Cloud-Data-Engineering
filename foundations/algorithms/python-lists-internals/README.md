# Python Lists Internals

## Overview

This document explains how Python lists work internally, how dynamic arrays operate, and the time complexity of common list operations.

## 1. Arrays and Memory

An array stores elements in consecutive memory locations.

Because the computer can calculate an element's location directly using its index, accessing an element takes **O(1)** time.

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[3])  # 40
```

## 2. Dynamic Arrays

Python lists use a dynamic-array implementation.

They can grow when more space is needed. Python occasionally allocates a larger memory area and transfers existing references.

This allows lists to grow without requiring a fixed size in advance.

## 3. Python List Operations

| Operation | Time Complexity |
|---|---|
| Access by index | O(1) |
| Modify by index | O(1) |
| Append to end | O(1) amortized |
| Insert at beginning | O(n) |
| Remove from beginning | O(n) |
| Remove from end | O(1) |
| Search for a value | O(n) |

### Important concepts

- **O(1) indexing:** The element's location can be calculated directly.
- **O(n) insertion at the beginning:** Existing elements must shift.
- **Amortized O(1) append:** Most appends are constant time, but occasional resizing takes O(n).

## 4. Practical Example

```python
def build_customer_list(customer_ids):
    results = []

    for customer_id in customer_ids:
        results.append(customer_id)

    return results
```

- Time complexity: O(n) amortized.
- Space complexity: O(n).

Using `append()` is generally more efficient than repeatedly inserting elements at the beginning.

## 5. Key Takeaways

- Python lists are dynamic arrays of object references.
- Index access is O(1).
- Inserting at the beginning is O(n).
- Appending is O(1) amortized.
- Choosing the right operation matters when processing large datasets.

## Learning Progress

- **Status:** Completed
- **Month:** 1 — Computer Science Foundations
- **Topic:** Data Structures
- **Next:** Python Dictionaries and Hash Tables Internally
