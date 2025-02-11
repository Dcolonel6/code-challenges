from typing import List


class Solution:

    def max_profit(self, prices: List[int]) -> int:
        max_profit = 0
        buying_price = float("inf")

        for price in prices:
            buying_price = min(buying_price, price)
            max_profit = max(max_profit, price - buying_price)

        return max_profit


if __name__ == "__main__":
    print(Solution().max_profit([7, 1, 5, 3, 6, 4]))
