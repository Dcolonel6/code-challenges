from collections import deque
from typing import List

class Solution:

    def maximum_sliding_window(self, nums:List[int], k:int) -> List[int]:
        result = []
        queue = deque()
        left = 0

        for index, num in enumerate(nums):
            # checks to see if the item at the front of queue is bigger than the current num
            while queue and num > nums[queue[-1]]:
                # if current num is larger pop the remaining items until you find the biggest
                queue.pop()
            # add index in queue
            queue.append(index)

            # check if the last item in the window is leaving the window, if it has remove it from queue
            if left > queue[0]:
                queue.popleft()

            # check if window is equal to or larger to k
            if index + 1 >= k:
                result.append(nums[queue[0]])
                left += 1

        return result




if __name__ == "__main__":
    # print(Solution().maximum_sliding_window([1, -1], 1))
    print(Solution().maximum_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))