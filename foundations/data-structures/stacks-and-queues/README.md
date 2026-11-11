# Stacks and Queues

## Overview
Stacks and queues are linear data structures that organize elements according to the order in which they are added and removed.

## Stacks (LIFO)
Last In, First Out.

- `push()`: Add an element to the top.
- `pop()`: Remove and return the top element.
- `peek()`: Return the top element without removing it.
- `is_empty()`: Check whether the stack is empty.

**Python implementation:** Lists using `append()` and `pop()`.

## Queues (FIFO)
First In, First Out.

- `enqueue()`: Add an element to the back.
- `dequeue()`: Remove and return the front element.
- `peek()`: Return the front element.
- `is_empty()`: Check whether the queue is empty.

**Python implementation:** `collections.deque`, using `append()` and `popleft()`.

## Time Complexity

| Operation | Complexity |
|---|---|
| Stack push | O(1) amortized |
| Stack pop | O(1) |
| Stack peek | O(1) |
| Queue enqueue (deque) | O(1) |
| Queue dequeue (deque) | O(1) |
| Queue peek | O(1) |
| List pop(0) | O(n) |

## Practical Applications
- Stacks: undo operations, function calls, nested bracket validation.
- Queues: task scheduling, message processing, data pipelines.

## Key Takeaways
- Stacks follow LIFO.
- Queues follow FIFO.
- Python lists work well for stack operations at the end.
- Python deque is more efficient than a list for queue operations at the front.
