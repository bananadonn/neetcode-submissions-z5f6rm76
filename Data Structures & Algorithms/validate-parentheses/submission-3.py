class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']':'[',')':'(','}':'{'}
        stack = []
        
        for i in s:
            if not stack:
                stack.append(i)
                continue
            if i not in pairs:
                stack.append(i)
            else:
                if stack[-1] == pairs[i]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False