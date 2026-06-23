# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def finddiameter(root,res):
            if root:
                lheight = finddiameter(root.left,res)
                rheight = finddiameter(root.right,res)
                res[0] = max(res[0],lheight+rheight)
                return 1+max(lheight,rheight)
            else:
                return 0
        finddiameter(root,res)
        return res[0]