class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 1 or n == 0):
            return 1;
        t0 = 1;
        t1 = 1;
        t = t0 + t1;
        for i in range(2,n):
            t0 = t1;
            t1 = t;
            t = t0 + t1;
        return t;
