class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for c  in s:
            if c == '[' or c == '(' or c == '{':
                brackets.append(c)
            elif c == ']':
                if brackets[-1] == '[':
                    brackets.pop()
                else:
                    return False
            elif c == ')':
                if brackets[-1] == '(':
                    brackets.pop()
                else:
                    return False
            elif c == '}':
                if brackets[-1] == '{':
                    brackets.pop()
                else:
                    return False
        if len(brackets) == 0:
            return True
        else:
            return False