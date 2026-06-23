class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                stack.append([c,i])
            elif c == ')':
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            else:
                stars.append([c,i])
        
        while stack:
            if stars and stars[-1][1] > stack[-1][1]:
                stack.pop()
                stars.pop()
            else:
                return False
        return True
