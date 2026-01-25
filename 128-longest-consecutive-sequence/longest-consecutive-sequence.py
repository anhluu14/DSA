from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) #một kiểu dữ liệu trong Python dùng để lưu tập hợp các phần tử KHÔNG TRÙNG LẶP, và quan trọng nhất là kiểm tra tồn tại rất nhanh (O(1)).
        longest = 0
        for x in s:
            #check if its the start of sequence
            if x - 1 not in s: #if it does not have a left neighbor then its the start of the sequence 
                length = 1
                while x + length in s:
                    length += 1
                longest = max(longest, length)
        return longest
