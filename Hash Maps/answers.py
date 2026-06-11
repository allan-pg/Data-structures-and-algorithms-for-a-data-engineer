
### 1. Count Character Frequency

```python
s = 'banana'
count = {}

# loop through each character in s this is O(n) linear time complexity 
for char in s:
    """ check if char is a key in count and if yes add 1 
        to the value if no set the value as 1
    """

    if char in count:
        count[char] += 1
    else:
        count[char] = 1
        
print(count)   
```

---

### 2. Count how many times each word appears.

```python
fruits = ["apple", "banana", "apple", "orange"]

count = {}

# loop though your list O(n) linear time complexity
for fruit in fruits:
    """ check if the key is in count e.g is apple in count and if yes 
        add 1 to value if no set value as 1 """
    
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1
        
print(count)
```