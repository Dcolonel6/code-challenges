import math
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return high + 1

        while low <= high:
            mid = (low + high) // 2
            mid_value = nums[mid]

            if mid_value == target:
                return mid
            # mid value is > than target
            elif target > mid_value:
                # adjust the high pointer
                low = mid + 1
            elif target < mid_value:
                high = mid - 1
        return low


if __name__ == "__main__":
    print(Solution().searchInsert([1,3,5,6], 2))
    # print(Solution().searchInsert([1], 1))