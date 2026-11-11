# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return search(root)


def search(root):
    depth = 0
    
    if not root:
        return 0

    leftdepth = search(root.left)
    rightdepth = search(root.right)

    depth += 1+max(leftdepth, rightdepth)
    return depth