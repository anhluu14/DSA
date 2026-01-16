class Solution:
    
        #N elements, 0<= Ai< N
        #A = [0, 1, 2, ..., N-1]

        #i: build first i-th elements
    def backtrack(self, i:int, n: int, k:int, nums):
            #base case
        if i == n:
            if self.check() == True:
                perm = []
                for j in range(n):
                        perm.append(nums[self.A[j]])
                self.perms.append(perm)
            print(self.A)
            return
        #recursion
        #first i-th elements, build the (i+1)-th element, means A[i]
        for v in range(k):
            self.A[i] = v
            self.backtrack(i + 1, n, k, nums)
            self.A[i] = -1
    #CHECK FUNCTION TO SEE IF A IS PERMUTATION
    #Check if there exists a pair (Ai, Aj) having: Ai = Aj
    def check(self) -> bool:
        for i in range(len(self.A)):
            for j in range(i):
                if self.A[i] == self.A[j]:
                    return False
        return True

    def permute(self, nums: List[int]) -> List[List[int]]:
        #init
        n = len(nums)
        self.A = [-1] * n
        self.perms = []
        self.backtrack(0, n, n, nums)

        return self.perms
