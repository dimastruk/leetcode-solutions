parentheses = {
    "(": ")",
    "{": "}",
    "[": "]"
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if len(stack) > 0 and stack[-1] in parentheses.keys() and i == parentheses[stack[-1]]:
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0