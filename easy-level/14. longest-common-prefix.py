from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if "" in strs:
            return ""
        
        characters = list(map(lambda x: x[0], strs))
        isCommonPrefix = all(c == characters[0] for c in characters)

        result = characters[0] if isCommonPrefix else ""
        nextPrefix = self.longestCommonPrefix(list(map(lambda x: x[1:len(x)], strs))) if isCommonPrefix else ""

        return result + nextPrefix