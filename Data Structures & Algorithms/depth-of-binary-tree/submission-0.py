# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxheight = [0]
        height = 0
        def findheight(cur,height,maxheight):
            if cur:
                if height > maxheight[0]:
                    maxheight[0] = height
                findheight(cur.left,height+1,maxheight)
                findheight(cur.right,height+1,maxheight)
        findheight(root,height+1,maxheight)
        return maxheight[0]