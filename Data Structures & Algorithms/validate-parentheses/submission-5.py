class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == '}' and stack.pop() != '{':
                    return False
                if char == ')' and stack.pop() != '(':
                    return False
                if char == ']' and stack.pop() != '[':
                    return False
        return True if not stack else False