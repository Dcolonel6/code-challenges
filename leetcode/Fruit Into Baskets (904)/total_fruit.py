from typing import List
from collections import Counter, defaultdict


class Solution:
    def total_fruit(self, fruits: List[int]) -> int:
        tracker_count = defaultdict(int)
        max_length = float("-inf")
        left = 0

        for index, num in enumerate(fruits):
            tracker_count[num] += 1
            if len(tracker_count) > 2:
                left_fruit = fruits[left]
                tracker_count[left_fruit] -= 1
                if tracker_count[left_fruit] == 0:
                    tracker_count.pop(left_fruit)
                left += 1

            window = index - left + 1
            max_length = max(max_length, window)
        return max_length


if __name__ == "__main__":
    print(Solution().total_fruit([0, 1, 2, 2])) # 3




