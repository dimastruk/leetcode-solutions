class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            l = []
            while x != 0:
                l.append(x % 10)
                x //= 10
            return(list(reversed(l))==l)
        
# Testing
s = Solution()

print(s.isPalindrome(121))
print(s.isPalindrome(1221))