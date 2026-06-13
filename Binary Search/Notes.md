# Binary Search

Binary Search is a searching algorithm used to quickly locate a value in a sorted collection. Instead of checking every element one by one,  
Binary Search compares the target with the middle element and eliminates half of the remaining search space after each comparison.  
This makes it one of the most efficient searching algorithms for sorted data.

## When to Use Binary Search

Use Binary Search when: 
* The data is sorted
* Fast lookups are required
* The dataset is large
* Random access to elements is available (such as arrays and lists)

Example:

```python
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]

target = 13
```

Instead of scanning every element, Binary Search repeatedly narrows the search range until the target is found.  
Scanning each element is O(n) linear time complexity since you are checking element by element and comparing that with your target.

---

## How Binary Search Works

Given the sorted array:

```python
[1, 3, 5, 7, 9, 11, 13, 15, 17]
```

Find:

```python
13
```

### Step 1

Check the middle element:

```python
9
```

Since:

```python
13 > 9
```

Ignore everything to the left.

Remaining search space:

```python
[11, 13, 15, 17]
```

### Step 2

Check the middle:

```python
13
```

Target found.

---

## Why It Is Fast

Each comparison removes half of the remaining elements.

Example:

```text
100 elements
50
25
12
6
3
1
```

The number of operations grows logarithmically rather than linearly.

---

## Requirement

The collection must be sorted.

Valid:

```python
[1, 3, 5, 7, 9]
```

Invalid:

```python
[5, 1, 9, 3, 7]
```

Without sorted data, Binary Search cannot determine which half to discard.

---

## Complexity

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(1)            |
| Average Case | O(log n)        |
| Worst Case   | O(log n)        |

Space Complexity:

* Iterative: O(1)
* Recursive: O(log n)

---

## Real-World Applications

- Databases use index structures such as B-Trees to locate records efficiently without scanning every row.
- Query engines use metadata, partition pruning, and indexing techniques that rely on the same divide-and-conquer principles as Binary Search.

---

## Point to Note

* Binary Search works on sorted data.
* Compare against the middle element.
* Eliminate half of the search space each step.
* Time Complexity is O(log n).
* Widely used in databases, search systems, and large-scale data processing.
