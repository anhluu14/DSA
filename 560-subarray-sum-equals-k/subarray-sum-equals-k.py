class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #initialization
        n = len(nums)
        pre_sum = [0] * (n+1) #Định nghĩa pre_sum [i] là sum của i số đầu
        dictionary = {}
        ans = 0

        #calculate pre_sum
        pre_sum[0] = 0
        for i in range (1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1] #tại vì mảng được đánh số từ 0
        
        #fix r, count L: sum (L,R) = k
        for R in range(0, n):

            dictionary[pre_sum[R]] = dictionary.get(pre_sum[R], 0) + 1

            ans += dictionary.get(pre_sum[R + 1] - k, 0)

        return ans