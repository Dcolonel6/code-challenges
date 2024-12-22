from typing import List


class Solution:
    def find_max_average(self, nums: List[int], k: int) -> float:
        maximum_average = float('-inf')
        left = 0
        window = 0
        sum_subary = 0
        if len(nums) <= 1:
            return nums[0]

        for index, element in enumerate(nums):
            window = index - left + 1
            sum_subary += element
            if window == k:
                maximum_average = max(maximum_average, sum_subary / k)
                sum_subary -= nums[left]
                left += 1
        return maximum_average


if __name__ == "__main__":
    print(Solution().find_max_average([1, 12, -5, -6, 50, 3], 4))
