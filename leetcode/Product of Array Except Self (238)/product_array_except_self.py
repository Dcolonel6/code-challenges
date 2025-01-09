from typing import List


class Solution:

    def product_except_self(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_product_ary = [1] * length
        right_product_ary = [1] * length
        ans = [1] * length
        running_product = 1

        # get the product to the left of the current element
        for index, num in enumerate(nums):
            left_product_ary[index] = running_product
            running_product *= num

        running_product = 1

        # get the product to the right of the current element  in nums and then multiply left_ary[i] * right[n-i-1]
        # basically the reverse
        for idx, num in enumerate(nums[::-1]):
            ans[idx] = running_product * left_product_ary[length - 1 - idx]
            running_product *= num

        return ans[::-1]


if __name__ == "__main__":
    print(Solution().product_except_self([-1,1,0,-3,3]))