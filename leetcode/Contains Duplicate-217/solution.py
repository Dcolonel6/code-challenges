from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        tracker = {}

        for index, num in enumerate(nums):
            if num in tracker:
                return True
            tracker[num] = index
        return False


if __name__ == "__main__":
    print(Solution().contains_duplicate([1,2,3,1]))