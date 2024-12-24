from typing import List


"""
    You are given an integer array nums and two integers l and r. 
    Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) 
    and whose sum is greater than 0.
    Return the minimum sum of such a subarray. If no such subarray exists, return -1.
    A subarray is a contiguous non-empty sequence of elements within an array.
"""
class Solution:
    def minimum_sum_subarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        current_sum = 0
        start = 0
        found = False

        for end in range(n):
            current_sum += nums[end]  # Expand the window

            # Shrink the window if it exceeds size r
            while end - start + 1 > r:
                current_sum -= nums[start]
                start += 1

            # Check if the window size is within [l, r]
            if l <= end - start + 1 <= r:
                if current_sum > 0:
                    min_sum = min(min_sum, current_sum)
                    found = True

        return min_sum if found else -1


if __name__ == "__main__":
    # print(Solution().minimum_sum_subarray([3, -2, 1, 4], 2, 3)) # 1
    # print(Solution().minimum_sum_subarray([-2, 2, -3,  1], 2, 3)) # -1
    # print(Solution().minimum_sum_subarray([1, 2, 3, 4], 2, 4)) # 3
    # print(Solution().minimum_sum_subarray([-12, 8], 1, 1)) # 8
    print(Solution().minimum_sum_subarray([-3, 17], 1, 2))  # 14






