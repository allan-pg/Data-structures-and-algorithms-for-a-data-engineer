
### Remove Duplicates

duplicated_list = [1,2,3,1,2,4]
deduplicated = set()
deduplicated_list = []

def deduplicate(num):

    for index,nums in enumerate(num):
        if nums not in deduplicated:
            deduplicated.add(nums)
            deduplicated_list.append(nums)

    print(deduplicated_list)

deduplicate(duplicated_list)   

