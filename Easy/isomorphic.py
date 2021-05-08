"""https://leetcode.com/problems/isomorphic-strings/"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmap={}
        out=""
        for i in range(len(s)):
            if s[i] not in hmap:
                flag=0
                for key, val in hmap.items():
                    if val == t[i]:
                        flag=1
                if flag==0:
                    hmap[s[i]]=t[i]
                    out+=t[i]
            else:
                if hmap[s[i]]==t[i]:
                    out+=t[i]
        if t==out:
            return True
        else:
            return False