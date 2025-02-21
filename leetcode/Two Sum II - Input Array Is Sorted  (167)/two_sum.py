from typing import List


class Solution:
    def two_sum_solution1(self, numbers:List[int], target: int) -> List[int]:
        tracker = {}

        for index, num in enumerate(numbers):
            difference = target - num
            if num in tracker:
                return [tracker[num] + 1, index +1]
            else:
                tracker[difference] = index

    def two_sum_binary_search(self, numbers:List[int], target: int) -> int:
        length = len(numbers)
        left, right = 0, length - 1

        while left <= right:
            sub_sum = numbers[left] + numbers[right]

            if sub_sum == target:
                return [left + 1, right + 1]

            elif sub_sum < target:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    print(Solution().two_sum_binary_search([2, 7, 11, 15], 9))
