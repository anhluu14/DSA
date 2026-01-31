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
    def decode(self, x) -> int:
        if x == '(':
            return 1
        if x == '[':
            return 2
        if x == '{':
            return 3
        if x == ')':
            return -1
        if x == ']':
            return -2
        if x == '}':
            return -3
        return 0

    def isValid(self, s: str) -> bool:
        self.open_parentheses = []
        stack = Stack()
        for i in range(len(s)):
            num = self.decode(s[i])

            if num > 0:
                stack.push(num)
            else:
                if stack.size() > 0:
                    last_parenthese = stack.peek()
                    if last_parenthese + num == 0:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack.size() > 0:
            return False
        else:
            return True




