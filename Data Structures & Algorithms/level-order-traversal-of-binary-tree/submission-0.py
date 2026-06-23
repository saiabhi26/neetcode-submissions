# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = []
        d = {}
        res = []
        q.append([root,0])
        while len(q)!=0:
            temp = q.pop(0)
            if temp[0].left != None:
                q.append([temp[0].left,temp[1]+1])
            if temp[0].right != None:
                q.append([temp[0].right,temp[1]+1])
            if temp[1] not in d:
                d[temp[1]] = [temp[0].val]
            else:
                d[temp[1]].append(temp[0].val)
        for k in d:
            res.append(d[k])
        return res