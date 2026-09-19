class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            "+": lambda x,y : x+y,
            "-": lambda x,y : x-y,
            "*": lambda x,y : x*y,
            "/": lambda x,y : x/y,
        }
        
        stack = []
        for token in tokens:
            if token in op:
                x = op[token](stack[-2],stack[-1])
                stack.pop()
                stack.pop()
                stack.append(int(x))
            else: 
                stack.append(int(token))
            
                
        return stack[-1]