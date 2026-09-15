class Solution:
    def isValid(self, s: str) -> bool:
        parent= {'(': ')',  '{': '}', '[' : ']'}
        stack = []
        for i in s:
            if i in parent:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    x = stack.pop()
                    if parent[x] != i:
                        return False
                    
        return len(stack) == 0



