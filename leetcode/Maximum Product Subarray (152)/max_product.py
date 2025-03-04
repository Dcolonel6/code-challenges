from typing import List


class Solution:
    def maximum_product(self, arr:List[int]) -> int:
        current_min = current_max = arr[0]
        running_product = 1
        left = 0

        for index, num in enumerate(arr):
            running_product *= num
            current_max = max(num, current_max, running_product)
            current_min = min(running_product, num, current_min)

            if current_min > running_product:
                left = index
            if num == 0:
                running_product = 1
        return current_max




if __name__ =="__main__":
    print(Solution().maximum_product([-1, 2, 0, -3, 4]))