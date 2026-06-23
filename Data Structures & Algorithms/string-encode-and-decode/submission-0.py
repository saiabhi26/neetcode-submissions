class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s = s+str(len(i))+"#"+i
        return s
    def decode(self, s: str) -> List[str]:
        arr = []
        i=0
        num=""
        while i<len(s):
            if s[i]=='#':
                l = int(num)
                num=""
                arr.append(s[i+1:i+l+1])
                i+=l+1
            else:
                num+=s[i]
                i+=1
        return arr