class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pair = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for bracket in s:
            if stack and bracket in bracket_pair:
                top = stack[-1]
                if top == bracket_pair[bracket]:
                    stack.pop()
                else:
                    stack.append(bracket)
            else:
                stack.append(bracket)
        return not stack
        