# LeetCode No: 378 - Kth Smallest in Sorted Matrix  https://leetcode.com/problems/kth-smallest-in-sorted-matrix/

def kthSmallest( matrix, k):
    n, beg, end = len(matrix), matrix[0][0], matrix[-1][-1]
    
    def check(m):
        i, j, cnt = 0, n-1, 0
        for i in range(n):
            while j >= 0 and matrix[i][j] > m: j -= 1
            cnt += (j + 1)
        return cnt
        
    while beg < end:
        mid = (beg + end)//2
        if check(mid) < k:
            beg = mid + 1
        else:
            end = mid
            
    return beg

# Test
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 7
print(kthSmallest(matrix, k))

# Time Complexity: O(log(n))
# Space Complexity: O(1)