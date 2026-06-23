# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [0]
        cnt = [0]
        def traverse(root,res,cnt):
            if root:
                traverse(root.left,res,cnt)
                cnt[0]+=1
                if cnt[0] == k:
                    res[0] = root.val
                    return
                traverse(root.right,res,cnt)
        traverse(root,res,cnt)
        return res[0]
        