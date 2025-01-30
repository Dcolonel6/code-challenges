from typing import List
from collections import defaultdict

class Solution:
    def count_distinct(self, arr:List[int], k:int):
        freq = defaultdict(int)
        left = 0
        unique_elements = set()
        res = []

        for index, num in enumerate(arr):
            window = index - left + 1
            freq[num] += 1
            unique_elements.add(num)
            if window == k:
                left_num = arr[left]
                res.append(len(unique_elements))
                if freq[left_num] == 1:
                    unique_elements.discard(left_num)
                left += 1
                freq[left_num] -= 1
        return res


if __name__ == "__main__":
    print(Solution().count_distinct([1, 2, 1, 3, 4, 2, 3], 4))