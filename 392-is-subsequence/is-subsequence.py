class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        prev_idx = -1

        for i in range(len(s)):
            prev_idx += 1
            while prev_idx < len(t) and s[i] != t[prev_idx]:
                prev_idx += 1
                
        return prev_idx < len(t)