from typing import List

"""
    Given an array of positive integers nums and a positive integer target, return the minimal length of a
    subarray
    whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

class Solution:

    def min_sub_array_len(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        subary_minimum = float('inf')
        left = 0
        sum_subarry = 0

        for index, element in enumerate(nums):
            sum_subarry += element
            while sum_subarry >= target:
                subary_minimum = min(subary_minimum, index - left + 1)
                sum_subarry -= nums[left]
                left += 1
        return 0 if subary_minimum == float('inf') else subary_minimum


if __name__ =="__main__":
    print(Solution().min_sub_array_len(7, [2, 3, 1, 2, 4, 3]))

