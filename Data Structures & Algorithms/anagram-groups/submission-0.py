class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            cnt = [0]*26
            for j in strs[i]:
                cnt[ord(j)-ord('a')]+=1
            k = tuple(cnt)
            if k not in d:
                d[k]=[strs[i]]
            else:
                d[k].append(strs[i])
        ans = []
        for key,value in d.items():
            ans.append(value)
        return ans    
