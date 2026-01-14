class Solution:
    # N elements, 0<=Ai<=1 moi phan tu co 2 cach chon
    # co 2^n cach chon
    # i:build first i-th so luong phan tu da xay
    def backtrack(self, i: int, n: int, k: int):

        #base case 
        if i == n:
            #we have state self.A=>self.A[i]=0 => num[i] is not selected
            #self.A[i]=1 is selected
            subset = []
            for j in range(n):
                if self.A[j] == 0:
                    continue
                elif self.A[j] == 1:
                    subset.append(self.nums[j])
            self.subsets.append(subset)
            print(subset)
            return
        
        #recursion
        #first i-th elements, build the (i+1)-th element, means A[i]
        for v in range(k):
            self.A[i] = v
            self.backtrack(i + 1, n, k)
            self.A[i] = -1

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.nums = nums             
        self.A = [-1] * n
        self.subsets = []

        self.backtrack(0, n, 2)
        return self.subsets
