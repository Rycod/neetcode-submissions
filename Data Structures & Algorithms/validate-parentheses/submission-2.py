class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cl = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in cl:
                if not stack or cl[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return len(stack) == 0 
