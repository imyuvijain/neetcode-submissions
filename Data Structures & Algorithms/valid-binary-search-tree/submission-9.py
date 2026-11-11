# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], lower=None, upper=None) -> bool:
        
        if not root:
            return True

        if root.left:
            if root.left.val >= root.val:
                return False
            if lower != None:
                if root.left.val <= lower:
                    return False
        
        if root.right:
            if root.right.val <= root.val:
                return False

            if upper != None:
                if root.right.val >= upper:
                    return False

        isLeftValid = self.isValidBST(root.left, upper=min(root.val, upper if upper != None else root.val), lower=lower)
        isRightValid = self.isValidBST(root.right, lower=max(root.val, lower if lower != None else root.val), upper=upper)
        return isLeftValid and isRightValid
