# LeetCode No: 62 - Unique Paths  https://leetcode.com/problems/unique-paths/

def uniquePaths(m: int, n: int) -> int:
    if m==1 or n==1:
        return 1
    return uniquePaths(m-1,n)+uniquePaths(m,n-1)

# Test
print(uniquePaths(3,7))

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)