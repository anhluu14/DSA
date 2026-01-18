class Solution:
    def power(self, x:float, n:int) -> float:
        if n == 0: 
            return 1

        if n % 2 == 0:
            return self.power(x * x, n // 2)
        return self.power(x * x, n // 2) * x

    def myPow(self, x: float, n: int) -> float:
  
    # recursion formula
    # x^n = x^(n / 2) * x^(n / 2) if n is even
    # x^n = x * x^(n - 1) if n is odd
    
    # if n is even
    

    # n is odd
        if n > 0:
            return self.power (x, n)
        else:
            return self.power(1 / x, -n)

        