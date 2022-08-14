# LeetCode No: 62 - Unique Paths  https://leetcode.com/problems/unique-paths/

def uniquePaths(m: int, n: int) -> int:
    if m==1 or n==1:
        return 1
    return uniquePaths(m-1,n)+uniquePaths(m,n-1)

# Alternate Solution:
def uniquePaths(self, m: int, n: int) -> int:
    dp = [1] * n
    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j - 1] + dp[j]
    return dp[-1] if m and n else 0

    
# Test
print(uniquePaths(3,7))

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)