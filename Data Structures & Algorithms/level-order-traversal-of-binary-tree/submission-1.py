# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        levels = [[root.val],]
        
        lastLevel = [root,]

        while True:
            currentLevel = []
            levelValues = []

            if lastLevel:
                
                for node in lastLevel:
                    if node:
                        if node.left:
                            currentLevel.append(node.left)
                            levelValues.append(node.left.val)

                        if node.right:
                            currentLevel.append(node.right)
                            levelValues.append(node.right.val)
                        

                if levelValues: levels.append(levelValues)

                lastLevel = list(currentLevel)
            else:
                break
        
        return levels


