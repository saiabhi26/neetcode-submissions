class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curset = set()

        l = 0
        r = 0
        res = 0
        curlen = 0
        while r < len(s):

            while s[r] in curset:
                curset.remove(s[l])
                l+=1
                curlen-=1

            curset.add(s[r])
            curlen+=1
            res = max(res, curlen)
            r+=1
        
        return res