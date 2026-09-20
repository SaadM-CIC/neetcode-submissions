class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations = {
            '+': lambda x, y: x+y,
            '-': lambda x,y : x-y,
            '*': lambda x,y : x * y,
            '/': lambda x,y : int(x/y)
        }
        for token in tokens:
            if token in operations:
                y=stack.pop()
                x = stack.pop()
                stack.append(operations[token](x,y))
            else:
                stack.append(int(token))
        return stack[0]