adding_rules = {
    0: '0',
    1: '1',
    2: '0',
    3: '1'
}

class Solution:        
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        extra_value = False
        first_number = list(a)
        second_number = list(b)

        while len(first_number) > 0 or len(second_number) > 0:
            first = '' if len(first_number) == 0 else first_number.pop()
            second = '' if len(second_number) == 0 else second_number.pop()

            addition = first + second

            if extra_value:
                addition += '1'

            key =  addition.count('1')
            extra_value = key >= 2
            res = adding_rules[key] + res

        if extra_value:
            res = '1' + res

        return res