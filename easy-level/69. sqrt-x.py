class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        res = 0

        if x <= 1:
            return x

        while start != end:
            pointer = int((start + end) / 2)

            if pointer**2 == x:
                return pointer
            elif pointer**2 < x:
                start = pointer + 1
                res = pointer
            else:
                end = pointer
            
        return res

# Testing
s = Solution()

print(s.mySqrt(2))