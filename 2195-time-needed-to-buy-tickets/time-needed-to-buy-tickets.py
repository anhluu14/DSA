from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        n = len(tickets)
        ans = 0
        for i in range(n):
            queue.append(i)
        
        while True:
            ans += 1
            person = queue.popleft()
            tickets[person] -= 1

            if tickets[person] > 0:
                queue.append(person)
            else:
                if person == k:
                    break
        return ans