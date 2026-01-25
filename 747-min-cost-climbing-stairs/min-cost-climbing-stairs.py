class Solution:
    def f(self, i: int) -> int:
        if i == 0:
            return 0
        if i == 1:
            return 0
        return min(self.f(i - 1) + self.nums[i - 1], self.f(i - 2) + self.nums[i - 2])
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        self.cost = cost.copy()

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        #formula
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
       
        return dp[n]
        