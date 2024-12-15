from typing import List


class Solution:
    def pivot_index(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        right_sum = total_sum

        for index, num in enumerate(nums):
            right_sum -= num
            left_sum = total_sum - (right_sum + num)

            if left_sum == right_sum:
                return index
        return -1


if __name__ == "__main__":
    print(Solution().pivot_index([1, 7, 3, 6, 5, 6]))

