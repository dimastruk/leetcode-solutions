from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        index = 0

        while start != end:
            index = int((start + end) / 2)
            if nums[index] == target:
                return index
            elif nums[index] < target:
                start = index + 1
            else:
                end = index

        index = start + 1 if nums[start] < target else start
        
        return index