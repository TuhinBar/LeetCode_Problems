# Problem Number 268(missing number)

def missingNumber(nums):
    n= len(nums)
    exp_sum= n*(n+1)//2
    curr_sum=sum(nums)
    return exp_sum - curr_sum

# Driver code
nums=[3,0,1]
print(missingNumber(nums))