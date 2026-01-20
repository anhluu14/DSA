class Solution:
    def f(self, nums: List[int], x: int, target: int) -> bool:
        if nums[x] >= target:
            return True
        return False

    def ff(self, nums: List[int], x: int, target: int) -> bool:
        if nums[x] <= target:
            return True
        return False

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #non-decreasing: mang co nhung phan tu giong nhau
        # tang dan : mang khong the co phan tu giong nhau
       # L = 0
       # R = len(nums) - 1
       # start = len(nums) #minimal index having value is target
        

        #Answers is in range [L, R]
       # while L <= R:
       #     mid = (L + R) // 2 #Index of middle

       #     if nums[mid] == target:
       #         start = min(start, mid)
       #         R = mid - 1 #de check coi no co phai so dau tien khong
       #     elif nums[mid] < target:
       #         L = mid + 1 #di ve ben phai
       #     else:
        #        R = mid - 1#di ve ben trai 
       # print(start)
       # return -1

    #existence
    #minimal index satisfying something
    # Find minimal x: <=> f(x) = True
    # f(x) = True when x >= target
    # f(x) = False when x < target

    #Find maximal x: f(x) = True
    #Maximal index satisfying something 
        if len(nums) == 0:
            return [-1, -1]

        L = 0
        R = len(nums) - 1
        start = 0
        
        while L <= R:
            mid = (L + R) // 2

            if self.f(nums, mid, target):
                start = mid
                R = mid - 1

            else:
                L = mid + 1
        
    #start is the minimal index satisfy f(start) = True => nums[start] >= target
        if nums[start] != target:
            start = -1
     # We must find maximal "end" such that nums[end] <= target
        # If we define f(end) = True if nums[start] <= target
        # => Find maximal "end" such that f(end) = True
        # ATTENTION: f(X) must satisfies 2 things:
        #   + If f(X) = True, then f(X - 1) = f(X - 2) = ... = True
        #   + If f(X) = False, then f(X + 1) = f(X + 2) = ... = False
        # The code belows is the template for all Binary Search problem to find maximal number that satisfies a condition
        end = 0
        L = 0
        R = len(nums) - 1
        
        while L <= R:
            mid = (L + R) // 2

            if self.ff(nums, mid, target):
                end = mid
                L = mid + 1

            else:
                R = mid - 1
        # After binary search, we must recheck the real condition, since we have lossen the condition for BS
        if nums[end] != target:
            end = -1
    
        answer = [start, end]
        return answer
        
