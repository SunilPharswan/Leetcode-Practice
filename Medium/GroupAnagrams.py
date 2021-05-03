'''https://leetcode.com/problems/group-anagrams/'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs1=[]
        out=[]
        unique=[]
        for x in strs:
            strs1.append("".join(sorted(x)))
        [unique.append(x) for x in strs1 if x not in unique]
        for x in range(len(unique)):
            match=[]
            for i in range(len(strs1)):
                if unique[x] == strs1[i]:
                    match.append(strs[i])
            out.append(sorted(match))
        out=sorted(out,key=len)
        return(out)