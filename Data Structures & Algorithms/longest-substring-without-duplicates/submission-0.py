class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        dup = set()
        maxlen = 0
        curlen = 0
        while r < len(s):
            if s[r] not in dup:
                dup.add(s[r])
                curlen += 1
                if curlen > maxlen:
                    maxlen = curlen
                r+=1  
            else:
                dup.remove(s[l])
                curlen -= 1
                l+=1
        return maxlen