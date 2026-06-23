# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        def traverse(root,res):
            if root:
                lmax = traverse(root.left,res)
                rmax = traverse(root.right,res)
                lmax = max(0,lmax)
                rmax = max(0,rmax)
                res[0] = max(res[0], root.val+lmax+rmax)
                return root.val + max(lmax,rmax)
            else:
                return 0
        traverse(root,res)
        return res[0]
