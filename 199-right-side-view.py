# LeetCode: 199 - Binary Tree Right Side View (Medium) https://leetcode.com/problems/binary-tree-right-side-view/
# Description: Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# For example:
# Given the following binary tree,
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
# You should return [1, 3, 4].

# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def rightSideView (self, root):
            if not root:
                return []
            q=deque([root])
            ans=[]
            while q:
                n = len(q)
                ans.append(q[-1].val)
                for i in range(n):
                    node= q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            return ans

# Driver Code
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(root.rightSideView(root))