# LeetCode 202 - Happy Number - https://leetcode.com/problems/happy-number/
# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: 
# Starting with any positive integer, 
# replace the number by the sum of the squares of its digits,
# repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers.
# Example: 19 is a happy number
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Approach 1: If number != 1, then continue to sum the squares of the digits.
def isHappy(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return True

# Driver Code
print(isHappy(19))

# Approach 2: If number not in set, then add to set and continue to sum the squares of the digits.

def isHappy(n: int) -> bool:
    ans_set = set()
    while n not in ans_set:
        ans_set.add(n)
        n = sum(int(i)**2 for i in str(n))
        if n == 1:
            return True
    return False

# Time Complexity: O(n)
# Space Complexity: O(n)