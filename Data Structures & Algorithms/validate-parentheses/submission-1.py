class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        opens = {'(':1, '[':2, '{':3}
        closes = {')':1, ']':2, '}':3}
        for i in s:
            if i in opens:
                st.append(i)
            else:
                if len(st) == 0:
                    return False
                ob = st.pop()
                if opens[ob] != closes[i]:
                    return False
        if len(st)==0:
            return True
        return False