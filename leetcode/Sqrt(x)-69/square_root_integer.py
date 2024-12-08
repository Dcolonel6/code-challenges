class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x

        while low <= high:
            mid = (low + high) // 2
            mid_squared = mid * mid

            if mid_squared == x:
                return mid
            elif mid_squared > x:
                high = mid - 1
            else:
                low = mid + 1
        return high



if __name__ == "__main__":
    print(Solution().mySqrt(11))
