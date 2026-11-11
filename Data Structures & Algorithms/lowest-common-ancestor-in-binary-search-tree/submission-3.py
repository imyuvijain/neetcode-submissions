# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        pAncestors = self.getAncestors(root, p)
        qAncestors = self.getAncestors(root, q)

        commonAncestors = []

        for ancestor in pAncestors:
            if ancestor in qAncestors:
                if ancestor:
                    commonAncestors.append(ancestor)
                    

        return commonAncestors[-1]

    
    def getAncestors(self, root, node):

        currentNode = root

        ancestors = []

        while node not in ancestors:
            ancestors.append(currentNode)
            if currentNode:
                if node.val > currentNode.val:
                    currentNode = currentNode.right
                elif node.val < currentNode.val:
                    currentNode = currentNode.left
                else:
                    break
            else:
                break
        return ancestors



