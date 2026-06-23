class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1arr = [0]*26
        s2arr = [0]*26
        for i in s1:
            s1arr[ord(i) - ord('a')]+=1
        wordlen = 0
        for i in range(len(s2)):
            if wordlen < len(s1):
                s2arr[ord(s2[i]) - ord('a')]+=1
                wordlen+=1
            else:
                if s1arr == s2arr:
                    return True
                s2arr[ord(s2[i-len(s1)])-ord('a')]-=1
                s2arr[ord(s2[i])-ord('a')]+=1
        return s1arr == s2arr
