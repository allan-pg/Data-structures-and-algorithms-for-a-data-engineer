
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

#### First Approach

```python
# list with duplicate
duplicate = [3,5,7,2,5,9, 3]

seen = set()

#function to get the first item duplicated
def get_first_duplicate(duplicate_list):
    """ Iterate through your list and this is O(n) Linear time complexity
    """
    for num in duplicate_list:
        ## Check if num is in your set called seen if not add it
        if num not in seen:
            seen.add(num)
"""
  When adding an element to set and we find an element already exists
  you output the first element to be duplicated and break out of the 
  loop since you have already found your first element to be 
  duplicated
"""
        else:
            print(f"{num} is first duplicate")
            break

get_first_duplicate(duplicate)     

```
        

#### second approach

```python
duplicate = [3, 5,7,2,5,9, 3]
#create an empty dictionary
seen = {}

## create a function to get the first duplicated num in our case its 5

def get_first_duplicate(duplicated_list):
    """
       use enumerate to get index and value of your list and by looping
       for loops are O(n) time complexity
    """
    
    for index, num in enumerate(duplicated_list):
        """ check if num is in your dictionary if yes thats the first
          duplicate and break out of your loop since you found first
          duplicate and its index is also returned
        """
        if num in seen:
            print(f"{num} is first duplicate found at {index}")
            break
        """ Swap your value with index so for example 3 becomes your index
            and 0 its index becomes value since indexes are unique
        """
        else:
            seen[num] = index
            

get_first_duplicate(duplicate)

```


---

### 4. Remove duplicate values while preserving order.

#### First approach

```python

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

#### second approach

```python
# This is your list you want to remove duplicates
duplicated_list = [1,2,3,1,2,4]

#create a function that removes duplicates from your list
def get_deduplicated_list(duplicates):
    # create an empty dictionary and list
    seen = {}
    dedup_list = []
    # iterate through your list 
    for num in duplicates:
        
        # if key is not in dictionary set value to true
        if num not in seen:
            seen[num] = True
            # append this key into your list which is dedup_list
            dedup_list.append(num)
        
    return dedup_list
    
print(get_deduplicated_list(duplicated_list))

```

---

### 5. Return True if duplicates exist.

#### First approach

```python
# This is your duplicated list
duplicated_list = [1,2,3,4, 4]

# fuction to check if there are duplicates and returns true if there is
def check_duplicates(duplicated_list):
    seen = {}
    # loop through your list
    for num in duplicated_list:
        """
          if num is not in dictionary set its value to true
          note num in this case is a key in our dict and 
          seen[num] sets value to True so in first value 
          in the list we wii have 1:True
        """
        if num not in seen:
            seen[num] = True
        # if the key is a duplicated we return true and break out of loop
        else:
            print('True')
            break
            
check_duplicates(duplicated_list)

```

#### second approach you use sets


```python
duplicated_list = [1,2,3,4, 4]
# You can also choose to use sets as the store only keys and a key must be unique
seen = set()

for num in duplicated_list:
    # if key is not in seen we add it
    if num not in seen:
        seen.add(num)
    else:
    """ if we encounter a key that already exists in the set print True 
        and break out of the loop since you have encountered a duplicate 
        instance
    """
        print("True")
        break
    
```

---

### 6. Find two numbers that add up to a target.

```python

## Check two numbers in list that add up to target 9 e.g 2+7 = 9
nums = [2,7,11,15, -2]
target = 9

# create a function to get the two numbers
def get_index_that_form_sum(nums):
    # define an empty dictionary
    seen = {}
    # loop through the list to get index and value of what is in list
    for index, num in enumerate(nums):
        """
            create a complement that take target 9 - num e.g 2 
            you get 7 as complement
        """
        complement = target - num
        
        """ 
            check to see if complement is in seen e.g 9-2 = 7 and 7 is not 
            yet in seen. so we move to 9 -7 we get 2 and since 2 is in seen 
            we get the value of 2 which 0 and index of 7 from list which is 1
        """
        if complement in seen:
            print(seen[complement], index)
        # swap values with indexes
        else:
            seen[num] = index
    
