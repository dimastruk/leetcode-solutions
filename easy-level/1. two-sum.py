from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        stored_values = {}
        
        for index, value in enumerate(nums):
            if target - value in stored_values:
                return [stored_values[target - value], index]
            
            else:
                stored_values[value] = index
                
        return -1