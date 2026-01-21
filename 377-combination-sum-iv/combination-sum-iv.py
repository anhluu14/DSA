
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def f(self, target: int) -> int:
        # Base case
        if target < 0:
            return 0
        if target == 0:
            return 1
        
        #Recursion
        answer = 0
        for i in range(self.n):
            answer += self.f(target - self.nums[i])
        return answer

    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.n = len(nums) #luu nhung gi minh co vao bien self
        self.nums = nums.copy()
        return self.f(target)

