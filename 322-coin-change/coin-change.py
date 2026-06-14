from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        queue = deque([(0, 0)]) 
        visited = set([0])
        while queue:
            curr, steps = queue.popleft()
            for coin in coins:
                new_amount = curr + coin
                if new_amount == amount:
                    return steps + 1
                if new_amount < amount and new_amount not in visited:
                    visited.add(new_amount)
                    queue.append((new_amount, steps + 1))
        return -1
        