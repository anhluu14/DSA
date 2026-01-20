class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #n = len(nums)

        #for i in range(n):
            #find the minimum number's index from i + 1 to N - 1:
           # min_idx = i

            #for j in range(i + 1, n):
                #if nums[j] < nums[min_idx]:
                    #min_idx = j #Gan bang phan tu J

            #swap phan tu thu i va min_idx-th element
            #dung mot bien nho de luu lai 
            #tmp = nums[i]
            #nums[i] = nums[min_idx]
            #nums[min_idx] = tmp
        nums.sort()
        return nums
    
#

        