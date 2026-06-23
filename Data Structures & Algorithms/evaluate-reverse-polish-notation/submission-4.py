class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def eval(a,b,operator):
            if operator == "+":
                return a+b
            if operator == "-":
                return a-b
            if operator == "*":
                return a*b
            if operator == "/":
                if a/b < 0:
                    return  math.ceil(a/b)
                return a//b
        operands = []
        operators = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in operators:
                operands.append(int(i))
            else:
                val = eval(operands[-2], operands[-1], i)
                print(operands[-2],i,operands[-1],"=",val)
                operands.pop()
                operands.pop()
                operands.append(val)
        return operands[0]