# Python Sets and Hash Tables

## Overview
Python sets store unique, hashable elements using a hash-table-based structure.

## Key Concepts
- Sets contain unique elements and have no guaranteed iteration order.
- Hashing enables average O(1) membership checks.
- Elements must be hashable. Lists and dictionaries cannot be set elements.
- Hash collisions are handled through probing and equality checks.

## Set Operations

| Operation | Meaning |
|---|---|
| `A | B` | Union |
| `A & B` | Intersection |
| `A - B` | Difference |
| `A ^ B` | Symmetric difference |

## Time and Space Complexity

| Operation | Average complexity |
|---|---|
| Membership | O(1) |
| Add / Remove | O(1) |
| Build set from n items | O(n) |
| Iterate | O(n) |
| Storage | O(n) |

## Data Engineering Applications
- Removing duplicate IDs.
- Checking whether records exist.
- Tracking processed transactions.
- Comparing datasets using set operations.

## Learning Progress
- [x] Hash-based set implementation
- [x] Membership and uniqueness
- [x] Hash collisions
- [x] Set operations
- [x] Time and space complexity
- [x] Dataset comparison exercise
