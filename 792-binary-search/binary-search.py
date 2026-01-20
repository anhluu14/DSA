class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        #Answers is in range [L, R]
        while L <= R:
            mid = (L + R) // 2 #Index of middle

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1 #di ve ben phai
            else:
                R = mid - 1#di ve ben trai 
        return -1
 
            
        