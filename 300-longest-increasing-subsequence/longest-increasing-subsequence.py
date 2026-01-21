from functools import lru_cache
class Solution:
    @lru_cache(None)
    def f(self, n:int) -> int:
        # Base case
        if n <= 0:
            return 0
        
        # Recursion
        answer = 1
        for i in range(1, n):
            if self.nums[i - 1] < self.nums[n - 1]:
                answer = max(answer, self.f(i) + 1)
        return answer
            
    def lengthOfLIS(self, nums: List[int]) -> int:
        self.nums = nums.copy()

        answer = 0
        for n in range(1, len(nums) + 1):
            answer = max(answer, self.f(n))
        
        return answer