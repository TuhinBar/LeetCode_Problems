# Leetcode: (41)First missing positive

def firstMissingPositive( nums):
    nums.sort()
    a = 0
    for i in nums:
        if i > 0 :
            a = nums.index(i)
            break

    del nums[0:a]
    nums.insert(0, 0)
    nums = set(nums)
    nums = list(nums)

    if min(nums) > 1:
        return 1
    else:
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)


# Driver Code

nums=[1,3,4,7,8,2]
print(firstMissingPositive(nums))