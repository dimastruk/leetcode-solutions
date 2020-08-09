symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        res = 0

        for i in range(len(s)):
            if i > 0 and symbols[s[i]] < symbols[s[i - 1]]:
                res -= symbols[s[i]]
            else:
                res += symbols[s[i]]
        
        return res
