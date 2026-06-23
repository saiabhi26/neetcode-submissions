# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = {}
        def traverse(root,d,h):
            if root:
                traverse(root.right,d,h+1)
                if h not in d:
                    d[h] = root.val
                traverse(root.left,d,h+1)
        traverse(root,d,0)
        res = [0]*len(d)
        for k in d:
            res[k] = d[k]
        return res
                