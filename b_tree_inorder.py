# Leetcode: 94-  Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorderTraversal(self, root):
        if root is None: return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# Driver Code
root=[1,None,2,3]
print(inorderTraversal(root))