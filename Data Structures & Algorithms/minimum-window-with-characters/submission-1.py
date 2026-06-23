class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        needmap = {}
        havemap = {}
        need = 0
        have = 0
        for c in t:
            needmap[c] = needmap.get(c,0) + 1
        need = len(needmap)
        l = 0
        r = 0
        res = []
        reslen = float('inf')
        while r < len(s):
            c = s[r]
            havemap[c] = havemap.get(c,0) + 1
            if c in needmap and havemap[c] == needmap[c]:
                have+=1
            while have == need:
                if r-l+1 < reslen:
                    res = [l,r]
                    reslen = r-l+1
                havemap[s[l]]-=1
                if s[l] in needmap and havemap[s[l]] < needmap[s[l]]:
                    have-=1
                l+=1
            r+=1
        if res == []:
            return ""
        return s[res[0]:res[1]+1]