# HashMap Practice Questions

---

# Level 1: HashMap Fundamentals

Learn how to store, retrieve, and update key-value pairs.

### 1. Count Character Frequency 

**Problem**

Count the occurrences of each character in a string.

**Example**

```python
banana
```

**Expected Output**

```python
{
    "b": 1,
    "a": 3,
    "n": 2
}
```

---

### 2. Count Word Frequency 

**Problem**

Count how many times each word appears.

**Example**

```python
["apple", "banana", "apple", "orange"]
```


### 3. Find First Duplicate 

**Problem**

Return the first duplicate value.

**Example**

```python
[3,5,7,2,5,9]
```

**Expected Output**

```python
5
```

### 4. Remove Duplicates

**Problem**

Remove duplicate values while preserving order.

**Example**

```python
[1,2,3,1,2,4]
```

**Expected Output**

```python
[1,2,3,4]
```

### 5. Contains Duplicate 

**Problem**

Return True if duplicates exist.

**Example**

```python
[1,2,3,4,2]
```

**Expected Output**

```python
True
```

# Level 2: HashMap Lookup Optimization

Learn how HashMaps reduce O(n²) solutions to O(n).

### 6. Two Sum

**Problem**

Find two numbers that add up to a target.

**Example**

```python
nums = [2,7,11,15]
target = 9
```

**Expected Output**

```python
[0,1]
```


### 7. Find Missing Number

**Problem**

Find the missing number from a sequence.

**Example**

```python
[0,1,3]
```

**Expected Output**

```python
2
```


### 8. Group Anagrams

**Problem**

Group words that are anagrams.

**Example**

```python
["eat","tea","ate","cat"]
```


### 9. Top K Frequent Elements

**Problem**

Return the K most common values.

**Example**

```python
[1,1,1,2,2,3]
```

**Expected Output**

```python
[1,2]
```

### 10. Majority Element

**Problem**

Find the number that appears more than n/2 times.

**Input**

```python
nums = [2,2,1,2,2]
```

**Output**

```python
2
```


### 11. Deduplicate Customer Records


**Problem**

Remove duplicate customers based on customer_id.

**Input**

```python
customers = [
    {"customer_id": 1, "name": "Brian"},
    {"customer_id": 2, "name": "John"},
    {"customer_id": 1, "name": "Brian"}
]
```

**Output**

```python
[
    {"customer_id": 1, "name": "Brian"},
    {"customer_id": 2, "name": "John"}
]
```

**Concepts**

- Deduplication
- Primary Keys

---

### 12. Build a Lookup Table

**Problem**

Convert a customer list into a lookup dictionary.

**Input**

```python
customers = [
    {"customer_id": 1, "name": "Brian"},
    {"customer_id": 2, "name": "John"}
]
```

**Output**

```python
{
    1: {"customer_id": 1, "name": "Brian"},
    2: {"customer_id": 2, "name": "John"}
}
```

### 13. Perform an In-Memory Join

**Problem**

Join customers and orders using a HashMap.

**Input**

```python
customers = [
    {"customer_id": 1, "name": "Brian"},
    {"customer_id": 2, "name": "John"}
]

orders = [
    {"customer_id": 1, "amount": 100},
    {"customer_id": 2, "amount": 200}
]
```

**Output**

```python
[
    {"customer_id": 1, "name": "Brian", "amount": 100},
    {"customer_id": 2, "name": "John", "amount": 200}
]
```


### 14. Aggregate Sales by Product

**Problem**

Calculate total sales per product.

**Input**

```python
sales = [
    ("Laptop", 500),
    ("Phone", 200),
    ("Laptop", 300)
]
```

**Output**

```python
{
    "Laptop": 800,
    "Phone": 200
}
```


### 15. Find Duplicate Invoice IDs

**Problem**

Identify duplicate invoice IDs.

**Input**

```python
invoice_ids = [1001,1002,1003,1002,1004]
```

**Output**

```python
[1002]
```


### 16. Streaming Event Counter

**Problem**

Count incoming events.

**Input**

```python
events = [
    "login",
    "logout",
    "login",
    "purchase"
]
```

**Output**

```python
{
    "login": 2,
    "logout": 1,
    "purchase": 1
}
```


### 17. Sessionization by User

**Problem**

Group events by user.

**Input**

```python
events = [
    ("user1", "login"),
    ("user1", "view_product"),
    ("user2", "login"),
    ("user1", "checkout")
]
```

**Output**

```python
{
    "user1": [
        "login",
        "view_product",
        "checkout"
    ],
    "user2": [
        "login"
    ]
}
```

### 18. Build an SCD Lookup Table

**Problem**

Keep only the latest customer version.

**Input**

```python
customers = [
    {"customer_id": 1, "name": "Brian"},
    {"customer_id": 1, "name": "Brian Mwangi"},
    {"customer_id": 2, "name": "John"}
]
```

**Output**

```python
{
    1: {"customer_id": 1, "name": "Brian Mwangi"},
    2: {"customer_id": 2, "name": "John"}
}
```

### 19. Streaming Deduplication

**Problem**

Remove duplicate events.

**Input**

```python
events = [
    {"event_id": 1},
    {"event_id": 2},
    {"event_id": 1},
    {"event_id": 3}
]
```

**Output**

```python
[
    {"event_id": 1},
    {"event_id": 2},
    {"event_id": 3}
]
```

### 20. Build a Hash Join from Scratch

**Problem**

Implement SQL JOIN behavior using HashMaps.

**Input**

```python
customers = [
    {"customer_id": 1, "name": "Brian"},
    {"customer_id": 2, "name": "John"}
]

orders = [
    {"order_id": 101, "customer_id": 1},
    {"order_id": 102, "customer_id": 2}
]
```

**Output**

```python
[
    {
        "order_id": 101,
        "customer_id": 1,
        "name": "Brian"
    },
    {
        "order_id": 102,
        "customer_id": 2,
        "name": "John"
    }
]
```