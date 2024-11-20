from operator import index
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracking_dict = dict()
        for i, element in enumerate(nums):
            difference = target - element
            # check if element is in the the dict
            #element = abs(element)
            if element in tracking_dict:
                tracking_dict[element] = tracking_dict[element] +  [i] # tracking_dict[element].append(i)
                return tracking_dict[element]
            else:
                tracking_dict[difference] = [i]

if __name__ == "__main__":
    s = Solution().twoSum([2,7,11,15],  9)
    print(s)
