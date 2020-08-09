from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                nums.pop(i)
                i -= 1

            i += 1
        
        return len(nums)