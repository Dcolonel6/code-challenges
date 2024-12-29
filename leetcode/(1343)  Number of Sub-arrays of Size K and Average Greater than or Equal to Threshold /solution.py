from typing import List

class Solution:
    def num_of_subarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # when array is smaller than k
        length = len(arr)
        if length < k:
            return 0
        left = 0
        count_subarray = 0
        running_sum = 0

        for index, num in enumerate(arr):
            window = index - left + 1
            running_sum += num
            # is window equal to k?
            if window == k:
                # has sum reached the threshold?
                avg = running_sum / k
                if avg >= threshold:
                    count_subarray += 1
                left_num = arr[left]
                running_sum -= left_num
                left += 1
        return count_subarray


if __name__ == "__main__":
    print(Solution().num_of_subarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
