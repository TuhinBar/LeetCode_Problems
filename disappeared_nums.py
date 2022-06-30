# Leetcode: (448)Find All Numbers In Disappeared Array[easy](can be optimized)

def findDisappearedNumbers(nums):
    hash_dict = {i: 0 for i in range(1,len(nums)+1)}
        
    for i in range(len(nums)):
        hash_dict[nums[i]] += 1
    
    ans = []
    for i in range(1, len(nums)+1):
        if hash_dict[i] ==  0:
            ans.append(i)
    return ans 

nums=[1,1]
print(findDisappearedNumbers(nums))