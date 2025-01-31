from collections import deque
from typing import List

class Solution:

    def first_negative_integer(self, arr:List[int], k:int) -> List[int]:
        left = 0
        res = []
        negatives_queue = deque()

        for index, num in enumerate(arr):
            window = index - left + 1

            if num < 0:
                negatives_queue.append(index)
            if window == k:
                # we have a negative value
                if negatives_queue:
                    first_negative_idx = negatives_queue[0]
                    # check if the negative value is the element exiting the current window
                    if left == first_negative_idx:
                        # if yes, remove it from queue
                        x = negatives_queue.popleft()
                        res.append(arr[x])
                    else:
                        # if not keep it
                        res.append(arr[first_negative_idx])
                else:
                    res.append(0)
                left += 1

        return res


if __name__ == "__main__":
    # print(Solution().first_negative_integer([-8, 2, 3, -6, 10], 2))
    print(Solution().first_negative_integer([12, -1, -7, 8, -15, 30, 16, 28], 3))

            
        