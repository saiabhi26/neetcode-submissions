# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = [None]
        a = min(p.val,q.val)
        b = max(p.val,q.val)
        def traverse(root,a,b,res):
            if root:
                if root.val >= a and root.val <= b:
                    res[0] = root
                    return
                elif root.val < a:
                    traverse(root.right,a,b,res)
                elif root.val > b:
                    traverse(root.left,a,b,res)
        traverse(root,a,b,res)
        return res[0]