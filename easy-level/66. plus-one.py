from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: 
        end = len(digits) - 1
        changeFlag = True

        for i in range(end, -1, -1):
            if i == end or (digits[i + 1] == 0 and changeFlag):
                digits[i] = digits[i] + 1 if digits[i] != 9 else 0
            else:
                changeFlag = False
            
            if i == 0 and digits[i] == 0:
                digits.insert(0, 1)

        return digits