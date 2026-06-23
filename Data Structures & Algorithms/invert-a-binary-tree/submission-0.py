# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root
        def invert(cur):
            if cur:
                invert(cur.left)
                invert(cur.right)
                temp = cur.left
                cur.left = cur.right
                cur.right = temp
        invert(root)
        return root