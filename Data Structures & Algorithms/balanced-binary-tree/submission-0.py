# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def traverse(root,res):
            if root:
                lheight = traverse(root.left,res)
                rheight = traverse(root.right,res)
                if abs(lheight-rheight) > 1:
                    res[0] = False
                return 1+max(lheight,rheight)
            else:
                return 0
        traverse(root,res)
        return res[0]