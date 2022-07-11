


def twoSum(nums,target):
    hash_map={}
        
    for i,n in enumerate(nums):
        diff= target-n
        if diff in hash_map:
            return hash_map[diff],i
        hash_map[n]=i
    return



# driver code

nums=[3,2,3]
target=6
print(twoSum(nums,target))
