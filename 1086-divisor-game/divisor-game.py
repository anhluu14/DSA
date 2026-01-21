from functools import lru_cache
class Solution:
    @lru_cache(None)
    def divisorGame(self, n: int) -> bool:
        
        # Base case
        if n <= 1:
            return False
        # But There is no integer strictly between 0 and 1 So: Alice cannot make any move According to the rules → the player who cannot move loses

# Alice loses immediately    
        # Recursion
        winable = False
        
        for x in range(1, n):
            if n % x == 0:
                if self.divisorGame(n-x) == False: #thang di truoc se thang
                    winable = True
                    break

        return winable
#TLE: Too many states got recalculated
#6 -> 1 -> 5 -> 4
#2 -> 4 -> 3 -> 2
#3 -> 2 
        