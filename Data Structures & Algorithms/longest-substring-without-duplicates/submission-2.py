class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        l = 0
        r = 0
        maxlen = 0
        curlen = 0
        while r < len(s):
            if s[r] not in myset:
                myset.add(s[r])
                curlen+=1
                maxlen = max(maxlen,curlen)
                r+=1
            else:
                while s[r] in myset:
                    myset.remove(s[l])
                    curlen-=1
                    l+=1
        return maxlen