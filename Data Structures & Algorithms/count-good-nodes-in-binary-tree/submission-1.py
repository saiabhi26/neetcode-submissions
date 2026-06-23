# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def traverse(root,arr,res):
            if root:
                add = True
                for i in arr:
                    if i > root.val:
                        add = False
                if add:
                    temp = list(arr)
                    temp.append(root.val)
                    arr = tuple(temp)
                    res[0]+=1
                traverse(root.left,arr,res)
                traverse(root.right,arr,res)
        traverse(root,(),res)
        return res[0]