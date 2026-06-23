class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        up = [i for i in range(m)]
        down = [m - 1 - i for i in range(m)]
        for _ in range(3, n + 1):
            pref_down = [0] * (m + 1)
            for i in range(m):
                pref_down[i + 1] = (pref_down[i] + down[i]) % MOD
            suff_up = [0] * (m + 1)
            for i in range(m - 1, -1, -1):
                suff_up[i] = (suff_up[i + 1] + up[i]) % MOD
            new_up = [0] * m
            new_down = [0] * m
            for i in range(m):
                new_up[i] = pref_down[i]
                new_down[i] = suff_up[i + 1]
            up = new_up
            down = new_down
        return (sum(up) + sum(down)) % MOD