get_index_that_form_sum(nums)

```

---

### 7. Find the missing number from a sequence.

```python 
# Your list is missing 2
seq = [0,1,3]

# function to get the missing number
def get_missing_num(seq):
    # create an empty list and get the length of your list which is 3
    seen = {}
    a = len(seq)
    
    # iterate your list to get index and value
    for index, num in enumerate(seq):
        # check if key exist in dict and if not add it and set its value to True
        if num not in seen:
            seen[num] = True   
        # swap the value and indexes
        else:
            seen[num] = index
    # loop through the range of length of your list         
    for i in range(a + 1):
        # check if i is in seen and if not print i and break out to not print 4
        if i not in seen:
            print(i)
            break
            
    
get_missing_num(seq)

```

#### solution for b

```python
# This is another list but it doesnt start from 0
nums = [3, 7, 1, 2, 8, 4, 5]

def get_missing_number(nums):
    seen = {}
    a = len(nums)
    
    for index, nums in enumerate(nums):
        if nums not in seen:
            seen[nums] = True
        
    """
    loop through len of your list and start from 1 sinnce it starts from 1
    and make sure now to include upper bound we have numbers upto 8 
    we need to include 9 the upper bound so that the range includes also 8
    """
    for i in range(1, a + 2):
        if i not in seen:
            print(i)
            break
        
get_missing_number(nums)

```

---

### 8. Group words that are anagrams.

```python
# list of anagram words
words = ["eat","tea","ate","cat"]

# create a function to group anagrams
def get_anagram_words(words):
    # anagrams are words with same length and have similar characters e.g eat, ate
    anagrams = {}
    # loop through your list
    for word in words:
        # sort your list to get a key for similar words e.g eat and ate when sorted its ate
        key = "".join(sorted(word))
        
        # if key is not yet in our dictionary create an empty list for the key
        if key not in anagrams:
            anagrams[key] = []
        # then append anagram words to the created list    
        anagrams[key].append(word)
    print(anagrams)
            
get_anagram_words(words)

```
---
### 9. Return the K most common values.

```python
# list of numbers
numbers = [1,1,1,2,2,3]
# create an empty dictionary
count = {}

# use enumerate to get index, and value
for index, num in enumerate(numbers):
    # create a frequency of how many times each value appears e.g 3:1
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
  
# sort through your items      
sorted_items = sorted(count.items(), reverse=True)

```

---
    
### 10. Find the number that appears more than n/2 times.

```python
# list of numbers
nums = [2,2,1,2,2]
# create an empty dictionary
count = {}
# get the length of items and divide it by 2
n_times = len(nums)/2

# loop through your list and create a frequency of how many times a value is in list
for index, value in enumerate(nums):
    if value in count:
        count[value] += 1
        
    else:
        count[value] = 1

# loop through your dictionary and check for value that is greater than n_items and print the key        
for key, value in count.items():
    if value > n_times:
        print(key)

```

---

### 11. Remove duplicate customers based on customer_id.

```Python
customers = [
    {"customer_id": 1, "name": "Brian"},
    {"customer_id": 2, "name": "John"},
    {"customer_id": 1, "name": "Brian"}
]
# create an empty list and dictionary
dedup = {}
new_customer = []

# loop through your list of dictionaries
for customer in customers:
    customer_id = customer['customer_id']
    print(customer_id)

    # check if a customer_id is in the dictionary
    if customer_id not in dedup:
        dedup[customer_id] = True
        new_customer.append(customer)
        
        
print(new_customer)

```
---

### 13. Convert a customer list into a lookup dictionary.

# your list of dictionary
customers = [
    {"customer_id": 1, "name": "Brian"},
    {"customer_id": 2, "name": "John"}
]

# create an empty dict
look_up = {}

# loop through your list of dictionaries
for customer in customers:
    # assign your key a dictionary
    look_up[customer['customer_id']] = customer
    
print(look_up)

---

### 14. Join customers and orders using a HashMap.

```python
customers = [
    {"customer_id": 1, "name": "Brian"},
    {"customer_id": 2, "name": "John"}
]

