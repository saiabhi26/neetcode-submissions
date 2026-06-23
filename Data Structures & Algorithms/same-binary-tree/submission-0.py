# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = [True]
        def traverse(p,q,res):
            if p and q:
                if p.val != q.val:
                    res[0] = False
                traverse(p.left,q.left,res)
                traverse(p.right,q.right,res)
            elif p and not q:
                res[0] = False
            elif not p and q:
                res[0] = False
        traverse(p,q,res)
        return res[0]
