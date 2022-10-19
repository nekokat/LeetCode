"""
30. Substring with Concatenation of All Words   https://leetcode.com/problems/substring-with-concatenation-of-all-words/
"""


from collections import Counter
import re

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        w = Counter(words)
        wl = len(words[0])
        l = len(words)
        res = []
        for i in range(0, len(s)-wl*l+1):
            findw = re.findall(f"{'.'*wl}", s[i:i + wl*l])
            if Counter(findw) == w:
                res.append(i)           
        return res
      
