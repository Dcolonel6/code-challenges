from typing import List


class Solution:

    def maximum_sum_subarray(self, arr:List[int], k:int) -> int:
        max_sum_subary = float("-inf")
        running_sum = 0
        left = 0


        for index, num in enumerate(arr):
            window = index - left + 1
            running_sum += num

            if window == k:
                max_sum_subary = max(max_sum_subary, running_sum)
                left_num = arr[left]
                running_sum -= left_num
                left += 1
        return max_sum_subary


if __name__ == "__main__":
    print(Solution().maximum_sum_subarray([100, 200, 300, 400], 2))
