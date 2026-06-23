class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for i in s:
            i = i.lower()
            if i.isalnum():
                s1+=i
        i = 0
        j = len(s1)-1
        while i<j:
            if s1[i]!=s1[j]:
                return False
            i+=1
            j-=1
        return True 