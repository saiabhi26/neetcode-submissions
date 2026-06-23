class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):    
            while len(stack)!=0 and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()    
            stack.append(i)
        while len(stack) != 0:
            res[stack[-1]] = 0
            stack.pop()
        return res