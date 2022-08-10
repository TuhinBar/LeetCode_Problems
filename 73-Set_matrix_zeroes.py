# LeetCode 73. Set Matrix Zeroes (Medium) https://leetcode.com/problems/set-matrix-zeroes/
# Description: Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Example 1:
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]

def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0,rows,cols = False,len(matrix),len(matrix[0])
        
        for i in range(rows):
            if matrix[i][0] ==0:
                col0= True
            for j in range(1,cols):
                if(matrix[i][j]==0):
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
                    
        for i in range(1,rows):
            for j in range(1,cols):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j]= 0
        if matrix[0][0] ==0:
            for j in range(cols):
                matrix[0][j] = 0
        if col0:
            for i in range(rows):
                matrix[i][0] = 0

# Driver code
matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
setZeroes(matrix)
print(matrix)