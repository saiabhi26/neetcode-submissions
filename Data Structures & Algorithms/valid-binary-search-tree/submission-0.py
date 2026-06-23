# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def traverse(root,arr):
            if root:
                traverse(root.left,arr)
                arr.append(root.val)
                traverse(root.right,arr)
        traverse(root,arr)
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False
        return True