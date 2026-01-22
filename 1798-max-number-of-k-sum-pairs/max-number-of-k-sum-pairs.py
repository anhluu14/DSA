class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Initialization
        n = len(nums)
        j = n - 1 # The position that matches with i will not greater than j
        ans = 0 

        # Sort the array
        nums.sort()

        # Two-pointers approach
        for i in range(n):
            while j > i and nums[i] + nums[j] > k: #lon hon thi di tiep va vi tri j lon hon i
                j -= 1
                        
        #j is the only candidate to match with i
            if j > i and nums[i] + nums[j] == k:
                ans += 1
                j -= 1 #do j ko duoc dung nua

        return ans


#Sort the array
#k = 5
#1 1 2 2 3 3 4 4 
