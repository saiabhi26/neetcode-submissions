class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = strs[0]
        for i in range(1,len(strs)):
            j = 0
            while j < min(len(lcp),len(strs[i])):
                if lcp[j]!=strs[i][j]:
                    break
                j+=1
            lcp = lcp[:j]
        return lcp    