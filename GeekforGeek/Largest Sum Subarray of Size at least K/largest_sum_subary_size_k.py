from typing import List


class Solution:
    def max_sum_with_k(self, a: List[int], n: int, k: int) -> int:
        # Step 1: Compute prefix sum of the first k elements
        arr = a
        curr_sum = sum(arr[:k])
        max_sum = curr_sum  # This ensures we have at least k elements

        prev_sum = 0  # Tracks the sum before removing elements
        min_prev_sum = 0  # Tracks the minimum sum we can remove

        # Step 2: Extend the subarray beyond k
        for i in range(k, n):
            curr_sum += arr[i]  # Expand the window by adding next element
            prev_sum += arr[i - k]  # Track sum of elements we can remove

            # Maintain the smallest `prev_sum` to keep valid subarrays
            min_prev_sum = min(min_prev_sum, prev_sum)

            # Maximize the result by removing the smallest sum possible
            max_sum = max(max_sum, curr_sum - min_prev_sum)

        return max_sum


if __name__ == "__main__":
    print(Solution().max_sum_with_k([1, -2, 2, -3], 4, 2))

