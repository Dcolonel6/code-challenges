from typing import List


"""
    Given an integer array nums, find the
    subarray
    with the largest sum, and return its sum.
    i used kadane's algorithm
"""
class Solution:

    def maximum_subarray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = float('-inf')
        left = 0

        for idx, num in enumerate(nums):
            current_sum += num
            max_sum = max(current_sum, max_sum)
            if current_sum < 0:
                current_sum = 0
                left = idx

        return max_sum


if __name__ == "__main__":
    print(Solution().maximum_subarray([5,4,-1,7,8]))
