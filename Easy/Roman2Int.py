"""https://leetcode.com/problems/roman-to-integer/"""
class Solution:
    def romanToInt(self, s: str) -> int:
        out=0
        mapkey={"IV":4,
                "IX":9,
                "XL":40,
                "XC":90,
                "CD":400,
                "CM":900,
                "I":1,
                "V":5,
                "X":10,
                "L":50,
                "C":100,
                "D":500,
                "M":1000}
        for key in mapkey:
            if key in s:
                out+=s.count(key)*mapkey[key]
                s=s.replace(key, "")
        return out