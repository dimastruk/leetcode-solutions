class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1])
        if 2**31 <= res:
            return 0

        return res if x > 0 else res - res * 2