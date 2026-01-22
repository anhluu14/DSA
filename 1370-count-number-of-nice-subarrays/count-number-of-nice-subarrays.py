class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        #Initialzation
        n = len(nums)
        pre_odd_number = [0] * (n + 1) #do so luong so le tu i toi n thi tu 0 toi n co tong cong n + 1 so
        ans = 0
        #Two - pointers approach
        first = 0 #smallest number satisfies pre_odd_number[i] - pre_odd_number[j] <= k:
        last = 0 #smallest number satisfies pre_odd_number[i] - pre_odd_number[j] < k:
        

        #Calculate pre_odd_number
        pre_odd_number[0] = 0
        for i in range(1, n + 1):
            if nums[i - 1] % 2 == 0:
                pre_odd_number[i] = pre_odd_number[i - 1]
            else:
                pre_odd_number[i] = pre_odd_number[i - 1] + 1
        
        # Two pointers approach
        for i in range(n + 1):
            while first < i and pre_odd_number[i] - pre_odd_number[first] > k:
                first += 1

            while last < i and pre_odd_number[i] - pre_odd_number[last] >= k:
                last += 1

            # if j between first and last -1, pre_odd_number[i] - pre_odd_number[j] = k
            ans += last - first

        return ans

# Count the number of (i, j)
# for l in range (n):
# for r in range (l, n):
# num_odd = 0
# for k in range (l ,r):
# if nums[k] % 2 == 1:
#    num_odd += 1
#
#if num_odd == k:
#ans += 1