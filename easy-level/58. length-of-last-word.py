class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        arr = s.split(' ')
        return len(arr[-1])