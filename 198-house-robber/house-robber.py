class Solution:
    def f(self, i: int) -> int: #Maximum money can be robbed
        if i < 0:
            return 0
        if i == 0:
            return 0
        # Recursion
        # 0, 1, 2, ..., i - 3, i - 2, i - 1
        # i - 1 is robbed => f(i - 3) + self.nums[i - 1]
        # i -1 is not robbed => f(i - 1)
        return max(self.f(i - 2) + self.nums[i - 1], self.f(i - 1))
    # khi cuop ngoi nha i - 1 thi ngoi nha i - 2 se k bi cuop thi minh se xet tu 0 toi i - 3 thi tong so ngoi nha can xet la i - 2
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        self.nums = nums.copy()

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]

        #formula
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
       
        return dp[n]