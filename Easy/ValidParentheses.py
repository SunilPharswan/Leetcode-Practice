"""https://leetcode.com/problems/valid-parentheses/"""
class Solution:
    def isValid(self, instr: str) -> bool:
        x,y,z="()","{}","[]"
        while True:
            if x not in instr and y not in instr and z not in instr and len(instr) != 0:
                return False
                break
            else:
                if len(instr)==0:
                    return True
                    break
                if x in instr:
                    instr=instr.replace(x,"")
                if y in instr:
                    instr=instr.replace(y, "")
                if z in instr:
                    instr=instr.replace(z, "")