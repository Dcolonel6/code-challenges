from typing import List


class Solution:
    def two_sum(self, numbers:List[int], target: int) -> List[int]:
        tracker = {}

        for index, num in enumerate(numbers):
            difference = target - num
            if num in tracker:
                return [tracker[num] + 1, index +1]
            else:
                tracker[difference] = index


if __name__ == "__main__":
    print(Solution().two_sum([2, 7, 11, 15], 9))
