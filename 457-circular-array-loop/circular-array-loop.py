class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            direction = nums[i] > 0
            slow = i
            fast = i

            while True:
                # Slow moves once
                nxt = next_index(slow)

                if nums[slow] == 0 or (nums[slow] > 0) != direction:
                    break

                slow = nxt

                # Fast moves twice
                for _ in range(2):
                    if nums[fast] == 0 or (nums[fast] > 0) != direction:
                        break
                    fast = next_index(fast)
                else:
                    if slow == fast:
                        # Ignore one-element cycle
                        if slow != next_index(slow):
                            return True
                        break

                    continue

                break

        return False