orders = [
    {"customer_id": 1, "amount": 100},
    {"customer_id": 2, "amount": 200}
]

# create an empty list and an empty dict
joined = []
customer_lookup = {}

# loop through your list of customer dictionary
for customer in customers:
    customer_lookup[customer['customer_id']] = customer
    
# loop through orders
for order in orders:
    customer_id = order['customer_id']
    
    # check if customer id exist as a key in the lookup
    if customer_id in customer_lookup:
        customer = customer_lookup[customer_id]
        
        # append your list now with the correct values
        joined.append({
            "customer_id": customer['customer_id'],
            "name": customer['name'],
            "amount": order["amount"]
        })
        
print(joined)

```
    
---

### 14. Calculate total sales per product.

```python 
# a list of tuples
sales = [
    ("Laptop", 500),
    ("Phone", 200),
    ("Laptop", 300)
]


sal = {}

# for tuples you can loop through it
for product, amount in sales:
    # check if a product is in dict if not set value as amount if yes add amounts
    if product not in sal:
        sal[product] = amount
        
    else:
        sal[product] += amount
        
print(sal)

```

--- 

### 15. Identify duplicate invoice IDs.

```python
# list of items
invoice_ids = [1001,1002,1003,1002,1004]

# empty dict
dedup = {}

# loop through your list
for id in invoice_ids:
    
    # set value as True for ids
    if id not in dedup:
        dedup[id] =  True
    # print a duplicate id
    else:
        print(id)
```

---

### 16. Count incoming events.

```python
# list of events
events = [
    "login",
    "logout",
    "login",
    "purchase"
]

events_dict = {}

# loops through your list
for event in events:
    # check if event is in events_dict if not assign value 1 if yes add 1 to value
    if event not in events_dict:
        events_dict[event] = 1
        
    else:
        events_dict[event] += 1
        
print(events_dict)

```

---

### 17. Group events by user.

```python
# list of events
events = [
    ("user1", "login"),
    ("user1", "view_product"),
    ("user2", "login"),
    ("user1", "checkout")
]

event = {}

# loop through your list of tuples
for user, activity in events:
    # if user doesnt exist in event create an empty list
    if user not in event:
        event[user] = []
    # append activities to list    
    event[user].append(activity)
    
print(event)

```
---


### 18. Keep only the latest customer version.

### this question is same as question number 11

### 19. Remove duplicate events.

```python
### list of events

events = [
    {"event_id": 1},
    {"event_id": 2},
    {"event_id": 1},
    {"event_id": 3}
]

deduplicated_events={}

for event in events:
    # deduplicate the events
    deduplicated_events[event['event_id']] = event
    
    
    
print(list(deduplicated_events.values()))

```
---

### 20. Implement SQL JOIN behavior using HashMaps.


```python
# customer and orders

customers = [
    {"customer_id": 1, "name": "Brian"},
    {"customer_id": 2, "name": "John"}
]

orders = [
    {"order_id": 101, "customer_id": 1},
    {"order_id": 102, "customer_id": 2}
]

# create an empty dict
hash_join = {}

Joined_customers_order = []

# create a look up customer table
for customer in customers:
    
    hash_join[customer['customer_id']] = customer
    
# loop through orders
for order in orders:
    # get customer_ids from your order dictionaries
    customer_id = order['customer_id']
    # check if a customer id exist in our hash_join dict
    if customer_id in hash_join:
        customer = hash_join[customer_id]
        
        #append the matching ids to our empty list
        Joined_customers_order.append(
            {
                "customer": customer['customer_id'],
                "name": customer["name"],
                "order_id": order['order_id']
            }
            )
            
print(Joined_customers_order)
```
        
---
## The End
---


               