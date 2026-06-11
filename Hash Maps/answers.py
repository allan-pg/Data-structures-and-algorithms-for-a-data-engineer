
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

---

### 3. Return the first duplicate value.


---

### 4. Remove duplicate values while preserving order.

```python
# First approach
duplicated_list = [1,2,3,1,2,4]

# create an empty list and set- sets do not accept duplicates
seen = set()
deduplicated_list=[]

# iterate through your list this is O(n) time complexity
for num in duplicated_list:
    """check if num is in seen and if not add it to a set then append your empty list
       because a set doesnt keep order so you append elements in list to preserve order
       - appending a list is O(1) constant time complexity since you are adding at the
       end of the list so no element moves
    """
    if num not in seen:
        seen.add(num)
        deduplicated_list.append(num)
        
print(deduplicated_list)
```