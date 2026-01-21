class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for idx, num in enumerate(nums):
            arr.append((num, idx))
        arr.sort()
        
        i = 0
        j = len(arr) - 1
        while i < j:
            curr_sum = arr[j][0] + arr[i][0] #arr[left][0] = take the number value

            if curr_sum  == target:
                return [arr[i][1], arr[j][1]]
            elif curr_sum < target:
                i += 1
            else:
                j -= 1