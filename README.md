# Algorithms and Data Structures - Homework 02

This repository contains solutions for homework assignment 02, focusing on **Divide and Conquer** and **Greedy Algorithms**.

## Assignment Overview

This homework consists of two independent algorithmic tasks:

1. **Task 1**: Finding Maximum and Minimum Elements using Divide and Conquer
2. **Task 2**: 3D Printer Queue Optimization using Greedy Algorithm

## Task 1: Finding Maximum and Minimum Elements

### Description
Implements a function that finds both the maximum and minimum elements in an array using the **divide and conquer** approach.

### Key Features
- **Recursive approach**: Divides the array into smaller subarrays
- **Time complexity**: O(n)
- **Space complexity**: O(log n) due to recursion stack
- **Returns**: Tuple `(minimum, maximum)`

### Algorithm Explanation
1. **Base cases**:
   - Single element: return `(element, element)`
   - Two elements: compare and return `(min, max)`
2. **Divide**: Split array into two halves
3. **Conquer**: Recursively find min/max in each half
4. **Combine**: Compare results from both halves to get overall min/max

### Usage
```bash
python task1.py
```

### Example
```python
from task1 import find_min_max

arr = [3, 1, 4, 1, 5, 9, 2, 6]
min_val, max_val = find_min_max(arr)
print(f"Minimum: {min_val}, Maximum: {max_val}")
# Output: Minimum: 1, Maximum: 9
```

## Task 2: 3D Printer Queue Optimization

### Description
Optimizes a 3D printing queue considering job priorities and printer constraints (maximum volume and maximum items per batch) using a **greedy algorithm**.

### Priority Levels
- **Priority 1** (Highest): Thesis/Diploma projects
- **Priority 2** (Medium): Lab work
- **Priority 3** (Lowest): Personal projects

### Key Features
- **Greedy approach**: Sorts jobs by priority, then by volume
- **Batching**: Groups multiple models for simultaneous printing
- **Constraint handling**: Respects `max_volume` and `max_items` limits
- **Time calculation**: Batch time = max(print_time) of jobs in batch
- **Data structures**: Uses Python `dataclass` for type safety

### Algorithm Explanation
1. **Sort jobs**:
   - Primary key: Priority (ascending, so 1 comes first)
   - Secondary key: Volume (ascending, for better packing)
2. **Batch creation**:
   - Try to add each job to current batch
   - Check volume and item constraints
   - If constraints exceeded, start new batch
3. **Time calculation**:
   - Each batch takes time = max print time of jobs in that batch
   - Total time = sum of all batch times

### Usage
```bash
python task2.py
```

### Example
```python
from task2 import optimize_printing

jobs = [
    {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
    {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
    {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}
]

constraints = {
    "max_volume": 300,
    "max_items": 2
}

result = optimize_printing(jobs, constraints)
print(f"Print order: {result['print_order']}")
print(f"Total time: {result['total_time']} minutes")
# Output:
# Print order: ['M2', 'M1', 'M3']
# Total time: 270 minutes
```

## Test Cases

Both tasks include comprehensive test cases that verify:

### Task 1 Tests
- Regular arrays
- Single element arrays
- Two element arrays
- Negative numbers
- Mixed positive/negative numbers
- Arrays with duplicate elements
- Floating point numbers
- Large arrays

### Task 2 Tests
- **Test 1**: Jobs with same priority
- **Test 2**: Jobs with different priorities
- **Test 3**: Volume constraints exceeded (jobs must print separately)
- **Test 4**: All jobs fit in one batch
- **Test 5**: Max items constraint exceeded

## Requirements

- Python 3.7 or higher (for dataclasses support)
- Standard library only (no external dependencies)

## File Structure

```
goit-algo2-hw-02/
├── README.md           # This file
├── task1.py           # Divide and Conquer: Min/Max finder
└── task2.py           # Greedy Algorithm: Printer queue optimization
```

## Running Tests

Each task file can be run independently to execute its test suite:

```bash
# Test Task 1
python task1.py

# Test Task 2
python task2.py
```
