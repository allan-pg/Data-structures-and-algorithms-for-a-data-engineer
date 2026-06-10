# HashMaps (Dictionaries in Python)

## What is a HashMap?

A **HashMap** is a data structure that stores data as **key-value pairs**.

- **Key** → A unique identifier
- **Value** → The data associated with that key

Think of it like a real-world dictionary:

| Key | Value |
|------|---------|
| "apple" | "A fruit" |
| "car" | "A vehicle" |
| "python" | "A programming language" |

In Python, HashMaps are implemented using **dictionaries (`dict`)**.

```python
student = {
    "name": "Brian",
    "age": 25,
    "country": "Kenya"
}

print(student["name"])  # Brian
```

---

# Why Are HashMaps So Powerful?

HashMaps trade a little extra memory for **extremely fast lookups**.

Instead of scanning through every element one by one like a list, a HashMap uses a **hash function** to determine where data should be stored and retrieved.

This allows most operations to happen in:

**O(1) Average Time Complexity**

Meaning the operation takes roughly the same amount of time whether there are:

- 10 items
- 1,000 items
- 1,000,000 items

---

# HashMap vs List

| Feature | List | HashMap (Dictionary) |
|----------|----------|----------|
| Lookup | O(n) | O(1) average |
| Insert | O(1) at end, O(n) in middle | O(1) average |
| Delete | O(n) | O(1) average |
| Search | O(n) | O(1) average |
| Duplicate Detection | O(n) | O(1) average |
| Ordering | Ordered | Ordered (Python 3.7+) |
| Best Use Case | Storing collections of items | Fast lookups and mappings |

---

# Example: Lookup

## Using a List

To find a number in a list, Python may need to scan through the entire list.

```python
nums = [3, 5, 7, 9, 11]

target = 9

for num in nums:
    if num == target:
        print("Found")
```

### Time Complexity

```text
O(n)
```

Worst case:

- Target is last element
- Target doesn't exist

---

## Using a HashMap

```python
nums = {
    3: True,
    5: True,
    7: True,
    9: True,
    11: True
}

print(9 in nums)
```

### Time Complexity

```text
O(1) Average
```

Python can jump directly to where the value should be.

---

# Common HashMap Use Cases

## 1. Fast Lookups

```python
users = {
    101: "Brian",
    102: "John",
    103: "Sarah"
}

print(users[102])
```

Output:

```text
John
```

---

## 2. Counting Frequencies

A very common interview problem.

```python
word = "banana"

count = {}

for char in word:
    count[char] = count.get(char, 0) + 1

print(count)
```

Output:

```python
{
    'b': 1,
    'a': 3,
    'n': 2
}
```

---

## 3. Detecting Duplicates

### Without HashMap

```python
nums = [3, 5, 7, 3]

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            print("Duplicate found")
```

Time Complexity:

```text
O(n²)
```

---

### With HashMap

```python
nums = [3, 5, 7, 3]

seen = {}

for num in nums:
    if num in seen:
        print("Duplicate found")
        break

    seen[num] = True
```

Time Complexity:

```text
O(n)
```

---

## 4. Solving Two Sum

This is one of the most famous interview questions.

```python
nums = [3, 2, 4]
target = 6

seen = {}

for index, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        print(seen[complement], index)

    seen[num] = index
```

Output:

```text
1 2
```

Time Complexity:

```text
O(n)
```

Instead of comparing every pair of numbers using nested loops (`O(n²)`), we use a HashMap to remember previously seen numbers.

---

# Understanding `seen[num] = index`

Example:

```python
nums = [3, 5, 7]

seen = {}

for index, num in enumerate(nums):
    seen[num] = index
```

After the loop:

```python
{
    3: 0,
    5: 1,
    7: 2
}
```

What happened?

| Number (Key) | Index (Value) |
|-------------|-------------|
| 3 | 0 |
| 5 | 1 |
| 7 | 2 |

The HashMap remembers:

> "I saw number 3 at index 0"

> "I saw number 5 at index 1"

> "I saw number 7 at index 2"

This allows us to instantly find where a number was previously seen.

---

# What is Enumerate?

`enumerate()` is a built-in Python function that allows you to loop through an iterable while automatically keeping track of the index.

Without `enumerate()`:

```python
nums = [10, 20, 30]

index = 0

for num in nums:
    print(index, num)
    index += 1
```

---

With `enumerate()`:

```python
nums = [10, 20, 30]

for index, num in enumerate(nums):
    print(index, num)
```

Output:

```text
0 10
1 20
2 30
```

---

# How Enumerate Works

Internally, `enumerate()` creates pairs:

```python
(0, 10)
(1, 20)
(2, 30)
```

When you write:

```python
for index, num in enumerate(nums):
```

Python unpacks each tuple into:

```python
index = 0
num = 10

index = 1
num = 20

index = 2
num = 30
```

---

# Why Enumerate Is Useful

Many problems require both:

- The value
- The position of the value

Instead of manually tracking a counter, `enumerate()` does it automatically.

Example:

```python
names = ["Brian", "John", "Sarah"]

for index, name in enumerate(names):
    print(f"{index}: {name}")
```

Output:

```text
0: Brian
1: John
2: Sarah
```

---

# HashMaps + Enumerate = Powerful Combination

Many efficient algorithms use both together.

Example:

```python
nums = [3, 5, 7, 3, 9, 5, 7, 3]

seen = {}

for index, num in enumerate(nums):

    if num in seen:
        print(
            f"Number {num} is a duplicate at index {index}"
        )
    else:
        seen[num] = index
```

Output:

```text
Number 3 is a duplicate at index 3
Number 5 is a duplicate at index 5
Number 7 is a duplicate at index 6
Number 3 is a duplicate at index 7
```

The HashMap remembers previously seen values, while `enumerate()` tells us where they occur.

---

# Key Takeaways

HashMaps store data as key-value pairs.

Python implements HashMaps using dictionaries (`dict`).

HashMaps provide O(1) average lookup, insert, and delete operations.

HashMaps are ideal for:
- Fast lookups
- Duplicate detection
- Frequency counting
- Joins and mappings
- Interview problems like Two Sum

`enumerate()` allows you to access both the index and value while iterating.

Combining HashMaps and `enumerate()` often reduces solutions from **O(n²)** to **O(n)**.

One of the biggest skills in Data Structures & Algorithms is learning when a problem can be optimized using a HashMap.