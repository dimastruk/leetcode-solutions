from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        current_sum = 0

        for n in nums:
            current_sum = max(n, current_sum + n)
            sum = max(sum, current_sum)
        
        return sum