# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
        res = [False]
        def traverse(root,subroot,res):
            def check(root,subroot):
                if root and subroot:
                    return check(root.left,subroot.left) and check(root.right, subroot.right) and root.val == subroot.val
                elif root and not subroot:
                    return False
                elif not root and subroot:
                    return False
                else:
                    return True
            if root:
                if root.val == subroot.val and res[0] == False:
                    res[0] = check(root,subroot)
                traverse(root.left,subroot,res)
                traverse(root.right,subroot,res)
        traverse(root,subRoot,res)
        return res[0]    


