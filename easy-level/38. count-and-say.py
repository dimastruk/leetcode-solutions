class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return '1' 

        number = self.countAndSay(n - 1)

        res = ''
        counter = 0
        
        for i in range(len(number)):
            if i == len(number) - 1 or number[i] != number[i + 1]:
                res += str(counter + 1) + number[i]
                counter = 0
            else:
                counter += 1


        return res