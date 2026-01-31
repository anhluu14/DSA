class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item: int) -> None:
        self.stack.append(item)
        
    def pop(self) -> None:
        self.stack.pop()
    
    def peek(self) -> int:
        if len(self.stack) == 0:
            return -1
        
        return self.stack[-1]
    
    def size(self) -> int:
        return len(self.stack)

class Solution:
    def type_string(self, s:str) -> str:
        stack = Stack()

        for i in range(len(s)):
            if s[i] != '#':
                stack.push(s[i])
            else:
                if stack.size() > 0:
                    stack.pop()
        ans = ""
        for i in range(stack.size()):
            ans += stack.stack[i]
        
        return ans
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = self.type_string(s)
        t = self.type_string(t)
        return s == t    
