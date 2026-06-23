class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = [[]]

        for num in nums:
            newperms = []
            while len(perms) != 0:
                cur = perms.pop()
                for i in range(len(cur)+1):
                    curcopy = cur.copy()
                    curcopy.insert(i,num)
                    newperms.append(curcopy)
            perms = newperms
        return perms


