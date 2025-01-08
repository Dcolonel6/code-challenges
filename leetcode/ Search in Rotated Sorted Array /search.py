from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot index
        pivot_index = self.find_pivot(nums)

        # using the pivot, split list into 2
        sublist_one = nums[:pivot_index]
        sublist_two = nums[pivot_index:]

        # check in each sub array
        if target in sublist_one:
            return self.binary_search(sublist_one, target)
        if target in sublist_two:
            return self.binary_search(sublist_two, target) + pivot_index
        return -1

    def binary_search(self, ary: List[int], target: int) -> int:
        n = len(ary)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            mid_value = ary[mid]

            # target is same as mid value
            if mid_value == target:
                return mid
            # midpoint value bigger than target
            elif mid_value > target:
                high = mid - 1
            elif mid_value < target:
                low = mid + 1

        # if we finish looping, then we didnt find target
        return -1

    def find_pivot(self, ary: List[int]) -> int:
        n = len(ary)
        low = 0
        high = n - 1

        while low < high:
            mid = (low + high) // 2
            mid_value, high_value = ary[mid], ary[high]
            # check if mid value is greater than the last value

            if mid_value > high_value:
                # move the low pointer to be mid + 1
                low = mid + 1

            # if its less than or equal to, move the high pointer to be
            # the same as mid pointer
            else:
                high = mid

        # after the loop, both the low and high pointer will converge to minvalue
        return low


def main():
    s = Solution()
    # print(f"binary search: {s.binary_search([1,2,3,4,5,6,7,8,9], 9)}")
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))


if __name__ == "__main__":
    main()
