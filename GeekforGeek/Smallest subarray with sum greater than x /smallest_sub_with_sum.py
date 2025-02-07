from typing import List
class Solution:

    def smallest_sub_with_sum(self, x: int, arr: List[int]) -> int:
        left = 0
        smallest_window = float("inf")
        running_sum = 0

        for index, num in enumerate(arr):
            running_sum += num
            while running_sum > x:
                window = index - left + 1
                smallest_window = min(smallest_window, window)
                left_num = arr[left]
                running_sum -= left_num
                left += 1

        return smallest_window if smallest_window != float("inf") else 0


if __name__ == "__main__":
    print(Solution().smallest_sub_with_sum(51, [1, 4, 45, 6, 0, 19]))
    # print(Solution().smallest_sub_with_sum(100, [1, 10, 5, 2, 7]))


