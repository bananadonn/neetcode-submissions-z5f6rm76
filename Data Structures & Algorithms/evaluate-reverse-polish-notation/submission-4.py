class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        q = deque()
        for token in tokens:
            print(q)
            if token == '+':
                x = q.pop()
                y = q.pop()
                q.append(y + x)
            elif token == '-':
                x = q.pop()
                y = q.pop()
                q.append(y - x)
            elif token == '*':
                x = q.pop()
                y = q.pop()
                q.append(y * x)
            elif token == '/':
                x = q.pop()
                y = q.pop()
                q.append(int(y / x))
            else:
                q.append(int(token))

        return q.pop()