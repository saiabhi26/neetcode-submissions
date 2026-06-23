class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        map1 = [0]*26
        map2 = [0]*26
        for c in s1:
            map1[ord(c) - ord('a')]+=1
        l = 0
        r = 0
        while r < len(s2):
            map2[ord(s2[r]) - ord('a')]+=1
            if r - l + 1 == len(s1):
                if map1 == map2:
                    return True
                map2[ord(s2[l])-ord('a')]-=1
                l+=1
            r+=1
        return False
