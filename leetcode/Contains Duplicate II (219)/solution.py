from typing import List


class Solution:
    def contains_nearby_duplicate(self, nums: List[int], k: int) -> bool:
        tracker = {}
        for index, element in enumerate(nums):
            if element in tracker:
                diff_abs = abs(tracker[element] - index)
                if diff_abs <= k:
                    return True
            tracker[element] = index
        return False


if __name__ == "__main__":
    print(Solution().contains_nearby_duplicate([1, 2, 3, 1], 3))
