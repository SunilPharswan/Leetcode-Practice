class Solution:
    def longestCommonPrefix(self, s) -> str:
        mini=min(s,key=len)
        if len(s)==1:
            return s[0]
        elif len(mini) in range(0,1):
            return mini
        else:
            for i in range(1,len(mini)+1):
                temp=mini[0:i]
                flag=0
                for j in s:
                    if not j.startswith(temp):
                        return temp[:-1]
                if temp==mini:
                    return temp
