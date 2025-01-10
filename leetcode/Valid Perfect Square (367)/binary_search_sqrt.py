
"""
    Given a positive integer num, return true if num is a perfect square or false otherwise.
    A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer
    with itself.
    You must not use any built-in library function, such as sqrt.

    Example 1:

    Input: num = 16
    Output: true
    Explanation: We return true because 4 * 4 = 16 and 4 is an integer.

    Example 2:

    Input: num = 14
    Output: false
    Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

    Constraints:

        1 <= num <= 231 - 1
"""


class Solution:
    def is_perfect_square(self, num: int) -> bool:
        high = num // 2
        if num == 1:
            return True

        left = 0

        while left <= high:
            mid = (high + left) // 2
            mid_sq = mid * mid

            if mid_sq == num:
                return True
            # if mid_sq is smaller
            elif mid_sq < num:
                left = mid + 1
            else:
                high = mid - 1

        return False


if __name__ == "__main__":
    print(Solution().is_perfect_square(4))
