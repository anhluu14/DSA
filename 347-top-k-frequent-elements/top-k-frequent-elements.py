class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] #empty array the size of our inputs + 1

        for n in nums:
            count[n] = 1 + count.get(n, 0) #1 plus what its current count is

        #going through each value that we counted
        for n, c in count.items():
            freq[c].append(n) #value n appears c times #at index count we're going to append to the list this value n
            #this value n occurs c numbers of time

        res = []
        for i in range(len(freq) - 1, 0, -1): #going descending order to check the most frequent k numbers -1 as the decrementer
            for n in freq[i]:   
                res.append(n)
                if len(res) == k:
                    return res