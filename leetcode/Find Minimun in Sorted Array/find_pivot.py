from typing import List


class Solution:
    def find_pivot(self, nums:List[int]) -> int:
        n = len(nums)
        low_index = 0
        high_index = n - 1

        while low_index < high_index:
            mid = (low_index + high_index) // 2
            mid_value, high_value = nums[mid], nums[high_index]

            if mid_value > high_value:
                # adjust the low to be mid index +1
                low_index = mid + 1
            else:
                high_index = mid
        return nums[low_index]


if __name__ == "__main__":
    s = Solution().find_pivot([7, 8, 9, 1, 2, 3, 4, 5, 6])
    print(s)
    