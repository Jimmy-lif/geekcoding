class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分法求平方根
        low = 0.0;
        high = x;
        mid = (low + high) / 2;
        delta = 0.0;
        while (1):
            mid = (low + high) / 2;
            delta = mid * mid - x;
            if (delta < 0):
                if (int(mid) + 1) * (int(mid) + 1) > x:
                    return int(mid);
                else:
                    low = mid;
            elif (delta > 0):
                if (int(mid)) * (int(mid)) <= x:
                    return int(mid);
                else:
                    high = mid;
            else:
                return int(mid);
