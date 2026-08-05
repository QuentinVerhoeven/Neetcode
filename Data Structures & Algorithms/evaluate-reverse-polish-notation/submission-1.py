class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isnumeric():
                stack.append(int(token))
                continue
            if token == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
                continue
            if token == "-":
                stack.append(int(stack.pop()) - int(stack.pop()))
                continue
            if token == "/":
                stack.append(int(stack.pop()) / int(stack.pop()))
                continue
            if token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
                continue

        return stack.pop()