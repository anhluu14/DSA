class Solution:

    memo = [-1] * (1000001) #so memo dai dien cho gia tri khoi tao chua duoc tinh ngoai khoan thoa man
    #fib(n) -> memo[n]
    #fib(x,y) -> memo[x][y]

    def fib(self, n: int) -> int:
        #base case
        if n == 0:
            return 0

        if n == 1:
            return 1
        
        #check if fib(n) is already calculated
        if self.memo[n] != -1:
            return self.memo[n]

        #recursion formula
        self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.memo[n]

    