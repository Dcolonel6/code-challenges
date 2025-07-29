from typing import List


# solved using kadane's variation in dynamic programming

class Solution:
    def maximum_product(self, nums:List[int]) -> int:
        current_min  = current_max = 1
        results = max(nums)

        for num in nums:

            # check if its zero
            if num == 0:
                # reset to zero
                current_min, current_max = 1, 1
                continue

            temp = current_max * num
            current_max = max(num, temp, current_min * num)
            current_min = min(num, current_min * num, temp)

            results = max(results, current_max )
        return results



if __name__ =="__main__":
    print(Solution().maximum_product([2, -5, -2, -4,  3]))