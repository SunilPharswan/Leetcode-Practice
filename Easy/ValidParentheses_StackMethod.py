"""https://leetcode.com/problems/valid-parentheses/"""
class Solution:
    def isValid(self, s: str) -> bool:
        keymap={"]":"[",")":"(","}":"{"}
        stack=[]
        for i in s:
            if i not in keymap:
                stack.append(i)
            else:
                if stack and stack[-1] == keymap[i]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False