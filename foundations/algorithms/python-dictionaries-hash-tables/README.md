# Python Dictionaries and Hash Tables

## Overview
Python dictionaries store key-value pairs using hash tables, enabling efficient data lookup.

## Key Concepts
- **Hash function:** Converts a key into an integer hash value.
- **Hash collision:** Occurs when different keys map to the same initial position.
- **Collision handling:** Python dictionaries use open addressing and probing.
- **Hashable keys:** Integers, strings, and tuples containing hashable elements.
- **Unhashable objects:** Lists and dictionaries.

## Time and Space Complexity

| Operation | Average complexity |
|---|---|
| Lookup | O(1) |
| Insertion | O(1) |
| Build dictionary from n records | O(n) |
| Search in a list | O(n) |
| Storage | O(n) |

## Practical Example

```python
def build_customer_lookup(customers):
    lookup = {}
    for customer in customers:
        lookup[customer["id"]] = customer
    return lookup
```

## Data Engineering Applications
- Looking up records by ID.
- Checking membership efficiently.
- Building mappings between entities.
- Processing structured data.

## Learning Progress
- [x] Hash functions and hash tables
- [x] Hash collisions
- [x] Dictionary internals
- [x] Hashable and unhashable objects
- [x] Time and space complexity
- [x] Customer lookup implementation
